#import os
import sys
import time
import logging

from watchdog.observers import Observer
#from watchdog.events import LoggingEventHandler
from events.file import CsvEventHandler
from utils.config import Config


class FileWatcher:
    def __init__(self, src_path):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__src_path = src_path
        self.__event_handler = CsvEventHandler()
        self.__event_observer = Observer()

    def run(self):
        print('FileWatcher run')
        self.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def start(self):
        self.__schedule()
        self.__event_observer.start()

    def stop(self):
        self.__event_observer.stop()
        self.__event_observer.join()

    def __schedule(self):
        self.__event_observer.schedule(
            self.__event_handler,
            self.__src_path,
            recursive=True
        )


if __name__ == "__main__":
    config = Config().load()
    src_path = config['sftp_drop_loc']
    FileWatcher(src_path).run()
    print(sys.path)
