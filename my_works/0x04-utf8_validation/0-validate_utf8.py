def validUTF8(data):
    result = []
    for elem in data:
        result.append(ord(elem))
    return result


print(validUTF8(["c296"]))
