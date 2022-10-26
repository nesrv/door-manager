from enum import Enum
from environs import Env

env = Env()
env.read_env()

# logging
LOG_LEVEL = env.enum(
    'LOG_LEVEL',
    type=Enum('LOG_LEVEL', 'DEBUG INFO WARNING ERROR CRITICAL'),
    ignore_case=True,
    default='INFO',
).name

JWT_ALGORITHM = env.str('JWT_ALGORITHM', 'RS256')
JWT_PRIVATE_KEY = env.str('JWT_PRIVATE_KEY')

HTTP_LISTEN_HOST = env.str('HTTP_LISTEN_HOST', '127.0.0.1')
HTTP_LISTEN_PORT = env.int('HTTP_LISTEN_PORT', 8000)
CONTROLLER_URL = f'http://{HTTP_LISTEN_HOST}:{HTTP_LISTEN_PORT}'

CONTROLLERS = [
    {'name': "Qotto", 'url': "http://127.0.0.1:8000"},
    {'name': "RBMG", 'url': "http://127.0.0.1:8001"},
]
