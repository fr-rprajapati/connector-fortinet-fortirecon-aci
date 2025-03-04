"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""
from typing import Dict
from ..make_rest_api_call import MakeRestApiCall


def get_intel_reports(config: Dict[str, any], params: Dict[str, any]) -> Dict[str, any]:

    MK = MakeRestApiCall(config=config)
    endpoint = "/aci/{org_id}/intel/reports"
    method = "GET"

    if params.get("start_date"):
        params["start_date"] = MK.handle_date(params.get("start_date"))
    if params.get("end_date"):
        params["end_date"] = MK.handle_date(params.get("end_date"))

    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response

def get_intel_report(config: Dict[str, any], params: Dict[str, any]) -> Dict[str, any]:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/intel/reports' + '/{report_id}'.format(report_id=params.pop('report_id'))
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response

def get_intel_iocs(config: Dict[str, any], params: Dict[str, any]) -> Dict[str, any]:

    MK = MakeRestApiCall(config=config)
    endpoint = "/aci/{org_id}/intel/iocs"
    method = "GET"

    if params.get("start_date"):
        params["start_date"] = MK.handle_date(params.get("start_date"))
    if params.get("end_date"):
        params["end_date"] = MK.handle_date(params.get("end_date"))

    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response

def get_intel_ioc(config: Dict[str, any], params: Dict[str, any]) -> Dict[str, any]:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/intel/iocs' + '/{ioc_id}'.format(ioc_id=params.pop('ioc_id'))
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response
