import pymssql

from checker import *
conn = pymssql.connect(server='127.0.0.1', user='T1000', password='qwerty',
                       database='TRN', port='53424')


def test_column_completeness_department_name_departments():
    assert verify_completeness(collect_result("hr.departments", "department_name", conn)), "department_name column is not " \
                                                                                        "complete "


def test_verify_department_FK():
    """
    Test checks whether all foreign keys are valid and exist

    """
    conn_cursor = conn.cursor()
    conn_cursor.execute("""
        SELECT COUNT(*) count_wrong_FK FROM (
        SELECT a.department_id FROM  hr.employees a
        LEFT JOIN hr.departments s 
        ON a.department_id = s.department_id WHERE s.department_id is NULL) AS t
                              """)
    result = conn_cursor.fetchall()
    assert result[0][0] == 0, "Foreign key is corrupted"


def test_min_value_length_postalcode_locations():
    assert verify_min_length(collect_result("hr.locations", "postal_code", conn), 2),\
        f'PostalCode value is shorter than 2 '


def test_allowed_values_region_id_employees():
    assert verify_allowed_values(collect_result("hr.regions", "region_id", conn), [1, 2, 3, 4]),\
        f'Status contains values that are not expected (1, 2, 3, 4)'


def test_min_value_length_phone_number_employees():
    assert verify_min_length(collect_result("hr.employees", "phone_number", conn), 2),\
        f'Owner value is shorter than 2 '


def test_counts_region_id():
    assert verify_counts(collect_result("hr.regions", "region_id", conn), 4),\
        f'Count of UnitMeasureCode does not equals to 4'


def test_uniqueness_jobTitle():
    assert verify_uniqueness(collect_result("hr.jobs", "job_title", conn)),\
        f'job_title values are not unique'

