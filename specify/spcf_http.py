# helper structures and functions for Specify's HTTP interactions

# configuration dependencies
from config import SPECIFY_SERVER, SPECIFY_AUTH

# data formatting dependencies
from typing import Dict, List
from urllib import parse

AUTH_QUERY: Dict[str, str] = {
    "response_type": "code",
    "redirect_uri":  SPECIFY_SERVER['uri_redirect'].format(SPECIFY_SERVER['url_base'], SPECIFY_SERVER['port']),
    "scope":         SPECIFY_SERVER['scopes'],
    "client_id":     SPECIFY_AUTH['client_id']
    }


def format_url_query(url: str, params: dict) -> str:

    param_pairs:   List[str]    = [f"{field}={parse.quote(content)}" for field, content in params.items()]
    concat_params: str          = "&".join(param_pairs)

    url_query:     str          = f"{url}/?{concat_params}"

    return url_query
