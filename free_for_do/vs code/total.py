#total 
sum=0
count=0
while True:
    point = input("ป้อนคะแนน: ")
    try:
        point=float(point)
    except ValueError:
      print("error")

    if point != 0:
        sum=point+sum
        count=count+1
    else:
        break

print("tatol is", total)