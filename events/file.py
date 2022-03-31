import re
import os
from watchdog.events import FileSystemEventHandler
from utils.config import Config


class CsvEventHandler(FileSystemEventHandler):
    CSV_REGEX = "[a-zA-Z]+\d+_(user|pos|org)\.csv"

    def __init__(self):
        super().__init__()

    def on_created(self, event):
        self.process(event)

    def process(self, event):
        matches = re.match(self.CSV_REGEX, event.src_path)

        if matches != None:
            print(matches[0])
            if '/' in event.src_path:
                last_slash = event.src_path.rfind('/')
                filename = event.src_path[last_slash+1:]
            else:
                filename = matches[0]
            file_path = event.src_path
            file_type = filename.split('.')[0].split('_')[1]
        else:
            print('Invalid file name detected ', event.src_path)
            return False

        # check if client directory exists, if not create it
        config = Config().load()
        clients_dir = config['clients_dir']
        client_idnumber = filename.split('_')[0].lower()
        client_dir = clients_dir + f'{client_idnumber}/'
        if not os.path.exists(client_dir):
            os.mkdir(client_dir)

        rename_path = clients_dir + f'{client_idnumber}/{file_type}.csv'
        '''
        print('process file: ', filename)
        print(f'clientid {client_idnumber}')
        print('file type: ', file_type)
        print('process fullpath: ', file_path)
        print('process rename path: ', rename_path)
        '''

        try:
            os.rename(file_path, rename_path)
        except OSError as error:
            print(error)
