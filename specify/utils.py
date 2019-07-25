import json
import requests as r

from flask import render_template

from config import SPOTIFY_API

def selector(action, headers):

    API:     str            = SPOTIFY_API['url_base'] + SPOTIFY_API['api_version']

    ACTIONS: Dict[str, str] = {
        'generic':      {'template': 'table.html',        'path': '{}'}, # accommodate this
        'user':         {'template': 'unknown',           'path': 'me/'},
        'current_song': {'template': 'current_song.html', 'path': 'me/player/currently-playing'},
        'analysis':     {'template': 'unknown',           'path': 'audio/analysis/{}'} # accommodate this
    }

    url:  str = f'{API}{ACTIONS[action]["path"]}'

    data = r.get(url, headers=headers).text
    j    = json.loads(data)

    return render_template(ACTIONS[action]["template"], data=j)
