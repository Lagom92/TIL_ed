def solution(priorities, location):

    for i in range(len(priorities)):
        for j in range(len(priorities)):
            if i != j:
                if priorities[i] < priorities[j]:
                    a = priorities.pop(priorities[i])
                    priorities.append(a)


    print(res)
    return


arr = [2, 1, 3, 2]
location = 2
result = solution(arr, location)

# print(result)