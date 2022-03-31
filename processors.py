import os

class Processor:
    def __init__(self, config, client) -> None:
        self.config = config
        self.client = client


class Rename(Processor):
    def __init__(self, config, client) -> None:
        super().__init__(config, client)

    def execute(self):
        print('Rename processor execute')
        clients_dir = self.config['clients_dir']
        sftp_drop_loc = self.config['sftp_drop_loc']
        for file in self.client.files:
            file_type = file.name.split('.')[0].split('_')[1]
            client_dir = clients_dir + f'{self.client.idnumber}/'
            file_path = sftp_drop_loc + file.name
            print(
                f'file type: {file_type}, client_dir: {client_dir}, file_path: {file_path}')
            if not os.path.exists(client_dir):
                os.mkdir(client_dir)

            rename_path = f'{client_dir}{file_type}.csv'
            print(f'rename path: {rename_path}')
            try:
                os.rename(file_path, rename_path)
            except OSError as error:
                print(error)


class Pgp(Processor):
    def __init__(self, config, client) -> None:
        super().__init__(config, client)

    def execute(self):
        print('Pgp processor execute')
        print(f'Pgp KEY: {self.client.pgp_public_key}')
