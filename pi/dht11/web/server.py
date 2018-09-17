from flask_mysqldb import MySQL
import time
from flask import Flask, jsonify, render_template

app = Flask(__name__)
app.config["MYSQL_HOST"] = "host"
app.config["MYSQL_USER"] = "user"
app.config["MYSQL_PASSWORD"] = "passwd"
app.config["MYSQL_DB"] = "db"
app.config["MYSQL_CHARSET"] = "utf8"
mysql = MySQL(app)


def change_time(t):
    local_time = time.localtime(t)
    return time.strftime("%Y-%m-%d %H:%M:%S", local_time)


@app.route("/")
def hello():
    h = {"message": "hello world"}
    return jsonify(h)


@app.route("/test/")
def return_info():
    cur = mysql.connection.cursor()
    cur.execute("select * from (select * from info order by tid desc limit 10) info order by tid")
    values = cur.fetchall()
    cur.close()
    d = list()
    for i in values:
        tid = i[0]
        nowtime = change_time(i[1])
        temperature = i[2]
        humidity = i[3]
        d.append({"tid": tid, "nowtime": nowtime, "temperature": temperature, "humidity": humidity})
    return render_template("test.html", d=d)


if __name__ == '__main__':
    app.run(debug=False, host="127.0.0.1", threaded=True)
    # app.run(debug=False, host="0.0.0.0", threaded=True)
