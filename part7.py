def greet():
    print("Hello")
    print("UCSPyay")
greet()

def greet_student(Name):
    print(f"Hello, {Name}!")
greet_student("Aung")
greet_student("Su")

def calcalate_average(score):
    if len(score)==0:
        return 0
    return sum(score)/len(score)
mark = [70,80,90]
result = calcalate_average(mark)
print("Average:",result)
def classify_score(score):
    if score<0 or score>100:
        return "Invalid"
    elif score >= 80:
        return "Excellent"
    elif score>= 60:
        return "Good"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"
print(classify_score(90))
print(classify_score(55))
print(classify_score(25))


def count_passed(score):
    passed_count=0
    for score in score:
        if score >=50:
            passed_count+=1
    return passed_count
scores=[70,40,90,30,50]
count=count_passed(scores)
print(count)


student_scores = [70,85,90,65,78]
print(student_scores)
print(student_scores[0])
print(student_scores[2])



scores = [70, 85, 90]
scores.append(95)
print(scores)
scores[0] = 75
print(scores)
scores.remove(85)
print(scores)
print("Count:", len(scores))
print("Highest:", max(scores))
print("Lowest:", min(scores))
scores = [55, 80, 35, 90, 65]
for score in scores:
    if score >= 80:
        print(score)


location = (16.8, 96.15)
print("Latitude:", location[0])
print("Longitude:", location[1])
print("Number of values:", len(location))

student = {
"name": "Su Su",
"age": 20,
"score": 88,
"passed": True
}
print(student["name"])
print(student["score"])

student = {
    "name": "Su Su",
    "score": 88
}
student["course"] = "Python for AI"
student["score"] = 92
print(student.get("name"))
print(student.get("grade", "Not assigned"))
print(student)

