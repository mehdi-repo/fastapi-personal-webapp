

import smtplib
from email.message import EmailMessage


class SendEmailVerify:

  def sendVerify(token):
    email_address = "Your Email" # type Email
    email_password = "Type password" # Create Gmail

    # create email
    msg = EmailMessage()
    msg['Subject'] = "Email subject"
    msg['From'] = email_address
    msg['To'] = "Your Email" # type Email
    msg.set_content(
       f"""\
<html>
  <head>
    <title>Document</title>
  </head>
  <body>
    <form method="post">
        <a class="signin__link"  href="http://localhost:8080/user/verify/{token}">verify account</a>
      </div>

    </form>
    </div>
  </body>
</html>
    """,
        
    )
    # send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
