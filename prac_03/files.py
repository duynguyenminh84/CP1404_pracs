""" 1/
outfile = "name.txt"
outfile = open(outfile, "w")
print("Please enter your name")
user_name= input("> ")
print(user_name, file=outfile)
outfile.close()
"""

""" 2/ 
outfile = "name.txt"
outfile = open(outfile, "r")
user_name = outfile.readline()
print("Hello " + user_name+ "!")
outfile.close()
"""

"""3/
outfile= "numbers.txt"

with open(outfile,"r") as out:
    first_number= int(out.readline())
    second_number= int(out.readline())
    out.close()
print(first_number + second_number)
"""

"""4/
outfile= "numbers.txt"

with open(outfile,"r") as out:
    total= 0
    for line in out:
        number= int(line)
        total += number
    out.close()
print(total)
"""

