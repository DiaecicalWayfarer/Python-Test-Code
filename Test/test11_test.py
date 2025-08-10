#测试代码

# from test11 import Employee
# def test_give_default_raise():
#     example_employee=Employee("小明","张","150000")
#     example_employee.give_raise()
#     assert example_employee.salary==155000
# def test_give_custom_raise():
#     example_employee=Employee("小明","张","150000")
#     example_employee.give_raise(10000)
#     assert example_employee.salary==160000

# 测试代码2

from test11 import Employee
import pytest
@pytest.fixture
def example_employee():
    example_emoloyee=Employee("小明","张","150000")
    return example_emoloyee
def test_give_default_raise(example_employee):
    example_employee.give_raise()
    assert example_employee.salary==155000
def test_give_custom_raise(example_employee):
    example_employee.give_raise(10000)
    assert example_employee.salary==160000

    
