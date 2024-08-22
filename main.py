# Dice sum probability calculator
# Författare: Viggo Carrefors
# Datum: 2024-08-22
from collections import Counter

def main():
    total=[]
    user_input = input().split(" ")
    for i in range(1,int(user_input[0])+1):
        for l in range(1,int(user_input[1])+1):
            total.append(i+l)
    count=Counter(total).most_common()
    for i in count:
        if i[1]==count[0][1]:
            print(i[0])

if __name__ == "__main__":
    main()