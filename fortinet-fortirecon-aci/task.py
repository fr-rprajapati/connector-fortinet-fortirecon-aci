"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

from .make_rest_api_call import MakeRestApiCall


def create_task(config, params):
    MK = MakeRestApiCall(config=config)
    endpoint = "/security-orchestration/{org_id}/tasks"
    response = MK.make_request(endpoint=endpoint, method="POST", json_data=params)
    return response


def update_task(config, params):
    MK = MakeRestApiCall(config=config)
    endpoint = "/security-orchestration/{org_id}"+"/tasks/{0}".format(params.pop("task_id"))
    response = MK.make_request(endpoint=endpoint, method="PATCH", json_data=params)
    return response
