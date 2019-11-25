def count_positives_sum_negatives(arr):
    if len(arr) == 0 or arr == 0:
        return []
    pos_count, neg_sum = 0, 0
    for num in arr:
        if num > 0:
            pos_count +=1
        elif num < 0:
            neg_sum += num
    return [pos_count, neg_sum]