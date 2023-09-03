def groupList(customList, size=4):
    groupedList = []
    for i in range(0, len(customList), size):
        groupedList.append(customList[i:i + size])
    return groupedList
