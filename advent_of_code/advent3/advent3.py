import re
import string
def read_text_file(file):
    text = open(file)
    text = text.read()
    return text
def text_to_article_list(text):
    lis = re.split('\n', text, flags = re.IGNORECASE)
    for obj in lis:
        if obj == "":
            lis.remove(obj)
    return lis
def split_by_3(list):
    tot = []
    for i in range(0,len(list), 3):
        tot.append(list[i:i + 3])
    return tot

def separate_strings(lis):
    total = []
    for string in lis:
        listy = []
        firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
        listy.append(firstpart)
        listy.append(secondpart)
        total.append(listy)    
    return total
def common_letter(lists):
    tot = []
    for list in lists:
        total= []
        for string in list:
            string_set = set()
            for letter in string:
                string_set.add(letter)
            total.append(string_set)
        i = 0
        while i < 1:
            common_set = total[i].intersection(total[i+1])
            i +=1
        tot.append(common_set.intersection(list[-1]))
    return tot
        
def get_score_of_letter(listt):
    total = []
    lower_alphabet = list(string.ascii_lowercase)
    upper_alphabet = list(string.ascii_uppercase)
    lower_alphabet.extend(upper_alphabet)
    for settt in listt:
        for stringg in settt:
            score = lower_alphabet.index(stringg) + 1
            total.append(score)
    return total

          
if __name__ == "__main__":
    list_of_segments = text_to_article_list(read_text_file("stuff.txt"))
    listy_list = common_letter(split_by_3(list_of_segments))
    print(sum(get_score_of_letter(listy_list)))
    
