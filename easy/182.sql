# Write your MySQL query statement below
select Email from Person group by Email having count(Email)>1;
-- 在 SQL 中增加 HAVING 子句原因是，WHERE 关键字无法与聚合函数一起使用。
-- HAVING 子句可以让我们筛选分组后的各组数据。
-- GROUP BY 语句用于结合聚合函数，根据一个或多个列对结果集进行分组。