# SQLCommand

---

�����ѯ

���麯��������һ�����ݣ� ����һ�����ݷ���һ��ֵ
���麯��AVG, SUM, MIN MAX, COUNT, WM_CONCAT, 
���麯������Ƕ��  MAX(AVG(COLUMN))
���麯�����Զ�����NULL  NVL����ʹ���麯���޷����Կ�ֵ
SELECT COUNT(NVL(COLUMN, 0)) FROM TABLE

�������� 
group by �Ӿ佫���е����ݷ�Ϊ������  
��SELECT�б�������δ�������麯���е��ж�Ӧ�ð�����GROUP BY �Ӿ���
SELECT A, B, C, COUNT(D) FROM TABLE GROUP BY A, B, C
group by �����ǿ   group by rollup(a,b)    <==>    group by a,b  + group a + group by null
 
���˷��� 
having �Ӿ����ڹ��˷���������

where �� having������
where���治���÷��麯�� having����
SQL�Ż��ĽǶ��� ����ʹ��where ��Ϊhaving�ȷ������� where�ȹ��˺����

�������� 
order by �Ӿ�Խ������ Ĭ������ asc  
order by �����ColumnҲ������SELECT LIST INDEX

DISTINCT ����ȥ���ظ��ļ�¼
select distinct(RSMCH1), RLLINE from getresourceinfo a where a.RSMCH1 in ('WB2680', 'WB2681', 'WB2682', 'WB2683', 'WB2684', 'WB2685', 'WB2686')
DISTINCT�����ǽ����еĲ�ͬ����г�����ֻ�ǵ���

---

����ѯ 

�ѿ�����
column = coulumn1 + column2
row = row1 * row2

���ӵ����� 
��ֵ����  =
����ֵ����  between low and high
������ ͨ�������ӣ� �ɶ������������������ļ�¼�� ��Ȼ���������Ľ���� 
�������ӣ� ����������������ʱ�� �Ⱥ���ߵı���Ȼ������
�������ӣ� ����������������ʱ�� �Ⱥ��ұߵı���Ȼ������  �ұ������ڵȺŵ����дһ���Ӻ�   table e , table b  where e.column(+)=b.column 
������ ͨ�������� ��ͬһ�ű���Ϊ���ű�  ������������ ���������� �ѿ���������ʱƽ����
��β�ѯ ? 

---


�Ӳ�ѯ SELECT����Ƕ��

1.�Ӳ�ѯ������С���ű��ʽ��
2.����ʹ���Ӳ�ѯ��λ�� where select having from  ������ʹ���Ӳ�ѯ��λ�� group by 
3.�Ӳ�ѯ������ѯ���Բ���ͬһ�ű� ֻҪ�Ӳ�ѯ�Ľ������ѯ����ʹ��
4.�����Ӳ�ѯֻ��ʹ�õ��в������� �����Ӳ�ѯֻ��ʹ�ö��в�����
5.ע���Ӳ�ѯ�ֵĿ�ֵ����  �����Ӳ�ѯ������null ��Ҫ��not in     a not in (10, 20, null) <==> a!=10 and a!=20 and a!=null     not in <=> all  
6.�Ӳ�ѯʵ��TOP N    select * from (select * from table order by column desc) where rownum<= 3
7.һ����ִ������ѯ����ִ���Ӳ�ѯ������Ӳ�ѯ����

����Ӳ�ѯ
�ڲ���ѯ�����ⲿ��ѯ�ı� �Ӳ�ѯ��ִ�еĴ����������ⲿ��ѯ�� �ⲿ��ÿִ��һ�У��Ӳ�ѯִ��һ��

���в�����
= < > <= >= <>

���в�����
IN �����б��е��κ�һ��
ANY ���Ӳ�ѯ���ص�����һ��ֵ�Ƚ�
ALL ���Ӳ�ѯ���ص�����ֵ�Ƚ�
IN 
and �����ȼ���or��

---

�ַ�������

UPPER ��д
LOWER Сд
INITCAP ����ĸ��д������Сд
LENGTH �ַ�������
SUBSTR �ַ�����ȡ
REPLACE �ַ����滻



�к�ֻ��ʹ�� < <= 
