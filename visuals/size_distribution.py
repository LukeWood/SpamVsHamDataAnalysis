import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

spam_lines = [" ".join(x.split("\t")[1:]) for x in open("../data/SMSSpamCollection") if x.split('\t')[0] == "spam"]
ham_lines = [" ".join(x.split("\t")[1:]) for x in open("../data/SMSSpamCollection") if x.split('\t')[0] == "ham"]
total_lines = [" ".join(x.split("\t")[1:]) for x in open("../data/SMSSpamCollection")]

spam_lines = filter(lambda x:len(x) < 160,spam_lines)
ham_lines = filter(lambda x:len(x) < 160,ham_lines)
total_lines = filter(lambda x:len(x) < 160,total_lines)

sns.distplot([len(x) for x in spam_lines]);
plt.show()

sns.distplot([len(x) for x in ham_lines]);
plt.show()

sns.distplot([len(x) for x in total_lines]);
plt.show()
