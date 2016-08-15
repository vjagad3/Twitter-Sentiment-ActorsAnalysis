import sys
import json

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	#TODO: Implement
	afinnfile = open('./data/AFINN-111.txt','r')
	scores = {}
	sentiment_scores = {}
	i=0
	j=0
	for line in afinnfile:
		term, score = line.split("\t")
		scores[term] = float(score)
	for line in tweet_file:
		line = line.strip('\n')
		tweet=json.loads(line)
		tweet_score=0
		tweets=tweet['text'].lower()
		tokens=tweets.split(" ") #.decode('utf-8')
		for each_token in tokens:
			if each_token in scores.keys():
				tweet_score=tweet_score+scores[each_token]
		sentiment_scores[tweets]=tweet_score
	for w in sorted(sentiment_scores, key=sentiment_scores.get, reverse=True):
		if(i<10):	
			t= str(sentiment_scores[w])
			print(t,':',w)			
			i=i+1
		else:
			break
	rev={}
	for w in sorted(sentiment_scores, key=sentiment_scores.get, reverse=False):
		if (j<10):
			rev[w]=sentiment_scores[w]
			j=j+1
		else:
			break
	for w in sorted(rev, key=rev.get, reverse=True):
		t= str(rev[w])
		print(t,':',w)			
		i=i+1
					
			
if __name__ == '__main__':
    main()
