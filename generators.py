import random as rnd


def checkDupes(list):
    if len(list) == len(set(list)):
        return False
    else:
        return True


def rd6():
    return rnd.randint(1, 6)


def r2d6():
    result = []
    result.append(rnd.randint(1, 6))
    result.append(sum(result))
    return result


def r3d6():
    result = []
    roll = []
    for x in range(3):
        roll.append(rnd.randint(1, 6))
    result.append(roll)
    result.append(sum(roll))
    result.append(checkDupes(roll))
    if result[2]:
        result.append(roll[2])
    else:
        result.append(0)
    # result is formatted: [[d1, d2, d3], sum, doubles?, doubles_count]
    return result


def modifier(rollsum):
    return {
        3: -2,
        4: -1,
        5: -1,
        6:  0,
        7:  0,
        8:  0,
        9: +1,
        10: +1,
        11: +1,
        12: +2,
        13: +2,
        14: +2,
        15: +3,
        16: +3,
        17: +3,
        18: +4
    }[rollsum]
