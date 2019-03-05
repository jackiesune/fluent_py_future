def co_average():
    total=0
    count=0
    term=0
    average=None
    while True:
        term=yield average
        total+=term
        count+=1
        average=total/count

