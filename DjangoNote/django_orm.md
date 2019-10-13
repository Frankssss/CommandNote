
# ORM object related mapping  对象关系映射 

## ORM总览

### orm 隐藏不同数据库的操作细节，把各个不同数据库的操作用同一套api来实现

正向操作 sql到object的转换
反向操作 object到sql的转换

三类查询

1. 基础查询
	实现对数据表的CRUD操作， 对于select形式的查询操作， django会返回一个query_set, 
	Blog.objects.all()
	Blog.objects.filter(user_id=123)
	Blog.objects.filter(user_id=123).delete()
2. 聚合函数
	1. 为整个的query_set生成聚合值， 支持的函数右Avg, Count, Max, Min等
		Blog.objects.count()
		Blog.objects.filter(user_id=123).count()
		Blog.objects.all().aggregate(Avg('user_id'))
		Blog.objects.all().aggregate(Max('user_id'))
	2. 为查询集的每个对象生成聚合值
		Blog.objects.annotate(tag_count=Count('tag'))
3. Q查询和F查询 
	Q查询： 对对象的复杂查询
		query = (Q(title__startswith='hello') | Q(title__startswith='world')
		Blog.objects.filter(query)
	F查询： 获取对数据库字段值的引用
		Blog.objects.filter(main__contains=F('title'))

		
### orm需要注意的地方
1. 出现filter, exclude, order_by这样的查询的时候考虑在需要的field上加上db_index=True
2. 不需要所有的数据一定要使用limit 而不是拿到整个数据集之后在做切片
3. 使用values_list获取需要的数据，而不是每条数据的所有field
4. 不要使用len(query_set)， 用count()代替，不是使用if query_set， 用exist()代替，不是代替
5. 复杂的查询， 例如表之间的join使用raw_sql代替


## orm核心模块
backends 多数据支持，通用的sql代码， 数据库连接， 管理游标
migrations model的更新触发重建表结构的功能， 即实现了South的功能
models 对象字段类型的提供， 对象管理， 基础查询， 聚合查询

