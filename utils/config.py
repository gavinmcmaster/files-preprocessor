import os
import json
from dotenv import load_dotenv


class Config():
    def __init__(self):
        load_dotenv()

        self.config_file = os.environ.get('configfile')
        print(self.config_file)
        if self.config_file is None:
            raise FileNotFoundError('Env variable configfile not set')

    def load(self):
        try:
            f = open(self.config_file)
            data = json.load(f)

            # print(data)
            # print(type(data)) # dict
            # print(data['sftp_drop_loc'])
            # print(data['clients_dir'])
            # exit()
            f.close()
            if self._is_valid(data):
                return data
            else:
                return False
        except OSError as error:
            print(error)
            return False

    def _is_valid(self, data):
        if "sftp_drop_loc" not in data:
            print(f'SFTP dir location not set. This is required.')
            return False

        if "clients_dir" not in data:
            print(f'Clients dir location not set. This is required.')
            return False

        if "clients" not in data:
            print(f'No clients have been set. This is required.')
            return False

        return True
