#!/usr/bin/env python3

from stravaio import strava_oauth2

CLIENT_ID=97461
CLIENT_SECRET="1c509fd8f02edac26fd433a0b0d7152eb0fcf3da"
ACCESS_TOKEN="b89ebb0678b61d4627346b4a53c1ac740130b42b"
REFRESH_TOKEN="67acbab19db7d0e2643b3722d949c07f1832be6d"

def get_access_token():
    strava_oauth2(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)




