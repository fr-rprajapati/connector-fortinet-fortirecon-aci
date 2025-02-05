"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

from ..make_rest_api_call import MakeRestApiCall


def get_iocs(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = "/aci/{org_id}/iocs"
    if 'report_id' in params:
        params["report_id"] = str(params["report_id"]).strip('[]')
    for date_param in ("start_date", "end_date"):
        if params.get(date_param):
            params[date_param] = MK.handle_date(params[date_param])
    if params.pop('get_all_records', None):
        params.pop('page', None)
        params['size'] = 500
        iocs = []
        while True:
            response = MK.make_request(endpoint=endpoint, method="GET", params=params)
            hits = response.get('hits', [])
            if not hits:
                break
            iocs.extend(hits)
            params['page'] = params.get('page', 1) + 1
        response['hits'] = iocs
        response['total'] = len(iocs)
        return response
    return MK.make_request(endpoint=endpoint, method="GET", params=params)
