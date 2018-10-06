#https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_truck = []
    complete = []

    while True:
        time +=1
        for i in range(len(complete)):
                complete[i] +=1

        if complete != [] and complete[0] >= bridge_length:
            complete.pop(0)
            bridge_truck.pop(0)

        if truck_weights != [] and weight >= sum(bridge_truck)+truck_weights[0]:
            bridge_truck.append(truck_weights.pop(0))
            complete.append(0)
       
        if truck_weights == [] and bridge_truck == []:
            break

    return time
