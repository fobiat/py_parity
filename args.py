# args.py
# Takes input from command args and config file

# Import argparse for commandline arguments
import argparse
# Import configparser for config file support
import configparser

# configuration class for argsparse, configparser

class Configuration():
    # Constructor for configuration file
    def __init__(self):
        self.conf()

    # class variables
    src = []
    dst = []

    # function to grab folders from config file
    # if config.ini FOLDERS are empty, asks for user input
    def conf(self):
        parser = configparser.ConfigParser()
        parser.read(r'config.ini')

        # Config doesn't contain source
        if not (parser.get('FOLDERS', 'src_folder')):
            print("Source folder not defined in config.ini")
            # Ask the user for input?
        else:
            self.src.append(parser.get('FOLDERS', 'src_folder'))

        # Config doesn't contain destination
        if not (parser.get('FOLDERS', 'dst_folder')):
            print("Destination folder not defined in config.ini")
            # Ask the user for input?
        else:
            self.dst.append(parser.get('FOLDERS', 'dst_folder'))

    # Get input arguments from commandline

    def get_args(self):
        ar_parser = argparse.ArgumentParser(
            add_help=True, description="Sync folder")
        ar_parser.add_argument('--source', action="store")
        ar_parser.add_argument('--destination', action="store")
        ar_parser.add_argument('-c', dest='action', action='store_const', const=Configuration.conf(
            self), default=False, help="Uses config file config.ini to input folders automatically.")

        args = ar_parser.parse_args()


config = Configuration()
config.get_args()
