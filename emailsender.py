import smtplib,re,os,xlrd
from email.mime.text import MIMEText

#read the configs
fp = open("mail_account.conf", 'r')
configs = re.findall(r"([\w\.]+)=(.*)",fp.read())
fp.close()
confs = {}
for config in configs:
    confs[config[0]] = config[1]

def send_mail(recipient,sub,msg):
    msg = MIMEText(msg,_subtype='plain',_charset='utf8')
    msg['Subject'] = sub
    msg['From'] = confs["smtp.user"]
    msg['To'] = recipient

    try:
        s = smtplib.SMTP()
        s.connect(confs["smtp.host"])
        s.login(confs["smtp.user"],confs["smtp.pass"])
        s.sendmail(msg['From'], [msg['To']], msg.as_string())
        s.quit()
        return True
    except Exception, e:
        print str(e)
        return False

if __name__ == '__main__':
    #read the template and build the msg
    log = open("log.txt","a")
    log.write("\n\n###################################\r\n")
    log.write("emailsender log start:\r\n\r\n")
    fp = open("template.txt", 'r')
    template = fp.read()
    fp.close()
    data = xlrd.open_workbook('data.xls')
    table = data.sheets()[0]
    users = []
    for j in range(table.nrows - 1):
        users.append({});        
        for i in range(table.ncols):
            key = str(table.cell(0,i).value)          
            value = table.cell(j+1,i).value
            if type(value) is float:
                value = str(value)
            else: 
                value = str(value.encode("utf8"))
            users[j][key] = value
    for user in users:
        sub = 'The %s score for the Programming Languages course' % user["workname"]
        msg = template
        for key in user.keys():
            msg = msg.replace("{%s}" % key,user[key])
        if send_mail(user["email"],sub,msg):
            print user["email"], " send success"
            log.write(user["name"] + " " + user["email"] + " send success\r\n")
        else:
            print user["email"], " send failed"
            log.write(user["name"] + " " + user["email"] + " send failed\r\n")
    print "All Task Finished! You can check the log.txt for more detail. ^_^\n"
    print "***********************"
    print "email sender, by Wu Jiang @ IST lab, SJTU"
    print "If you have any problem with this script, please contact wujiang007@gmail.com"

                      
