import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import CountVectorizer
from googletrans import Translator
from textblob import TextBlob
from sklearn.naive_bayes import MultinomialNB
import re                                  # library for regular expression operations
import string                              # for string operations
import pandas as pd
from nltk import TweetTokenizer
from nltk.corpus import stopwords          # module for stop words that come with NLTK
from nltk.stem import PorterStemmer        # module for stemming
from nltk.tokenize import TweetTokenizer   # module for tokenizing strings
import nltk
from nltk.corpus import twitter_samples
import numpy as np
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

def remove_hyperlinks_marks_styles(tweet):
    # remove old style retweet text "RT"
    new_tweet = re.sub(r'^RT[\s]+', '', tweet)

    # remove hyperlinks
    new_tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', new_tweet)

    # remove hashtags
    # only removing the hash # sign from the word
    new_tweet = re.sub(r'#', '', new_tweet)

    return new_tweet


tokenizer: TweetTokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                           reduce_len=True)


def tokenize_tweet(tweet):
    tweet_tokens = tokenizer.tokenize(tweet)

    return tweet_tokens


nltk.download('stopwords')

# Import the english stop words list from NLTK
stopwords_english = stopwords.words('english')

punctuations = string.punctuation


def remove_stopwords_punctuations(tweet_tokens):
    tweets_clean = []

    for word in tweet_tokens:
        if (word not in stopwords_english and word not in punctuations):
            tweets_clean.append(word)

    return tweets_clean


stemmer = PorterStemmer()


def get_stem(tweets_clean):
    tweets_stem = []

    for word in tweets_clean:
        stem_word = stemmer.stem(word)
        tweets_stem.append(stem_word)

    return tweets_stem


def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))

def process_tweet(tweet):
    processed_tweet = remove_hyperlinks_marks_styles(tweet)
    tweet_tokens = tokenize_tweet(processed_tweet)
    tweets_clean = remove_stopwords_punctuations(tweet_tokens)
    tweets_stem = get_stem(tweets_clean)

    return tweets_stem


ds=pd.read_csv("distilBertOutput.csv")




print(ds.head())

x = np.array(ds["clean_text"])
y = np.array(ds["Sentiment"])
y_test=np.array(ds["Sentiment"])
for i in range(0,2999):
    y_test[i]='neutral'
translator = Translator()

for i in range(0,2999):
    x[i] =listToString(process_tweet(x[i]))
for i in range(0,2999):
    out = translator.translate(x[i], dest="en", src="hi")
    analysis = TextBlob(out.text)
    if analysis.sentiment.polarity > 0:
        y_test[i]='positive'
    elif analysis.sentiment.polarity == 0:
        y_test[i]='neutral'
    else:
        y_test[i]='negative'

print(classification_report(y,y_test))





news_headline = "Bakwas phone hai"
out = translator.translate(news_headline, dest="en", src="hi")
news_headline =out.text
analysis = TextBlob(out.text)
if analysis.sentiment.polarity > 0:
    print('positive')
elif analysis.sentiment.polarity == 0:
    print('neutral')
else:
    print('negative')



news_headline = "Acha hai bohot"
out = translator.translate(news_headline, dest="en", src="hi")
news_headline =out.text
analysis = TextBlob(out.text)
if analysis.sentiment.polarity > 0:
    print('positive')
elif analysis.sentiment.polarity == 0:
    print('neutral')
else:
    print('negative')




