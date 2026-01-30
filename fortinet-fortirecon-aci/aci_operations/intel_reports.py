"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""
from typing import Dict
from ..make_rest_api_call import MakeRestApiCall


def get_intel_reports(config: Dict[str, any], params: Dict[str, any]) -> Dict[str, any]:

    MK = MakeRestApiCall(config=config)
    endpoint = "/aci/{org_id}/intel/reports"

    if params.get("start_date"):
        params["start_date"] = MK.handle_date(params.get("start_date"))
    if params.get("end_date"):
        params["end_date"] = MK.handle_date(params.get("end_date"))

    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response

def get_intel_report(config: Dict[str, any], params: Dict[str, any]) -> Dict[str, any]:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/intel/reports' + '/{report_id}'.format(report_id=params.pop('report_id'))
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response

def get_intel_iocs(config: Dict[str, any], params: Dict[str, any]) -> Dict[str, any]:

    MK = MakeRestApiCall(config=config)
    endpoint = "/aci/{org_id}/intel/iocs"
    if 'report_ids' in params:
        params["report_ids"] = str(params["report_ids"]).strip('[]')
    if params.get("first_seen"):
        params["first_seen"] = MK.handle_date(params.get("first_seen"))
    if params.get("last_seen"):
        params["last_seen"] = MK.handle_date(params.get("last_seen"))
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
            if len(iocs) >= 10000:
                break
            params['page'] = params.get('page', 1) + 1
        response['hits'] = iocs
        response['total'] = len(iocs)
        return response
    return MK.make_request(endpoint=endpoint, method="GET", params=params)

def get_intel_ioc(config: Dict[str, any], params: Dict[str, any]) -> Dict[str, any]:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/intel/iocs' + '/{ioc_id}'.format(ioc_id=params.pop('ioc_id'))
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response
