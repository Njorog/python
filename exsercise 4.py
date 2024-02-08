maths = int(input("Maths"))
eng = int(input("Eng"))
kisw = int(input("Kisw"))
bio = int(input('Bio'))
chem = int(input("Chem"))


if maths < 0 or eng < 0:
    print("invalid number")

if kisw < 0 or bio < 0:
    print("invalid number")

if chem < 0:
    print("incorrect")

if maths > 100 or eng > 100:
    print("invalid number")

if kisw > 100 or bio > 100:
    print("invalid number")

if chem > 100:
    print("incorrect")
average = ((maths+eng+kisw+bio+chem)/5)
print(average)

if  average >0 and average < 40:
    print("E")
if average >41 and average <51:
    print("D")
if average >52 and average <60:
    print("C")
if average >61 and average <71:
    print("B")
if average > 71 and average < 100:
    print("A")










