import glob
import shutil
import subprocess
from constants import *

# get public part
original_fn = glob.glob("QCA*.pem")[0]
shutil.copy(original_fn, public_cert_filename)

cmd = ["openssl", "pkcs12", "-export", "-out", joined_fn, "-inkey", private_key_filename, "-in", public_cert_filename]
out = subprocess.check_output(cmd)

print(f">>>> certificate stored in {joined_fn} : {out}")
