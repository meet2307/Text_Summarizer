from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from youtube_transcript_api import YouTubeTranscriptApi

def summmary(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    stoppingWords = set(stopwords.words("english"))
    print(sentences)

    freq_table = dict()
    for word in words:
        word = word.lower()
        if word in stoppingWords:
            continue
        if word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1

    sent_value = dict()
    for sentence in sentences:
        for word, freq in freq_table.items():
            if word in sentence.lower():
                if sentence in sent_value:
                    sent_value[sentence] += freq
                else:
                    sent_value[sentence] = freq

    freq_sum = 0
    for sentence in sent_value:
        freq_sum += sent_value[sentence]

    average = int(freq_sum / len(sent_value))

    summery = ''
    for sentence in sentences:
        if (sentence in sent_value) and (sent_value[sentence] > average * 1.3):
            summery += ' ' + sentence
    print(len(summery))
    return summery


def ytlink(link):

    videoid=link.split("=")[1]
    tns=YouTubeTranscriptApi.get_transcript(videoid)
    text=''
    for txt in tns:
        text+=" "+txt['text']
    print(len(text))

    return summmary(text)
