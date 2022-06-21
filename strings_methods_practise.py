''' Practise session'''

# Diff b/w index, count, find

# s = ('python' 'programming')        # 2
# print(s.count('m'))

# d = ('Wecome! to my world')   # 3
# print(d.index('o'))
# print(d.rindex('o'))        # 15  

# c = ('Hello! Welcome to coding environment')
# f = c.find('e')
# l = c.rfind('e')
# print(f)
# print(l)



# o = ('Shahed')
# print(o[-4])

# s = "I,want,to,be,a,programmer"
# d = s.split(',')
# print(d)

# b = ' ....ldjfhhf//..,,skdk,  Biryani  mmjd..,,skmd           '
# c = b.strip(" ..,ldjksmhf/ ")
# print(c+','+" is my favorite food. ")

# r = b.rstrip(" ..,ldjksmhf/ ")
# print(r)
# print(b.lstrip(" ..,ldjksmhf/ "))

# e = "I am a developer\nWelcome! to my world"
# d =e.splitlines(False)
# print(d)



''' Other string methods practise session'''

# print(isinstance("Hello!",int))             # False
# print(isinstance(" Thanos",str))            # True
# print(isinstance("Iron man",float))         # False



# r = '    I am an hacker!😎'        
# print(r.find('a'))          # 6
# print(len(r))             # 20
# print(r.rfind('a'))          # 13



t = '123654125'          # False
print(t.isalpha())         
print('Hacker!✌️'.isalpha())   # False
print("Programmer".isalpha())      # True
 

v = "Environment"
print(v.isalnum())         # True 
print('_.encoding'.isalnum())        # False
print('~@<>?'.isalnum())        # False


# print('45623'.isdecimal())       # True
# print(''.isdecimal())            # False
# print('python'.isdecimal())     # False






