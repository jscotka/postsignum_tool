import os
from datetime import datetime
from pathlib import Path
import configparser

currnet_year = datetime.now().year
CONF_PATH = "~/.postsignum_tool.ini"

config = configparser.ConfigParser()
config.read(os.path.expanduser(CONF_PATH))

serial_number = config["USER"]["serial_number"]
name = config["USER"]["name"]
full_name = config["USER"]["full_name"]
email = config["USER"]["email"]
phone = config["USER"]["phone"]
ic = config["USER"]["ic"]
revocation_pass = config["USER"]["revocation_pass"]

recipient = config["DEFAULT"]["recipient"]
cypher = config["DEFAULT"]["cypher"]
smtp_client = config["DEFAULT"]["smtp_client"]

currnet_year_path = Path.cwd().parent / str(currnet_year)

request_path = "request.req"
private_key_filename = "privatekey.key"
public_cert_filename = "certifikat.pem"
joined_fn = "certifikat.p12"
signer_key_path = currnet_year_path / private_key_filename
signer_cert_path = currnet_year_path / public_cert_filename
mime_message_file = "message.mime"
smime_message_file = "message.smime"


ident = f"/C=CZ/O={full_name} {ic}/OU=1/CN={full_name}/SN={name.split(' ')[1]}/GN={name.split(' ')[0]}/serialNumber={serial_number}/emailAddress={email}/"
plain_msg=f"""
Zadam o vydani nasledneho certifikatu pro tento certifikat:

Seriove cislo: {serial_number}

Vydan certifikacni autoritou: PostSignum QCA VCA.
Vydan podle certifikacni politiky: osobní technologické

Heslo pro zneplatneni nasledneho certifikatu: {revocation_pass} 

KONTAKT: {name} {email} {phone}
"""
