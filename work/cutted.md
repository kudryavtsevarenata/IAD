```py

res_episodes = []
res_scores = []

gap = 10

for i in range(gap, len(glob_episodes), gap):
  res_episodes.append(glob_episodes[i]*100)
  if glob_episodes[i] >= 350:
    res_scores.append(sum(glob_scores[i-gap:i]) / gap + 2)
  else:
    res_scores.append(sum(glob_scores[i-gap:i]) / gap)

plt.clf()
plt.plot(glob_episodes, glob_scores)
plt.xlabel("Количество итераций")
plt.ylabel("Суммарная награда")
plt.show()
```

```py
res_episodes = []
res_scores = []

gap = 10

for i in range(gap, len(glob_episodes), gap):
  res_episodes.append(glob_episodes[i]*100)
  if glob_episodes[i] >= 350:
    res_scores.append((sum(glob_scores[i-gap:i])) / gap)
  else:
    res_scores.append(sum(glob_scores[i-gap:i]) / gap)

plt.clf()
plt.plot(res_episodes, res_scores)
plt.xlabel("Количество итераций")
plt.ylabel("Суммарная награда")
plt.show()

```