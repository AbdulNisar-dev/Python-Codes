#
# class Employee:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#         # self.email = f"{fname}.{lname}@codewithharry.com"
#
#     def explain(self):
#         return f"This employee is {self.fname} {self.lname}"
#
#     @property
#     def email(self):
#         if self.fname==None or self.lname == None:
#             return "Email is not set. Please set it using setter"
#         return f"{self.fname}.{self.lname}@codewithharry.com"
#
#     @email.setter
#     def email(self, string):
#         print("Setting now...")
#         names = string.split("@")[0]
#         self.fname = names.split(".")[0]
#         self.lname = names.split(".")[1]
#
#     @email.deleter
#     def email(self):
#         self.fname = None
#         self.lname = None
#
#
# hindustani_supporter = Employee("Hindustani", "Supporter")
# # nikhil_raj_pandey = Employee("Nikhil", "Raj")
#
# print(hindustani_supporter.email)
#
# hindustani_supporter.fname = "US"
#
# print(hindustani_supporter.email)
# hindustani_supporter.email = "this.that@codewithharry.com"
# print(hindustani_supporter.fname)
#
# del hindustani_supporter.email
# print(hindustani_supporter.email)
# hindustani_supporter.email = "Harry.Perry@codewithharry.com"
# print(hindustani_supporter.email)
#


class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@gmail.com"

    def Explain(self):
        return f"This employee is {self.fname}{self.lname}"

    # this property decorator is used to make methods called directly as an attribute rather than as fn() in print()
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@gmail.com"

    # this is used to customize/ change/set/create an attribute by taking inputs
    @email.setter
    def email(self,string):
        print("Setting Now ...")
        self.names=string.split("@")[0]
        self.fname=string.split(".")[0]
        self.lname=string.split(".")[1]

    # this is used to delete the setter decorated method ,this is needed to del the settermethod otherwise it wont deley\te
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None




nisar=Employee("abdul","nisar")
print(nisar.Explain())
print(nisar.email)
nisar.fname="abdulnisar"
nisar.lname="mulla"
print(nisar.email)
nisar.email="abdultaswar.mulla@gmail.com"
print(nisar.fname)
print(nisar.lname)
print(nisar.names)


del nisar.email
print(nisar.email)

