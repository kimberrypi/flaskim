from flask import Flask, render_template, request, redirect

app = Flask(__name__, static_url_path='')

#index.html
@app.route('/')
def index():
	return render_template('index.html')

#phase one, activity one
@app.route('/p1a1')
def details(): 
	return render_template('one.html')

#phase one, activity two
@app.route('/p1a2')
def nomultiply():
	nums = []
	for n in nums(5):
		nums.append(-8)
		return()

#phase one, activity three
@app.route 

#phase two, activity one
@app.route('/p2a1')
def signup():
	return render_template('/regform-1.html')

#html form view result v1.0
@app.route('/results', methods=['POST'])
def registered():
	fullname = request.form['fullname']
	birthday = request.form['birthday']
	age = request.form['age']
	school = request.form['school']
	gender = request.form['gender']
	return (fullname + '<br>' 
		+ birthday + '<br>'
		+ age + '<br>' 
		+ school + '<br>'
		+ gender)

#phase two, activity two

#phase three, activity one
@app.route('/p3a1')
def signup2():
	return render_template('/regform-2.html')

#html form view result v 2.0
@app.route('/results2', methods = ['POST'])
def result():
	result = request.form
	return render_template('registered.html', result=result)

#activity 
@app.route('/actthree')
def tree():
	asterisks = ['*']
	for asterisk in range(10):
		tree.append('*')
		tree = print(asterisks)

	return (asterisks)

if __name__=='__main__':
	app.run(debug=True)