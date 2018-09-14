from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message
import os

#driver = WhatsAPIDriver(loadstyles=False)
driver = WhatsAPIDriver(client='remote', command_executor=os.environ["SELENIUM"], profile='/app/'+ os.getenv('PHONE_NUMBER'))
print("Waiting for QR")
driver.wait_for_login()

print("Bot started")

try:

    phone_safe = "5585996361001" # Phone number with country code
    phone_whatsapp = "{}@c.us".format(phone_safe) # WhatsApp Chat ID
    image_path = "img.jpg" # Local path file
    caption = "Testing a media sender!" # The caption sent under the image, optional
    
    driver.send_media(image_path, phone_whatsapp, caption) # Expected send_media(self, path, chatid, caption)
    print("Media file was successfully sent to {}".format(phone_whatsapp))
    
except:
    print("Error while trying to send the midia file.")
    print ("Unexpected error:", sys.exc_info())
