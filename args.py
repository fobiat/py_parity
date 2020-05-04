# args.py
# Takes input from command args and config file

# Import argparse for commandline arguments
import argparse
# Import configparser for config file support
import configparser
from configparser import ConfigParser

# configuration class for argsparse, configparser
class CONFIGURATION():
    # class variables
    src = []
    dst = []

    # function to grab folders from config file
    # if config.ini FOLDERS are empty, asks for user input
    def conf(self):
        if arg(self) == True:
            parser = configparser.ConfigParser()
            parser.read('config.ini')
        if parser.get('FOLDERS', 'src_folder') == '':
            print("Source folder not defined in config.ini")
        else:
            self.src.append(parser.get('FOLDERS', 'src_folder'))
        if parser.get('FOLDERS', 'dst_folder') == '':
            print("Destination folder not defined in config.ini")
        else:
            self.dst.append(parser.get('FOLDERS', 'dst_folder'))

    # function to input arguments from commandline
    def arg(self):
        ar_parser = argparse.ArgumentParser(add_help=True, description="Sync folder")
        ar_parser.add_argument('--source', action="store")
        ar_parser.add_argument('--destination', action="store")
        ar_parser.add_argument('-c', dest='action', action='store_const', const=CONFIGURATION.conf(self), default=False, help="Uses config file config.ini to input folders automatically.")
#        ar_parser.add_argument('-c', '--config', dest='action', action=CONFIGURATION.conf(self), const=CONFIGURATION.conf, default=False, help="Uses config file config.ini to input folders automatically.")

#        if args.command == 'config':
#            CONFIGURATION.conf()       
        args = ar_parser.parse_args()

configclass = CONFIGURATION()
configclass.arg()
#configclass = CONFIGURATION()
#configclass.arg()
#configclass.conf()
#print(configclass.src)
#print(configclass.dst)


       
    

# argparse config
#def args(self):
#    parser = argparse.ArgumentParser(description="Synchronise folders")
#    parser.add_argument('-c'), '--config', 
    





#parser = argparse.ArgumentParser(description='Synchronise folders and files between locations.')
#parser.add_argument('-c', '--configfile', default="config.ini",help='Read directories from config')
#parser.parse_args()

# Import configparser
#import configparser
#config = configparser.ConfigParser()
#defaults = 'config.ini'
#config.read('config.ini')
#defaults = config['FOLDERS']
#src = config.get('FOLDERS', 'src_folder')
#print(src)

#ef read_config(FOLDERS):
#    configfolders = []
   