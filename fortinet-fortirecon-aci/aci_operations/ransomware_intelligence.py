"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

from ..make_rest_api_call import MakeRestApiCall


URL = {
    "Top Ransomware Victims By Sector": "top_ransomware_victims_by_sector",
    "Top Ransomware Victims By Revenue": "top_ransomware_victims_by_revenue",
    "Top Ransomware Victims By Country": "top_ransomware_victims_by_country",
    "Top Ransomware Groups": "top_ransomware_groups",
    "Ransomware Victims Over Time": "ransomware_victims_over_time",
    "Latest Active Ransomware Groups": "latest_active_ransomware_groups"
}


TIME_RANGE_MAPPING = {
    "All Time": "all",
    "Last 90 Days": "last90days",
    "Last 30 Days": "last30days",
    "Last 15 Days": "last15days",
    "Last 7 Days": "last7days",
    "Current Month": "current_month",
    "Previous Month": "previous_month"
}

def get_ransomware_victims(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/ransomware_intelligence/victims'
    if params.get("start_date"):
        params["start_date"] = MK.handle_date(params.get("start_date"))
    if params.get("end_date"):
        params["end_date"] = MK.handle_date(params.get("end_date"))
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response

def get_ransomware_victims_details_by_id(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/ransomware_intelligence/victims'+'/{id}'.format(id=params.pop('id'))
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response

def get_ransomware_intel_vendors_watchlist(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/ransomware_intelligence/vendor_watchlist/monitored'
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response

def get_ransomware_intel_vendors_watchlist_matched(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/ransomware_intelligence/vendor_watchlist/matched'
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response

def get_ransomware_intelligence_statistics(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    time_range_type = params.get("time_range_type")
    if time_range_type:
        params["time_range_type"] = TIME_RANGE_MAPPING.get(time_range_type)
    endpoint = '/aci/{org_id}/ransomware_intelligence/stats'+'/{url}'.format(url=URL.get(params.get('type_of_info'))) if params.get('type_of_info') else ""
    if params.get("start_date"):
        params["start_date"] = MK.handle_date(params.get("start_date"))
    if params.get("end_date"):
        params["end_date"] = MK.handle_date(params.get("end_date"))
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response

def get_ransomware_threat_campaigns(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/ransomware_intelligence/ransomware_threat_campaigns'
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response

def get_ransomware_potential_victims(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/ransomware_intelligence/potential_victims'
    if params.get("start_date"):
        params["start_date"] = MK.handle_date(params.get("start_date"))
    if params.get("end_date"):
        params["end_date"] = MK.handle_date(params.get("end_date"))
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response

def get_ransomware_intel_org_watchlist(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/ransomware_intelligence/org_watchlist/monitored'
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response

def get_ransomware_intel_org_watchlist_matched(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/ransomware_intelligence/org_watchlist/matched'
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response

def get_technical_indicators_for_given_ransomware_group(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/ransomware_intelligence/group'+'/{group_name}'.format(group_name=params.pop('group_name'))+'/technical_indicators'
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response

def get_ransomware_group_info(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = '/aci/{org_id}/ransomware_intelligence/group'+'/{group_name}'.format(group_name=params.pop('group_name'))+'/info'
    response = MK.make_request(endpoint=endpoint, method="GET", params=params)
    return response
