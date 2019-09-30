used = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]


def can_partition(iterstart, array, used, k, current_Bucket_sum, target_bucket_sum):
    if k == 1: return True
    if target_bucket_sum == current_Bucket_sum:
        return can_partition(0, array, used, k - 1, 0, target_bucket_sum)

    for i in range(iterstart, len(array)):
        if not used[i] or current_Bucket_sum + i > target_bucket_sum:
            used[i] = True
            if can_partition(i + 1, array, used, k, current_Bucket_sum + i, target_bucket_sum):
                return True
            used[i] = False
    return False


def canpartition_ksubsets(array, k):
    val = 0
    for j in array:
        val += j
    if k == 0 or val % k != 0:
        return False

    else:
        return can_partition(0, array, used, k, 0, val // k) == True


print(canpartition_ksubsets([4, 3, 2, 3, 5, 2, 1], 4))
