# https: // programmers.co.kr/learn/courses/30/lessons/42587


class node:
    a = 0

    def __init__(self, value, index):
        self.value = value
        self.index = index

    def __str__(self):
        return '{} {} {}'.format(self.value, self.index, self.a)


def solution(priorities, location):
    nodelist = []
    answerlist = []
    for i in range(len(priorities)):
        nodelist.append(node(priorities[i], i))
    cnt = 1
    while True:
        check = True
        for i in range(len(nodelist)):
            if i == 0:
                pass
            if nodelist[0].value < nodelist[i].value:
                check = False
                temp = nodelist.pop(0)
                nodelist.append(temp)
                break
        if check:
            temp = nodelist.pop(0)
            temp.a = cnt
            cnt += 1
            answerlist.append(temp)
        if nodelist == []:
            break

    for i in range(len(answerlist)):
        if answerlist[i].index == location:
            return answerlist[i].a

    return True
