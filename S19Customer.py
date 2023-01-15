class Customer:

    # Constructor
    def __init__(self, name=None, phone=None, email=None, remark=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.remark = remark


    def insert_sql(self):
        return "insert into Customer (name, phone, email, remark) " \
               "values " \
               "('{name}', '{phone}', '{email}', '{remark}');".format_map(vars(self))


    def select_sql(self):
        return "select * from Customer"


