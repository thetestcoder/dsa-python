def find_log(num, log_val):
    if num // 2 == 0:
        return log_val
    else:
        log_val += 1
        return find_log(num/2, log_val)


num = 8
print(find_log(num, 0))