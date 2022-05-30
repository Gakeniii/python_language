#Progrmme to write numbers in reverse

num = int(input("Enter the number"))
rev_num = 0
while num != 0:
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num //=10
print("rev_num" + str(rev_num))
