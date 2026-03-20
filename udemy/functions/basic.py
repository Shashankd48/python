def hello_world(name):
    print("It says Hello world! -", name)
    pass

hello_world("Tony")

# Scoped and namespace
def update_tech():
    stack = "MERN"
    def select_stack():
        stack = "MEAN"
        print("Selected stack - ", stack)
    select_stack()

update_tech()

# NonLocal scope

def update_order():
    chai_type = "Masala"
    
    def kitchen():
        nonlocal chai_type
        chai_type = "Elaichi"
        print("Current chai order type - ", chai_type)
    
    kitchen()
    print("Final order type - ", chai_type)

update_order()

# Global scope

design_type = "CSS"

def select_design_type():
    global design_type
    design_type = "SCSS"
    print("Selected design type - ", design_type)

select_design_type()
