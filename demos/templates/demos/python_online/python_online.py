# -*- coding:utf-8
import os, codecs

def application(params):
	
	if "cmd" in params and params["cmd"][0].strip():
		os.chdir('/home/admin/django/my_blog/demos/templates/demos/python_online/workspace/')
		with open("tmp.py", 'w') as writer:
			writer.write("# -*- coding: utf-8\r\n")
			writer.write(params["cmd"][0].encode("utf-8"))
		os.chdir('/home/admin/django/my_blog/demos/templates/demos/python_online/')
		data = os.popen("bash sh 2>err.log", 'r').readlines()
		if len(data) == 1:
			data = codecs.open("err.log", 'r', encoding="utf-8").readlines()[1:]
		else:
			data = data[: -1]
		result = ""
		for line in data:
			result += '<p class="result_p">{}</p>'.format(line)
		return result
	else:
		return '<p class="result_p">Bad Parameters!' + str(params) + '</p>'
