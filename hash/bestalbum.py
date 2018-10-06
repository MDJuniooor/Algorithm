#https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    dic = dict()
    rank = []
    rank_genre = []
    mix = []
    answer = []
    idx = 0
    for genre, play in zip(genres, plays):
        mix.append([genre,play,idx])
        idx+=1
        if genre in dic:
            dic[genre] = dic[genre]+play
        else:
            dic[genre] = play
    for value in dic.values():
        rank.append(value)
    rank.sort(reverse=True)
    for i in rank:
        num = dic.keys()
        for key in dic.keys():
            if dic[key] == i:
                rank_genre.append(key)
                dic[key] = -1
    
    for genre in range(len(rank_genre)):
        for i in range(len(mix)):
            if mix[i][0] == rank_genre[genre]:
                mix[i][0] = genre
    
    answerlist = sorted(mix, key=lambda music: (music[0], -music[1]))
    
    for i in range(answerlist[-1][0]+1):
        cnt = 0
        for item in answerlist:
            if cnt <2 and item[0] == i :
                answer.append(item[2])
                cnt+=1


    return answer


def solution(genres, plays):
    answer = []
    dic = dict()
    rank = []
    rank_genre = []
    mix = []
    answer = []
    idx = 0
    for genre, play in zip(genres, plays):
        mix.append([genre, play, idx])
        idx += 1
        if genre in dic:
            dic[genre] = dic[genre]+play
        else:
            dic[genre] = play
    for value in dic.values():
        rank.append(value)
    rank.sort(reverse=True)
    for i in rank:
        num = dic.keys()
        for key in dic.keys():
            if dic[key] == i:
                rank_genre.append(key)
                dic[key] = -1

    for genre in range(len(rank_genre)):
        for i in range(len(mix)):
            if mix[i][0] == rank_genre[genre]:
                mix[i][0] = genre

    answerlist = sorted(mix, key=lambda music: (music[0], -music[1]))

    for i in range(answerlist[-1][0]+1):
        cnt = 0
        for item in answerlist:
            if cnt < 2 and item[0] == i:
                answer.append(item[2])
                cnt += 1

    return answer
