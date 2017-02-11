import pandas as pd

def get_pairs(lines):
    d={}
    for text in lines:
        i=1
        words = text.replace("\n","").split(" ")
        while(i < len(words)):
            key = words[i]+" "+words[i-1]
            if not key in d:
                d[key]=0
            d[key]+=1
            i+=1
    return d

def get_top_25(lines):
    d = get_pairs(lines)
    df = pd.DataFrame([(x,y) for x,y in d.items()])
    return df.sort([1])[-25:]

spam_lines = [" ".join(x.split("\t")[1:]).lower() for x in open("../data/SMSSpamCollection") if x.split('\t')[0] == "spam"]
ham_lines = [" ".join(x.split("\t")[1:]).lower() for x in open("../data/SMSSpamCollection") if x.split('\t')[0] == "ham"]

top_spam = get_top_25(spam_lines)
top_ham = get_top_25(ham_lines)

print(top_ham)
print(top_spam)
