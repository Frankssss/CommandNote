# GitCommand

HEAD �ؼ���ָ��ǰ��֧ĩ�����µ�һ���ύ

branch  ��֧ һ����

tag ��ǩ һ����

git init   
����һ���յ�Git�ֿ�����³�ʼ��һ�����вֿ�

git add <file>  
���������ļ����ӵ��ݴ���

git commit -m <message>  
���ݴ������ļ��������ύ����֧

git add origin master <url>  
����Զ�ֿ̲�

git clone <url>  
��¡Զ�̴洢��

git status  
�鿴�ݴ����͹�������״̬

git log  
�鿴�ύ��־��ʷ��Ϣ

git diff <file>  
�Աȹ��������ݴ����ļ��Ĳ���

git diff HEAD -- <file>  
�鿴�������Ͱ汾������

git diff --staged / git diff --cached  
�Ƚ��ݴ����Ͱ汾�����

git reset HEAD <commit>  
����ǰ��֧HEAD��λ��ָ��״̬

git reset --hard <commit>  
���ݴ����͹���������һ��commit��ĸ��Ķ������� ����HEADָ��<commit>

git rm <file>  
ɾ�����������ݴ������ļ�

git checkout -- <file>  
���ݴ����ļ��ָ���������

git mv <source> <destination>  
�ƶ��������ļ�

git mv <filename> <filename>
�������������ļ�

git branch  
�鿴��ǰ��֧

git branch <branchname>  
������֧

git checkout <branchname>  
�л���ָ����֧

git checkout -b  <branchname>  
�������л�����֧

git merge <branchname>  
�ϲ���֧

git branch -d <branchname>  
ɾ����֧

git tag  
�鿴���б�ǩ

git tag <name>  
����ǰ��֧���ӱ�ǩ

git tag <name> <commit>  
���ύ��ʷ�ӱ�ǩ

git tag -d name  
ɾ����ǩ

git push origin name  
��ǩ����

git config --global alias.st status
���ñ���
