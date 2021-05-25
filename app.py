
import smtplib
from email.message import EmailMessage
from flask import Flask, render_template, request


app = Flask(__name__)


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["to"] = to

    user = "vastseliinaabi@gmail.com"
    msg["from"] = user
    password = "punqzhlfzwulstnr"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


@app.route("/", methods=['GET'])  # http://127.0.0.1:5000/ töötaks serveris
def index():
    valik_list = ['E-Kool', 'Tehnika', 'Wifi', 'MS Teams']
    return render_template("index.html", valik_list=valik_list)


# http://127.0.0.1:5000/success töötkas serveris
# ilma methods= ita tule teade - Method Not Allowed
@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':

        valik_list = request.form["valik_list"]
        problem = request.form["problem_name"]
        room = request.form["room_name"]

        vastus = [[valik_list], [problem], [room]]  # 2x tsükkel
        for x in vastus:
            for y in x:
                print(y)
        print(vastus[2], vastus[0], vastus[1], "ewerex@gmail.com")

        # Tuleks konsoolis ühele reale
        email_alert(room, valik_list + " - " +
                    problem, "ewerex@gmail.com")

        ennik = (valik_list, problem, room)  # Tuple
        outfile = open('log.txt', 'a')
        outfile.write(ennik[0] + ' - ')
        outfile.write(ennik[1] + ' - ')
        outfile.write(ennik[2] + "\n")
        outfile.close()

        return render_template("success.html")
    else:
        return render_template("index.html")


@app.route("/log")  # http://127.0.0.1:5000/log töötaks serveris
def log():
    with open("log.txt", "r") as f:
        content = f.read()
    return render_template("log.html", content=content)


if __name__ == '__main__':
    app.debug = True
    app.run()

##############################################
