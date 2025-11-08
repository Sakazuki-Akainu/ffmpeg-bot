import multiprocessing
import os
from bot.__main__ import app, something
from gunicorn.app.base import BaseApplication

class StandaloneApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

def run_gunicorn():
    port = os.environ.get('PORT', '10000')
    options = {
        'bind': f'0.0.0.0:{port}',
        'workers': 1,
    }
    StandaloneApplication(app, options).run()

if __name__ == '__main__':
    gunicorn_process = multiprocessing.Process(target=run_gunicorn)
    bot_process = multiprocessing.Process(target=something)

    gunicorn_process.start()
    bot_process.start()

    gunicorn_process.join()
    bot_process.join()
