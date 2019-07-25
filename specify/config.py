from local_settings import CLIENT_ID, CLIENT_SECRET
from typing import Dict

# generic Spotify API parameters
SPOTIFY_API: Dict[str, str] = {
                                "url_base":    "https://api.spotify.com",
                                "url_auth":    "https://accounts.spotify.com/authorize",
                                "url_token":   "https://accounts.spotify.com/api/token",
                                "api_version": "/v1/"
                              }

# authentication params for this application (register on https://developer.spotify.com/applications)
SPECIFY_AUTH: Dict[str, str] = {
                                "client_id":     f"{CLIENT_ID}",
                                "client_secret": f"{CLIENT_SECRET}"
                               }

# server params for this application
SPECIFY_SERVER: Dict[str, str] = {
                                  # example values for local testing purposes
                                  "url_base":     "http://localhost",
                                  "port":         "8888",
                                  "uri_redirect": "{}:{}/callback/",

                                  # separated as e.g. "playlist-modify-public playlist-modify-private"
                                  "scopes":       "user-library-read user-read-currently-playing",
                                 }
