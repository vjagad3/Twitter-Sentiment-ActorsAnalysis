import sys
import json

def main():
	tweet_file = open(sys.argv[2])
	stop_words_file = open(sys.argv[1])
	dict1=dict()
	stop_words = []
	count=0
	i=0
    #TODO: Implement
	for sw in stop_words_file:
		sw = sw.strip('\n')
		stop_words.append(sw)
	for line in tweet_file:
		line = line.strip('\n')
		parsed_line = json.loads(line)
		tweet = parsed_line['text']
		tokens=tweet.split()
		l_tokens=[element.strip().lower() for element in tokens]
		for items in l_tokens:
			if items not in stop_words: 
				if items in dict1.keys():
					dict1[items]=dict1[items]+1
				else:
					dict1[items]=1
				count=count+1	
	for w in sorted(dict1, key=dict1.get, reverse=True):			
		t= str(float(dict1[w])/count) #'%.5f'%(dict1[w]/count) 
		print (w,' ',t)
		print ("world")
		i=i+1
		

if __name__ == '__main__':
    main()
