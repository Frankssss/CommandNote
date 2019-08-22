# SQLCommand

---

分组查询

分组函数作用于一组数据， 并对一组数据返回一个值
分组函数AVG, SUM, MIN MAX, COUNT, WM_CONCAT, 
分组函数可以嵌套  MAX(AVG(COLUMN))
分组函数会自动忽略NULL  NVL函数使分组函数无法忽略空值
SELECT COUNT(NVL(COLUMN, 0)) FROM TABLE

分组数据 
group by 子句将表中的数据分为若干组  
在SELECT列表中所有未包含在组函数中的列都应该包含在GROUP BY 子句中
SELECT A, B, C, COUNT(D) FROM TABLE GROUP BY A, B, C
group by 语句增强   group by rollup(a,b)    <==>    group by a,b  + group a + group by null
 
过滤分组 
having 子句用于过滤分组后的数据

where 和 having的区别
where后面不能用分组函数 having可以
SQL优化的角度上 尽量使用where 因为having先分组后过滤 where先过滤后分组

分组排序 
order by 子句对结果排序 默认升序 asc  
order by 后面跟Column也可以是SELECT LIST INDEX

DISTINCT 用于去除重复的记录
select distinct(RSMCH1), RLLINE from getresourceinfo a where a.RSMCH1 in ('WB2680', 'WB2681', 'WB2682', 'WB2683', 'WB2684', 'WB2685', 'WB2686')
DISTINCT多列是将多列的不同组合列出，不只是单列

---

多表查询 

笛卡尔集
column = coulumn1 + column2
row = row1 * row2

连接的类型 
等值连接  =
不等值连接  between low and high
外连接 通过外连接， 吧对于连接条件不成立的记录， 仍然包含在最后的结果中 
左外连接， 当连接条件不成立时， 等号左边的标仍然被包含
右外连接， 当连接条件不成立时， 等号右边的标仍然被包含  右边连接在等号的左边写一个加号   table e , table b  where e.column(+)=b.column 
自连接 通过别名， 将同一张表视为多张表  当数据量过大 甚用自连接 笛卡尔集至少时平方集
层次查询 ? 

---


子查询 SELECT语句的嵌套

1.子查询必须在小括号表达式种
2.可以使用子查询的位置 where select having from  不可以使用子查询的位置 group by 
3.子查询和主查询可以不是同一张表， 只要子查询的结果主查询可以使用
4.单行子查询只能使用单行操作符， 多行子查询只能使用多行操作符
5.注意子查询种的空值问题  多行子查询若包含null 不要用not in     a not in (10, 20, null) <==> a!=10 and a!=20 and a!=null     not in <=> all  
6.子查询实现TOP N    select * from (select * from table order by column desc) where rownum<= 3
7.一般先执行主查询，在执行子查询但相关子查询除外

相关子查询
内部查询引用外部查询的表， 子查询的执行的次数依赖于外部查询， 外部传每执行一行，子查询执行一次

单行操作符
= < > <= >= <>

多行操作符
IN 等于列表中的任何一个
ANY 和子查询返回的任意一个值比较
ALL 和子查询返回的所有值比较
IN 
and 的优先级比or高

---

字符串函数

UPPER 大写
LOWER 小写
INITCAP 首字母大写，其余小写
LENGTH 字符串长度
SUBSTR 字符串截取
REPLACE 字符串替换



行号只能使用 < <= 
