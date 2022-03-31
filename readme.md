Processes files according to rules specified in loaded config file. Extensible to allow new file processors.

#### Setup

- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`

#### Config

Sample config.json, path added to configfile env variable

```
{
    "sftp_drop_loc": "/home/username/apps/data/filemanage/sftp/",
    "clients_dir": "/home/username/apps/data/filemanage/clients_ready/",
    "clients": [
       {
            "name": "Client 1",
            "idnumber": "client1",
            "allowed_types": "user,org",
            "processors": "pgp",
            "pgp_public_key": "xoxoxoxoxoxo"
       },
       {
            "name": "Random Client Name",
            "idnumber": "client23",
            "allowed_types": "pos,org",
            "processors": ""
       }
    ]
}
```

#### Run

2 runnable files:

- FileWatcher.py. Always running process, detects new files and renames/moves if valid
- cron.py - Processes files according to clients data in loaded config file
