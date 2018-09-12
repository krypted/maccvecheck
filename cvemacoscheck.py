#!/usr/bin/python
import sys, urllib, json, os, platform
if len(sys.argv) > 1:
	url = 'https://cve.circl.lu/api/search/apple/mac_os_x:{}'.format(sys.argv[1])
	print([j['id'] for j in json.loads(urllib.urlopen(url).read().decode('utf-8'))])
else:
	version = platform.mac_ver()
	url = 'https://cve.circl.lu/api/search/apple/mac_os_x:{}'.format(version[0])
	print([j['id'] for j in json.loads(urllib.urlopen(url).read().decode('utf-8'))])
