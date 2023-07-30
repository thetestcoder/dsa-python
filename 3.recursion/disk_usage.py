import os


def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            child_path = os.path.join(path, filename)
            total += disk_usage(child_path)
    print('{0:<7}'.format(total), path)
    return total

path = input("please enter a relative path: ")

total_size = disk_usage(path)

print(f"Total Size: {total_size}")