import os
import subprocess
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from constants import *

# installed openssl, msmtp

print(">>>> generating new key")
req_command = ["openssl", "req", "-out", request_path, "-new", "-newkey", cypher, "-keyout", private_key_filename, "-subj", ident]

subprocess.check_output(req_command)

print(">>>> creating message")
msg_root = MIMEMultipart('mixed')

msg_text = MIMEText(plain_msg, 'plain', 'utf-8')
msg_text.replace_header('content-transfer-encoding', 'quoted-printable')
msg_text.set_payload(plain_msg)
msg_root.attach(msg_text)

fname = os.path.basename(request_path)
with open(request_path, 'rb') as f:
    msg_attach = MIMEBase('application', 'octet-stream')
    msg_attach.set_payload(f.read())
    msg_attach.add_header('Content-Disposition', 'attachment',
                          filename=(Header(fname, 'utf-8').encode()))
    msg_attach.add_header('Content-ID', '<%s>' % (Header(fname)))
    msg_root.attach(msg_attach)


mime_message = msg_root
with open(mime_message_file, "w") as fd:
    fd.write(mime_message.as_string())

print(">>>> signing message with older key")
proc_openssl = subprocess.check_output(["openssl", "smime", "-sign",
                                        "-in", mime_message_file,
                                        "-subject", f"Zadam o vydani nasledneho certifikatu pro tento certifikat: {serial_number}",
                                        "-from", email,
                                        "-to", recipient,
                                        "-signer", str(signer_cert_path),
                                        "-inkey", str(signer_key_path)])

with open(smime_message_file, "wb") as fd:
    fd.write(proc_openssl)

print(">>>> sending message")
print(proc_openssl.decode())
ready = input(f"Are you sure to send email to {recipient} via msmtp (type: yes)")
if "yes" in ready:
    subprocess.check_output(["msmtp", recipient], input=proc_openssl)
