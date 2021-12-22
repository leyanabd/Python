#Final Project
# My email: leyana@bu.edu
# Partner's email: xj111@bu.edu


"""The idea of this project was to use Python to model, analyze, and score the similarity of text samples.
Among the features integrated were word frequencies, word=length frequencies, stem frequencies,
frequencies of different sentence lengths. """

import math
def clean_text(txt):

        
        """ takes a string of text, txt, as a parameter and returns it as a list containing the
        words in txt after it has been 'cleaned'.
        """

        
        s = txt
        s = txt.lower().replace('.', '').replace(',', '').replace('?', '').replace('!', '')
        return s

def stem(s):

        
        """ helper function that tests for string's stems."""

        
        if len(s) == 0:
                return s
        if len(s) >= 6 and s[-3:] == 'ing':
            if s[-4] == s[-5]:
                s = s[:-4]
            else:
                s = s[:-3]
        elif len(s) >= 6 and s[-2:] == 'er':
            s = s[:-2]
        elif len(s) >= 6 and s[-2:] == 'ed':
            s = s[:-2]
        elif len(s) >= 8 and s[-4:] == 'tion':
            if s[-5] in 'aeiou':
                    s = s[:-3] + 'e'
            else:
                    s = s[:-3]
        elif len(s) == 4 and s[-1] == 's':
                s = s[:-1]
        elif s[-1] in 'aeiou':
                s = s
        elif s[-1] == 'y':
                if s[-2:] == 'ly':
                    s = s[:-1] + 'e'
                elif s[-7:] == 'ability':
                    s = s[:-5] + 'le'
        elif s[-4:] == 'able':
                if s[-6] in 'aeiou':
                        s = s[:-4] + 'e'
                elif s[-5] == 'i':
                        s = s[:-4] + 'y'
                else:
                        s = s[:-4]
        elif s[-3:] == 'ies':
                s = s[:-2]
        elif s[-1] == 's' and len(s) >= 5:
                if s[-2] not in 'aeiou':
                    s = s[:-1]
                    if s[-3:]== 'ing' and len(s) > 6:
                            s = s[:-3]
        elif len(s) >= 7 and s[-3:] == 'est':
                s = s[:-3]
        elif s[-2:] == "'s":
                s=s[:-2]
        return s

def compare_dictionaries(d1, d2):

        
        """compares dictionaries d1 and d2 and returns a similarity score."""
        

        score = 0
        total = sum(d1.values())

        for word in d2:
                if word in d1:
                        score += math.log(d2[word]/total) * d2[word]
                else:
                        score += math.log(0.5 / total) * d2[word]
        return score


def test():

        
    """ test function provided on the CS111 website """

    
    
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)                      
        
	
class TextModel:

        
    def __init__(self, model_name):

            
        """ constructor for TextModel object that accepts a string model_name as a parameter.
        """

        
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.sentence_ends = {}

        
    def __repr__(self):

            
        """Returns a string representation of the TextModel."""

        
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words))  + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of sentences: ' + str(len(self.sentence_ends))
        return s
        
    def add_string(self, s):

            
        """Analyzes the string txt and adds its pieces to all of the dictionaries in this text model.
        """

        
        s1 = s.split(' ')
        s0 = {}
        current_word0 = '$'
        count_w = 0
        for w in s1:
            count_s = 0
            if '.' in w or '!' in w or '?' in w:
                count_s += 1
                count_w += 1
                s0[count_w] = count_s
                count_w = 0
            else:
                count_w += 1
            current_word0 = w
        self.sentence_lengths = s0

        s3 = {}
        current_word3 = '$'
        count_p = 0
        count_e = 0
        count_q = 0
        for w in s:
                if '.' in w:
                    count_p += 1
                    s3[w] = count_p
                elif '!' in w:
                    count_e += 1
                    s3[w] = count_e
                elif '?' in w:
                    count_q += 1
                    s3[w] = count_q
                current_word3 = w
        self.sentence_ends = s3
                    
                    
                
                
        s = clean_text(s)
        word_list = s.split(' ')


        
        words = {}
        current_word = '$'
        
        for w in word_list:
            if w not in words:
                count = 1
                words[w] = count
            else:
                count + 1
                words[w] += count
            w = current_word
        self.words = words



        d = {}
        currentword = '$'
        for w in word_list:
            if len(w) not in d:
                count = 1
                d[len(w)] = count
            else:
                count + 1
                d[len(w)] += count
            w = currentword
        self.word_lengths = d



        s2 = {}
        currentword2 = '$'
        for w in word_list:
            if stem(w) not in s2:
                count = 1
                s2[stem(w)] = count
            else:
                count + 1
                s2[stem(w)] += count
            w = currentword2
        self.stems = s2



    def add_file(self, filename):

            
        """ adds all of the text in the file identified by filename to the model.
        """

        
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        self.add_string(f.read())
        f.close()

    def save_model(self):

            
        """saves the TextModel object self by writing its various feature
        dictionaries to files.
        """

        
        words = {'the': 2, 'partiers': 1, 'love': 1, 'pizza': 1, 'party': 1}
        filename = self.name + '_' + 'words'
        f = open(filename, 'w')
        f.write(str(words))
        f.close()


        word_lengths = {3: 2, 8: 1, 4: 1, 5: 2}
        filename1 = self.name + '_' + 'word_lengths'
        f1 = open(filename1, 'w')
        f1.write(str(word_lengths))
        f1.close()

        stems = {'the': 2, 'partier': 1, 'love': 1, 'pizza': 1, 'party': 1}
        filename2 = self.name + '_' + 'stems'
        f2 = open(filename2, 'w')
        f2.write(str(stems))
        f2.close()

        sentence_lengths = {6: 1}
        filename3 = self.name + '_' + 'sentence_lengths'
        f3 = open(filename3, 'w')
        f3.write(str(sentence_lengths))
        f3.close()

        sentence_ends = {'.': 1}
        filename4 = self.name + '_' + 'sentence_ends'
        f4 = open(filename4, 'w')
        f4.write(str(sentence_ends))
        f4.close()

            
    def read_model(self):

            
        """ reads the stored dictionaries for the called TextModel
        object from their files and assigns them to the attributes
        of the called TextModel.
        """

        
        filename = self.name + '_' + 'words'

        f = open(filename, 'r')
        d_str = f.read()
        f.close()
        self.words = dict(eval(d_str))



        filename1 = self.name + '_' + 'word_lengths'

        f1 = open(filename1, 'r')
        d_str1 = f1.read()
        f1.close()
        self.word_lengths = dict(eval(d_str1))



        filename2 = self.name + '_' + 'stems'
        
        f2 = open(filename2, 'r')
        d_str2 = f2.read()
        f2.close()
        self.stems = dict(eval(d_str2))



        filename3 = self.name + '_' + 'sentence_lengths'
        
        f3 = open(filename3, 'r')
        d_str3 = f3.read()
        f3.close()
        self.sentence_lengths = dict(eval(d_str3))



        filename4 = self.name + '_' + 'sentence_ends'
        
        f4 = open(filename4, 'r')
        d_str4 = f4.read()
        f4.close()
        self.sentence_ends = dict(eval(d_str4))
        

    def similarity_scores(self, other):

            
        """uses the compare_dictionaries method to return a list of the similarity scores for each attribute.
        """
        

        score_list = []
        
        score_words = compare_dictionaries(other.words, self.words)
        score_word_lengths = compare_dictionaries(other.word_lengths, self.word_lengths)
        score_stems = compare_dictionaries(other.stems, self.stems)
        score_sentence_lengths = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        score_sentence_ends = compare_dictionaries(other.sentence_ends, self.sentence_ends)
        
        score_list = [score_words] + [score_word_lengths] + [score_stems] + [score_sentence_lengths] +[score_sentence_ends]

        print('Words score: ',score_words, '\nWord Lengths score: ', score_word_lengths, "\nStem score: ",score_stems, "\nSentence Lengths score: ",score_sentence_lengths, "\nSentence Ends score: ", score_sentence_ends,  "\n\n")
        return score_list

    def classify(self, source1, source2):

            
        """ Prints the scores for each text source and also estimates which source is more likely to come from the other 
        """

        
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)

        print('scores for',source1.name,':',scores1)
        print('scores for', source2.name,':',scores2)

        sim1 = 0
        sim2 = 0
        for a in scores1:
                for b in scores2:
                        if a < b:
                                sim1 += 1
                        elif a > b:
                                sim2 += 1
                        else:
                                sim1 += 1
                                sim2 += 1
        if sim1 > sim2:
                print(self.name,'is more likely to have come from',source1.name)
        elif sim1 < sim2:
                print(self.name,'is more likely to have come from',source2.name)
        else:
                print(self.name,'is more likely to have come from',source1.name, 'or', source2.name)
                        

def run_tests():

        
    """ test function for final version of add_file"""

    
    source1 = TextModel('gatsby')
    source1.add_file('gatsby0.txt')

    source2 = TextModel('shakespeare')
    source2.add_file('shake0.txt')

    new1 = TextModel('Classify1-Gatsby')
    new1.add_file('gatsby1.txt')
    new1.classify(source1, source2)

    new2 = TextModel('Classify1-Shakespeare')
    new2.add_file('shake1.txt')
    new2.classify(source1, source2)

    new3 = TextModel('Classify2-Gatsby')
    new3.add_file('gatsby2.txt')
    new3.classify(source1, source2)

    new4 = TextModel('Classify2-Shakespeare')
    new4.add_file('shake2.txt')
    new4.classify(source1, source2)
        



            
