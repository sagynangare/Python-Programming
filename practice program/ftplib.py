from ftplib import FTP

ftp = FTP('domainname.com')
ftp.login(user='username', passwd='password')
ftp.cwd('/specificdomain-or-location/')

def grabFile():
    filename = 'fileName.txt'
    localfile = open(filename,'wb')
    ftp.retrbinary('RETR ' + filename, local)
