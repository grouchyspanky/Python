import smtplib

'sending an email using yahoo'

# Set the server and port
server = smtplib.SMTP('smtp.mail.yahoo.com', 587)

# Start TLS encryption
server.starttls()

# Login to the server (if required)
server.login('jesusojeda@yahoo.com', '')

# Set the email parameters
from_address = 'jesusojeda@yahoo.com'
to_address = 'alexaayala0@gmail.com'
subject = 'Hello'
body ="""Ahoy Matey!

I hope this message finds ye well. Allow me to introduce myself - I am Captain Jesus, notorious pirate of the high seas and proud owner of the world's most impressive pirate hat collection. I've sailed these waters for many a year, and I've seen many a thing. But never have I come across such a fine crew as yours.

I'm writing to ye today with an offer. Ye see, I've recently come into possession of a map that leads to a treasure beyond anyone's wildest dreams. And I'm looking for a crew to join me on this adventure. Ye don't even have to be able to swim - I've got a couple of inflatable ducks we can use as life rafts.

What do ye say? Are ye game? I promise ye a share of the loot and a thrilling voyage. And if ye're really lucky, I might even let ye have a turn steering the ship (just don't tell the parrot). Let me know if ye're interested and we'll set a course for the treasure.

Yours truly,
Captain Jesus"""

# Construct the email
email = f'Subject: {subject}\n\n{body}'

# Send the email
server.sendmail(from_address, to_address, email)

# Disconnect from the server
server.quit()