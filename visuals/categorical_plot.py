spam_lines = [" ".join(x.split("\t")[1:]) for x in open("../data/SMSSpamCollection") if x.split('\t')[0] == "spam"]
ham_lines = [" ".join(x.split("\t")[1:]) for x in open("../data/SMSSpamCollection") if x.split('\t')[0] == "ham"]

print(" ".join(ham_lines))
