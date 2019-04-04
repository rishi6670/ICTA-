from flask import Flask
app=Flask(_name_)
@app.route("/")
def greeting():
	return "<h1 style='color:green'>Hello World!</h1>
if_name_=="_main_":
	app.run(host='0.0.0.0')
