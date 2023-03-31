# DB Jupyter Notebooks

This repository contains Jupyter Notebooks that I create for different purposes. These are often of my own creation but will also borrow heavily (with permission) from other notebooks or presentations I have been exposed to. Special recognition goes to Ember Crooks and Mark Gillis (Triton Consulting) for great source material.

**Resources to get you started**
- [datageek.blog - Connecting to Db2 from Jupyter Notebook](https://datageek.blog/en/2017/05/18/connecting-to-db2-from-jupyter-notebook/)
- [Db2 Night Show, Episode 202 - George Baklarz](https://www.dbisoftware.com/db2nightshow/20180202DB2Night202.pdf)
- [Db2 Night Show, Episode 220 - Ember Crooks](https://www.dbisoftware.com/db2nightshow/20191213DB2Night220.pdf)

**Note**: 
Notebooks will utilize a variables file for connection information. The variable file should be in the same directory as the Jupyter Notebook. Comments in the file will provide direction on how to use it.


**Known Issue**:

During a March 2023 notebook update, two bugs were discovered that may require manual intervention when setting up Jupyter notebook for the first time. These issues are documented in two seperate threads - [Python 3.7 Db2 - Symbol Not Found](https://github.com/ibmdb/python-ibmdb/issues/540#issuecomment-1451990285) and [IBM_DB_SA RETRUNS CONDITIONAL](https://stackoverflow.com/questions/75837491/import-ibm-db-sa-fails-with-attributeerror-type-object-string-has-no-attribu).

The first issue may be mac specific and is due to the ibm_sa package and Mac builds of the cli driver. The workaround to this issue is to:

- Reinstall GCC: *brew install gcc*
- Add to user profile (this may e the .zshrc file on a Mac): export DYLD_LIBRARY_PATH='/usr/local/Cellar/gcc/12.2.0/lib/gcc/12:${DYLD_LIBRARY_PATH}'

The second issue is due to the recent release of ibm_db_sa not being copatible with the latest version of SQLAlchemy (2.0). This requires you to downlevel the installed version of SQLAlchemy, which in turns forces a down level of ipython-sql. So your install commands now look like:

- pip3 install ipython-sql==0.4.1
- pip3 install sqlalchemy==1.4.47


**Notebooks**:
 - **General Database Check** : Overall database health, best practices, and performance analysis for a Db2 database.
