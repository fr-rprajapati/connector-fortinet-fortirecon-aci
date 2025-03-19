#### Following enhancements have been made to the Fortinet FortiRecon ACI Connector in version 2.0.0: 

- Added following new actions and their playbooks:
   - Get ICL Saved Searches
   - Get ICL Saved Searches By ID
   - Get Leaked Stealers Infections
   - Get Potential Ransomware Victims
   - Get Ransomware Group Information
   - Get Ransomware Intelligence Orgs Watchlist To Monitor
   - Get Ransomware Intelligence Stats
   - Get Ransomware Threat Campaign
   - Get Ransomware Vendors Added For Ransomware Intelligence Monitoring
   - Get Ransomware Vendors Matched
   - Get Ransomware Victim Details By ID
   - Get Ransomware Victims
   - Get Stealers Infections Leaked Count
   - Get Stealers Infections On Sale
   - Get Stealers Infections On Sale Count
   - Get The Matched Organizations For Ransomware Intelligence Monitoring
   - Get The Technical Indicators For The Given Ransomware Group
   - Get Vendor Details By ID
   - Get Vendor Exposures By Vendor ID
   - Get Vendor Watchlist
   - Get Vulnerability Intelligence CVEs
   - Get Vulnerability Intelligence CVEs By ID
   - Get Vulnerability Intelligence Stats For CVE ID
   - Get Vulnerability Intelligence hits By CVE ID
   - Get Vulnerability Intelligence vulnerable products
   - Get Vulnerability Intelligence vulnerable vendors
   - Update Stealers Leaked Status
   - Update Stealers On Sale Marketplaces Status

- The action Get Stealers Log is now deprecated and hence removed. 

- Added a new parameter Get All Records in the action Get IOCs. 

- The following playbooks have been added: 
   - FortiSOAR Threat Intel Feeds Using Threat Intel Report > Create
   - Get FortiRecon ACI Threat Intel Report IOC
   - FortiRecon ACI Threat Intel Report > Fetch

- The following playbooks are now removed:
   - Get Stealers Log
   - Get FortiRecon ACI Report IOC
   - FortiRecon ACI Report > Fetch
   - FortiSOAR Threat Feeds Using FortiRecon ACI Report > Create

- Updated the data ingestion parameters.