# CheckPoint-Mgmt-Policy-Convertor

This code converts the input csv file into format acceptable by CheckPoint Management API for Bulk configuration.
---

>Example:
>Input csv may contains multiple objects/groups per cell for a column X. In order to configure Policy Package on CheckPoint >MDSM server, we need to split column data with multiple objects into new columns.

```
position	Active/New	rule name if group (grp) used	src	port	dst	port (port names)	protocol	action	Logging	comments
1	Active	MDM server to Firewall allow	Host_198.18.251.12	Any	Any	Any	Any	Accept	Log	
2	Active	Firewall to MDM server allow	Any	Any	Host_198.18.251.12	Any	Any	Accept	Log	
3	Active	allow-sgall-to-s4-usw1-prod	GRPNET-ap-sg-rhq-all-001	Any	az-us-usw1-s4-prd-fiori-001; az-us-usw1-s4-lbfe-ps1-ascs-001; az-us-usw1-pwflapp01-001; az-us-usw1-pwflapp02-001; az-us-usw1-ps1lapp10-001; az-us-usw1-ps1lapp11-001	Any	https; sap-ms-3645; sap-disp-3202; sap-disp-3203	Accept	None	
4	Active	allow-sgall-to-mdg-usw1-prod	GRPNET-ap-sg-rhq-all-001	Any	az-us-usw1-mdg-prd-fiori-001; az-us-usw1-mdg-lbfe-pm1-ascs-001; az-us-usw1-pwflapp01-001; az-us-usw1-pwflapp02-001; az-us-usw1-pm1lapp10-001; az-us-usw1-pm1lapp11-001	Any	https; sap-ms-3600	Accept	None	
5	Active	allow-sgall-to-grc-usw1-prod	GRPNET-ap-sg-rhq-all-001	Any	az-us-usw1-pgrlapp01-001	Any	https; sap-disp-3200; sap-gw-3300	Accept	None	
```


>Output:
>Each column with multiple objects(either separated by '\n' or ';' are divided into new column enteries. Each column now has a >new column name in the format <header_name.X> where X is number

```
position	Active/New	rule name if group (grp) used	src.1	src.2	port	dst.1	dst.2	dst.3	dst.4	dst.5	dst.6	dst.7	dst.8	dst.9	dst.10	dst.11	dst.12	dst.13	dst.14	dst.15	dst.16	protocol	service.1	service.2	service.3	service.4	service.5	service.6	service.7	service.8	service.9	service.10	service.11	service.12	service.13	service.14	action	Logging	comments
1	Active	MDM server to Firewall allow	Host_198.18.251.12	Host_198.18.251.12	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Accept	Log	NA
2	Active	Firewall to MDM server allow	Any	Any	Any	Host_198.18.251.12	Host_198.18.251.12	Host_198.18.251.12	Host_198.18.251.12	Host_198.18.251.12	Host_198.18.251.12	Host_198.18.251.12	Host_198.18.251.12	Host_198.18.251.12	Host_198.18.251.12	Host_198.18.251.12	Host_198.18.251.12	Host_198.18.251.12	Host_198.18.251.12	Host_198.18.251.12	Host_198.18.251.12	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Any	Accept	Log	NA
3	Active	allow-sgall-to-s4-usw1-prod	GRPNET-ap-sg-rhq-all-001	GRPNET-ap-sg-rhq-all-001	Any	az-us-usw1-s4-prd-fiori-001	az-us-usw1-s4-lbfe-ps1-ascs-001	az-us-usw1-pwflapp01-001	az-us-usw1-pwflapp02-001	az-us-usw1-ps1lapp10-001	az-us-usw1-ps1lapp11-001	az-us-usw1-ps1lapp11-001	az-us-usw1-ps1lapp11-001	az-us-usw1-ps1lapp11-001	az-us-usw1-ps1lapp11-001	az-us-usw1-ps1lapp11-001	az-us-usw1-ps1lapp11-001	az-us-usw1-ps1lapp11-001	az-us-usw1-ps1lapp11-001	az-us-usw1-ps1lapp11-001	az-us-usw1-ps1lapp11-001	Any	https	sap-ms-3645	sap-disp-3202	sap-disp-3203	sap-disp-3203	sap-disp-3203	sap-disp-3203	sap-disp-3203	sap-disp-3203	sap-disp-3203	sap-disp-3203	sap-disp-3203	sap-disp-3203	sap-disp-3203	Accept	None	NA
4	Active	allow-sgall-to-mdg-usw1-prod	GRPNET-ap-sg-rhq-all-001	GRPNET-ap-sg-rhq-all-001	Any	az-us-usw1-mdg-prd-fiori-001	az-us-usw1-mdg-lbfe-pm1-ascs-001	az-us-usw1-pwflapp01-001	az-us-usw1-pwflapp02-001	az-us-usw1-pm1lapp10-001	az-us-usw1-pm1lapp11-001	az-us-usw1-pm1lapp11-001	az-us-usw1-pm1lapp11-001	az-us-usw1-pm1lapp11-001	az-us-usw1-pm1lapp11-001	az-us-usw1-pm1lapp11-001	az-us-usw1-pm1lapp11-001	az-us-usw1-pm1lapp11-001	az-us-usw1-pm1lapp11-001	az-us-usw1-pm1lapp11-001	az-us-usw1-pm1lapp11-001	Any	https	sap-ms-3600	sap-ms-3600	sap-ms-3600	sap-ms-3600	sap-ms-3600	sap-ms-3600	sap-ms-3600	sap-ms-3600	sap-ms-3600	sap-ms-3600	sap-ms-3600	sap-ms-3600	sap-ms-3600	Accept	None	NA
```

Cell valis duplicated across remaining column enteries,wherever object/group count is less than max.

---
Process:
1. Convert your .xlxs into .csv format
2. Change the input file path in the pythin script at line no. 105
```df = pd.read_csv("input/Book7.csv")```
3. Make sure pandas is installed. If not, run 'pip install pandas'
4. Execute the script. Output file will be saved in same directory with name 'converted.csv'
5. You can configure policy/access rules in Bulk using CheckPoint MGMT_CLI or PostMan REST API(using external csv data)
---

External Links:

Mgmt REST API: <https://sc1.checkpoint.com/documents/latest/APIs/#web/add-access-rule~v1.8%20>
MGMT_CLI Batch Cmd: <https://supportcenter.checkpoint.com/supportcenter/portal?action=portlets.SearchResultMainAction&eventSubmit_doGoviewsolutiondetails=&solutionid=sk113078>
