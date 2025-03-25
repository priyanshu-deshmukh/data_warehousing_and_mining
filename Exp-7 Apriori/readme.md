# Apriori Algorithm for Frequent Itemset Mining

## Dataset Information
This project uses a transaction dataset where each entry represents a set of items purchased together. The dataset is structured as follows:

```python
 dataset = [
    ['Milk', 'Bread', 'Eggs'],
    ['Bread', 'Butter'],
    ['Milk', 'Bread', 'Butter'],
    ['Milk', 'Butter'],
    ['Bread', 'Eggs']
 ]
```

Each sublist represents a transaction, and the goal is to find frequently occurring itemsets based on a minimum support threshold.

## Apriori Algorithm
The Apriori algorithm is used for frequent itemset mining. It follows these steps:

1. **Generate Candidate Itemsets (Ck)**: Create itemsets of increasing size by combining frequent itemsets from the previous iteration.
2. **Prune Infrequent Itemsets**: Remove candidates that contain subsets that are not frequent.
3. **Count Support**: Determine how often each itemset appears in transactions.
4. **Filter Frequent Itemsets**: Keep itemsets that meet the minimum support threshold.
5. **Repeat Until No More Frequent Itemsets Can Be Found**.

### Implementation
- Uses Python’s `itertools.combinations` for candidate generation.
- Uses a dictionary for counting support efficiently.
- Prunes itemsets whose subsets are not frequent.

## Sample Code Output
When the algorithm runs with `min_support = 2`, the frequent itemsets are:

```
Frequent Itemsets:
Level 1 (Itemsets of size 1): [('Bread',), ('Butter',), ('Eggs',), ('Milk',)]
Level 2 (Itemsets of size 2): [('Bread', 'Butter'), ('Bread', 'Eggs'), ('Bread', 'Milk'), ('Butter', 'Milk')]
```

## Usage
Run the script with Python to extract frequent itemsets from the dataset. You can adjust the `min_support` value to change the frequency threshold.

---
This is not an actual analysis. It is just a practice code for DWM lab.
