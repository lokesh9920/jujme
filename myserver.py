from flask import Flask, render_template, request,redirect
import random
app = Flask(__name__)
data_dict = {}
scribble_dict = {}
opins = {}
temp_mail="dummy@gmail.com"

@app.route("/")
def initpage():
	return redirect("/home")

@app.route("/home")
def homepage():
	return render_template("index.html")

@app.route("/Login_page")
def myregistration():
	return render_template("loginpage.html")
@app.route("/successregistration", methods = ["POST"])
def sucreg():
	# save the details and give a link
	password = request.form.get("password")
	repassword = request.form.get("repassword")
	name = request.form.get("name")
	email_id = request.form.get("email_id")
	dob  = request.form.get("dob")
	if not password or not repassword:
		return "Password should not be empty..."
	if(password != repassword):
			return "sorry passwords didn't match... Please try again..."
	if not name or not email_id or not dob:
			return "please enter valid details... "

	data_list =[email_id,password,name,dob]
	key = 0
	while(key in list(data_dict.keys()) or  key is  0):
		key  =str(random.randint(65535,999999)* random.randint(65535,999999))
	
	data_dict[key] = data_list 
	# Here is the redundancy here iam saving the same data twice.
	#
	#
	#
	data_dict[email_id] = password
	return render_template("successreg.html",key = key)
@app.route("/loginsuccess", methods = ["POST"])
def loggedinsucc():
	email = request.form.get("email")
	passw = request.form.get("password")
	if email in list( data_dict.keys()):
		if data_dict[email] ==  passw:
			# "you are logged in successfully"
			if email not in list(opins.keys()):
				 return "Uh Oh ! No one Judged you yet, Feel lucky The world didn't judge you !!"
			personal_list = opins[email]
			return render_template("private.html", opines = personal_list,name = email)
		else:
			return "you entered wrong password"
	else:	
		return "Oh ! You are not registered yet"

@app.route("/scribble")
def scribbling():
	s_key= request.args.get("key")
	if not s_key:
		return "invalid URL .. not entered any key value"
	if s_key not in list(data_dict.keys()):
			return "Invalid key entered"
	#opinion = 
	#return render_template("private_page",key = s_key, dic =  scribble_dict)
	if s_key  not in  list(data_dict.keys()):
		return "Invalid URL...key doesnt exist"
	global temp_mail
	temp_mail = data_dict[s_key][0]
	name  = data_dict[s_key][2]
	return render_template("scribbling_page.html", name = name)

@app.route("/scribbled", methods = ["POST"])
def donescribbling():
	opinion = request.form.get("opinion")
	if temp_mail  not in list(opins.keys()):
			opins[temp_mail] = []
	opins[temp_mail].append(opinion)
	return "You have scribbled successfully!"
#if(__name__ == "__main__"):
#	app.run()
