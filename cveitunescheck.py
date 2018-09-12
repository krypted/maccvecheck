#!/usr/bin/python
import sys, urllib, json, os, platform, subprocess
if len(sys.argv) > 1:
	url = 'https://cve.circl.lu/api/search/apple/itunes:{}'.format(sys.argv[1])
	print([j['id'] for j in json.loads(urllib.urlopen(url).read().decode('utf-8'))])
else:
	version = subprocess.check_output("mdls -name kMDItemVersion /Applications/iTunes.app | cut -d '\"' -f2", shell=True)
	version = repr(version)
	version = version.strip('\'').strip('n')
	version = version[:-1]
	print version
	url = 'https://cve.circl.lu/api/search/apple/itunes:{}'.format(version)
	print([j['id'] for j in json.loads(urllib.urlopen(url).read().decode('utf-8'))])
