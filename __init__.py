from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL



app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'sql12.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql12348567'
app.config['MYSQL_PASSWORD'] = 'ZhHGk3cE8P'
app.config['MYSQL_DB'] = 'sql12348567'

mysql = MySQL(app)
		
		
@app.route('/Login')
def login():
    return render_template('Login.html')

# @app.route("/checkUser",methods=["POST"])
# def check():
	# username = str(request.form["user"])
	# password = str(request.form["password"])
	# cursor = conn.cursor()
	# cursor.execute("SELECT name FROM user WHERE name ='"+username+"'")
	# user = cursor.fetchone()
	
	# if len(user) is 1:
		# return redirect(url_for("home"))
	# else:
		# return "failed"
	

@app.route('/homeAdmin')
def Index():
    return render_template('homeAdmin.html')

@app.route('/index2')
def users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM reporters")
    data = cur.fetchall()
    cur.close()

    return render_template('index2.html', reporters=data )
	
	

# @app.route('/')
# def reports():
    # cur = mysql.connection.cursor()
    # cur.execute("SELECT id, article, picture, sound FROM content")
    # data = cur.fetchall()
    # cur.close()
	
    # return render_template('Reports.html', content=data)
	
	
@app.route('/uploadR', methods = ['POST'])
def uploadR():

    if request.method == "POST":
        flash("Data Uploaded Successfully")
        contributor = request.form['contributor']
        article = request.form['article']
        picture = request.form['picture']
        sound = request.form['sound']
		
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO content (contributor, article, picture, sound) VALUES (%s, %s, %s, %s)", (contributor, article, picture, sound))
        mysql.connection.commit()
        return redirect(url_for('reports'))
		

@app.route('/updateR',methods=['POST','GET'])
def updateR():

    if request.method == 'POST':
        id = request.form['id']
        contributor = request.form['contributor']
        article = request.files['article']
        picture = request.files['picture']
        sound = request.files['sound']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE content SET contributor=%s, article=%s, picture=%s, sound=%s WHERE id=%s", (contributor, article, picture, sound, id))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('reports'))

		
@app.route('/deleteR/<string:id_data>', methods = ['GET'])
def deleteR(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM content WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('reports'))
	
	

@app.route('/GR')
def GR():
    cur = mysql.connection.cursor()
    cur.execute("SELECT reporter, subject, tag FROM post")
    data = cur.fetchall()
    cur.close()
	
    return render_template('GReports.html', post=data)
	

@app.route('/insertGR', methods = ['POST'])
def insertGR():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        reporter = request.form['reporter']
        subject = request.form['subject']
        tag = request.form['tag']
		
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO post (reporter, subject, tag) VALUES (%s, %s, %s)", (reporter, subject, tag))
        mysql.connection.commit()
        return redirect(url_for('GR'))

		
# @app.route('/post', methods = ['GET'])
# def Gpost():
    # cur = mysql.connection.cursor()
    # cur.execute("SELECT reporter, subject, tag FROM post")
    # data = cur.fetchall()
    # cur.close()
	
    # return render_template('GReports.html', post=data)

	

		
@app.route('/viewG/<string:GR_data>', methods = ['GET'])
def viewG(GR_data):
    cur = mysql.connection.cursor()
    cur.execute("SELECT groups FROM reporters WHERE groups =%s", (GR_data,))
    mysql.connection.commit()
    return redirect(url_for('GR'))
	
		
		
		
@app.route('/deleteGR/<string:GR_data>', methods = ['GET'])
def deleteGR(GR_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM post WHERE subject=%s", (GR_data,))
    mysql.connection.commit()
    return redirect(url_for('GR'))
	
	

@app.route('/groups')
def groups():
    cur = mysql.connection.cursor()
    cur.execute("SELECT groups, COUNT(*) FROM reporters GROUP BY groups")
    data = cur.fetchall()
    cur.close()
	
	
    return render_template('groups.html', reporters=data )
	
	
@app.route('/insertG', methods = ['POST'])
def insertG():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
		
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO reporters (groups) VALUES (%s)", (name))
        mysql.connection.commit()
        return redirect(url_for('groups'))
		
		
@app.route('/deleteG/<string:G_data>', methods = ['GET'])
def deleteG(G_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM groups WHERE groups=%s", (G_data))
    cur.execute("DELETE FROM reporters WHERE groups=%s ", (G_data))
    mysql.connection.commit()
    return redirect(url_for('groups'))
	
	


@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        groups = request.form['groups']
        email = request.form['email']
        password = request.form['password']
		
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO reporters (name, groups, email, password) VALUES (%s, %s, %s, %s)", (name, groups, email, password))
        mysql.connection.commit()
        return redirect(url_for('users'))




@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM reporters WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('users'))





@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        groups = request.form['groups']
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE reporters
               SET name=%s, groups=%s, email=%s, password=%s
               WHERE id=%s
            """, (name, groups, email, password, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('users'))




if __name__ == "__main__":
    app.run(debug=True)
