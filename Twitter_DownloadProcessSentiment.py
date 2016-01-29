from pattern.web import Twitter
from textblob import TextBlob


t = Twitter()
i = None
for j in range(3):
    for tweet in t.search('trump', start=i, count=30):

        print tweet.id
        print tweet.name
        print tweet.text

        blob = TextBlob(tweet.text)
        for sentence in blob.sentences:
            print(sentence.sentiment.polarity)

    def fail(self, link):
        print 'failed:', repr(link.url)

#p = Polly(links=['http://www.research.vcu.edu/'], delay=1)
#while not p.done:
#    p.crawl(method=2, cached=False, throttle=1)