# Edit the config_and_params.json file and add the necessary parameter values.
# Ensure that the provided input_params yield the correct output schema.
# Add logic for validating conditional_output_schema or if schema is other than dict.
# Add any specific assertions in each test case, based on the expected response.

"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

import pytest
from testframework.conftest import valid_configuration, invalid_configuration, valid_configuration_with_token,\
    connector_id, connector_details, info_json, params_json
from testframework.helpers.test_helpers import run_health_check_success, run_invalid_config_test, run_success_test,\
    run_output_schema_validation, run_invalid_param_test, set_report_metadata


def run_invalid_param_test_wrapper(connector_details, operation_name, param_name, param_type, action_params):
    result = run_invalid_param_test(connector_details, operation_name, param_name,
                                    param_type, action_params)
    assert result.get('data', {}).get('hits') == []
    assert result.get('status') == 'Success'


@pytest.mark.check_health
def test_check_health_success(valid_configuration, connector_details):
    set_report_metadata(connector_details, "Health Check", "Verify with valid Configuration")
    result = run_health_check_success(valid_configuration, connector_details)
    assert result.get('status') == 'Available'
    

@pytest.mark.check_health
def test_check_health_invalid_org_id(invalid_configuration, connector_id, connector_details, params_json):
    set_report_metadata(connector_details, "Health Check", "Verify with invalid Organization ID")
    result = run_invalid_config_test(invalid_configuration, connector_id, connector_details, param_name='org_id',
                                     param_type='text', config=params_json['config'])
    assert result.get('status') == "Disconnected"
    

@pytest.mark.check_health
def test_check_health_invalid_api_key(invalid_configuration, connector_id, connector_details, params_json):
    set_report_metadata(connector_details, "Health Check", "Verify with invalid API Key")
    result = run_invalid_config_test(invalid_configuration, connector_id, connector_details, param_name='api_key',
                                     param_type='password', config=params_json['config'])
    assert result.get('status') == "Disconnected"
    

@pytest.mark.check_health
def test_check_health_invalid_server_url(invalid_configuration, connector_id, connector_details, params_json):
    set_report_metadata(connector_details, "Health Check", "Verify with invalid Server URL")
    result = run_invalid_config_test(invalid_configuration, connector_id, connector_details, param_name='server_url',
                                     param_type='text', config=params_json['config'])
    assert result.get('status') == "Disconnected"
    

@pytest.mark.get_iocs
def test_get_iocs_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IOCs", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_iocs',
                                   action_params=params_json['get_iocs']):
        assert result.get('status') == "Success"


@pytest.mark.get_iocs
def test_validate_get_iocs_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get IOCs", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_iocs', info_json, params_json['get_iocs'])
    

@pytest.mark.get_iocs
def test_get_iocs_invalid_report_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IOCs", "Verify with invalid Report ID")
    result = run_invalid_param_test(connector_details, operation_name='get_iocs', param_name='report_id',
                                    param_type='text', action_params=params_json['get_iocs'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_iocs
def test_get_iocs_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IOCs", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_iocs', param_name='page',
                                    param_type='integer', action_params=params_json['get_iocs'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_iocs
def test_get_iocs_invalid_ioc_type(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IOCs", "Verify with invalid IOC Type")
    result = run_invalid_param_test(connector_details, operation_name='get_iocs', param_name='ioc_type',
                                    param_type='text', action_params=params_json['get_iocs'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_iocs
def test_get_iocs_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get IOCs", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_iocs', param_name='size',
                                    param_type='integer', action_params=params_json['get_iocs'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_leaked_cards
def test_get_leaked_cards_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Leaked Cards", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_leaked_cards',
                                   action_params=params_json['get_leaked_cards']):
        assert result.get('status') == "Success"


@pytest.mark.get_leaked_cards
def test_validate_get_leaked_cards_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Leaked Cards", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_leaked_cards', info_json, params_json['get_leaked_cards'])
    

@pytest.mark.get_leaked_cards
def test_get_leaked_cards_invalid_bin(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Leaked Cards", "Verify with invalid Bin")
    result = run_invalid_param_test(connector_details, operation_name='get_leaked_cards', param_name='bin',
                                    param_type='text', action_params=params_json['get_leaked_cards'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_leaked_cards
def test_get_leaked_cards_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Leaked Cards", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_leaked_cards', param_name='page',
                                    param_type='integer', action_params=params_json['get_leaked_cards'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_leaked_cards
def test_get_leaked_cards_invalid_type(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Leaked Cards", "Verify with invalid Type")
    result = run_invalid_param_test(connector_details, operation_name='get_leaked_cards', param_name='type',
                                    param_type='text', action_params=params_json['get_leaked_cards'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_leaked_cards
def test_get_leaked_cards_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Leaked Cards", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_leaked_cards', param_name='size',
                                    param_type='integer', action_params=params_json['get_leaked_cards'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_widgets
def test_get_widgets_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Widgets", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_widgets',
                                   action_params=params_json['get_widgets']):
        assert result.get('status') == "Success"


@pytest.mark.get_widgets
def test_validate_get_widgets_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Widgets", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_widgets', info_json, params_json['get_widgets'])
    

@pytest.mark.get_widgets
def test_get_widgets_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Widgets", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_widgets', param_name='size',
                                    param_type='integer', action_params=params_json['get_widgets'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_widgets
def test_get_widgets_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Widgets", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_widgets', param_name='page',
                                    param_type='integer', action_params=params_json['get_widgets'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_osint_feeds
def test_get_osint_feeds_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get OSINT Feeds", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_osint_feeds',
                                   action_params=params_json['get_osint_feeds']):
        assert result.get('status') == "Success"


@pytest.mark.get_osint_feeds
def test_validate_get_osint_feeds_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get OSINT Feeds", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_osint_feeds', info_json, params_json['get_osint_feeds'])


@pytest.mark.get_osint_feeds
def test_get_osint_feeds_invalid_widget_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get OSINT Feeds", "Verify with invalid Widget ID")
    result = run_invalid_param_test(connector_details, operation_name='get_osint_feeds', param_name='widget_id',
                                    param_type='text', action_params=params_json['get_osint_feeds'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_osint_feeds
def test_get_osint_feeds_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get OSINT Feeds", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_osint_feeds', param_name='size',
                                    param_type='integer', action_params=params_json['get_osint_feeds'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_osint_feeds
def test_get_osint_feeds_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get OSINT Feeds", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_osint_feeds', param_name='page',
                                    param_type='integer', action_params=params_json['get_osint_feeds'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_osint_feeds
def test_get_osint_feeds_invalid_keyword(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get OSINT Feeds", "Verify with invalid Keyword")
    result = run_invalid_param_test(connector_details, operation_name='get_osint_feeds', param_name='keyword',
                                    param_type='text', action_params=params_json['get_osint_feeds'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_reports
def test_get_reports_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_reports',
                                   action_params=params_json['get_reports']):
        assert result.get('status') == "Success"


@pytest.mark.get_reports
def test_validate_get_reports_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Reports", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_reports', info_json, params_json['get_reports'])
 

@pytest.mark.get_reports
def test_get_reports_invalid_report_type(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid Report Type")
    result = run_invalid_param_test(connector_details, operation_name='get_reports', param_name='report_type',
                                    param_type='text', action_params=params_json['get_reports'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_reports
def test_get_reports_invalid_information_reliability(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid Information Reliability")
    result = run_invalid_param_test(connector_details, operation_name='get_reports', param_name='information_reliability',
                                    param_type='text', action_params=params_json['get_reports'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_reports
def test_get_reports_invalid_adversary(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid Adversary")
    result = run_invalid_param_test(connector_details, operation_name='get_reports', param_name='adversary',
                                    param_type='text', action_params=params_json['get_reports'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_reports
def test_get_reports_invalid_keyword(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid Keyword")
    result = run_invalid_param_test(connector_details, operation_name='get_reports', param_name='keyword',
                                    param_type='text', action_params=params_json['get_reports'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_reports
def test_get_reports_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_reports', param_name='page',
                                    param_type='integer', action_params=params_json['get_reports'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_reports
def test_get_reports_invalid_industry(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid Industry")
    result = run_invalid_param_test(connector_details, operation_name='get_reports', param_name='industry',
                                    param_type='text', action_params=params_json['get_reports'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_reports
def test_get_reports_invalid_source_reliability(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid Source Reliability")
    result = run_invalid_param_test(connector_details, operation_name='get_reports', param_name='source_reliability',
                                    param_type='text', action_params=params_json['get_reports'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_reports
def test_get_reports_invalid_source_category(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid Source Category")
    result = run_invalid_param_test(connector_details, operation_name='get_reports', param_name='source_category',
                                    param_type='text', action_params=params_json['get_reports'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_reports
def test_get_reports_invalid_tags(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid Tags")
    result = run_invalid_param_test(connector_details, operation_name='get_reports', param_name='tags',
                                    param_type='text', action_params=params_json['get_reports'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_reports
def test_get_reports_invalid_relevance_rating(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid Relevance Rating")
    result = run_invalid_param_test(connector_details, operation_name='get_reports', param_name='relevance_rating',
                                    param_type='text', action_params=params_json['get_reports'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_reports
def test_get_reports_invalid_geography(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid Geography")
    result = run_invalid_param_test(connector_details, operation_name='get_reports', param_name='geography',
                                    param_type='text', action_params=params_json['get_reports'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_reports
def test_get_reports_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_reports', param_name='size',
                                    param_type='integer', action_params=params_json['get_reports'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_reports_with_iocs
def test_get_reports_with_iocs_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports With IOCs", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_reports_with_iocs',
                                   action_params=params_json['get_reports_with_iocs']):
        assert result.get('status') == "Success"


@pytest.mark.get_reports_with_iocs
def test_validate_get_reports_with_iocs_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Reports With IOCs", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_reports_with_iocs', info_json, params_json['get_reports_with_iocs'])
    

@pytest.mark.get_reports_with_iocs
def test_get_reports_with_iocs_invalid_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Reports With IOCs", "Verify with invalid ID")
    result = run_invalid_param_test(connector_details, operation_name='get_reports_with_iocs', param_name='id',
                                    param_type='text', action_params=params_json['get_reports_with_iocs'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_icl_saved_searches
def test_get_icl_saved_searches_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get ICL Saved Searches", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_icl_saved_searches',
                                   action_params=params_json['get_icl_saved_searches']):
        assert result.get('status') == "Success"


@pytest.mark.get_icl_saved_searches
def test_validate_get_icl_saved_searches_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get ICL Saved Searches", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_icl_saved_searches', info_json, params_json['get_icl_saved_searches'])
    

@pytest.mark.get_icl_saved_searches
def test_get_icl_saved_searches_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get ICL Saved Searches", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_icl_saved_searches', param_name='page',
                                    param_type='integer', action_params=params_json['get_icl_saved_searches'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_icl_saved_searches
def test_get_icl_saved_searches_invalid_q(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get ICL Saved Searches", "Verify with invalid Search By Keyword")
    result = run_invalid_param_test(connector_details, operation_name='get_icl_saved_searches', param_name='q',
                                    param_type='text', action_params=params_json['get_icl_saved_searches'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_icl_saved_searches
def test_get_icl_saved_searches_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get ICL Saved Searches", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_icl_saved_searches', param_name='size',
                                    param_type='integer', action_params=params_json['get_icl_saved_searches'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_icl_saved_searches_by_id
def test_get_icl_saved_searches_by_id_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get ICL Saved Searches By ID", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_icl_saved_searches_by_id',
                                   action_params=params_json['get_icl_saved_searches_by_id']):
        assert result.get('status') == "Success"


@pytest.mark.get_icl_saved_searches_by_id
def test_validate_get_icl_saved_searches_by_id_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get ICL Saved Searches By ID", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_icl_saved_searches_by_id', info_json, params_json['get_icl_saved_searches_by_id'])
    

@pytest.mark.get_icl_saved_searches_by_id
def test_get_icl_saved_searches_by_id_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get ICL Saved Searches By ID", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_icl_saved_searches_by_id', param_name='page',
                                    param_type='integer', action_params=params_json['get_icl_saved_searches_by_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_icl_saved_searches_by_id
def test_get_icl_saved_searches_by_id_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get ICL Saved Searches By ID", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_icl_saved_searches_by_id', param_name='size',
                                    param_type='integer', action_params=params_json['get_icl_saved_searches_by_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_icl_saved_searches_by_id
def test_get_icl_saved_searches_by_id_invalid_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get ICL Saved Searches By ID", "Verify with invalid ID")
    result = run_invalid_param_test(connector_details, operation_name='get_icl_saved_searches_by_id', param_name='id',
                                    param_type='integer', action_params=params_json['get_icl_saved_searches_by_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_stealers_infections_leaked_count
def test_get_stealers_infections_leaked_count_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Stealers Infections Leaked Count", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_stealers_infections_leaked_count',
                                   action_params=params_json['get_stealers_infections_leaked_count']):
        assert result.get('status') == "Success"


@pytest.mark.get_stealers_infections_leaked_count
def test_validate_get_stealers_infections_leaked_count_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Stealers Infections Leaked Count", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_stealers_infections_leaked_count', info_json, params_json['get_stealers_infections_leaked_count'])
    

@pytest.mark.get_stealers_infections_leaked_count
def test_get_stealers_infections_leaked_count_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Stealers Infections Leaked Count", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_stealers_infections_leaked_count', param_name='size',
                                    param_type='integer', action_params=params_json['get_stealers_infections_leaked_count'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_stealers_infections_leaked_count
def test_get_stealers_infections_leaked_count_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Stealers Infections Leaked Count", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_stealers_infections_leaked_count', param_name='page',
                                    param_type='integer', action_params=params_json['get_stealers_infections_leaked_count'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_leaked_stealers_infections
def test_get_leaked_stealers_infections_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Leaked Stealers Infections", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_leaked_stealers_infections',
                                   action_params=params_json['get_leaked_stealers_infections']):
        assert result.get('status') == "Success"


@pytest.mark.get_leaked_stealers_infections
def test_validate_get_leaked_stealers_infections_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Leaked Stealers Infections", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_leaked_stealers_infections', info_json, params_json['get_leaked_stealers_infections'])
    

@pytest.mark.get_leaked_stealers_infections
def test_get_leaked_stealers_infections_invalid_affiliated_domain(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Leaked Stealers Infections", "Verify with invalid Affiliated Domain")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_leaked_stealers_infections', param_name='affiliated_domain',
                                    param_type='text', action_params=params_json['get_leaked_stealers_infections'])
    

@pytest.mark.get_leaked_stealers_infections
def test_get_leaked_stealers_infections_invalid_stealer_name(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Leaked Stealers Infections", "Verify with invalid Stealer Name")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_leaked_stealers_infections', param_name='stealer_name',
                                    param_type='text', action_params=params_json['get_leaked_stealers_infections'])
    

@pytest.mark.get_leaked_stealers_infections
def test_get_leaked_stealers_infections_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Leaked Stealers Infections", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_leaked_stealers_infections', param_name='page',
                                    param_type='integer', action_params=params_json['get_leaked_stealers_infections'])
    assert result.get('status') == "failed"


@pytest.mark.get_leaked_stealers_infections
def test_get_leaked_stealers_infections_invalid_q(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Leaked Stealers Infections", "Verify with invalid Search By Keyword")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_leaked_stealers_infections', param_name='q',
                                    param_type='text', action_params=params_json['get_leaked_stealers_infections'])
    

@pytest.mark.get_leaked_stealers_infections
def test_get_leaked_stealers_infections_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Leaked Stealers Infections", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_leaked_stealers_infections', param_name='size',
                                    param_type='integer', action_params=params_json['get_leaked_stealers_infections'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_vendor_exposures_by_id
def test_get_vendor_exposures_by_id_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vendor Details By ID", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_vendor_exposures_by_id',
                                   action_params=params_json['get_vendor_exposures_by_id']):
        assert result.get('status') == "Success"


@pytest.mark.get_vendor_exposures_by_id
def test_validate_get_vendor_exposures_by_id_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Vendor Details By ID", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_vendor_exposures_by_id', info_json, params_json['get_vendor_exposures_by_id'])
    

@pytest.mark.get_vendor_exposures_by_id
def test_get_vendor_exposures_by_id_invalid_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vendor Details By ID", "Verify with invalid ID")
    result = run_invalid_param_test(connector_details, operation_name='get_vendor_exposures_by_id', param_name='id',
                                    param_type='text', action_params=params_json['get_vendor_exposures_by_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_vendor_watchlist
def test_get_vendor_watchlist_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vendor Watchlist", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_vendor_watchlist',
                                   action_params=params_json['get_vendor_watchlist']):
        assert result.get('status') == "Success"


@pytest.mark.get_vendor_watchlist
def test_validate_get_vendor_watchlist_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Vendor Watchlist", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_vendor_watchlist', info_json, params_json['get_vendor_watchlist'])
    

@pytest.mark.get_vendor_watchlist
def test_get_vendor_watchlist_invalid_name(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vendor Watchlist", "Verify with invalid Filter By Name")
    result = run_invalid_param_test(connector_details, operation_name='get_vendor_watchlist', param_name='name',
                                    param_type='text', action_params=params_json['get_vendor_watchlist'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_vendor_watchlist
def test_get_vendor_watchlist_invalid_domain(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vendor Watchlist", "Verify with invalid Filter By Domain")
    result = run_invalid_param_test(connector_details, operation_name='get_vendor_watchlist', param_name='domain',
                                    param_type='text', action_params=params_json['get_vendor_watchlist'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_vendor_watchlist
def test_get_vendor_watchlist_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vendor Watchlist", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_vendor_watchlist', param_name='page',
                                    param_type='integer', action_params=params_json['get_vendor_watchlist'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_vendor_watchlist
def test_get_vendor_watchlist_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vendor Watchlist", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_vendor_watchlist', param_name='size',
                                    param_type='integer', action_params=params_json['get_vendor_watchlist'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_vendor_details_by_id
def test_get_vendor_details_by_id_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vendor Details By ID", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_vendor_details_by_id',
                                   action_params=params_json['get_vendor_details_by_id']):
        assert result.get('status') == "Success"


@pytest.mark.get_vendor_details_by_id
def test_validate_get_vendor_details_by_id_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Vendor Details By ID", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_vendor_details_by_id', info_json, params_json['get_vendor_details_by_id'])
    

@pytest.mark.get_vendor_details_by_id
def test_get_vendor_details_by_id_invalid_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vendor Details By ID", "Verify with invalid ID")
    result = run_invalid_param_test(connector_details, operation_name='get_vendor_details_by_id', param_name='id',
                                    param_type='text', action_params=params_json['get_vendor_details_by_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_vulnerability_intelligence_cves
def test_get_vulnerability_intelligence_cves_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence CVEs", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_vulnerability_intelligence_cves',
                                   action_params=params_json['get_vulnerability_intelligence_cves']):
        assert result.get('status') == "Success"


@pytest.mark.get_vulnerability_intelligence_cves
def test_validate_get_vulnerability_intelligence_cves_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence CVEs", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_vulnerability_intelligence_cves', info_json, params_json['get_vulnerability_intelligence_cves'])
    

@pytest.mark.get_vulnerability_intelligence_cves
def test_get_vulnerability_intelligence_cves_invalid_vendors(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence CVEs", "Verify with invalid Vendors")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_vulnerability_intelligence_cves', param_name='vendors',
                                    param_type='text', action_params=params_json['get_vulnerability_intelligence_cves'])
    

@pytest.mark.get_vulnerability_intelligence_cves
def test_get_vulnerability_intelligence_cves_invalid_keyword(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence CVEs", "Verify with invalid Keyword")
    result = run_invalid_param_test(connector_details, operation_name='get_vulnerability_intelligence_cves', param_name='keyword',
                                    param_type='text', action_params=params_json['get_vulnerability_intelligence_cves'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_vulnerability_intelligence_cves
def test_get_vulnerability_intelligence_cves_invalid_products(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence CVEs", "Verify with invalid Products")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_vulnerability_intelligence_cves', param_name='products',
                                    param_type='text', action_params=params_json['get_vulnerability_intelligence_cves'])
    

@pytest.mark.get_vulnerability_intelligence_cves
def test_get_vulnerability_intelligence_cves_invalid_years(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence CVEs", "Verify with invalid CVE Year")
    result = run_invalid_param_test(connector_details, operation_name='get_vulnerability_intelligence_cves', param_name='years',
                                    param_type='text', action_params=params_json['get_vulnerability_intelligence_cves'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_vulnerability_intelligence_cves
def test_get_vulnerability_intelligence_cves_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence CVEs", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_vulnerability_intelligence_cves', param_name='page',
                                    param_type='integer', action_params=params_json['get_vulnerability_intelligence_cves'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_vulnerability_intelligence_cves
def test_get_vulnerability_intelligence_cves_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence CVEs", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_vulnerability_intelligence_cves', param_name='size',
                                    param_type='integer', action_params=params_json['get_vulnerability_intelligence_cves'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_vulnerability_intelligence_cves_by_id
def test_get_vulnerability_intelligence_cves_by_id_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence CVEs By ID", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_vulnerability_intelligence_cves_by_id',
                                   action_params=params_json['get_vulnerability_intelligence_cves_by_id']):
        assert result.get('status') == "Success"


@pytest.mark.get_vulnerability_intelligence_cves_by_id
def test_validate_get_vulnerability_intelligence_cves_by_id_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence CVEs By ID", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_vulnerability_intelligence_cves_by_id', info_json, params_json['get_vulnerability_intelligence_cves_by_id'])
    

@pytest.mark.get_vulnerability_intelligence_cves_by_id
def test_get_vulnerability_intelligence_cves_by_id_invalid_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence CVEs By ID", "Verify with invalid ID")
    result = run_invalid_param_test(connector_details, operation_name='get_vulnerability_intelligence_cves_by_id', param_name='id',
                                    param_type='text', action_params=params_json['get_vulnerability_intelligence_cves_by_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_vulnerability_intelligence_vulnerable_products
def test_get_vulnerability_intelligence_vulnerable_products_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence vulnerable products", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_vulnerability_intelligence_vulnerable_products',
                                   action_params=params_json['get_vulnerability_intelligence_vulnerable_products']):
        assert result.get('status') == "Success"


@pytest.mark.get_vulnerability_intelligence_vulnerable_products
def test_validate_get_vulnerability_intelligence_vulnerable_products_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence vulnerable products", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_vulnerability_intelligence_vulnerable_products', info_json, params_json['get_vulnerability_intelligence_vulnerable_products'])
    

@pytest.mark.get_vulnerability_intelligence_vulnerable_products
def test_get_vulnerability_intelligence_vulnerable_products_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence vulnerable products", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_vulnerability_intelligence_vulnerable_products', param_name='size',
                                    param_type='integer', action_params=params_json['get_vulnerability_intelligence_vulnerable_products'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_vulnerability_intelligence_vulnerable_products
def test_get_vulnerability_intelligence_vulnerable_products_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence vulnerable products", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_vulnerability_intelligence_vulnerable_products', param_name='page',
                                    param_type='integer', action_params=params_json['get_vulnerability_intelligence_vulnerable_products'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_vulnerability_intelligence_vulnerable_vendors
def test_get_vulnerability_intelligence_vulnerable_vendors_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence vulnerable vendors", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_vulnerability_intelligence_vulnerable_vendors',
                                   action_params=params_json['get_vulnerability_intelligence_vulnerable_vendors']):
        assert result.get('status') == "Success"


@pytest.mark.get_vulnerability_intelligence_vulnerable_vendors
def test_validate_get_vulnerability_intelligence_vulnerable_vendors_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence vulnerable vendors", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_vulnerability_intelligence_vulnerable_vendors', info_json, params_json['get_vulnerability_intelligence_vulnerable_vendors'])
    

@pytest.mark.get_vulnerability_intelligence_vulnerable_vendors
def test_get_vulnerability_intelligence_vulnerable_vendors_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence vulnerable vendors", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_vulnerability_intelligence_vulnerable_vendors', param_name='size',
                                    param_type='integer', action_params=params_json['get_vulnerability_intelligence_vulnerable_vendors'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_vulnerability_intelligence_vulnerable_vendors
def test_get_vulnerability_intelligence_vulnerable_vendors_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence vulnerable vendors", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_vulnerability_intelligence_vulnerable_vendors', param_name='page',
                                    param_type='integer', action_params=params_json['get_vulnerability_intelligence_vulnerable_vendors'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_vulnerability_intelligence_hits_by_cve_id
def test_get_vulnerability_intelligence_hits_by_cve_id_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence hits By CVE ID", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_vulnerability_intelligence_hits_by_cve_id',
                                   action_params=params_json['get_vulnerability_intelligence_hits_by_cve_id']):
        assert result.get('status') == "Success"


@pytest.mark.get_vulnerability_intelligence_hits_by_cve_id
def test_validate_get_vulnerability_intelligence_hits_by_cve_id_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence hits By CVE ID", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_vulnerability_intelligence_hits_by_cve_id', info_json, params_json['get_vulnerability_intelligence_hits_by_cve_id'])
    

@pytest.mark.get_vulnerability_intelligence_hits_by_cve_id
def test_get_vulnerability_intelligence_hits_by_cve_id_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence hits By CVE ID", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_vulnerability_intelligence_hits_by_cve_id', param_name='size',
                                    param_type='integer', action_params=params_json['get_vulnerability_intelligence_hits_by_cve_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_vulnerability_intelligence_hits_by_cve_id
def test_get_vulnerability_intelligence_hits_by_cve_id_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence hits By CVE ID", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_vulnerability_intelligence_hits_by_cve_id', param_name='page',
                                    param_type='integer', action_params=params_json['get_vulnerability_intelligence_hits_by_cve_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_vulnerability_intelligence_hits_by_cve_id
def test_get_vulnerability_intelligence_hits_by_cve_id_invalid_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence hits By CVE ID", "Verify with invalid ID")
    result = run_invalid_param_test(connector_details, operation_name='get_vulnerability_intelligence_hits_by_cve_id', param_name='id',
                                    param_type='integer', action_params=params_json['get_vulnerability_intelligence_hits_by_cve_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_vulnerability_intelligence_stats_for_cve_id
def test_get_vulnerability_intelligence_stats_for_cve_id_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence Stats For CVE ID", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_vulnerability_intelligence_stats_for_cve_id',
                                   action_params=params_json['get_vulnerability_intelligence_stats_for_cve_id']):
        assert result.get('status') == "Success"


@pytest.mark.get_vulnerability_intelligence_stats_for_cve_id
def test_validate_get_vulnerability_intelligence_stats_for_cve_id_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence Stats For CVE ID", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_vulnerability_intelligence_stats_for_cve_id', info_json, params_json['get_vulnerability_intelligence_stats_for_cve_id'])
    

@pytest.mark.get_vulnerability_intelligence_stats_for_cve_id
def test_get_vulnerability_intelligence_stats_for_cve_id_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence Stats For CVE ID", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_vulnerability_intelligence_stats_for_cve_id', param_name='size',
                                    param_type='integer', action_params=params_json['get_vulnerability_intelligence_stats_for_cve_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_vulnerability_intelligence_stats_for_cve_id
def test_get_vulnerability_intelligence_stats_for_cve_id_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence Stats For CVE ID", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_vulnerability_intelligence_stats_for_cve_id', param_name='page',
                                    param_type='integer', action_params=params_json['get_vulnerability_intelligence_stats_for_cve_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_vulnerability_intelligence_stats_for_cve_id
def test_get_vulnerability_intelligence_stats_for_cve_id_invalid_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vulnerability Intelligence Stats For CVE ID", "Verify with invalid ID")
    result = run_invalid_param_test(connector_details, operation_name='get_vulnerability_intelligence_stats_for_cve_id', param_name='id',
                                    param_type='integer', action_params=params_json['get_vulnerability_intelligence_stats_for_cve_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_stealers_infections_on_sale_count
def test_get_stealers_infections_on_sale_count_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Stealers Infections On Sale Count", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_stealers_infections_on_sale_count',
                                   action_params=params_json['get_stealers_infections_on_sale_count']):
        assert result.get('status') == "Success"


@pytest.mark.get_stealers_infections_on_sale_count
def test_validate_get_stealers_infections_on_sale_count_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Stealers Infections On Sale Count", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_stealers_infections_on_sale_count', info_json, params_json['get_stealers_infections_on_sale_count'])
    

@pytest.mark.get_stealers_infections_on_sale_count
def test_get_stealers_infections_on_sale_count_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Stealers Infections On Sale Count", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_stealers_infections_on_sale_count', param_name='size',
                                    param_type='integer', action_params=params_json['get_stealers_infections_on_sale_count'])
    assert result.get('status') == "Success"


@pytest.mark.get_stealers_infections_on_sale_count
def test_get_stealers_infections_on_sale_count_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Stealers Infections On Sale Count", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_stealers_infections_on_sale_count', param_name='page',
                                    param_type='integer', action_params=params_json['get_stealers_infections_on_sale_count'])
    assert result.get('status') == "Success"


@pytest.mark.get_stealers_infections_on_sale
def test_get_stealers_infections_on_sale_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Stealers Infections On Sale", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_stealers_infections_on_sale',
                                   action_params=params_json['get_stealers_infections_on_sale']):
        assert result.get('status') == "Success"


@pytest.mark.get_stealers_infections_on_sale
def test_validate_get_stealers_infections_on_sale_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Stealers Infections On Sale", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_stealers_infections_on_sale', info_json, params_json['get_stealers_infections_on_sale'])
    

@pytest.mark.get_stealers_infections_on_sale
def test_get_stealers_infections_on_sale_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Stealers Infections On Sale", "Verify with invalid Page")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_stealers_infections_on_sale', param_name='page',
                                    param_type='integer', action_params=params_json['get_stealers_infections_on_sale'])
    

@pytest.mark.get_stealers_infections_on_sale
def test_get_stealers_infections_on_sale_invalid_stealers(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Stealers Infections On Sale", "Verify with invalid Stealer Name")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_stealers_infections_on_sale', param_name='stealers',
                                    param_type='text', action_params=params_json['get_stealers_infections_on_sale'])
    

@pytest.mark.get_stealers_infections_on_sale
def test_get_stealers_infections_on_sale_invalid_marketplaces(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Stealers Infections On Sale", "Verify with invalid Marketplace Name")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_stealers_infections_on_sale', param_name='marketplaces',
                                    param_type='text', action_params=params_json['get_stealers_infections_on_sale'])
    

@pytest.mark.get_stealers_infections_on_sale
def test_get_stealers_infections_on_sale_invalid_search_string(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Stealers Infections On Sale", "Verify with invalid Search By Keyword")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_stealers_infections_on_sale', param_name='search_string',
                                    param_type='text', action_params=params_json['get_stealers_infections_on_sale'])
    

@pytest.mark.get_stealers_infections_on_sale
def test_get_stealers_infections_on_sale_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Stealers Infections On Sale", "Verify with invalid Size")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_stealers_infections_on_sale', param_name='size',
                                    param_type='integer', action_params=params_json['get_stealers_infections_on_sale'])
    

@pytest.mark.get_stealers_infections_on_sale
def test_get_stealers_infections_on_sale_invalid_countries(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Stealers Infections On Sale", "Verify with invalid Country Name")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_stealers_infections_on_sale', param_name='countries',
                                    param_type='text', action_params=params_json['get_stealers_infections_on_sale'])
    

@pytest.mark.get_stealers_infections_on_sale
def test_get_stealers_infections_on_sale_invalid_states(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Stealers Infections On Sale", "Verify with invalid State Name")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_stealers_infections_on_sale', param_name='states',
                                    param_type='text', action_params=params_json['get_stealers_infections_on_sale'])
    

@pytest.mark.get_stealers_infections_on_sale
def test_get_stealers_infections_on_sale_invalid_matched_domains(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Stealers Infections On Sale", "Verify with invalid Matched Domain")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_stealers_infections_on_sale', param_name='matched_domains',
                                    param_type='text', action_params=params_json['get_stealers_infections_on_sale'])
    

@pytest.mark.get_stealers_infections_on_sale
def test_get_stealers_infections_on_sale_invalid_isps(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Stealers Infections On Sale", "Verify with invalid ISP Name")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_stealers_infections_on_sale', param_name='isps',
                                    param_type='text', action_params=params_json['get_stealers_infections_on_sale'])
    

@pytest.mark.get_ransomware_victims
def test_get_ransomware_victims_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ransomware Victims", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_ransomware_victims',
                                   action_params=params_json['get_ransomware_victims']):
        assert result.get('status') == "Success"


@pytest.mark.get_ransomware_victims
def test_validate_get_ransomware_victims_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Ransomware Victims", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_ransomware_victims', info_json, params_json['get_ransomware_victims'])
    

@pytest.mark.get_ransomware_victims
def test_get_ransomware_victims_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ransomware Victims", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_ransomware_victims', param_name='page',
                                    param_type='integer', action_params=params_json['get_ransomware_victims'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ransomware_victims
def test_get_ransomware_victims_invalid_ransomware_name(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ransomware Victims", "Verify with invalid Filter By Ransomware Name")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_ransomware_victims', param_name='ransomware_name',
                                    param_type='text', action_params=params_json['get_ransomware_victims'])
    

@pytest.mark.get_ransomware_victims
def test_get_ransomware_victims_invalid_sectors(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ransomware Victims", "Verify with invalid Sectors")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_ransomware_victims', param_name='sectors',
                                    param_type='text', action_params=params_json['get_ransomware_victims'])
    

@pytest.mark.get_ransomware_victims
def test_get_ransomware_victims_invalid_q(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ransomware Victims", "Verify with invalid Search By Keyword")
    result = run_invalid_param_test(connector_details, operation_name='get_ransomware_victims', param_name='q',
                                    param_type='text', action_params=params_json['get_ransomware_victims'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ransomware_victims
def test_get_ransomware_victims_invalid_country(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ransomware Victims", "Verify with invalid Country")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_ransomware_victims', param_name='country',
                                    param_type='text', action_params=params_json['get_ransomware_victims'])
    

@pytest.mark.get_ransomware_victims
def test_get_ransomware_victims_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ransomware Victims", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_ransomware_victims', param_name='size',
                                    param_type='integer', action_params=params_json['get_ransomware_victims'])
    assert result.get('status') == "failed"

@pytest.mark.get_ransomware_victims_details_by_id
def test_get_ransomware_victims_details_by_id_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vendor Details By ID", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_ransomware_victims_details_by_id',
                                   action_params=params_json['get_ransomware_victims_details_by_id']):
        assert result.get('status') == "Success"


@pytest.mark.get_ransomware_victims_details_by_id
def test_validate_get_ransomware_victims_details_by_id_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Vendor Details By ID", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_ransomware_victims_details_by_id', info_json, params_json['get_ransomware_victims_details_by_id'])
    

@pytest.mark.get_ransomware_victims_details_by_id
def test_get_ransomware_victims_details_by_id_invalid_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Vendor Details By ID", "Verify with invalid ID")
    result = run_invalid_param_test(connector_details, operation_name='get_ransomware_victims_details_by_id', param_name='id',
                                    param_type='text', action_params=params_json['get_ransomware_victims_details_by_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ransomware_intel_vendors_watchlist
def test_get_ransomware_intel_vendors_watchlist_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ransomware Victims", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_ransomware_intel_vendors_watchlist',
                                   action_params=params_json['get_ransomware_intel_vendors_watchlist']):
        assert result.get('status') == "Success"


@pytest.mark.get_ransomware_intel_vendors_watchlist
def test_validate_get_ransomware_intel_vendors_watchlist_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Ransomware Victims", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_ransomware_intel_vendors_watchlist', info_json, params_json['get_ransomware_intel_vendors_watchlist'])
    

@pytest.mark.get_ransomware_intel_vendors_watchlist
def test_get_ransomware_intel_vendors_watchlist_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ransomware Victims", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_ransomware_intel_vendors_watchlist', param_name='size',
                                    param_type='integer', action_params=params_json['get_ransomware_intel_vendors_watchlist'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ransomware_intel_vendors_watchlist
def test_get_ransomware_intel_vendors_watchlist_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ransomware Victims", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_ransomware_intel_vendors_watchlist', param_name='page',
                                    param_type='integer', action_params=params_json['get_ransomware_intel_vendors_watchlist'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ransomware_intel_vendors_watchlist_matched
def test_get_ransomware_intel_vendors_watchlist_matched_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ransomware Victims Matched", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_ransomware_intel_vendors_watchlist_matched',
                                   action_params=params_json['get_ransomware_intel_vendors_watchlist_matched']):
        assert result.get('status') == "Success"


@pytest.mark.get_ransomware_intel_vendors_watchlist_matched
def test_validate_get_ransomware_intel_vendors_watchlist_matched_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Ransomware Victims Matched", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_ransomware_intel_vendors_watchlist_matched', info_json, params_json['get_ransomware_intel_vendors_watchlist_matched'])
    

@pytest.mark.get_ransomware_intel_vendors_watchlist_matched
def test_get_ransomware_intel_vendors_watchlist_matched_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ransomware Victims Matched", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_ransomware_intel_vendors_watchlist_matched', param_name='size',
                                    param_type='integer', action_params=params_json['get_ransomware_intel_vendors_watchlist_matched'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ransomware_intel_vendors_watchlist_matched
def test_get_ransomware_intel_vendors_watchlist_matched_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ransomware Victims Matched", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_ransomware_intel_vendors_watchlist_matched', param_name='page',
                                    param_type='integer', action_params=params_json['get_ransomware_intel_vendors_watchlist_matched'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ransomware_intelligence_statistics
def test_get_ransomware_intelligence_statistics_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ransomware Intelligence Stats", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_ransomware_intelligence_statistics',
                                   action_params=params_json['get_ransomware_intelligence_statistics']):
        assert result.get('status') == "Success"


@pytest.mark.get_ransomware_intelligence_statistics
def test_validate_get_ransomware_intelligence_statistics_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Ransomware Intelligence Stats", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_ransomware_intelligence_statistics', info_json, params_json['get_ransomware_intelligence_statistics'])
    

@pytest.mark.get_ransomware_threat_campaigns
def test_get_ransomware_threat_campaigns_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ransomware Victims Matched", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_ransomware_threat_campaigns',
                                   action_params=params_json['get_ransomware_threat_campaigns']):
        assert result.get('status') == "Success"


@pytest.mark.get_ransomware_threat_campaigns
def test_validate_get_ransomware_threat_campaigns_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Ransomware Victims Matched", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_ransomware_threat_campaigns', info_json, params_json['get_ransomware_threat_campaigns'])
    

@pytest.mark.get_ransomware_threat_campaigns
def test_get_ransomware_threat_campaigns_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ransomware Victims Matched", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_ransomware_threat_campaigns', param_name='size',
                                    param_type='integer', action_params=params_json['get_ransomware_threat_campaigns'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ransomware_threat_campaigns
def test_get_ransomware_threat_campaigns_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ransomware Victims Matched", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_ransomware_threat_campaigns', param_name='page',
                                    param_type='integer', action_params=params_json['get_ransomware_threat_campaigns'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ransomware_potential_victims
def test_get_ransomware_potential_victims_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Potential Ransomware Victims", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_ransomware_potential_victims',
                                   action_params=params_json['get_ransomware_potential_victims']):
        assert result.get('status') == "Success"


@pytest.mark.get_ransomware_potential_victims
def test_validate_get_ransomware_potential_victims_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Potential Ransomware Victims", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_ransomware_potential_victims', info_json, params_json['get_ransomware_potential_victims'])
    

@pytest.mark.get_ransomware_potential_victims
def test_get_ransomware_potential_victims_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Potential Ransomware Victims", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_ransomware_potential_victims', param_name='page',
                                    param_type='integer', action_params=params_json['get_ransomware_potential_victims'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ransomware_potential_victims
def test_get_ransomware_potential_victims_invalid_sectors(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Potential Ransomware Victims", "Verify with invalid Sectors")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_ransomware_potential_victims', param_name='sectors',
                                    param_type='text', action_params=params_json['get_ransomware_potential_victims'])
    

@pytest.mark.get_ransomware_potential_victims
def test_get_ransomware_potential_victims_invalid_actor(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Potential Ransomware Victims", "Verify with invalid Filter By Actor Name")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_ransomware_potential_victims', param_name='actor',
                                    param_type='text', action_params=params_json['get_ransomware_potential_victims'])
    

@pytest.mark.get_ransomware_potential_victims
def test_get_ransomware_potential_victims_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Potential Ransomware Victims", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_ransomware_potential_victims', param_name='size',
                                    param_type='integer', action_params=params_json['get_ransomware_potential_victims'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ransomware_potential_victims
def test_get_ransomware_potential_victims_invalid_country(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Potential Ransomware Victims", "Verify with invalid Country")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_ransomware_potential_victims', param_name='country',
                                    param_type='text', action_params=params_json['get_ransomware_potential_victims'])
    

@pytest.mark.get_ransomware_intel_org_watchlist
def test_get_ransomware_intel_org_watchlist_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ransomware Intelligence orgs watchlist to monitor", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_ransomware_intel_org_watchlist',
                                   action_params=params_json['get_ransomware_intel_org_watchlist']):
        assert result.get('status') == "Success"


@pytest.mark.get_ransomware_intel_org_watchlist
def test_validate_get_ransomware_intel_org_watchlist_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Ransomware Intelligence orgs watchlist to monitor", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_ransomware_intel_org_watchlist', info_json, params_json['get_ransomware_intel_org_watchlist'])
    

@pytest.mark.get_ransomware_intel_org_watchlist
def test_get_ransomware_intel_org_watchlist_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ransomware Intelligence orgs watchlist to monitor", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_ransomware_intel_org_watchlist', param_name='size',
                                    param_type='integer', action_params=params_json['get_ransomware_intel_org_watchlist'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ransomware_intel_org_watchlist
def test_get_ransomware_intel_org_watchlist_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ransomware Intelligence orgs watchlist to monitor", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_ransomware_intel_org_watchlist', param_name='page',
                                    param_type='integer', action_params=params_json['get_ransomware_intel_org_watchlist'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ransomware_intel_org_watchlist_matched
def test_get_ransomware_intel_org_watchlist_matched_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get The Matched Organizations For Ransomware Intelligence Monitoring", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_ransomware_intel_org_watchlist_matched',
                                   action_params=params_json['get_ransomware_intel_org_watchlist_matched']):
        assert result.get('status') == "Success"


@pytest.mark.get_ransomware_intel_org_watchlist_matched
def test_validate_get_ransomware_intel_org_watchlist_matched_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get The Matched Organizations For Ransomware Intelligence Monitoring", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_ransomware_intel_org_watchlist_matched', info_json, params_json['get_ransomware_intel_org_watchlist_matched'])
    

@pytest.mark.get_ransomware_intel_org_watchlist_matched
def test_get_ransomware_intel_org_watchlist_matched_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get The Matched Organizations For Ransomware Intelligence Monitoring", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_ransomware_intel_org_watchlist_matched', param_name='size',
                                    param_type='integer', action_params=params_json['get_ransomware_intel_org_watchlist_matched'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ransomware_intel_org_watchlist_matched
def test_get_ransomware_intel_org_watchlist_matched_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get The Matched Organizations For Ransomware Intelligence Monitoring", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_ransomware_intel_org_watchlist_matched', param_name='page',
                                    param_type='integer', action_params=params_json['get_ransomware_intel_org_watchlist_matched'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_technical_indicators_for_given_ransomware_group
def test_get_technical_indicators_for_given_ransomware_group_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get The Matched Organizations For Ransomware Intelligence Monitoring", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_technical_indicators_for_given_ransomware_group',
                                   action_params=params_json['get_technical_indicators_for_given_ransomware_group']):
        assert result.get('status') == "Success"


@pytest.mark.get_technical_indicators_for_given_ransomware_group
def test_validate_get_technical_indicators_for_given_ransomware_group_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get The Matched Organizations For Ransomware Intelligence Monitoring", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_technical_indicators_for_given_ransomware_group', info_json, params_json['get_technical_indicators_for_given_ransomware_group'])
    

@pytest.mark.get_technical_indicators_for_given_ransomware_group
def test_get_technical_indicators_for_given_ransomware_group_invalid_group_name(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get The Matched Organizations For Ransomware Intelligence Monitoring", "Verify with invalid Ransomware Group Name")
    result = run_invalid_param_test(connector_details, operation_name='get_technical_indicators_for_given_ransomware_group', param_name='group_name',
                                    param_type='text', action_params=params_json['get_technical_indicators_for_given_ransomware_group'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_technical_indicators_for_given_ransomware_group
def test_get_technical_indicators_for_given_ransomware_group_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get The Matched Organizations For Ransomware Intelligence Monitoring", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_technical_indicators_for_given_ransomware_group', param_name='size',
                                    param_type='integer', action_params=params_json['get_technical_indicators_for_given_ransomware_group'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_technical_indicators_for_given_ransomware_group
def test_get_technical_indicators_for_given_ransomware_group_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get The Matched Organizations For Ransomware Intelligence Monitoring", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_technical_indicators_for_given_ransomware_group', param_name='page',
                                    param_type='integer', action_params=params_json['get_technical_indicators_for_given_ransomware_group'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ransomware_group_info
def test_get_ransomware_group_info_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ransomware Group Information.", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_ransomware_group_info',
                                   action_params=params_json['get_ransomware_group_info']):
        assert result.get('status') == "Success"


@pytest.mark.get_ransomware_group_info
def test_validate_get_ransomware_group_info_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Ransomware Group Information.", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_ransomware_group_info', info_json, params_json['get_ransomware_group_info'])
    

@pytest.mark.get_ransomware_group_info
def test_get_ransomware_group_info_invalid_group_name(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ransomware Group Information.", "Verify with invalid Ransomware Group Name")
    result = run_invalid_param_test(connector_details, operation_name='get_ransomware_group_info', param_name='group_name',
                                    param_type='text', action_params=params_json['get_ransomware_group_info'])
    assert result.get('status') == "failed"
    

@pytest.mark.update_stealers_leaked_status
def test_update_stealers_leaked_status_invalid_stealers_leaked_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update Stealers Leaked Status", "Verify with invalid Stealers Leaked Record ID")
    result = run_invalid_param_test(connector_details, operation_name='update_stealers_leaked_status', param_name='stealers_leaked_id',
                                    param_type='text', action_params=params_json['update_stealers_leaked_status'])
    assert result.get('status') == "failed"
    

@pytest.mark.update_stealers_on_sale_status
def test_update_stealers_on_sale_status_invalid_stealers_on_sale_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update Stealers On Sale(Marketplaces) Status", "Verify with invalid Stealers On Sale(Marketplaces) Record ID")
    result = run_invalid_param_test(connector_details, operation_name='update_stealers_on_sale_status', param_name='stealers_on_sale_id',
                                    param_type='text', action_params=params_json['update_stealers_on_sale_status'])
    assert result.get('status') == "failed"

