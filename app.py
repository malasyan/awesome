#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from flask import Flask
# from flask import request

# app = Flask(__name__)

# @app.route('/',methods=['GET','POST'])
# def home():
# 	return '<h1>Home</h1>'

# @app.route('/signin',methods=['Get'])
# def signin_from():
# 	return '''<form action="/signin" method="post">
# 			  <p><input name="username"></p>
#               <p><input name="password" type="password"></p>
#               <p><button type="submit">Sign In</button></p>
#               </form>'''

# @app.route('/signin',methods=['POST'])
# def signin():
# 	if request.form['username']=='admin' and request.form['password']=='password':
# 		return '<h3>Hello, admin!</h3>'
# 	return '<h3>Bad username or password.</h3>'

# if __name__ =='__main__':
# 	app.run()


############################################################################## 	

# from flask import Flask,request,render_template

# app = Flask(__name__)

# @app.route('/',methods=['GET','POST'])
# def home():
# 	return render_template('home.html')

# @app.route('/signin',methods=['Get'])
# def signin_from():
# 	return render_template('form.html')

# @app.route('/signin',methods=['POST'])
# def signin():
# 	username = request.form['username']
# 	password = request.form['password']
# 	if username=='admin' and password=='password':
# 		return render_template('signin-ok.html',username=username)
# 	return render_template('form.html',message='Bad username or password',username=username)

# if __name__ =='__main__':
# 	app.run()


	
############################################################################### 



import asyncio
from aiohttp import web

async def index(request):
	await asyncio.sleep(0.5)
	return web.Response(body=b'<h1>Index</h1>',content_type='text/html')

async def hello(request):
	await asyncio.sleep(0.5)
	text = '<h1>hello,%s!</h1>' % request.match_info['name']
	return web.Response(body=text.encode('utf-8'))

async def init(loop):
	app = web.Application(loop=loop)
	app.router.add_route('GET','/',index)
	app.router.add_route('GET','/hello/{name}',hello)
	srv = await loop.create_server(app.make_handler(),'127.0.0.1',8000)
	print('Server started at http://127.0.0.1:8000...')
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()



