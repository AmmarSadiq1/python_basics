#While and For Loops
    #While Loop


# x=0
# while(x<5):
#     print(x)
#     x=x+1

#     #For Loop

# for x in range(4,8):
#     print(x)

#Array

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Sunday"]
for d in days:
    # if (d == "Friday"): break
    if (d == "Friday"): continue
    print(d)