"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

from ..make_rest_api_call import MakeRestApiCall


URL = {
    "Attack Surface Exposure": "asm_exposure",
    "Darknet Exposure": "darknet_exposure",
    "Incidents": "incidents"
}


APPROVAL_STATUS_MAPPING = {
    "Pending": "pending",
    "Approved": "approved",
    "Rejected": "rejected"
}


STATUS_MAPPING = {
    "Pending": "pending",
    "Started": "started",
    "Failed": "failed",
    "Completed": "completed"
}


def get_vendor_watchlist(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    status = params.get("status")
    if status:
        params["status"] = STATUS_MAPPING.get(status)
    approval_status = params.get("approval_status")
    if approval_status:
        params["approval_status"] = APPROVAL_STATUS_MAPPING.get(approval_status)
    endpoint = '/aci/{org_id}/vendors_watchlist'
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response

def get_vendor_details_by_id(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/vendors'+'/{id}'.format(id=params.pop('id'))
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response

def get_vendor_exposures_by_id(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/vendors'+'/{id}'.format(id=params.pop('id'))+'/{url}'.format(url=URL.get(params.get('type_of_info'))) if params.get('type_of_info') else ""
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response
