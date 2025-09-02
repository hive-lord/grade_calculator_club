def grade_all(d):
    f = []
    l = d.values()
    for i in l:
        mark = i
        if mark >= 90:
            grade = "a"
        elif mark >= 75:
            grade = "b"
        elif mark >= 50:
            grade = "c"
        elif mark > 0 and mark < 50:
            grade = "f"
        else:
            print("enter a proper value")
            continue
        f.append(grade)
    return f
        

def sums(l):
    sum_is = sum(l)
    print(sum_is)
    return sum_is


def average(l):
    average = (sum(l) / len(l))
    print(average)
    

while True:
    print("grade calculator for 5 subjects\n___________________________________")
    lmarks = {}
    for i in range(5):
        while True:
            m = int(input("enter mark of subject {}: ".format(i)))
            if 0 <= m <= 100:
                lmarks[i] = m
                break
            else:
                print("entea valid num")
    break

while True:
    op = int(input("""enter 1 for average
enter 2 for sum
enter 3 for grade calculator
enter 4 to exit
enter option: """))
    if op == 1:
        average(list(lmarks.values()))
    
    elif op == 2:
        sums(list(lmarks.values()))
    
    elif op == 3:
        gradelist = grade_all(lmarks)
        print(gradelist)
    elif op == 4:
        break
    else:
        print("enter a valid option")
