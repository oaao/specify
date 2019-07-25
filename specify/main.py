import pysnooper

from typing import Dict

# configuration dependencies
from config import SPOTIFY_API, SPECIFY_AUTH, SPECIFY_SERVER
from utils import selector
from test_formatter import TestFormatter

# data formatting dependencies
import json
import base64

import spcf_http

# HTTP service/interaction dependencies
import requests as r
from flask import Flask, request, redirect, render_template

app = Flask(__name__)


@app.route("/")
@pysnooper.snoop()
def index():

    url_auth: str = spcf_http.format_url_query(SPOTIFY_API['url_auth'], spcf_http.AUTH_QUERY)

    return redirect(url_auth)


@app.route("/callback/")
@pysnooper.snoop()
def callback():

    auth_token:   str            = request.args['code']
    auth_payload: Dict[str, str] = {
                                    "grant_type":   "authorization_code",
                                    "code":         str(auth_token),                            # force str just in case
                                    "redirect_uri": spcf_http.AUTH_QUERY['redirect_uri']
                                   }

    spcf_auth:    bytes          = base64.b64encode(f"{SPECIFY_AUTH['client_id']}:{SPECIFY_AUTH['client_secret']}"
                                                    .encode('utf-8')
                                                    ).decode()

    auth_headers: Dict[str, str] = {"Authorization": f"Basic {spcf_auth}"}

    auth_request = r.post(SPOTIFY_API['url_token'], data=auth_payload, headers=auth_headers)

    if auth_request.status_code == 200:
        auth_resp = json.loads(auth_request.text)

        access_token:  str    = auth_resp['access_token']
        #refresh_token: str    = auth_resp['refresh_token']
        token_type:    str    = auth_resp['token_type']
        expires_in:    str    = auth_resp['expires_in']
        scope:         str    = auth_resp['scope']
    else:
        auth_request.raise_for_status()

    access_header: Dict[str, str] = {"Authorization": f"Bearer {access_token}"}

    #data = TestFormatter(j).build_data()

    return selector(action='top_artists', headers=access_header)

if __name__ == "__main__":
    app.run(debug=True, port=SPECIFY_SERVER['port'])
