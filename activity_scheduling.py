
activities=[(1,3,"A1"),(1,2,"A2"),(2,4,"A3"),(3,5,"A4"),(4,5,"A5")]

def scheduling(list):
    list.sort(key=lambda p:p[1])
    last_finished=list[0][1]
    scheduled_activities=[list[0][2]]
    for i in range(1,len(list)):
        if(list[i][0]>=last_finished):
            scheduled_activities.append(list[i][2])
            last_finished=list[i][1]
    return scheduled_activities

print(scheduling(activities))
    