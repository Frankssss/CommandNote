# Django Route System

·����ָ��������·��ӳ�䵽��Ӧ�������Ĺ��̡�

·��ģ����ָ����ж���Ĵ���·�ɹ��̵Ĳ��ԣ���·�ɹ���ʵ�ֵ����˼��

namespace app_name name ����
1. ������������ռ�
2. ��֤�������ӳ�䵽Ψһ��URL

django�е�����·��ӳ��ģ��
1. ��ͨurlӳ��
	+ url�Ͷ�Ӧ�Ĵ�����
2. ��̬urlӳ��
	+ url�а�����̬�ɱ������
3. ����urlӳ��
	+ url����url�ļ�·��ָʾ���ļ�

app_name Ӧ�������ռ�
��ʾ���ڲ����Ӧ�õ����ơ�һ��Ӧ�õ�ÿ��ʵ��������ͬ��Ӧ�������ռ�
namespace ʵ�������ռ�
��ʾӦ�õ�һ���ض���ʵ���� ʵ���������ռ���Ψһ�ģ�

path
����URLPattern ������յ���ͼ�����ǿɵ��ö���
����URLResolver ������յ���tuple

include 
����(urlconf_module, app_name, namespace) urlconf_module Ϊurlpatterns�б�

URLResolver.resolve ����ResolveMatch����