from starlette.config import Config

config = Config('.env')

DEBUG: bool = config('DEBUG', cast=bool, default=False)
