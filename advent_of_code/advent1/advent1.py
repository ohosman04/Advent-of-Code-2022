
import re

def read_number_file(file):
    text = open(file)
    text = text.read()
    return text
def text_to_article_list(text):
    lis = re.split('\n\n', text, flags = re.IGNORECASE)
    for obj in lis:
        if obj == "":
            lis.remove(obj)
    return lis
def list_as_int(list):
    i = 0
    while i < len(list):
        list[i] = int(list[i])
        i += 1
    return list
def split_nums(text):
    total = []
    lines = text.splitlines()
    for line in lines:
        words = line.split()
        for word in words:
            total.append(word)
    return total
def splitted_list(lis):
    total = []
    for string in lis:
        list = split_nums(string)
        total.append(list)
    return total
def splitted_list_as_int(list):
    for lis in list:
        lis = list_as_int(lis)
    return list
def get_sum(list):
    total = []
    maximum = 0
    for lis in list:
        total.append(sum(lis))
    sorted_total = sorted(total)
    second = sorted_total[-2]
    third = sorted_total[-3]
    return sum([max(total),second,third])
if __name__ == "__main__":
    #print(read_number_file("numbers.txt"))
    #print(text_to_article_list(read_number_file('numbers.txt')))
    entire_number_list = splitted_list_as_int(splitted_list(text_to_article_list(read_number_file("numbers.txt"))))
    print(get_sum(entire_number_list))
    #WE DID IT YESSSIRRRRRRRRRRRRRRR