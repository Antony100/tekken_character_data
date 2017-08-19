import json
import logging
import os

from nameko.extensions import DependencyProvider

log = logging.getLogger(__name__)

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
FRAMES_PATH = f'{CURRENT_PATH}/frames'
FILE_PATH = '{}/{}.json'


class JsonReader(DependencyProvider):

    def get_dependency(self, worker_ctx):
        return JsonReaderClient()


class JsonReaderError(Exception):
    pass


class JsonReaderClient:

    def load_file(self, name):
        log.info('Attempting to load %s', name)
        try:
            with open(FILE_PATH.format(FRAMES_PATH, name), 'r') as file:
                data = json.load(file)

        except FileNotFoundError as error:
            raise JsonReaderError(error)

        return data

