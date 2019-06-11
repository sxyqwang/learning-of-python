print('|---欢迎进入通讯录查找程序---|')
print('|-----1:查询联系人资料-----|')
print('|-----2:插入新的联系人-----|')
print('|-----3:删除已有联系人-----|')
print('|-----4:推出通讯录程序-----|')

dict1 = {'小甲鱼':'020-88974651'}
n = 1
while n:
    num = int(input('请输入相关的指令代码：'))
    while (num != 1 and num != 2 and num != 3 and num != 4):
        num = int(input('请重新输入正确代码：'))
    if num == 1:
        name1 = input('请输入联系人姓名：')
        while name1 not in dict1:
            name1 = input('未找到联系人，请重新输入姓名：')
        print(name1, dict1[name1])
    if num == 2:
        name2 = input('请输入联系人姓名：')
        if name2 in dict1:
            print('您输入的用户已存在-->', name2, dict1[name2])
            KEY = input('是否修改用户资料（YES/NO）:')
            while (KEY != 'YES' and KEY != 'NO'):
                KEY = input('输入有误，请重新输入指令：')
            if KEY == 'YES':
                num2 = input('请输入新的联系电话：')
                dict1[name2] = num2
                print('已修改联系人资料')
            if KEY == 'NO':
                print('未修改用户资料')
        else:
            num2 = input('请输入用户联系电话：')
            dict1[name2] = num2
            print('已增加新的联系人：', name2, dict1[name2])
    if num == 3:
        name3 = input('请输入需要删除的联系人：')
        while name3 not in dict1:
            name3 = input('输入有误，请重新输入需要删除的联系人：')
        del dict1[name3]
        print('已删除联系人')
    if num == 4:
        print('|--感谢使用通讯录程序--|')
        n = 0