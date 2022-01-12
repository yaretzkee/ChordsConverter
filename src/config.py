import json
import pathlib
from types import SimpleNamespace


class Config:
    def __init__(self, config_file=None):
        if not config_file:
            config_file = pathlib.Path(__file__).parents[1].joinpath('config.json')
        
        with open(file=config_file, mode='r', encoding='utf-8') as f:
            self.config = json.load(f, object_hook=lambda d: SimpleNamespace(**d))


if __name__ == '__main__':
    # for testing purpose only
    c = Config()
    print(c.config)
    