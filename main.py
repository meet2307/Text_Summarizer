from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize



# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def summerize(text):
    #tokenization

    sentences=sent_tokenize(text)
    words=word_tokenize(text)
    stoppingWords=set(stopwords.words("english"))



    freq_table=dict()
    for word in words:
        word=word.lower()
        if word in stoppingWords:
            continue
        if word in freq_table:
            freq_table[word]+=1
        else:
            freq_table[word]=1
    print (freq_table)

    sent_value=dict()
    for sentence in sentences:
        for word,freq in freq_table.items():
            if word in sentence.lower():
                if sentence in sent_value:
                    sent_value[sentence] +=freq
                else:
                    sent_value[sentence] = freq


    print(sent_value)



    freq_sum=0
    for sentence in sent_value:
        freq_sum+=sent_value[sentence]
    print(freq_sum)

    average=int(freq_sum/len(sent_value))
    print(average)

    summery=''
    for sentence in sentences:
        if(sentence in sent_value) and (sent_value[sentence]>average):
            summery+=' '+sentence
    print(summery)

if __name__ == '__main__':
    text= """ Enormous number of video recordings are being created and shared on the Internet through out the day. It has become really difficult to spend time in watching such videos which may have a longer duration than expected and sometimes our efforts may become futile if we couldn't find relevant information out of it. Summarizing transcripts of such videos automatically allows us to quickly look out for the important patterns in the video and helps us to save time and efforts to go through the whole content of the video."""
    summerize(text)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
