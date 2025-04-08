# Edit the config_and_params.json file and add the necessary parameter values.
# Ensure that the provided input_params yield the correct output schema.
# Add logic for validating conditional_output_schema or if schema is other than dict.
# Add any specific assertions in each test case, based on the expected response.

"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

import pytest
from testframework.conftest import valid_configuration, invalid_configuration, valid_configuration_with_token,\
    connector_id, connector_details, info_json, params_json
from testframework.helpers.test_helpers import run_health_check_success, run_invalid_config_test, run_success_test,\
    run_output_schema_validation, run_invalid_param_test, set_report_metadata


@pytest.mark.get_intel_reports
def test_get_intel_reports_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Intel Reports", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_intel_reports',
                                   action_params=params_json['get_intel_reports']):
        assert result.get('status') == "Success"


@pytest.mark.get_intel_reports
def test_validate_get_intel_reports_output_schema(cache, valid_configuration_with_token, connector_details,
                                            info_json, params_json):
    set_report_metadata(connector_details, "Get Reports", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_intel_reports', info_json, params_json['get_intel_reports'])


@pytest.mark.get_intel_reports
def test_get_intel_reports_invalid_report_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid Report ID")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_reports', param_name='report_id',
                                    param_type='text', action_params=params_json['get_intel_reports'])
    assert result['data']['total'] == 0


@pytest.mark.get_intel_reports
def test_get_intel_reports_invalid_tag(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid Tag")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_reports', param_name='tag',
                                    param_type='text', action_params=params_json['get_intel_reports'])
    assert result['data']['total'] == 0


@pytest.mark.get_intel_reports
def test_get_intel_reports_invalid_adversaries(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid Adversaries")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_reports', param_name='adversaries',
                                    param_type='text', action_params=params_json['get_intel_reports'])
    assert result['data']['total'] == 0


@pytest.mark.get_intel_reports
def test_get_intel_reports_invalid_source(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid source")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_reports',
                                    param_name='source',
                                    param_type='text', action_params=params_json['get_intel_reports'])
    assert result['data']['total'] == 0


@pytest.mark.get_intel_reports
def test_get_intel_reports_invalid_source_category(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid Source Category")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_reports', param_name='source_category',
                                    param_type='text', action_params=params_json['get_intel_reports'])
    assert result['data']['total'] == 0


@pytest.mark.get_intel_reports
def test_get_intel_reports_invalid_report_type(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid report type")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_reports', param_name='report_type',
                                    param_type='text', action_params=params_json['get_intel_reports'])
    assert result.get('status') == "failed"


@pytest.mark.get_intel_reports
def test_get_intel_reports_invalid_industries(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid industries")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_reports', param_name='industries',
                                    param_type='text', action_params=params_json['get_intel_reports'])
    assert result['data']['total'] == 0


@pytest.mark.get_intel_reports
def test_get_intel_reports_invalid_geographies(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid Geographies")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_reports', param_name='geographies',
                                    param_type='text', action_params=params_json['get_intel_reports'])
    assert result['data']['total'] == 0


@pytest.mark.get_intel_reports
def test_get_intel_reports_invalid_iocs(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid iocs")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_reports', param_name='iocs',
                                    param_type='text', action_params=params_json['get_intel_reports'])
    assert result['data']['total'] == 0


@pytest.mark.get_intel_reports
def test_get_intel_reports_invalid_source_reliability(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid Source Reliability")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_reports', param_name='source_reliability',
                                    param_type='text', action_params=params_json['get_intel_reports'])
    assert result.get('status') == "failed"


@pytest.mark.get_intel_reports
def test_get_intel_reports_invalid_information_reliability(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid Information Reliability")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_reports',
                                    param_name='information_reliability',
                                    param_type='text', action_params=params_json['get_intel_reports'])
    assert result.get('status') == "failed"


@pytest.mark.get_intel_reports
def test_get_intel_reports_invalid_report_generator_source(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid report generator source")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_reports',
                                    param_name='report_generator_source',
                                    param_type='text', action_params=params_json['get_intel_reports'])
    assert result.get('status') == "failed"


@pytest.mark.get_intel_reports
def test_get_intel_reports_invalid_insight_relevance(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid insight relevance")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_reports',
                                    param_name='insight_relevance',
                                    param_type='text', action_params=params_json['get_intel_reports'])
    assert result.get('status') == "failed"


@pytest.mark.get_intel_reports
def test_get_intel_reports_invalid_motivations(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid motivations")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_reports',
                                    param_name='motivations',
                                    param_type='text', action_params=params_json['get_intel_reports'])
    assert result['data']['total'] == 0


@pytest.mark.get_intel_reports
def test_get_intel_reports_invalid_keyword(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid Keyword")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_reports', param_name='keyword',
                                    param_type='text', action_params=params_json['get_intel_reports'])
    assert result.get('status') == "failed"


@pytest.mark.get_intel_reports
def test_get_intel_reports_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_reports', param_name='page',
                                    param_type='integer', action_params=params_json['get_intel_reports'])
    assert result.get('status') == "failed"


@pytest.mark.get_intel_reports
def test_get_intel_reports_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_reports', param_name='size',
                                    param_type='integer', action_params=params_json['get_intel_reports'])
    assert result.get('status') == "failed"


@pytest.mark.get_intel_report
def test_get_intel_report_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports With Specific Report ID", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_intel_report',
                                   action_params=params_json['get_intel_report']):
        assert result.get('status') == "Success"


@pytest.mark.get_intel_report
def test_validate_get_intel_report_output_schema(cache, valid_configuration_with_token, connector_details,
                                                      info_json, params_json):
    set_report_metadata(connector_details, "Get Reports With Specific Report ID", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_intel_report', info_json, params_json['get_intel_report'])


@pytest.mark.get_intel_report
def test_get_get_intel_report_invalid_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports with Specific Report ID", "Verify with invalid Report ID")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_report', param_name='report_id',
                                    param_type='text', action_params=params_json['get_intel_report'])
    assert result.get('status') == "failed"


@pytest.mark.get_intel_iocs
def test_get_intel_iocs_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IOCs", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_intel_iocs',
                                   action_params=params_json['get_intel_iocs']):
        assert result.get('status') == "Success"


@pytest.mark.get_intel_iocs
def test_validate_get_intel_iocs_output_schema(cache, valid_configuration_with_token, connector_details,
                                               info_json, params_json):
    set_report_metadata(connector_details, "Get IOCs", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_intel_iocs', info_json, params_json['get_intel_iocs'])


@pytest.mark.get_intel_iocs
def test_get_intel_iocs_invalid_report_ids(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IOCs", "Verify with invalid Report ID's")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_iocs', param_name='report_ids',
                                    param_type='text', action_params=params_json['get_intel_iocs'])
    assert result['data']['total'] == 0


@pytest.mark.get_intel_iocs
def test_get_intel_iocs_invalid_ioc_type(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IOCs", "Verify with invalid IOC Type")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_iocs', param_name='type',
                                    param_type='text', action_params=params_json['get_intel_iocs'])
    assert result.get('status') == "failed"


@pytest.mark.get_intel_iocs
def test_get_intel_iocs_invalid_ioc_name(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IOCs", "Verify with invalid IOC name")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_iocs', param_name='name',
                                    param_type='text', action_params=params_json['get_intel_iocs'])
    assert result['data']['total'] == 0


@pytest.mark.get_intel_iocs
def test_get_intel_iocs_invalid_ioc_first_seen(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IOCs", "Verify with invalid IOC first_seen")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_iocs', param_name='first_seen',
                                    param_type='text', action_params=params_json['get_intel_iocs'])
    assert result.get('status') == "failed"


@pytest.mark.get_intel_iocs
def test_get_intel_iocs_invalid_ioc_last_seen(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IOCs", "Verify with invalid IOC last_seen")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_iocs', param_name='last_seen',
                                    param_type='text', action_params=params_json['get_intel_iocs'])
    assert result.get('status') == "failed"


@pytest.mark.get_intel_iocs
def test_get_intel_iocs_invalid_ioc_keyword(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IOCs", "Verify with invalid keyword")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_iocs', param_name='keyword',
                                    param_type='text', action_params=params_json['get_intel_iocs'])
    assert result.get('status') == "failed"


@pytest.mark.get_intel_iocs
def test_get_intel_iocs_invalid_ioc_sort(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IOCs", "Verify with invalid sort ")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_iocs', param_name='sort',
                                    param_type='text', action_params=params_json['get_intel_iocs'])
    assert result['data']['total']


@pytest.mark.get_intel_iocs
def test_get_intel_iocs_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IOCs", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_iocs', param_name='page',
                                    param_type='integer', action_params=params_json['get_intel_iocs'])
    assert result.get('status') == "failed"


@pytest.mark.get_intel_iocs
def test_get_intel_iocs_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IOCs", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_iocs', param_name='size',
                                    param_type='integer', action_params=params_json['get_intel_iocs'])
    assert result.get('status') == "failed"


@pytest.mark.get_intel_ioc
def test_get_intel_ioc_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ioc details for specific Ioc ID", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_intel_ioc',
                                   action_params=params_json['get_intel_ioc']):
        assert result.get('status') == "Success"


@pytest.mark.get_intel_ioc
def test_validate_get_intel_ioc_output_schema(cache, valid_configuration_with_token, connector_details,
                                                      info_json, params_json):
    set_report_metadata(connector_details, "Ioc details for specific Ioc ID with validate schema", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_intel_ioc', info_json, params_json['get_intel_ioc'])


@pytest.mark.get_intel_ioc
def test_get_intel_ioc_invalid_ioc_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Ioc details for specific Ioc ID invalid Iocs id", "Verify with invalid Ioc ID")
    result = run_invalid_param_test(connector_details, operation_name='get_intel_ioc', param_name='ioc_id',
                                    param_type='text', action_params=params_json['get_intel_ioc'])
    assert result.get('status') == "failed"

