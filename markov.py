import numpy as np

class MarkovModel:
    def __init__(self, k):
        """
        Initialize a Markov model with a particular prefix length
        
        Parameters
        ----------
        k: int
            Length of prefix to use
        """
        self.k = k
        ## TODO: Setup any other member variables that might be useful
        self.grams = {}
    
    def load_file(self, filename):
        """
        Load in an entire file as one string and add
        it to the model

        Parameters
        ----------
        filename: string
            Path to file to load
        """
        fin = open(filename)
        self.add_string1(fin.read())
        fin.close()
    
    def load_file_lines(self, filename):
        """
        Load in an entire file as one string and add
        it to the model

        Parameters
        ----------
        filename: string
            Path to file to load
        """
        fin = open(filename)
        for line in fin.readlines():
            line = line.rstrip()
            if len(line) > 0:
                self.add_string1(line)
        fin.close()
    
    def add_string(self, s):
        """
        Incorporate a particular string into your model by adding any prefixes
        if they don't exist and by updating counts
        """
        ## TODO: Fill this in
        s1 = s + s
        firstChar = ' '
        containsKey = False
        charCount = 0
        #grams = {}
        N = self.k
        if ( len(s) >= self.k ):
            print(len(s))
            for i in range (len(s1)-len(s)):
                firstChar = s1[i + N]
                gram = s1[i:N]
                charCount = 0
                #containsKey = False
                if (gram not in self.grams):
                   self.grams[gram] = {}
                   charCount = 1
                   self.grams[gram][firstChar] = charCount
                   containsKey = True
                elif (firstChar in self.grams[gram] and gram in self.grams and containsKey == False):
                    charCount = self.grams[gram].get(firstChar)
                    charCount += 1
                    self.grams[gram][firstChar] = charCount
                elif (gram in self.grams and firstChar not in self.grams[gram] and containsKey == False):
                    charCount = 1
                    self.grams[gram][firstChar] = charCount
        else:
            pass
                    
                
            
        print(self.grams)
        return self.grams # This does nothing
    
    def add_string1(self, s):
        s1 = s + s
        firstChar = ' '
        charCount = 0
        for i in range(len(s1) - len(s)):
            gramLength = i + self.k
            gram = s1[i:self.k]
            if (gram not in self.grams):
                #self.grams[gram] = {}
                gramCounts = {}
                if(gramLength <= len(s)):
                    firstChar = s1[gramLength]
                    if(firstChar in gramCounts):
                        charCount = self.gramCounts.get(firstChar)
                        charCount += 1
                        gramCounts[firstChar] = charCount
                    else:
                        gramCounts[firstChar] = 1
                self.grams[gram] = gramCounts
            else:
                if gramLength <= len(s):
                    firstChar = s1[gramLength]
                    if (firstChar in self.grams[gram]):
                        charCount = self.grams[gram][firstChar]
                        charCount += 1
                        self.grams[gram][firstChar] = charCount
                    else:
                        self.grams[gram][firstChar] = 1
        
        print(self.grams)
        return self.grams
                        
                
                
            
    
    def get_log_probability(self, s):
        """
        Compute the log probability of a particular string according to the model

        Parameters
        ----------
        s: string
            String for which to compute the probability
        
        Returns
        -------
        float: Log probability
        """
        ## TODO: Fill this in
        return 0 # This is a dummy value

    def synthesize_text(self, length):
        """
        Synthesize random text of a particular length in the style captured
        by this model

        Parameters
        ----------
        length: int
            How many characters are in the string to synthesize
        
        Returns
        -------
        string: The synthesized text
        """
        ## TODO: Fill this in
        return "" # This does nothing