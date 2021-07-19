from flask import Flask
app=Flask(__name__)
import psycopg2
from flask import  render_template, redirect, url_for, request, session, flash, Blueprint, jsonify


@app.route('/abhi', methods=['GET','POST'])
def member_dashboard():
    if request.method == "POST":
        latitude = request.form['yes']
        t_host = "0.0.0.0"
        t_port = "5432"
        t_dbname = "tractor"
        t_software = "kempraju"
        t_pw = "12345"
        db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_software, password=t_pw)
        db_cursor = db_conn.cursor()
        db_cursor.execute(f"select * from venki where voterid='{latitude}'")
        data = db_cursor.fetchall()
        return render_template('aim.html', data=data)



    return render_template('aim.html')









if __name__=='__main__':
    # db_cursor.create_all()
    # db_cursor.session.commit()
    app.run(debug=True)