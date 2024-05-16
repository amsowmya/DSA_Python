# Calculate average temparture

numDay = int(input("How many days temparature?"))

temparature = list()
for i in range(numDay):
    temp = input(f"Day {i+1} higest temparature : ")
    temparature.append(int(temp))

avg = sum(temparature)/len(temparature)
print(f"Avg temparature is : {avg}")

total = 0
for val in temparature:
    if val > avg:
        total += 1 

print(f"total {total} day(s) above temparature")



