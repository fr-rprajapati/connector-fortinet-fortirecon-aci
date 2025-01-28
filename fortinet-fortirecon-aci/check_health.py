"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

from .make_rest_api_call import MakeRestApiCall


def _check_health(config: dict) -> bool:
    try:
        endpoint = "/aci/{org_id}/osint_feeds"
        method = "GET"
        MS = MakeRestApiCall(config=config)
        MS.make_request(endpoint=endpoint, method=method, params={"size": 1})
        return True
    except Exception as e:
        raise Exception(e)
