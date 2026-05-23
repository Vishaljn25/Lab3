import employee_info as ei


def test_get_employees_by_dept():
    department = "Engineering"
    expected_result=[{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    result=ei.get_employees_by_dept(department)
    assert result == expected_result


def test_calculate_average_salary():
   expected_result= (50000+60000+56000+70000+65000+60000)/6
   result=ei.calculate_average_salary()
   assert result == expected_result


def test_get_employees_by_age_range():
    age_lower_limit=34
    age_upper_limit=41
    expected_result= [{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]

    result=ei.get_employees_by_age_range(age_lower_limit, age_upper_limit)
    assert result==expected_result
