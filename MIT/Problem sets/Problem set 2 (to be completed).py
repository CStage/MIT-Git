x=1
y=150
PNA=(55,56,57,58,59,60,61,62)
for a in range(0,y):
    for b in range(0,y):
        for c in range(0,y):
            n=6*a+9*b+20*c
            if n in range(0,101):
                print("to get ", n, "nuggets. You need: ", a, "6-piece", b, "9-piece and", c, "20-piece")
