#Popping List from the end one by one and making a pattern

ls_or = [1,2,3,4,5,6,7]
# creating a iteration from 1 to 7 and the initiating the pop method which basically remove the content of list one by one from behind
for x in range(1,len(ls_or)):
  ls_or.pop()
  print(ls_or)
