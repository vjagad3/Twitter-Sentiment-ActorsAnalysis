import sys
import csv
def main():
	sent_file = open(sys.argv[1])
	csv_file = open(sys.argv[2])
	file_reader = csv.reader(csv_file)
	#TODO: Implement
	afinnfile = open('./data/AFINN-111.txt','r')
	scores = {}
	sentiment_scores={}
	count=0
	prev_actor=""
	for line in afinnfile:
		term, score = line.split("\t")
		scores[term] = float(score)
	header=next(file_reader)
	for line in file_reader:
		actor = line[0]
		tweet_score=0
		tweets=line[1] 
		tokens=tweets.split(" ")
		for each_token in tokens:
			if each_token in scores.keys():
				tweet_score=tweet_score+scores[each_token]
		if actor in sentiment_scores.keys():
			sentiment_scores[actor]=sentiment_scores[actor]+tweet_score
			count=count+1
		else:
			sentiment_scores[actor]=tweet_score
			if((actor!=prev_actor) & (prev_actor!="")):
				sentiment_scores[prev_actor]=(sentiment_scores[prev_actor]/float(count))
				count=1
			else:
				count=count+1
		prev_actor=actor
	sentiment_scores[actor]=(sentiment_scores[actor]/float(count))
	for w in sorted(sentiment_scores, key=sentiment_scores.get, reverse=True):
		print(w,':',str(sentiment_scores[w]))
			
			

if __name__ == '__main__':
    main()
