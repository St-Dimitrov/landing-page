from flask import Flask, render_template, url_for, request, redirect
import csv
from datetime import datetime

app = Flask(__name__)
# print(__name__)
# if __name__ == "__main__":
#     app.run(debug=True)

@app.route("/")
def my_default_home():
    return render_template('index.html')

@app.route("/components.html")
def components_redirect():
    return render_template('index.html')

@app.route("/work.html")
def work_redirect():
    return render_template('works.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

# def write_to_file(data):
#     with open("database.txt", mode='a') as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         dt = datetime.now()
#         file = database.write(f'\n{email}, {subject}, {message}, {dt}')

def write_to_csv(data):
    with open("database.csv", mode='a', newline='') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        dt = datetime.now()
        csv_writer = csv.writer(database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message,dt])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "did NOT save to database"
    else:
        return "something went wrong"
