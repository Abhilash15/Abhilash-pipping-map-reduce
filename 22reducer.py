# Case 2 - Reducer using standard input and output
# Easy to test locally in the terminal

import sys

thisKey = ""
thisValue = 0.0

for line in sys.stdin:
  datalist = line.strip().split('\t')
  if (len(datalist) == 2) : 
    Title, Salary = datalist

    if Title != thisKey:   # we've moved to another key
      if thisKey:
        # output the previous key-summaryvalue result
        print(thisKey,'\t',thisValue)

      # start over for each new key
      thisKey = Title 
      thisValue = 0.0
  
    # apply the aggregation function
    thisValue += float(Salary)

# output the final key-summaryvalue result outside the loop
print(thisKey,'\t',thisValue)

