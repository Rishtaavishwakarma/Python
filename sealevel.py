
def valley(steps,path):
    sea_level=0
    valleys=0
    for steps in path:
        if steps == 'U':
            sea_level += 1
        else:
            sea_level -= 1
        if steps == 'U' and sea_level == 0:
            valleys +=1
    return valleys
steps=input("Enter the number of steps")
path=input("Enter the path")
result = valley(steps,path)
print(result)
        




    