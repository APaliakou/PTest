Hello PyTest task

In this task you will create a project for running PyTest and perform basic testing of data from "AdventureWorks2012" database via SQL statements.

# Task:
1. Create 2 DIFFERENT test cases for data checks on "AdventureWorks2012" database (3 different tables) and document them (name, steps, expected results).
Example TC#1 count for column; TC#2 average function for column, TC#3 max\min values, TC#4 values in range of list ...... etc.
Tables to use: 
-[Person].[Address]
-[Production].[Document]
-[Production].[UnitMeasure]
As a result you should have 6 different test cases for 3 different tables (2 per table).
2. Create a project for running Pytest tests.
3. Automate test cases from step 1 so that they can connect to MS SQL DB from SQL Module on your localhost.
4. Store a test report.

# Expected output:
Git project on git.epam.com with test cases file, code project and test report example. 
Please write a meaningful Readme file, that will help to understand how anyone can use your project.

# Helpful links:
- Python SQL Driver https://learn.microsoft.com/en-us/sql/connect/python/pyodbc/python-sql-driver-pyodbc?view=sql-server-ver16
- PyTest https://realpython.com/pytest-python-testing/
- PyTest and SQL https://itnext.io/setting-up-transactional-tests-with-pytest-and-sqlalchemy-b2d726347629
- SQL Connection https://learn.microsoft.com/en-us/sql/connect/jdbc/building-the-connection-url?view=sql-server-ver16
- SQL Create User https://www.tutorialspoint.com/ms_sql_server/ms_sql_server_create_users.htm

# Hints:
- Don't forget to restart MS SQL server after user creation
- Debug connection issues via ERRORLOG of MS SQL Server

# Grades:
1. Test cases are well documented, meaninfull and different - 40 points
2. Pytest project is well structured and all tests work just fine on other machine according to Readme instructions - 40 points
3. Test report is present and easy to use - 10 points.
4. Code is following PEP8 recommendations - 10 points.

Pass grade is 80.
