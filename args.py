# args.py
# takes input from command args and config file

# Import argparse for commandline arguments
import argparse
# Import configparser for config file support
import configparser
from configparser import ConfigParser

# configuration class for both
class CONFIGURATION():
    # class variables
    src = []
    dst = []
    # function to grab folders from config file
    def conf(self):
        parser = configparser.ConfigParser()
        parser.read('config.ini')
        self.src.append(parser.get('FOLDERS', 'src_folder'))
        self.dst.append(parser.get('FOLDERS', 'dst_folder'))
configclass = CONFIGURATION()
configclass.conf()
print(configclass.src)
print(configclass.dst)

#config = CONFIGURATION()
#print config.conf.parser.get('FOLDERS', src_folder)
#print self.parser.get('FOLDERS', dst_folder)

#config = CONFIGURATION()
#config.conf.src()
#print(CONFIGURATION.config.src)
        
        
    

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
   