# MC-Handler
Minecraft Server Web Interface

## Intall

The following insttruction will guide you to install the MC-Handler.

> git clone https://github.com/Couapy/MC-Handler.git

### Create user minecraft

To create the minecraft user, please run :

> adduser --system --shell /bin/bash --home /opt/minecraft --group minecraft

### Add servers

> mkdir /opt/minecraft/servers

Place the servers in `/opt/minecraft/servers/`

### Create minecraft service

Copy the service to the systemd service folder :

> cp MC-Handler/minecraft/minecraft@.service /etc/systemd/system/minecraft@.service

### Install the website

Its depends on yours system : apache or nginx.

So I let you apply your skills ;), the website root is **MC-Handler/mchandler/**.

You must create a config file **config.cfg** like this :

```ini
[DJANGO]
SECRET_KEY = your_key_here

[GOOGLE]
KEY = your_key_here
SECRET = your_secret_key_here

[GITHUB]
KEY = your_key_here
SECRET = your_secret_key_here
```

### Give permissions

Add this ligne to `/etc/sudoers` (the user can be different, be carful)

> www-data ALL=(ALL) NOPASSWD:ALL
