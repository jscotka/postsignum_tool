# postsignum_tool

This tool helps you to create, send and merge certificates for Ceska posta postsignum via python.
My usecase was to be able to use it with fedora  linux 

## Usage
copy example config to your home dir `cp postsignum_tool.ini ~/.postsignum_tool.ini` and replace it with your variables.
have structure with dirs based on years (tool will read the current year certificates to create new one)
```
2022/
  request.req
  privatekey.key
  certifikat.pem
  certifikat.p12
```
create dir for next year cert e.g. `mkdir 2023; cd 2023` and call the tooling
```bash
# for generating keys
python3 ~/git/postsignum_tool/postsignum_tool/create.py

# for merging keys (you have to copy downloaded PEM file into this dir after postsignum set the key back)
python3 ~/git/postsignum_tool/postsignum_tool/merge.py
```

## Prerequisities

### Required installed packages
```bash
sudo dnf install python3 msmtp openssl
```

### configure msmtp
you can use any post client what allow to send raw messages via pipe, depends on server requirements

For gmail account
```bash

# replace username and password

cat > ~/.msmtprc << EOL
    account username@gmail.com
    host smtp.gmail.com
    port 587
    tls on
    tls_starttls on
    auth on
    user username
    from username@gmail.com
    # https://myaccount.google.com/apppasswords
    password "user pass gene bygo"
    # default account
    account default : username@gmail.com
 
EOL

chmod 600 ~/.msmtprc
```

