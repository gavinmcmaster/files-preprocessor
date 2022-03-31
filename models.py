from utils.files import File


class Client:
    def __init__(self, data, files):
        self.data = data
        self.files = files

    def load(self):
        #data = json.load(self.json_data)
        # print(self.data)
        # print(type(self.data))

        self.name = self.data['name']
        self.idnumber = self.data['idnumber']
        self.allowed_types = self._get_valid_file_types(
            self.data['allowed_types'].split(','))

        # Base processor for every client
        self.processors = ['rename']

        # Filter out empty values
        processors = list(filter(None, self.data['processors'].split(',')))
        #print(f'processors: {processors}')
        # print(len(processors))

        if len(processors) > 0:
            self.processors = processors + self.processors

        if 'pgp' in self.processors:
            try:
                self.pgp_public_key = self.data['pgp_public_key']
            except KeyError as error:
                print(error)

        return self._validate()

    def get_processors(self):
        return self.processors

    def _validate(self):
        # name and idnumber are set and at least one file type
        if self.name == None or self.idnumber == None or len(self.allowed_types) == 0:
            print('Invalid client config. Skipping...')
            return False
        return True

    def _get_valid_file_types(self, file_types):
        #print(f'_get_allowed_types {file_types}')
        # Ensure duplicates removed
        file_types = list(set(file_types))
        for file_type in file_types:
            if file_type not in File.VALID_TYPES:
                #print(f'remove file type: {file_type}')
                file_types.remove(file_type)
        return file_types
