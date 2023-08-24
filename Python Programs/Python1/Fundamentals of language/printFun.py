name = "Shakir"
salary = 50000000
friend = "arshad"

print("Hello {}, Your salary is {} and your friend {} is wating...".format(name,salary,friend))
print("Hello {1}, Your salary is {0} and your friend {2} is wating...".format(name,salary,friend))
print("Hello {n}, Your salary is {s} and your friend {f} is wating...".format(n=name,s=salary,f=friend))
print("Hello %s, Your salary is %d and your friend %s is waiting..." %(name,salary,friend))

