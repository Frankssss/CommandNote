# DjangoNote

+ Django2.0��1.11����
	+ ·�ɵı�д��ʽ�������Ϊ�򵥵�path���ʽ ͬʱͨ��re_path���ϼ���
	+ ���Ҫ����on_delete����
	+ ...
	
+ ���û�������
	+ import os
	+ os.environ['DJANGO_SETTINGS_MODULE'] = 'Blog.settings'

+ ��python����������Django shell
	+ import django
	+ django.setup()
	
+ DJANGO ·��ƥ����·�ɷַ���include�� �����ַ��� ����
	+ URLȡ����name���� ���Է������URL�� ����URLƥ��   ����URL��ѯ URL����
		+ ��ͼ�� reverse('name')
		+ ģ���� {% url 'name' %}
		+ orm get_absolute_url
	+ URL�����ռ���Ա�֤���鵽Ψһ��URL
		+ Ӧ�������ռ� ���ֶ��app app_name = "app_name"
		+ ʵ�������ռ� һ��app���Դ������ʵ���� ����ʹ�ö��URLӳ�䵽ͬһ��app  namespace=""
		+ ע�⣺ ��ʹ��ʵ�������ռ�֮ǰ��������ָ��һ��Ӧ�������ռ�

+HTTP
	+HTTP���󷽷�
		+GET�����ض���·����Դ
		+POST��ָ��·����Դ�ύ����
		+OPTIONS 1.��ȡ������֧�ֵ�HTTP���󷽷� 2.������������������
		+DELETE����ɾ��ָ����Դ
		+PUT�������ָ����Դ
		+HEAD
		+TARCE
	+GETPOST����
		+����
			+GET�������ض���·����Դ
			+POSt����ָ��·����Դ�ύ����
		+request�ύ���ݷ�ʽ
			+GET�������û��ύ������key=value����ʽ����&���������һ���Ϊһ�������ַ����� ������ǰ׺������ַ���ƴ�ӵ�URL��
			+POST��������ϱ����ݶ����ǽ��б��룬�������
		+GET��ȫ�ԵͶ�POST��ȫ�Ը���˽�Ժõ���POSTִ��Ч�ʱ�GET��һЩ
		+�������ݴ�С
			HTTPЭ��淶û�ж�URL���Ƚ������ƣ�Ҳû�жԴ�������ݴ�С�������ƣ�
			�����ض�������ͷ�������URL���������ƣ���IE��URL����������2083�ֽ�,		
	+Httpstatuscode
		+400badrequest
		+403httpforbidden
		+500servererror
		+404pagenotfound
		

Fields ������֤���벢ֱ����ģ����ʹ�� widget ������Ⱦ��ҳ��HTML��������Ԫ�غ���ȡ�ύ��ԭʼ����
	








+������������
	1web��������wsgi�������װ�󽻸�web���
	2�м�������������У����������������������������
	3·��ƥ��
	4��ͼ����
	5�м������Ӧ�����ݽ��д���
	6web������(wsgi)����Ӧ�����ݷ��͸������
		
+Django�����ļ��Ƕ��Բ��Ҵ��϶��µĶ�·����
	+MEDIA_ROOT
	+django����template�ļ��ķ���
	+��̬�ļ�
		+STATIC_ROOT���ڲ���̬�ļ�ʱ���еľ�̬�ļ��ۺ�Ŀ¼���Ե�ַ
		+STATICFILES_DIRS�ȵ�STATICFILES_DIRS�趨��Ŀ¼Ѱ�Ҿ�̬�ļ�������ٵ�����app��static�ļ����������
		+STATIC_URL
			+����ǰ׺static_url��ӳ��STATIC_ROOT,STATIC_URL��������STATIC_ROOT��ָ��ľ�̬�ļ�
			+ͨ��ģ���ǩstatic�͸��������·��������һ��URL{%loadstatic%}
		+MEDIA_ROOTsetupload_topath
		+MEDIA_URLͨ��ģ���ǩ�͸��������·������URL

+Django����
	+���淽ʽ
		+ȫ�ֻ������ȴ�
			```	
			MIDDLEWARE[
				'djangomiddlewarecacheUpdateCacheMiddleware',
				
				'djangomiddlewarecacheFetchFromCacheMiddleware',
			]
			```
		+��ͼ������������
			@cache_page(60)
		+ģ�建������С
			```
			{%loadcache%}
			{{now}}
			{%cache60key%}
				{{now}}
			{%endcache%}
			```
	
	+�ļ����漴Ӳ�̻��棬���ݿ�������socketͨ�ţ��ٶȲ��籾���ļ��飬�����ݿ����ݻ���Ҫ��Ⱦ
		```
		CACHES{
			'default':{
				'BACKEND':'djangocorecachebackendsfilebasedFileBasedCache',
				'LOCATION':'D:\cache',
				}
		}
		```
	+���ݿ⻺��:�洢�õ�����Ⱦ�õ��ַ���,ʹ��ǰ���������pythonmanagepycreatecachetable
		```
		CACHES{
			'default':{
				'BACKEND':'djangocorecachebackendsdbDatabaseCache',
				'LOCATION':'my_cache_table',
			}
		}
		```
	+Redis����
		```
		CACHES{
			'default':{
				'BACKEND':'django_rediscacheRedisCache',
				'LOCATION':'redis:127001:6379',
				OPTIONS:{
					CLIENT_CLASS:django_redisclientDefaultClient,
				},
			},
		}
		```

+cookie��Session
	+���ݰ�ȫ
		+cookie��¶��������ˣ����ݲ���ȫ
			```
			set_cookie(self,key,value'',max_ageNone,expiresNone,path'/',
						domainNone,secureFalse,httponlyFalse,samesiteNone)
			```
		+session����cookie���ݱ����ڷ���ˣ��ͻ���ֻ��sessionid��ȫ
			```
			requestsessionusername
			```
	+��С
		+cookie�ڿͻ��˴洢ֵ�д�С��,��Լ��KB,sessionû������


+csrf����
	+�û�����ҳ�棬����˲���һ������ַ�����Ϊtokenֵ��������Session��ͬʱ�����tokenֵ�ŵ�cookie�д��������
	+�û���ָ��·����Դ�ύ���ݻ������tokenֵ��cookie��������У���û���������cookie�е�tokenֵ��session�е�tokenֵ�Ƿ�һ��		
		
+djangomigrations����:
	+makemigrations
		+�ȶ�models�����model��migrations�������model�Աȣ�������µ��޸ģ��������µ�migrations����
	+migrate
		+����ص�Ǩ�ƽű������SQL��䣬�����ݿ���ִ�����SQL���
		+���SQLִ�гɹ�����Ǩ�ƽű������ּ�¼��django_migrations��
	+migrate��ô�ж���ЩǨ�ƽű���Ҫִ��
		+�ȶԴ����е�Ǩ�ƽű������ݿ���django_migrations�е�Ǩ�ƽű����жԱȣ�������ݿ���û�����Ǩ�ƽű�����ô�ͻ�ִ�����Ǩ�ƽű�
	+ִ��migrate��������취
		+�ҵ���ͬ��Ǩ�ƽű�ʹ��fake�������е�Ǩ�ƽű���ӵ�django_migrations���ǲ���ִ��sql
		+�ռ����������ɾ�����ݿ��Լ���������Ǩ���ļ�����makemigrations���migratefakeinitial����ִ��sql
		

+url��ȫslash
	+ĩβ��б��Ĭ��ΪĿ¼������Ŀ¼�µ�Ĭ����ҳ
	+ĩβ����б�ܣ�Ĭ��Ϊ�ļ������Ȼ�����ļ����Ҳ����ļ����Զ��Ķ�ȡ��Ŀ¼�µ�default�ļ�����˿��ܻ��һ���жϵĹ���

+htmlת�壺��html�ؼ���(������ǩ�������ַ���)���й����滻
+
+django�е�ת��https:wwwcnblogscom/MnCu8261/p/5903225html

+�ܵ���|�ɽ�����Ϊ������䴫����Ϣ�Ĺܵ���������ĳ���������������ṩ����һ����������

+djangoģ���ǩ������Ҳ�Ǻ�������ǩ��һ�㼴Ϊ��������Ҫ���ð������������Ⱦģ���Դ��ݹ����Ĳ�������һ�����߼��жϻ����󷵻�
	+djangoģ���ǩ����
		+simple_tag�򵥱�ǩ��������,����һ���ַ������߸�context���û���ӱ���
		+inclusion_tag������ǩ�������ݷ���һ����Ⱦ����ģ��

+url��path��������������(P<name>pattern)name:������;pattern:������ʽ

+modelmeta
	+abstract���嵱ǰģ�����ǲ��ǳ����࣬�����಻��ʵ�����������Ӧ���ݿ��
	+app_labelָ��ģ����������
	+db_table�Զ������ݿ����
	+db_tablespace�������ݿ��ռ�
	+get_latest_byָ�����һ����¼�ǰ����ĸ�field
	+managed���Զ�����ӳ������ݿ��
	+orderingָ���ֶ�����
	+order_with_respect_to
	+permissions
	+verbose_nameģ���������
	+verbose_name_pluralģ�͸�������

+����˵����������״̬�У������κ�һ���࣬���Ƕ��ܹ�֪�����������Щ����������
+CBVgetattr����
+FBVCBV����
	+CBV����˴�����ظ���
	+CBV�����˴���Ŀɶ���
	+CBV��FBV����Զ������̬Mixin
	+CBV���װ����@method_decorator(func)csfttokenװ����ֻ�ܼӵ�dispatch
		1ֱ����ӵ�Dispatch�ϣ�����ÿ����������ִ��
		2��ӵ�ÿһ��������
		3ֱ����ӵ����ϣ������name��ʾ��װ�εķ���
	
+include·��ת�������ַ�������һ�ֽ���ķ�ʽ

+gunicron

+render��������ģ����������������ֵ������һ�𣬲�����Ⱦ���ı�����һ��HttpResponse����

+redirect��һ��HttpResponseRedirect���ص����ݵĲ������ʵ�URL
	+HttpResponseRedirectֻ֧��Ӳ����
	+redirect���ݶ���obj�ض��򣬸�����ͼ�ض���
		+obj�ض���ģ�Ͷ�����get_absolute_urlredirect���Զ�����
		+��ͼ�ض��򣿣�����������https:blogcsdnnet/bluishglc/article/details/7953614
+reverseurl�������

+MTV��֤�˸���������ɢ���

+ORMObjectRelationMapping�����ϵӳ��
	+����
		1���������
		2ʵ��������ģ�������ݿ�Ľ�������˲�ͬ���ݿ�֮��Ĳ���

+�м����������
	+�м����һ����������Django���������Ӧ�Ŀ�ܼ���Ĺ��ӣ�����һ���������ͼ���Ĳ��ϵͳ��������ȫ�ַ�Χ�ڸı�Django������������

+�м�����������
+RequestԤ������process_request
	+ViewԤ������process_view
	+Templateģ����Ⱦ����process_template_response(Ĭ�ϲ�ִ�У�ֻ������ͼ�����ķ��ؽ����������render�����Ż�ִ��)
	+Exception������process_exception��View�����׳�δ��������쳣ʱ�Żᱻ���ã�
	+Response������process_response
	
+�м������
	+processrequest��urlƥ��ǰViewδ֪���������None����request����HttpResponseֱ��ִ�е�ǰmiddleware��process_response������
	+urlƥ������ͼ�������ƺͲ���
	+processview��View����ִ��ǰ��View��֪���������None��������HttpResponseֱ�ӷ���
	+view��View����ִ�к���������Response����

+�źţ�django���ṩ���źŵ��ȣ������ڿ��ִ�в����н���

+django��ʵ��ԭ��SQL

+·��ƥ��ԭ��
	+�����һ���͵ڶ���ͬʱ����ƥ���������ƥ���һ��
	+�����һΪ����ģ��ƥ�䣬�ڶ���Ϊ��ȷƥ�䣬����ƥ���һ��
	

+��������֮��Ĺ�ϵ

+rest_framework

+�������ĳ��÷�ʽ

+�źŵ�����

+querysetʲô�������Q

+on_deletemodelscascade����ɾ��on_updatemodelsmodelscascade��������
+������»�ɾ�������������Ҳ�����һ����»�ɾ��

+ormȡ������
	+usermodelsForeignKey(User,blankTrue,nullTrue,on_deletemodelsSET_NULL)

+��ѯ�����������ԣ�ʲô�Ƕ���ִ��

+��ѯ�����ص��б����������Щ
	+all������������
	+filter������������������
	+exclude������������֮�������
	+order_by����
	


+null��blank����
	+null��������ݿ���ԣ����nullTrue,�������ݿ��еĸ��ֶο���Υ��
	+blank����Ա��ģ����blankTrue��������д���ֶε�ʱ�����Ϊ��

+Tornado�ĺ���ʲô


	
			
+WSGIuwsgiuWSGI����

+djangoʹ��ԭ��SQL
	1
	```
	fromdjangodbimportconnection
		cursorconnectioncursor
		cursorexecute(insertintoblogapp_tag(name)values('tag2'))
	```
	2tagsTagobjectsraw('selectfromblogapp_tag')
	
+Django�в�ѯquerysetʱʲô�������Q

+django�е�model�ļ̳��м�����ʽ

+ormcodefirstdbfirst

+ģ�͵ļ̳�
	+�������
		+�̳�meta����abstractfalseû�й�����
	+���̳�
		+orderingget_latest_by�ᱻ�̳�
	+����ģ��
		+Լ��
			+����ģ�ͱ���̳���һ���ǳ���Ļ��࣬���Ҳ���ͬʱ�̳ж���ǳ������
			+����ģ�Ϳ���ͬʱ�̳�������������࣬ǰ������Щ�������û�ж����κ�ģ���ֶ�
			+����ģ�Ϳ���ͬʱ�̳ж����Ĵ���ģ�ͣ�ǰ������Щ����ģ�ͼ̳�ͬһ���ǳ�����
		+����ģ�ͻ�̳и���Ĺ�����
		
	
+������ࣨAbstractbaseclass�����������������ﶨ���˴����Ա�������ࡣ���麯��ֻ�ṩ�˽ӿڣ���û�о���ʵ��
+������಻�ܱ�ʵ���������ܴ������󣩣�ͨ������Ϊ���๩����̳У���������д�麯����ʵ�־���Ľӿڡ�
+����֮��ABC������������ʹ��һ�����麯���Ľӿڣ���ABC���������ཫ�ṩ������ľ���������ʹ�ó����麯����ʵ�����ֽӿ�
+�麯�������������е�ʱ��̬��ѡ����ʵĳ�Ա����
+���̳о��Ǹ��������е����ı�����ͨ������������ͨ�õķ���

+���ؼ̳кͶ��̳�

+����

+django�ṩ�ķ������URL����
	+ģ��url
	+��ͼreverse
	+ģ��get_absolute_url
	
	+URL�����ռ���Ա�֤���鵽Ψһ��URL
	
+app_namenamespace����
	+app_nameӦ�������ռ䣺��ʾ���ڲ����Ӧ�õ�����
	+namespaceʵ�������ռ䣺��ʾӦ�õ�һ���ض���ʵ��������ʵ���ڽ��д������
	
quick
	
+djangocommand
	+djangoadmincommand
		+djangoadminckeckapp���django��Ŀ��û�г�������
		+
	+pythonmanagepycommand
	+pythonmdjangocommand