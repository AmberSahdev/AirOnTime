import matplotlib.pyplot as plt

scores = []
with open('otrs.txt') as f:
    scores = f.read().split('\n')

temp = []
for score in scores:
    try:
        score = float(score)
    except:
        break
    if score%5 > 2.5:
        score += 5-(score%5)
    else:
        score -= score%5
    print(score)
    temp.append(score)
scores = temp

plt.hist(scores)

plt.savefig('score_dist.png')
