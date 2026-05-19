#           |  name  | form  |  score | grade |
results = [ [ "Ahmed", "10XT",   45,       7  ],
            [ "Belle", "10YO",   32,       5  ],
            [ "Clara", "10XO",   54,       9  ] ]

print(len( results )) # → 3, there are still only 3 things in the results list, they just happen to be other lists
form = input("Form: ")
score = 0
formSize = 0
#print all the names
for i in range( len( results ) ):
    if(results[i][1] == form ):
        print(results[i])
        score += results[i][2]
        formSize += 1
print("Score: ",score)
print("Average: ", score/formSize)