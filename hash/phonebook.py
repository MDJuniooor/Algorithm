# https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3


def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
                if i != j and phone_book[j].find(phone_book[i])==0:
                    return False 
    return True


# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True
