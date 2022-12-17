import smtplib

# Set the server and port
server = smtplib.SMTP('smtp.mail.yahoo.com', 587)

# Start TLS encryption
server.starttls()

# Login to the server (if required)
server.login('jesusojeda@yahoo.com', '')

# Set the email parameters
from_address = 'jesusojeda@yahoo.com'
to_address = 'jesusojeda@yahoo.com'
subject = 'Hello'
body = 'Hi there!'

# Construct the email
email = f'Subject: {subject}\n\n{body}'

# Send the email
server.sendmail(from_address, to_address, email)

# Disconnect from the server
server.quit()