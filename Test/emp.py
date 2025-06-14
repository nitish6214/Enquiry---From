from flask import Flask, render_template,request,request,redirect,url_for
from flask_mysqldb import MySQL
app=Flask(__name__)
#MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'employee'
mysql= MySQL(app)
@app.route('/')
def index():
    return render_template('emp.html')
@app.route('/submit',methods=['POST'])
def submit():
 if request.method == 'POST':
  t1 = request.form['t1']
  t2 = request.form['t2']
  t3 = request.form['t3']
  t4 = request.form['t4']
  btn=request.form['b1']
  if(btn=="Save"):
   cur=mysql.connection.cursor()
   cur.execute("INSERT INTO employee VALUES( "+t1+" ,' "+t2+" ' ,' "+t3+ " ',"+t4+")")
   mysql.connection.commit()
   cur.close()
   return redirect(url_for('index'))
  if(btn.lower()=="allsearch"):
   cur=mysql.connection.cursor()
   cur.execute("SELECT * FROM employee")
   data=cur.fetchall()
   cur.close()
   return render_template('empSearch.html',data=data)  

if __name__=='__main__':
	app.run(debug=True)


