# Case 2 - Mapper using standard input and output
# Easy to test locally in the terminal

import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split("    ")
  datalist = datalist[0].split(",")
  if (len(datalist) == 5) : 
    Company, Title,	Salary_Reported,	Location,	Salary = datalist

    # print intermediate key-value pairs to standard output
    print(Title,"\t",Salary)

