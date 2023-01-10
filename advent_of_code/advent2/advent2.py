import re
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

def get_scores_total(lis):
    outcomes = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
    }
    desired_outcomes = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7,
    }
    total = 0
    for string in lis:
        if string in desired_outcomes:
            score = desired_outcomes[string]
            total += score
    return total
    

if __name__ == "__main__":
    whole_list_of_battles = text_to_article_list(read_text_file("data.txt"))
    print(get_scores_total(whole_list_of_battles))