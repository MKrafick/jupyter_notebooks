## CONNECTION_VARIABLES.py | M. Krafick
##      v1 - Aug, 19 2022 | Initial creation
##
## This connection_variables.py file contains basic connection information
## for the General_Database_Check notebook. It should be located in the
## same directory as the notebook file.
##
## To expand connection information for multiple databases - change the
## 'project_' prefix to a specific project name. Then adjust the reference
## in the connection details section to meet your needs. If you have more
## than one project, then duplicate each entry with a unique project name
## and adjust the call in the connection details section.
##
## NOTE: The SCHEMA is not proactively set in this file. Adjust it
## in the connection details of the notebook.


project_inst = {
    'DEV':'db2inst1',
    'QA':'db2inst1',
    'PROD':'db2inst1',
}
project_user = {
    'DEV':'DB2INST1',
    'QA':'DB2INST1',
    'PROD':'DB2INST1',
}
project_host = {
    'DEV':'dns.hostname.com',
    'QA':'dns.hostname.com',
    'PROD':'dns.hostname.com'
}
project_db = {
    'DEV':'DBNAME',
    'QA':'DBNAME',
    'PROD':'DBNAME',
}
project_port = {
    'DEV':'PORTNO',
    'QA':'PORTNO',
    'PROD':'PORTNO'
}
