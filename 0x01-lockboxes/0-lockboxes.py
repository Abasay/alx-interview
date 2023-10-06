def canUnlockAll(boxes):
    unlocked = False
    keys = boxes[0]

    for key in keys:
        for i in boxes[key]:
            if not (i in keys):
                keys.append(i)
        for i in range(1, len(boxes)):
            if i in keys:
                unlocked = True
            else:
                unlocked = False
    return unlocked
