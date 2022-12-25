from flask import *
from customerapp import customer
from Databasehelper import databasehelper
app = flask("customermanagementapp", template_folder= 'cms')
db_helper = databasehelper()





@app.route("/")
def index():
    # return "welcome to cms app
    return render_template("index.html")

@app.route("/add")
def add():

    # return "welcome to cms app"
    return render_template("add customer.html")


@app.route("/view")
def view():
    #return "welcome to cms app"
    cref = customer()
    sql = cref.select_sql
    rows = db_helper.read(sql)
    return render_template("view customers.html", result = rows)

@app.route("/delete/<id>")
def delete_customer_from_db(id):
    cref = customer(id=id)
    sql = cref.delete_sql
    db_helper.write(sql)

    return render_template("success.html", message = " customer with id" +id+ "deleted succesfully..")

@app.route("/save-customer", methods = ["post"])
def save_customer_in_db():
    cref = customer(name =request.form["name"],
                    phone = request.form["phone"],
                    email = request.form["email"],
                    remarks = request.form["remarks"])
    if len(cref.name) ==0:
        return render_template("error.html", message="Name cannot be Empty...")

    print(vars(cref))
    sql = cref.insert_sql()
    db_helper.write(sql)

    # return cref.name+" Inserted Successfully..."
    return render_template("success.html", message=cref.name+" Inserted Successfully...")


@app.route("/update_customer")
def update_customer():
    return render_template("update_customer.html")


def main():
    app.run()


if _name_ == "_main_":
    main()


