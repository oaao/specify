# static configurations

# generic Spotify API parameters
SPOTIFY_API = {
                "url_base":    "https://api.spotify.com",
                "url_auth":    "https://accounts.spotify.com/authorize",
                "url_token":   "https://accounts.spotify.com/api/token",
                "api_version": "v1"
              }

# authentication params for this application (register on https://developer.spotify.com/applications)
SPECIFY_AUTH = {
                "client_id":     "",
                "client_secret": ""
              }

# server params for this application
SPECIFY_SERVER = {
                "url_base":     "",
                "url_callback": "",
                "port":         "",
                "scopes":       "",             # separated as e.g. "playlist-modify-public playlist-modify-private"
                 }
