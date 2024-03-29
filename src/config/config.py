import os
import yaml

DEFAULT_ENV = 'local'

with open(os.path.dirname(os.path.abspath(__file__)) + '/secret.yml', 'r') as yaml_conf:
    conf = yaml.safe_load(yaml_conf)[os.environ.get('APP_ENV', DEFAULT_ENV)]


class Config:
    database = conf['database']


config = Config()
