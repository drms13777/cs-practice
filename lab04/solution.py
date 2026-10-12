names = ["Аня", "Боря", "Вика"]
scores = [7.0, 9.0, 9.0]
def winner(names, scores):
    if not scores:
        return -1
    best_index = 0
    for i in range(1, len(scores)):
        if scores[i] > scores[best_index]:
            best_index = i
        return best_index
def average(scores):
    if not (scores):
        return 0.0
    sum = 0
    for i in range(0, len(scores)):
        sum+= scores[i]
    sum = sum /len(scores)
    return sum
def ranking(names, scores):
    sort_scr = sorted(zip(names, scores), key=lambda x:x[1], reverse=True)
    return [ name for name, score in sort_scr ]
def above_average(names, scores):
    ave = average(scores)
    return([names[i] for i in range(len(scores)) if scores[i]>ave])
print(f'winner_index - {winner(names, scores)}')
print(f'average_score = {average(scores)}')
print(f'ranking - {ranking(names, scores)}')
print(f'above_average - {above_average(names, scores)}')