from models import Client
from utils.config import Config
from utils.files import get_valid_files, get_client_files
from processors import Rename, Pgp

if __name__ == "__main__":

    # see all env vars
    # print(os.environ)
    try:
        config = Config()
        data = config.load()

        if data is False:
            exit('Invalid data. Exiting..')
    except FileNotFoundError:
        exit(f'Env variable config file not set. Exiting...')
    except OSError:
        exit(f'There was a problem retrieving the data. Exiting...')

    # print(data['sftp_drop_loc'])

    files = get_valid_files(data['sftp_drop_loc'])

    # for file in files:
    #   print(f'Valid file added: {file.name}')
    print(f'B4 clients process files len is {len(files)}')

    # now process clients
    for client_data in data['clients']:
        client_files = get_client_files(client_data['idnumber'], files)
        if len(client_files) == 0:
            continue

        client = Client(client_data, client_files)
        # Processor needs client and config data
        if client.load():
            # client.process()
            processors = client.get_processors()
            for processor_name in processors:
                print(f'processsor name: {processor_name}')
                if processor_name == 'rename':
                    processor = Rename(data, client)
                    processor.execute()
                elif processor_name == 'pgp':
                    processor = Pgp(data, client)
                    processor.execute()
                else:
                    print(f'Unknown processor')

        # Remove client_files from files array
        files = list(set(files) - set(client_files))
