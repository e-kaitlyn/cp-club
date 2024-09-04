import random
def bingo():
    bingo = {}
    ranges = [1,16,31,46,61,15,30,45,60,75]
    nums = [random.randint(1,15)]
    for i in range(24):
        x = (i+1)//5
        nums.append(random.randint(ranges[x],ranges[x+5]))
    bingo['B'] = nums[:5]
    bingo['I'] = nums[5:10]
    bingo['N'] = nums[10:15]
    bingo['G'] = nums[15:20]
    bingo['O'] = nums[20:]
    return bingo

def win(card):
    keys = ['B','I','N','G','O']

    for i in range(5):
        count = 0
        for key in keys:
            if card[key][i] == 0:
                count += 1
        if count == 5:
            return True

    for key in keys:
        count = 0
        for i in range(5):
            if card[key][i] == 0:
                count += 1
        if count == 5:
            return True

    count = 0
    for i in range(5):
        if card[keys[i]][i] == 0:
            count += 1
    if count == 5:
        return True
    count = 0
    for i in range(5):
        if card[keys[i]][4-i] == 0:
            count += 1
    if count == 5:
        return True
    return False

def game(card, calls):

    num_calls = 0
    for x in calls:
        num_calls += 1
        for key in card:
            if x in card[key]:
                card[key][card[key].index(x)] = 0
        if win(card):
            return num_calls
    return num_calls


minimum = 1000
maximum = 0
total_calls = 0
simulations = 1000

for x in range(simulations):
    card = bingo()
    calls = [f"{letter}{i}" for letter in ['B', 'I', 'N', 'G', 'O'] for i in range(1, 16)]
    random.shuffle(calls)
    calls = [int(call[1:]) for call in calls]
    num_calls = game(card, calls)
    minimum = min(minimum, num_calls)
    maximum = max(maximum, num_calls)
    total_calls += num_calls

avg = total_calls/simulations
print(f"Minimum number of calls: {minimum}")
print(f"Maximum number of calls: {maximum}")
print(f"Average number of calls: {avg}")

