"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""
from .aci_operations.osint import get_widgets, get_osint_feeds
from .aci_operations.iocs import get_iocs
from .aci_operations.leaked_cards import get_leaked_cards
from .aci_operations.stealers_leaked import (get_stealers_infections_leaked_count,
                                             get_leaked_stealers_infections,
                                             update_stealers_leaked_status)
from .aci_operations.reports import get_reports, get_reports_with_iocs
from .aci_operations.vulnerability_intelligence import (get_vulnerability_intelligence_cves,
                                                        get_vulnerability_intelligence_cves_by_id,
                                                        get_vulnerability_intelligence_vulnerable_products,
                                                        get_vulnerability_intelligence_vulnerable_vendors,
                                                        get_vulnerability_intelligence_hits_by_cve_id,
                                                        get_vulnerability_intelligence_stats_for_cve_id)
from .aci_operations.stealers_on_sale import (get_stealers_infections_on_sale_count,
                                              get_stealers_infections_on_sale,
                                              update_stealers_on_sale_status)
from .aci_operations.icl import get_icl_saved_searches, get_icl_saved_searches_by_id
from .aci_operations.vendor_monitoring import (get_vendor_watchlist,
                                               get_vendor_details_by_id,
                                               get_vendor_exposures_by_id)
from .aci_operations.ransomware_intelligence import (get_ransomware_victims,
                                                     get_ransomware_victims_details_by_id,
                                                     get_ransomware_intel_vendors_watchlist,
                                                     get_ransomware_intel_vendors_watchlist_matched,
                                                     get_ransomware_intelligence_statistics,
                                                     get_ransomware_threat_campaigns,
                                                     get_ransomware_potential_victims,
                                                     get_ransomware_intel_org_watchlist,
                                                     get_ransomware_intel_org_watchlist_matched,
                                                     get_technical_indicators_for_given_ransomware_group,
                                                     get_ransomware_group_info)
from .aci_operations.intel_reports import get_intel_reports, get_intel_report, get_intel_iocs, get_intel_ioc


operations = {
    "get_iocs": get_iocs,
    "get_leaked_cards": get_leaked_cards,
    "get_widgets": get_widgets,
    "get_osint_feeds": get_osint_feeds,
    "get_reports": get_reports,
    "get_reports_with_iocs": get_reports_with_iocs,
    "get_icl_saved_searches": get_icl_saved_searches,
    "get_icl_saved_searches_by_id": get_icl_saved_searches_by_id,
    "get_stealers_infections_leaked_count": get_stealers_infections_leaked_count,
    "get_leaked_stealers_infections": get_leaked_stealers_infections,
    "get_vendor_details_by_id": get_vendor_details_by_id,
    "get_vendor_watchlist": get_vendor_watchlist,
    "get_vendor_exposures_by_id": get_vendor_exposures_by_id,
    "get_vulnerability_intelligence_cves": get_vulnerability_intelligence_cves,
    "get_vulnerability_intelligence_cves_by_id": get_vulnerability_intelligence_cves_by_id,
    "get_vulnerability_intelligence_vulnerable_products": get_vulnerability_intelligence_vulnerable_products,
    "get_vulnerability_intelligence_vulnerable_vendors": get_vulnerability_intelligence_vulnerable_vendors,
    "get_vulnerability_intelligence_hits_by_cve_id": get_vulnerability_intelligence_hits_by_cve_id,
    "get_vulnerability_intelligence_stats_for_cve_id": get_vulnerability_intelligence_stats_for_cve_id,
    "get_stealers_infections_on_sale_count": get_stealers_infections_on_sale_count,
    "get_stealers_infections_on_sale": get_stealers_infections_on_sale,
    "get_ransomware_victims": get_ransomware_victims,
    "get_ransomware_victims_details_by_id": get_ransomware_victims_details_by_id,
    "get_ransomware_intel_vendors_watchlist": get_ransomware_intel_vendors_watchlist,
    "get_ransomware_intel_vendors_watchlist_matched": get_ransomware_intel_vendors_watchlist_matched,
    "get_ransomware_intelligence_statistics": get_ransomware_intelligence_statistics,
    "get_ransomware_threat_campaigns": get_ransomware_threat_campaigns,
    "get_ransomware_potential_victims": get_ransomware_potential_victims,
    "get_ransomware_intel_org_watchlist": get_ransomware_intel_org_watchlist,
    "get_ransomware_intel_org_watchlist_matched": get_ransomware_intel_org_watchlist_matched,
    "get_technical_indicators_for_given_ransomware_group": get_technical_indicators_for_given_ransomware_group,
    "get_ransomware_group_info": get_ransomware_group_info,
    "update_stealers_on_sale_status": update_stealers_on_sale_status,
    "update_stealers_leaked_status": update_stealers_leaked_status,
    "get_intel_reports": get_intel_reports,
    "get_intel_report": get_intel_report,
    "get_intel_iocs": get_intel_iocs,
    "get_intel_ioc": get_intel_ioc
}
