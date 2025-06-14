from flask import Flask, render_template,request,request,redirect,url_for
from flask_mysqldb import MySQL
app=Flask(__name__)

#MySQL configurations

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'enquiry'
mysql= MySQL(app)
@app.route('/')
def index():
    return render_template('enquiryform.html')
@app.route('/submit',methods=['POST'])
def submit():
 if request.method == 'POST':
  t1 = request.form['t1']
  t2 = request.form['t2']
  t3 = request.form['t3']
  t4 = request.form['t4']
  t5 = request.form['t5']
  t6 = request.form['t6']
  t7 = request.form['t7']
  t8 = request.form['t8']
  t9 = request.form['t9']
  t10 = request.form['t10']
  t11= request.form['t11']
  t12= request.form['t12']
  t13= request.form['t13']
  t14= request.form['t14']
  btn=request.form['b1']
  if(btn=="Save"):
   cur=mysql.connection.cursor()
   cur.execute("INSERT INTO enquiry VALUES( "+t1+" ,' "+t2+" ' ,' "+t3+ " ','"+t4+"','"+t5+"' ,' "+t6+" ' ,' "+t7+ " ','"+t8+"','"+t9+" ',' "+t10+" ' ,' "+t11+" ','"+t12+"',' "+t13+" ','"+t14+"')")
   mysql.connection.commit()
   cur.close()
   return redirect(url_for('index'))
  if(btn.lower()=="allsearch"):
   cur=mysql.connection.cursor()
   cur.execute("SELECT * FROM enquiry")
   data=cur.fetchall()
   cur.close()
   return render_template('enquiryformsearch.html',data=data)
  if(btn=="Psearch"):
      cur = mysql.connection.cursor()
      cur.execute("select * from enquiry where s_no ="+t1+"")
      data=cur.fetchall()
      cur.close()
      return render_template('enquiryformsearch.html',data=data)
 if(btn=="Delete"):
      cur = mysql.connection.cursor()
      cur.execute("Delete from enquiry where s_no="+t1+"")
      mysql.connection.commit()
      cur.close()
      return redirect(url_for('index'))
 if(btn=="Update"):
      cur = mysql.connection.cursor()
      cur.execute("Update enquiry set name='"+t2+"', dob='"+t3+"', gender='"+t4+"',father_name='"+t5+"',address='"+t6+"',contact_no='"+t7+"', email_id='"+t8+"',education_qualification='"+t9+"',school_college='"+t10+"',course_interested='"+t11+"',date='"+t12+"',counseled='"+t13+"',signature='"+t14+"' where s_no="+t1+"")
      mysql.connection.commit()
      cur.close()
      return redirect(url_for('index'))  

if __name__=='__main__':
	app.run(debug=True) 