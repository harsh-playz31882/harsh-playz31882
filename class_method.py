class employee:
    a=1

    @classmethod   #reads class object value, not instance value
    def show(cls):
        print(f'class value of a is {cls.a}') 

e = employee()
e.a = 45
e.show()


