def myfun(my_list):
  s = 0
  for item in my_list:
    s = s + item
  return s;
my_list=[1,2,3,4,5]
s = myfun(my_list)
print("La somma è: {}". format(s))