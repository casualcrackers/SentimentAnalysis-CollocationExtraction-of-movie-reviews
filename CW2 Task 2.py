#imports 
from nltk import word_tokenize
from nltk import pos_tag
from nltk import bigrams
import operator
import itertools 

#function to compute frequency of unfiltered co-occurance frequencies
#function takes an input of a list of bigrams with pos tags, previously extracted using the
#function list(bigrams()) and it should return a dictionary with the following keys/values:
#key of dictionary: Tuple: <first word of bigram, second word of bigram>
#value of dictionary : frequency of bigram 
def compute_frequency_of_bigrams(bigrams_with_pos_tags):
    bigrams_with_frequencies = {}
    for first_element, second_element in bigrams_with_pos_tags:
        first_word_of_bigram, first_word_pos_tag = first_element[0], first_element[1]
        second_word_of_bigram, second_word_pos_tag = second_element[0], second_element[1]
        if (first_word_of_bigram, second_word_of_bigram) in bigrams_with_frequencies:
            bigrams_with_frequencies[(first_word_of_bigram, second_word_of_bigram)] += 1     
        else:  
            bigrams_with_frequencies[(first_word_of_bigram, second_word_of_bigram)] = 1           
    return bigrams_with_frequencies

#function to compute frequency of filtered co-occurance frequencies 
#function takes an input of a list of bigrams with pos tags, previously extracted using the
#function list(bigrams()) and it should return a dictionary with the following keys/values:
#key of dictionary: Tuple: <first word of bigram, second word of bigram>
#value of dictionary : frequency of bigram
#uses a condition to assure that the first words POS tag is VB or JJ and the second word pos tag is NN
def compute_frequency_of_bigrams_filtered(bigrams_with_pos_tagsF):
    bigrams_with_frequenciesF = {}
    for first_elementF, second_elementF in bigrams_with_pos_tagsF:
        first_word_of_bigramF, first_word_pos_tagF = first_elementF[0], first_elementF[1]
        second_word_of_bigramF, second_word_pos_tagF = second_elementF[0], second_elementF[1]
        if ((first_word_pos_tagF == "VB") or (first_word_pos_tagF == "JJ")):
            if  (second_word_pos_tagF == 'NN'):
                if (first_word_of_bigramF, second_word_of_bigramF) in bigrams_with_frequenciesF:
                    bigrams_with_frequenciesF[(first_word_of_bigramF, second_word_of_bigramF)] += 1     
                else:  
                    bigrams_with_frequenciesF[(first_word_of_bigramF, second_word_of_bigramF)] = 1           
    return bigrams_with_frequenciesF
                
            
#opens and reads negative reviews found in sentiment analysis and stores them as a variable
with open('Negative_reviews.txt') as f:
    lines = f.readlines()
#converts all text to string to prevent any errors from erroneous lines
    document = str(lines)
#text is tokenized using word_tokenize nltk function and stored in words variable
    words = word_tokenize(document)
#tokenized text is pos tagged using pos_tag nltk function and stored in words_with_pos_tags variable 
    words_with_pos_tags = pos_tag(words)
#pos tagged text are converted to bigrams and stored in a list using nltk bigrams function,
#which is then stored in bigrams_with_pos_tags variable     
    bigrams_with_pos_tags = list(bigrams(words_with_pos_tags))
#frequency of bigrams are calculated using compute_frequency_of_bigrams function, which uses
#bigrams_with_pos_tags variable as a parameter for the function, result is stored in bigrams_with_frequencies variable
    bigrams_with_frequencies = compute_frequency_of_bigrams(bigrams_with_pos_tags)
#sorts bigrams from highest to lowest based on their frequency scores and
#stores in bigrams_with_frequencies_sorted variable by using bigrams_with_frequencies as a parameter
    bigrams_with_frequencies_sorted = dict(sorted(bigrams_with_frequencies.items(),
                                                        key=operator.itemgetter(1),reverse=True)) 
#fetches top 40 bigrams from bigrams_with_frequencies_sorted and stored in topBigrams variable
    topBigrams = (dict(itertools.islice(bigrams_with_frequencies_sorted.items(),40)))
#opens txt file named Unfiltered_Negative_reviews and writes the topBigrams variable to it as a string
    with open('Unfiltered_Negative_reviews.txt', 'w') as i:
        i.write(str(topBigrams))
    #prints text stored in Unfiltered_Negative_reviews.txt
    print("--------------------------most popular Unfiltered Negative co-occurance frequencies----------------")
    f = open("Unfiltered_Negative_reviews.txt", "r")
    print(f.read())
    print("---------------------------------------------------------------------------------------------------")
    
#opens and reads Positive reviews found in sentiment analysis and stores them as a variable
with open('Positive_reviews.txt') as f:
      lines = f.readlines()
#converts all text to string to prevent any errors from erroneous lines      
      document= str(lines)
#text is tokenized using word_tokenize nltk function and stored in words variable      
      words = word_tokenize(document)
#tokenized text is pos tagged using pos_tag nltk function and stored in words_with_pos_tags variable       
      words_with_pos_tags = pos_tag(words)
#pos tagged text are converted to bigrams and stored in a list using nltk bigrams function,
#which is then stored in bigrams_with_pos_tags variable       
      bigrams_with_pos_tags = list(bigrams(words_with_pos_tags))
#frequency of bigrams are calculated using compute_frequency_of_bigrams function, which uses
#bigrams_with_pos_tags variable as a parameter for the function, result is stored in bigrams_with_frequencies variable      
      bigrams_with_frequencies = compute_frequency_of_bigrams(bigrams_with_pos_tags)
#sorts bigrams from highest to lowest based on their frequency scores and
#stores in bigrams_with_frequencies_sorted variable by using bigrams_with_frequencies as a parameter      
      bigrams_with_frequencies_sorted = dict(sorted(bigrams_with_frequencies.items(),
                                                          key=operator.itemgetter(1),reverse=True)) 
#fetches top 40 bigrams from bigrams_with_frequencies_sorted and stored in topBigrams variable      
      topBigrams = (dict(itertools.islice(bigrams_with_frequencies_sorted.items(),40)))
#opens txt file named Unfiltered_Positive_reviews and writes the topBigrams variable to it as a string      
      with open('Unfiltered_Positive_reviews.txt', 'w') as i:
          i.write(str(topBigrams))
      #prints text stored in Unfiltered_Positive_reviews.txt    
      print("--------------------------most popular Unfiltered Positive co-occurance frequencies----------------")
      f = open("Unfiltered_Positive_reviews.txt", "r")
      print(f.read())
      print("---------------------------------------------------------------------------------------------------")
      
#opens and reads Negative reviews found in sentiment analysis and stores them as a variable
with open('Negative_reviews.txt') as f:
    lines = f.readlines()
#converts all text to string to prevent any errors from erroneous lines      
    document= str(lines)
#text is tokenized using word_tokenize nltk function and stored in words variable        
    words = word_tokenize(document)
#tokenized text is pos tagged using pos_tag nltk function and stored in words_with_pos_tagsF variable           
    words_with_pos_tagsF = pos_tag(words)
#pos tagged text are converted to bigrams and stored in a list using nltk bigrams function,
#which is then stored in bigrams_with_pos_tagsF variable     
    bigrams_with_pos_tagsF = list(bigrams(words_with_pos_tagsF))
#frequency of bigrams are calculated using compute_frequency_of_bigrams_filtered function, which uses
#bigrams_with_pos_tagsF variable as a parameter for the function, result is stored in bigrams_with_frequenciesF variable     
    bigrams_with_frequenciesF = compute_frequency_of_bigrams_filtered(bigrams_with_pos_tagsF)
#sorts bigrams from highest to lowest based on their frequency scores and
#stores in bigrams_with_frequencies_sortedF variable by using bigrams_with_frequenciesF as a parameter     
    bigrams_with_frequencies_sortedF = dict(sorted(bigrams_with_frequenciesF.items(),
                                                        key=operator.itemgetter(1),reverse=True))
#fetches top 40 bigrams from bigrams_with_frequencies_sortedF and stored in topBigrams variable     
    topBigrams = (dict(itertools.islice(bigrams_with_frequencies_sortedF.items(),40)))
    with open('Filtered_Negative_reviews.txt', 'w') as i:
        i.write(str(topBigrams))
#prints text stored in Filtered_Negative_reviews.txt          
    print("--------------------------most popular Filtered Negative co-occurance frequencies----------------")
    f = open("Filtered_Negative_reviews.txt", "r")
    print(f.read())
    print("---------------------------------------------------------------------------------------------------")
    
#opens and reads Positive reviews found in sentiment analysis and stores them as a variable    
with open('Positive_reviews.txt') as f:
    lines = f.readlines()
#converts all text to string to prevent any errors from erroneous lines          
    document= str(lines)
#text is tokenized using word_tokenize nltk function and stored in words variable    
    words = word_tokenize(document)
#tokenized text is pos tagged using pos_tag nltk function and stored in words_with_pos_tagsF variable     
    words_with_pos_tagsF = pos_tag(words)
#pos tagged text are converted to bigrams and stored in a list using nltk bigrams function,
#which is then stored in bigrams_with_pos_tagsF variable      
    bigrams_with_pos_tagsF = list(bigrams(words_with_pos_tagsF))
#frequency of bigrams are calculated using compute_frequency_of_bigrams_filtered function, which uses
#bigrams_with_pos_tagsF variable as a parameter for the function, result is stored in bigrams_with_frequenciesF variable    
    bigrams_with_frequenciesF = compute_frequency_of_bigrams_filtered(bigrams_with_pos_tagsF)
#sorts bigrams from highest to lowest based on their frequency scores and
#stores in bigrams_with_frequencies_sortedF variable by using bigrams_with_frequenciesF as a parameter     
    bigrams_with_frequencies_sortedF = dict(sorted(bigrams_with_frequenciesF.items(),
                                                        key=operator.itemgetter(1),reverse=True))  
#fetches top 40 bigrams from bigrams_with_frequencies_sortedF and stored in topBigrams variable        
    topBigrams = (dict(itertools.islice(bigrams_with_frequencies_sortedF.items(),40)))
    with open('Filtered_Positive_reviews.txt', 'w') as i:
        i.write(str(topBigrams))
#prints text stored in Filtered_Positive_reviews.txt 
    print("--------------------------most popular Filtered positive co-occurance frequencies----------------")
    f = open("Filtered_Positive_reviews.txt", "r")
    print(f.read())
    print("---------------------------------------------------------------------------------------------------")
    
     