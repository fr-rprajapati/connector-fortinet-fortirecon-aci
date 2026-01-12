"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

from ..make_rest_api_call import MakeRestApiCall

URL = {
    "Matched Domain": "count_by_matched_domain",
    "Stealer": "count_by_stealer"
}


def get_stealers_infections_on_sale_count(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/stats/stealers_infections/on_sale' + '/{url}'.format(url=URL.get(params.get('based_on')))

    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response


def get_stealers_infections_on_sale(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/stealers_infections/on_sale'
    if params.get("start_date"):
        params["start_date"] = MK.handle_date(params.get("start_date"))
    if params.get("end_date"):
        params["end_date"] = MK.handle_date(params.get("end_date"))
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response


def update_stealers_on_sale_status(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    status = params.pop("status")
    payload = {"status": status}
    endpoint = '/aci/{org_id}/stealers_infections/on_sale'+'/{id}'.format(id=params.pop('stealers_on_sale_id'))
    response = MK.make_request(endpoint=endpoint, method="PATCH", params=params, json_data=payload)
    return response
