score=[70,85,30,60,90,45]
pas_c=0
fai_c=0
for i in score:
    if i >40:
     pas_c +=1
    
    elif i<40:
     fai_c +=1

print(f"Fail student{fai_c}")
print(f"Pass student{pas_c}")