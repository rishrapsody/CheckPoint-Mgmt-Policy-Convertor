# CheckPoint-Mgmt-Policy-Convertor

This code converts the input csv file into format acceptable by CheckPoint Management API for Bulk configuration.

Example:
Input csv may contains multiple objects/groups per cell for a column X. In order to configure Policy Package on CheckPoint MDSM server, we need to split column data with multiple objects into new columns.

```
position	Active/New	rule name if group (grp) used	src	port	dst	port (port names)	protocol	action	Logging	comments
1	Active	MDM server to Firewall allow	Host_198.18.251.12	Any	Any	Any	Any	Accept	Log	
2	Active	Firewall to MDM server allow	Any	Any	Host_198.18.251.12	Any	Any	Accept	Log	
3	Active	allow-sgall-to-s4-usw1-prod	GRPNET-ap-sg-rhq-all-001	Any	az-us-usw1-s4-prd-fiori-001; az-us-usw1-s4-lbfe-ps1-ascs-001; az-us-usw1-pwflapp01-001; az-us-usw1-pwflapp02-001; az-us-usw1-ps1lapp10-001; az-us-usw1-ps1lapp11-001	Any	https; sap-ms-3645; sap-disp-3202; sap-disp-3203	Accept	None	
4	Active	allow-sgall-to-mdg-usw1-prod	GRPNET-ap-sg-rhq-all-001	Any	az-us-usw1-mdg-prd-fiori-001; az-us-usw1-mdg-lbfe-pm1-ascs-001; az-us-usw1-pwflapp01-001; az-us-usw1-pwflapp02-001; az-us-usw1-pm1lapp10-001; az-us-usw1-pm1lapp11-001	Any	https; sap-ms-3600	Accept	None	
5	Active	allow-sgall-to-grc-usw1-prod	GRPNET-ap-sg-rhq-all-001	Any	az-us-usw1-pgrlapp01-001	Any	https; sap-disp-3200; sap-gw-3300	Accept	None	
```
