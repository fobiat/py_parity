# configargparse args2
import configargparse
conf = configargparse.ArgParser(default_config_files=['config.ini'])
conf.add('-c', '--config', required=False, is_config_file=False, help='config file path')

options = conf.parse_args()

