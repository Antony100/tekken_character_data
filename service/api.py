import json
import logging

from nameko.web.handlers import http

from .dependencies.json_reader import JsonReader, JsonReaderError

log = logging.getLogger(__name__)


class CharacterDataService:

    name = "character_data"

    json_reader = JsonReader()

    @http('GET', '/frames/<name>')
    def get_frames(self, requests, name):
        try:
            frames = self.json_reader.load_file(name)

        except JsonReaderError as error:
            log.error(str(error))
            return 404, f'sorry, could not find {name}'

        return json.dumps(frames)
