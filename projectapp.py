from flask import Flask,render_template,request
import sqlalchemy
app = Flask(__name__)

app=Flask(__name__,template_folder="templates")
app.config['SECRET_KEY']="shr1503"
@app.route("/contact")
def contact():
	return render_template("contact.html")
	
@app.route('/about')
def about():
	return render_template("about.html")
@app.route('/')
def home():
	return render_template("index.html")
if __name__=='__main__':

	app.run(debug=True)
