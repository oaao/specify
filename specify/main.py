from typing import Dict

# configuration dependencies
from specify.config import SPOTIFY_API, SPECIFY_AUTH, SPECIFY_SERVER

# data formatting dependencies
from specify import spcf_http
import json
import base64

# HTTP service/interaction dependencies
import requests as r
from flask import Flask, request, redirect, render_template

app = Flask(__name__)


@app.route("/")
def index():

    url_auth: str = spcf_http.format_url_query(SPOTIFY_API['url_auth'], spcf_http.AUTH_QUERY)

    return redirect(url_auth)


@app.route("/callback/")
def callback():

    auth_token:   str            = request.args['code']
    auth_payload: Dict[str, str] = {
                                    "grant_type":   "authorization_code",
                                    "code":         str(auth_token),                            # force str just in case
                                    "redirect_uri": spcf_http.AUTH_QUERY['redirect_uri']
                                   }

    spcf_auth:    bytes          = base64.b64encode(
                                                    "{}:{}"
                                                    .format(SPECIFY_AUTH['client_id'], SPECIFY_AUTH['client_secret'])
                                                    .encode('utf-8')
                                                   )

    auth_headers: Dict[str, str] = {"Authorization": "Basic {}".format(spcf_auth)}

    auth_request = r.post(SPOTIFY_API['url_token'], data=auth_payload, headers=auth_headers)

    if auth_request.status_code == 200:
        auth_resp = json.loads(auth_request.text)
    else:
        # log status code, and perform any further desired behaviour dependently
        pass

    # currently unsafe: assumes auth_request status code check passes
    access_token:  str    = auth_resp['access_token']
    refresh_token: str    = auth_resp['refresh_token']
    token_type:    str    = auth_resp['token_type']
    expires_in:    str    = auth_resp['expires_in']

    access_header: str = {"Authorization: Bearer {}".format(access_token)}


if __name__ == "__main__":
    app.run(debug=False, port=SPECIFY_SERVER['port'])
