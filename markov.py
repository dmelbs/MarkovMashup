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
        self.add_string(fin.read())
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
                self.add_string(line)
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
        grams = {}
        N = self.k
        if (len(s) >= self.k ):
            for i in range (len(s1)-len(s)):
                firstChar = s1[i + N]
                gram = s1[i:N]
                charCount = 0
                containsKey = False
                if (gram not in grams):
                   grams[gram] = {}
                   charCount = 1
                   grams[gram][firstChar] = charCount
                   containsKey = True
                elif (firstChar in grams[gram] and gram in grams and containsKey == False):
                    charCount = grams[gram].get(firstChar)
                    charCount += 1
                    grams[gram][firstChar] = charCount
                elif (gram in grams and firstChar not in grams[gram] and containsKey == False):
                    charCount = 1
                    grams[gram][firstChar] = charCount
                elif(len(s)> N):
                    pass
                    
                
            
        print(grams)
        return grams # This does nothing
    
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