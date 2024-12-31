# Requirements

| Requirement | Description | Implementation | Type | Phase |
|---|---|---|---|---|
| Near-time price feed | get every 15-60 minutes new 'geizhals' data | Price feed service | data architecture | 1 |
| object store | S3 |  |  | 1 |
| object store | Further progress (open source?) |  |  | 2 |
| configuration management | keep service configurable  (CP, CU; which cloud?; ...) |  |  | 1 |
| configuration management |  |  |  | 2/3 |
| harmonisation of data import | fetch data from DWH and FTP-Server and store in Postgres (CU + CP) | 2 services for data import | data architecture | 1 |
| Near-time transaction data | data from SAP Pro (inventory, costs, ….) |  |  | 2 |
| harmonisation of data bus | data bus / message queue / API | tbd. | data architecture | 2 |
| harmonisation of data export | Export to FTP-server | FTP export | data architecture | 0 |
| harmonisation of data export | transparent API | tbd. | data architecture | 2 |
| PSE voucher algorithm | as is: sript runs within Postgres |  | processing logic | 0 |
| PSE voucher algorithm | to be: NoSQL data handling; batch to event |  | processing logic | 2 |
| dockerization | dockerize services for CI/CD |  | infrastructure | 1 |
| deployment | semi-automatic deployment | Jenkins | infrastructure | 1 |
| deployment | automatic deployment | Jenkins | infrastructure | 2 |
| automated testing | unit, integretation, end-to-end | Jenkins |  | 2 |
| monitoring/logging | go live / operation processes |  |  | 1 |
| service orchestration | multi-cloud  / cloud-agnostic | Kubernetes, minio(?),... | infrastructure | 2 |
| monitoring/logging | stdout, stderr, standardization |  | processing logic | 1 |
| monitoring/logging | central service | logs.io | infrastructure | 2 |
| create infrastructure automatically |  | Terraform or CloudFormation | infrastructure | 1 |
| parameter configuration | script to S3 (equivalent) |  |  | 2 |
| quick wins processing logic |  |  |  | 2 |
| historization in object store | also for configuration files |  |  | 2 |
|  |  |  |  |  |
| replacement channel pilot | as an own service |  |  | 3 |
| scalability / enterprise readiness |  |  |  | 3 |
| documentation guidelines jangtse |  |  |  |  |
| configuration UI | as an own service |  |  | 3 |
| product-related vouchers | 1:1 voucher code - product relation |  |  | 2 |

