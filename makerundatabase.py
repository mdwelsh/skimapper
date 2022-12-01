#!/usr/bin/env python3

import requests
import yaml
from bs4 import BeautifulSoup


DATABASE_FILE="crystalmountain.yaml"
OUTFILE="crystalmountain-new.yaml"

CRYSTAL_MOUNTAIN_WAY_NUMBERS = [
  "127126804", # Downhill
  "127126798", # Queens
  "127128246", # Lucky Shot
  "127128250", # Green Valley
  "127126797", # Lower Arwine's
  "127128253", # Middle Ferk's
]

def download_node(node):
  node_number = node.attrs["ref"]
  node_url = f"https://www.openstreetmap.org/api/0.6/node/{node_number}"
  result = requests.get(node_url)
  soup = BeautifulSoup(result.text, features="xml")
  lat = float(soup.osm.node.attrs["lat"])
  lon = float(soup.osm.node.attrs["lon"])
  return [lat, lon]


def download_way(waynumber):
  nodes=[]
  way_url = f"https://www.openstreetmap.org/api/0.6/way/{waynumber}"
  result = requests.get(way_url)
  soup = BeautifulSoup(result.text, features="xml")
  # Iterate over all the nodes in the way
  for node in soup.osm.way.find_all("nd"):
    nodes.append(download_node(node))
  name = soup.find("tag", k="name").attrs["v"]
  difficulty = soup.find("tag", k="piste:difficulty").attrs["v"]
  type = soup.find("tag", k="piste:type").attrs["v"]
  return name, difficulty, type, nodes


def add_run(waynumber, data):
  name, difficulty, type, nodes = download_way(waynumber)
  data["runs"][str(waynumber)] = {
    "name": name,
    "difficulty": difficulty,
    "type": type,
    "nodes": [ { "lat": lat, "lon": lon } for (lat, lon) in nodes ]
  }


def main():
  with open(DATABASE_FILE) as infile:
    data = yaml.load(infile, yaml.Loader)
  if "runs" not in data or not data["runs"]:
    data["runs"] = {}
  
  for waynumber in CRYSTAL_MOUNTAIN_WAY_NUMBERS:
    add_run(waynumber, data)
  
  with open(OUTFILE, "w") as outfile:
    yaml.dump(data, outfile)

if __name__ == "__main__":
  main()