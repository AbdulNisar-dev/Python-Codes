class Class1:
    c1v="I am class1 variable//// to call me after iam overridden in class2 use super().class_variable_name"
    def  __init__(self):
        self.var1=" Instance variable of Class1"
        self.var2=" Instance variable and class variable are different"
        self.var3=" Super()__init__()   is used to fetch the overidden constructer's variables "

class Class2(Class1):
    c1v="I am Class2 variable"
    def  __init__(self):
        print(super().c1v)
        self.var1="The position of the super().__init__() is also important"
        self.var2="The position of calling of var's in the print() are also important"
        self.var3="Once we give same name to the var's in class1 and class2 then the var gets overridden"
        super().__init__()


obj2=Class2()

# after overridden the vars and inherited occurence
# When called for inst_var of obj from c2 ,first it checks for inst_var in c2==>checks for the same in c1
# afer that checks for the classvar in c2 and ==> classvar in c1
print(obj2.c1v,obj2.var3,obj2.var1)