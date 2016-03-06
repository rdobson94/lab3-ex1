import smtplib

fromaddr = 'r.dobson1094@gmail.com'

toaddr  = ['r_dobson@live.com']

#message = """From: {} <{r.dobson1094@gmail.com}>

#To: {To Person} <{r_dobson@live.com}>

#Subject: {SMTP e-mail test}

#{}"""
message = """Test"""
Subject = "Did You actually get this?"
messagetosend = message.format(
                             fromaddr,


                             toaddr,


                             message)

# Credentials (if needed)

username = 'r.dobson1094@gmail.com'

password = 'evix iytx odpe jafp'


# Prepare actual message

message = """\
fromaddr: %s
toaddr: %s
messagetosend: %s
%s
""" % (fromaddr, ", ".join(toaddr), messagetosend, Subject)

# Send the mail

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddr, messagetosend)

server.quit()