def frequency(l):
    if not l:
        return ([], [])

    counts = {}
    for num in l:
        counts[num] = counts.get(num, 0) + 1

    min_freq = min(counts.values())
    max_freq = max(counts.values())

    minfreqlist = sorted([k for k, v in counts.items() if v == min_freq])
    maxfreqlist = sorted([k for k, v in counts.items() if v == max_freq])

    return (minfreqlist, maxfreqlist)

print(frequency([13,12,11,13, 14, 13,7, 11, 13, 14, 12, 14,14,7]))

def onehop(l):
    if not l:
        return []

    hops = set()
    for i, k in l:
        for k2, j in l:
            # Requires an intermediate city k distinct from both origin i and destination j
            if k == k2 and i != j and i != k and k != j:
                hops.add((i, j))

    return sorted(list(hops))

print(onehop([(2,3),(1,2)]))