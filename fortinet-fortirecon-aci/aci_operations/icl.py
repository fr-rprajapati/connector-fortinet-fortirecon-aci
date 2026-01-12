"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

from ..make_rest_api_call import MakeRestApiCall

URL = {
    "Archived Forums": "archived_forums",
    "Defacements": "defacements",
    "Forums": "forums",
    "Leak Docs": "leak_docs",
    "Osint Feeds": "osint_feeds",
    "Pastes": "pastes",
    "Ransomware": "ransomware",
    "Telegram": "telegram",
}


def get_icl_saved_searches_by_id(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/icl_saved_searches'+'/{id}/{url}/result'.format(url=URL.get(params.get('based_on')), id=params.pop('id'))
    if params.get("start_date"):
        params["start_date"] = MK.handle_date(params.get("start_date"))
    if params.get("end_date"):
        params["end_date"] = MK.handle_date(params.get("end_date"))
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response

def get_icl_saved_searches(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/icl_saved_searches'
    if params.get("start_date"):
        params["start_date"] = MK.handle_date(params.get("start_date"))
    if params.get("end_date"):
        params["end_date"] = MK.handle_date(params.get("end_date"))
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response