import json
import requests as r

from flask import render_template

from config import SPOTIFY_API

def selector(action, headers):

    API:     str            = SPOTIFY_API['url_base'] + SPOTIFY_API['api_version']

    ACTIONS: Dict[str, str] = {
        'generic':         {'template': 'table.html',        'path': '{}'}, # accommodate this
        'user':            {'template': 'table.html',        'path': 'me/'},
        'current_song':    {'template': 'current_song.html', 'path': 'me/player/currently-playing'},
        'analysis':        {'template': 'unknown',           'path': 'audio/analysis/{}'}, # accommodate this
        'top_tracks':      {'template': 'table.html',        'path': 'me/'},
        'top_artists':     {'template': 'top_artists.html',  'path': 'me/top/artists'},
        'top_tracks':      {'template': 'top_tracks.html',   'path': 'me/top/tracks'},
        'recommendations': {'template': 'table.html',        'path': '/recommendations'}
    }

    url:  str = f'{API}{ACTIONS[action]["path"]}'

    data = r.get(url, headers=headers).text

    try:
        j    = json.loads(data)
    except ValueError:
        raise ValueError('ruh roh')

    return render_template(ACTIONS[action]["template"], data=j)
