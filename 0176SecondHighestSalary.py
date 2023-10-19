# -- Table: Employee
# --
# -- +-------------+------+
# -- | Column Name | Type |
# -- +-------------+------+
# -- | id          | int  |
# -- | salary      | int  |
# -- +-------------+------+
# -- id is the primary key (column with unique values) for this table.
# -- Each row of this table contains information about the salary of an employee.
# --
# --
# --
# -- Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).
# --
# -- The result format is in the following example.
# --
# --
# --
# -- Example 1:
# --
# -- Input:
# -- Employee table:
# -- +----+--------+
# -- | id | salary |
# -- +----+--------+
# -- | 1  | 100    |
# -- | 2  | 200    |
# -- | 3  | 300    |
# -- +----+--------+
# -- Output:
# -- +---------------------+
# -- | SecondHighestSalary |
# -- +---------------------+
# -- | 200                 |
# -- +---------------------+
# --
# -- Example 2:
# --
# -- Input:
# -- Employee table:
# -- +----+--------+
# -- | id | salary |
# -- +----+--------+
# -- | 1  | 100    |
# -- +----+--------+
# -- Output:
# -- +---------------------+
# -- | SecondHighestSalary |
# -- +---------------------+
# -- | null                |
# -- +---------------------+

import pandas as pd
from pandasql import sqldf

data = {
    'id': [1],
    'salary': [100]
}
Employee = pd.DataFrame(data)

##
query = """
with part as (select distinct salary as SecondHighestSalary from Employee order by SecondHighestSalary desc)
select case
    when
        (select count(*) from part) <= 1
    then
        NULL
    else
        (select SecondHighestSalary FROM part LIMIT 1 OFFSET 1)
    end as SecondHighestSalary;
"""

print(sqldf(query))
