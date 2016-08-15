import sys
import json
import types

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	#TODO: Implement
	#file_reader = csv.reader(csv_file)
	afinnfile = open('./data/AFINN-111.txt','r')
	scores = {}
	ss_scores = {}
	state_abbr={"AL":"Alabama","AK":"Alaska","AZ":"Arizona","AR":"Arkansas","CA":"California","CO":"Colorado","CT":"Connecticut","DE":"Delaware", "DC":"District of Columbia", "FL":"Florida","GA":"Georgia","HI":"Hawaii","ID":"Idaho","IL":"Illinois","IN":"Indiana","IA":"Iowa","KS":"Kansas","KY":"Kentucky","LA":"Louisiana","ME":"Maine","MT":"Montana","NE":"Nebraska","NV":"Nevada","NH":"New Hampshire","NJ":"New Jersey","NM":"New Mexico","NY":"New York","NC":"North Carolina","ND":"North Dakota","OH":"Ohio","OK":"Oklahoma","OR":"Oregon","MD":"Maryland","MA":"Massachusetts","MI":"Michigan","MN":"Minnesota","MS":"Mississippi","MO":"Missouri","PA":"Pennsylvania","RI":"Rhode Island","SC":"South Carolina","SD":"South Dakota","TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont","VA":"Virginia","WA":"Washington","WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming"}
	i=0
	j=0
	for line in afinnfile:
		term, score = line.split("\t")
		scores[term] = float(score)
	for line in tweet_file:
		line = line.strip('\n')
		tweet=json.loads(line)
		tweet_score=0
		#for item in tweet:
		if 'text' in tweet:
			tweets=tweet['text'].lower()
			tokens=tweets.split(" ") #.decode('utf-8')
			for each_token in tokens:
				if each_token in scores.keys():
					tweet_score=tweet_score+scores[each_token]
		if 'place' in tweet and tweet['place'] is not None :
			if 'full_name' in tweet['place'] and tweet['place']['full_name'] is not None:
				if 'country' in tweet['place'] and tweet['place']['country'] is not None:
					if tweet['place']['country'] == 'United States':
						location=tweet['place']['full_name']
						address=location.split()
						state=address[-1]
						if state in state_abbr.keys():
							state_l = state_abbr[state]
							if state_l in ss_scores.keys():
								ss_scores[state_l]=ss_scores[state_l]+tweet_score
							else:
								ss_scores[state_l]=tweet_score
	
	for w in sorted(ss_scores, key=ss_scores.get, reverse=True):	
		t= str(ss_scores[w])
		print(t,':',w)			
			
			

if __name__ == '__main__':
    main()
