from Config import Config
from services.EventService import EventService
from flask_script import Server
from log import setup_logger
import logging
import requests

from services.ComponentService import ComponentService

setup_logger('root')
logger = logging.getLogger('root')


class FlaskServer(Server):
    def __call__(self, app, *args, **kwargs):
        self.init()
        return Server.__call__(self, app, *args, **kwargs)

    @staticmethod
    def register_listeners():
        ComponentService.left_distance_sensor.triggered = EventService.sendDistanceSensorEvent
        # ComponentService.left_distance_sensor.triggered = EventService.sendDistanceSensorEvent

    @staticmethod
    def init():
        FlaskServer.register_listeners()
        requests.post(f'{Config.externalServerUrl}/numbers/{Config.roomNumber}/register', headers={'API-Key': Config.apiKey})
