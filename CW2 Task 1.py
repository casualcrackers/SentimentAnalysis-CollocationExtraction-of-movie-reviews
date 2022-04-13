#imports
import pandas as pd
from textblob import TextBlob

#using pandas to read in movie reviews csv file
df = pd.read_csv('Movie_reviews.csv',
                  delimiter='\t',
                  header=None)

#converting the item at 3rd index to string, index 0 and 1 are not part of the review
#reviews must be converted to string so that they can be read and erroneous lines do not cause errors
df[2] = df[2].astype(str)
#assigning a variable equal to items at 3rd index
Movie_reviews_text = df[2]

#clearing txt files due so that text isnt written twice
open('Positive_reviews.txt', 'w').close()
open('Negative_reviews.txt', 'w').close()

#for loop iterating over each sentence in movie_reviews csv file
for index, review_text in enumerate(Movie_reviews_text):
    #variable to track sentence sentiment polarity for full review 
    overall = 0
    #using Textblob on the review text and storing it in a variable named "blob"
    blob = TextBlob(review_text)
    #for loop to iterate for every individual sentence in a review
    for sentence in blob.sentences: 
        #prints sentence as well as the sentence's sentiment score
        print('----------SENTIMENT OF SENTENCE---------------')
        print(sentence,'\t', sentence.sentiment.polarity)
        print('-------------END-------------')
        #adds sentiment score to an attribute to track sentiment score of the full review
        overall += sentence.sentiment.polarity       
#condition that checks is overall sentiment score is negative, and if so appends review to
#txt file that stores all negative reviews. also prints out review and its overall score
        if overall < 0:
             print('----------------overall sentiment------------------')
             print(review_text, overall)
             print('------------------------------------------------------')
             print('negative')
             print('--------------------------------------------------')
             with open('Negative_reviews.txt', 'a') as f:
                f.write(review_text)
#condition that checks is overall sentiment score is neutral, and if so, prints out review and its overall score
        elif overall == 0:
            print('----------------overall sentiment------------------')
            print(review_text, overall)
            print('------------------------------------------------------')
            print('neutral')
            print('--------------------------------------------------')
#condition that checks is overall sentiment score is positive, and if so appends review to
#txt file that stores all positive reviews. also prints out review and its overall score
        else:
            print('----------------overall sentiment------------------')
            print(review_text, overall)
            print('------------------------------------------------------')
            print('positive')
            print('--------------------------------------------------')
            with open('Positive_reviews.txt', 'a') as i:
                i.write(review_text)