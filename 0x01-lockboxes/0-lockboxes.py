def canUnlockAll(boxes):
    keys = boxes[0]

    for i in range(0, len(boxes)):
        for key in keys:
            for i in boxes[key]:
                if not (i in keys):
                    keys.append(i)

    for i in range(0, len(boxes)):
        if i == 0:
            continue
        if not (i in keys):
            return False

    return True
