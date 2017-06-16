# -*-coding:utf-8 -*-


import os

import smtplib
from email.mime.text import MIMEText


def compare_2_files(dir1,dir2):
    
    # 获取2个目录下文件数量和所有文件名
    os.chdir(dir1)
    dir1_file_qty = len(os.listdir('.'))
    file_name1 = []
    for x in os.listdir('.'):
        file_name1.append(x)

    os.chdir(dir2)
    dir2_file_qty = len(os.listdir('.'))
    
    file_name2 = []
    for x in os.listdir('.'):
        file_name2.append(x)

    
    # 判断2个目录下文件数量是否为0、数量是否相同、每个文件的大小是否相同
    if dir1_file_qty != 0 and dir2_file_qty !=0:
        if dir1_file_qty == dir2_file_qty:
            print('2个文件夹下的文件数量相同!')

            file_size1=[]
            file_size2=[]

            for x in os.listdir(dir2):
                
                file_size2.append(os.path.getsize(x))

            os.chdir(dir1)

            for x in os.listdir(dir1):
                
                file_size1.append(os.path.getsize(x))



            for x in range(dir1_file_qty):

                if file_size1[x] == file_size2[x]:
                    print(u'所有文件大小相同！')
                else:
                    print(u'以下2个文件大小不同:')
                    print(os.path.abspath(file_name1[x]))
                    os.chdir(dir2)
                    print(os.path.abspath(file_name2[x]))
                    break
        else:

            error_info = [dir1 + ' 中有' + str(dir1_file_qty) + ' 文件（包含文件夹数量）' , dir2 + ' 中有' + str(dir2_file_qty) + ' 文件（包含文件夹数量）']
            error_info = ','.join(error_info)
            send_email(error_info)




    else:
        print(dir1+u' 中有'+str(dir1_file_qty)+u' 文件（包含文件夹数量）')
        print(dir2+u' 中有'+str(dir2_file_qty)+u' 文件（包含文件夹数量）')


def send_email(error_info):

    sender = '348156796@qq.com'  # 发送人
    auth_code = 'qbnjwlqndkbcbjeb'  # 授权码
    receivers = ['1756508746@qq.com, 2629917751@qq.com'] # 收件人
    
    
    msg = MIMEText(error_info)
    msg['Subject'] = u'来自 compare_files.py 脚本异常信息！'
    msg['From'] = sender
    msg['To'] = ','.join(receivers)


    try:
        smtpObj = smtplib.SMTP_SSL('smtp.qq.com',465)
        smtpObj.login(sender, auth_code)
        smtpObj.sendmail(sender, receivers, msg.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException:
        print "Error: 无法发送邮件"

if __name__ == '__main__':

    # 2个文件的目录
    dir1 = r"C:\Users\qlchat.test\Desktop\dir1"  
    dir2 = r"C:\Users\qlchat.test\Desktop\dir2"  

    print '='*20

    compare_2_files(dir1,dir2)


    










    
