# Write a function nearly equal to test whether two strings are nearly equal.
# Two strings a and b are nearly equal when a can be generated by single mutation on b and vice versa.


def nearly_equal(str1, str2):
    str1_len, str2_len = len(str1), len(str2)

    if abs(str1_len - str2_len) > 1:
        # print('Case 1')  # debugging
        return False

    if str1_len == str2_len:
        # print('Case 2')  # debugging
        diffs = 0
        for i, j in zip(str1, str2):
            if i != j:
                diffs += 1
                if diffs > 1:
                    return False
        return True

    if abs(str1_len - str2_len) == 1:
        # print('Case 3')  # debugging
        small, big = (str1, str2) if (str1_len < str2_len) else (str2, str1)
        i = j = 0
        mutated = False
        while True:
            if small[i] != big[j]:
                if mutated:
                    return False
                mutated = True
            else:
                i += 1
                if i == min(str1_len, str2_len):
                    break
            j += 1
        return True


print('Nearly Equal:', nearly_equal(str1=input('\nstr1: '), str2=input('str2: ')))
