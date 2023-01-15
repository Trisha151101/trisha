from flask import *

from S19Customer import Customer
from S19DataBaseHelper import DataBaseHelper

app = Flask("CustomerManagementApp", template_folder="cms")
db_helper = DataBaseHelper()


@app.route("/")
def index():
    # return "Welcome to CMS App"
    return render_template("index.html")


@app.route("/add")
def add():
    # return "Welcome to CMS App"
    return render_template("add-customer.html")


@app.route("/view")
def view():

    cref = Customer()
    sql = cref.select_sql()
    rows = db_helper.read(sql)
    return render_template("view-customer.html", result=rows)


@app.route("/save-customer", methods=["POST"])
def save_customer_in_db():
    cref = Customer(name=request.form["name"],
                    phone=request.form["phone"],
                    email=request.form["email"],
                    remark=request.form["remark"])
    print(vars(cref))
    sql = cref.insert_sql()
    db_helper.write(sql)
    return cref.name+" Inserted Successfully..."


def main():
    app.run()


if __name__ == "__main__":
    main()
