c=8
m=3
counts=[[0,3,0],
        [0,0,1],
        [0,0,1],
        [1,0,0],
        [0,0,1],
        [3,1,1],
        [0,1,0],
        [1,0,1]]
for i in range(c):
# Process the ith row
      for j in range(m) :
# Process the jth column in the ith row
           print("%8d" % counts[i][j], end="")
      print()
print(counts[2][2])