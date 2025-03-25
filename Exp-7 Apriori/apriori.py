from itertools import combinations
from collections import defaultdict

 dataset = [
    ['Milk', 'Bread', 'Eggs'],
    ['Bread', 'Butter'],
    ['Milk', 'Bread', 'Butter'],
    ['Milk', 'Butter'],
    ['Bread', 'Eggs']
 ]

def generate_Ck(Lk_prev, k):
   
    Ck = []
    n = len(Lk_prev)
    for i in range(n):
        for j in range(i+1, n):
            itemset1, itemset2 = Lk_prev[i], Lk_prev[j]
            if k > 2 and itemset1[:-1] != itemset2[:-1]:
                continue
            if itemset1[-1] < itemset2[-1]:
                new_candidate = tuple(itemset1) + (itemset2[-1],)
                Ck.append(new_candidate)
    return Ck

def prune_Ck(Ck, Lk_prev, k):
    
    Lk_prev_set = set(Lk_prev)
    pruned_Ck = []
    for candidate in Ck:
        valid = True
        for subset in combinations(candidate, k-1):
            if tuple(sorted(subset)) not in Lk_prev_set:
                valid = False
                break
        if valid:
            pruned_Ck.append(candidate)
    return pruned_Ck

def count_support(dataset, candidates):
    
    counts = defaultdict(int)
    for transaction in dataset:
        for candidate in candidates:
            if all(item in transaction for item in candidate):
                counts[candidate] += 1
    return counts

def apriori(dataset, min_support):
    
    C1 = defaultdict(int)
    for transaction in dataset:
        for item in transaction:
            C1[item] += 1

    L1 = [tuple([item]) for item in C1 if C1[item] >= min_support]
    L1.sort()
    L = [L1]
    k = 2

    while True:
        if len(L) < k-1:
            break
        Ck_candidates = generate_Ck(L[k-2], k)
        if not Ck_candidates:
            break
        Ck_pruned = prune_Ck(Ck_candidates, L[k-2], k)
        support_counts = count_support(dataset, Ck_pruned)
        Lk = [candidate for candidate in Ck_pruned if support_counts[candidate] >= min_support]
        if not Lk:
            break
        L.append(Lk)
        k += 1
    return L
