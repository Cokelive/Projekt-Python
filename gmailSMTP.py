import smtplib
import mimetypes
from email.message import EmailMessage

def sendOnEmail(recvrs, pdfFiles):
    
    user = 'projektauzs@gmail.com'
    password = 'projektauzs123'
    textfile = 'mail.template'
    fromAddr = user
    
    msg = EmailMessage()
    msg['Subject'] = f'Pdf '
    msg['From'] = fromAddr
    msg['To'] = recvrs
    
    with open(textfile) as fp:
        msg.set_content(fp.read())
        
    if type(recvrs) == list:
        recvrs  = ', '.join(recvrs)
    
    
    if type(pdfFiles) == str:
        pdfFiles = [pdfFiles]
    
    for file in pdfFiles:
        ctype, encoding = mimetypes.guess_type(file)
        if ctype is None or encoding is not None:
                ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        with open(file, 'rb') as fp:
            msg.add_attachment(fp.read(),
                               maintype=maintype,
                               subtype=subtype,
                               filename=file)
        

    server = smtplib.SMTP('smtp.gmail.com')
    server.starttls()
    server.login(user, password)
    
    server.set_debuglevel(1)
    
    server.send_message(msg)
    server.quit()
