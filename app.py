from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
	return render_template("index.html")

@app.route("/friedQuery.html")
def friedQuery():
	return render_template("friedQuery.html")
	
@app.route("/listOrders.html")
def listOrders():
	return render_template("listOrders.html")

#購物車開發
@app.route("/cart.html")
def cart():
	return render_template("cart.html")

@app.route("/shopCart.html")
def shopCart():
	return render_template("shopCart.html")

#失敗待續
@app.route("/vue")
def vue():
	return render_template("vue.html")
	
@app.route('/upload')
def upload():
	return redirect("https://script.google.com/macros/s/AKfycbwOcUFcWgiwzBZiJYGRPVplvZI8-tTiQLh3OWIw1xYxZgT6f8Nseq30I41jQ2Jof8QXKg/exec")

@app.route('/listUploadFiles')
def listUploadFiles():
	return redirect("https://script.google.com/macros/s/AKfycbwxY9ZvBQ0RdQlzQ2RcmijKe1BfjqSGPZu4SP-w1xvRMLpQzC_DT7kiZlI99s4V2Fqq/exec")

@app.route("/home")
def home():
	return "賴田埔手202"

if __name__ == '__main__':
	app.run()
