import configparser
import os


def get_config(section='DEFAULT'):
	config_parser = configparser.ConfigParser()
	config_parser.read('./config.ini')
	return config_parser[section]

def get_token():	
	config = get_config()
	print(os.getenv('SPOTICAST_TOKEN'))
	token = os.getenv('SPOTICAST_TOKEN') or config.get('SPOTICAST_TOKEN')
	return token


print(get_token())

