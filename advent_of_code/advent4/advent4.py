import re

def read_text_file(file):
    text = open(file)
    text = text.read()
    return text
def split_by_pairs(string):
    total = []
    lis = re.split('\n', string, flags = re.IGNORECASE)
    for string in lis:
        tot = []
        r1,r2 = string.split(",")
        tot.append(r1)
        tot.append(r2)
        total.append(tot)
    return total
def split_pair_by_range(lists):
    tot =[]
    for list in lists:
        ranges = []
        for string in list:
            r1,r2 = string.split("-")
            ranges.append(int(r1))
            ranges.append(int(r2))
        tot.append(ranges)
    return tot
def this_in_that(lists):
    count = 0
    for list in lists:
        if (list[0] >= list[2] and list[1] <= list[3]) or (list[2] >= list[0] and list[3] <= list[1]):
            count += 1
    return count
def not_empty(set):
    if len(set) > 0:
        return True
    else:
        return False
def overlap(lists):
    count = 0
    for lis in lists:
        r1 = set(range(lis[0],lis[1]+1))
        r2 = set(range(lis[2],lis[3]+1))
        if not_empty(r1.intersection(r2)):
            count += 1
    return count



if __name__ == "__main__":
    print(overlap(split_pair_by_range(split_by_pairs(read_text_file("stuffy.txt")))))
    #[5,7,7,9] [2,8,3,7]
    pass