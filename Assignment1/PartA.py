import sys

class FreqMapper:


    #Let 'l' be the number of lines in the file 
    #Let 'c' be the number of character on a line 
    #Let 'n' be the number of tokens 
    #In the worst case we have to go through every character on each line which is
    #O(lc) time. 
    #Then we convert each word to lower case whch is O(n) time.
    #This results in a final time complexity of O(lc+n).

    def tokenize(self, file_path):
        """
        input : String with the file name  

        output : List of String with tokens
        """
        try:
            
            tokens=[];
            
            #opening the file for reading 
            with open(file_path, 'r') as file:
                for line in file:

                    #extending the tokens list with the list of words from current line
                    tokens.extend(line.split())


            #convert each word to lower case so same words with different Casing
            #are counted as one
            for i in range (0, len(tokens)):
                tokens[i]=tokens[i].lower()
                

            return tokens
        
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return []
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return []
        

    #Let 'n' be the number of tokens
    #We are looping through each token once
    #Thefore then time complexity is O(n)    
    def computeWordFreq(self, tokenList):

        """
        input : List of String with tokens 

        output : Map of tokens to frequency
        """

        freqMap = {}
        for token in tokenList:
            if token in freqMap:
                #matching word has been found
                freqMap[token] += 1
            else:
                #first occurance of a word
                freqMap[token] = 1
        return freqMap
    


    #Let 'n' be the number of tokens
    #We are looping through each token once
    #Thefore then time complexity is O(n) 
    def printMap(self, freqMap):

        """
        input :  Map of tokens to frequency 

        output : N/A
        """
        
        sorted_counts = sorted(freqMap.items(), key=lambda item: (-item[1], item[0]))

        for word, count in sorted_counts:
            print(f"{word}->{count}")

if __name__ == "__main__":

    #Check for correct number of arguments, always one extra
    if len(sys.argv) != 2 :
        print("Format : python PartA.py <file_path>")
        sys.exit(1)

    #store the argument 
    arg1 = sys.argv[1]


    mapper = FreqMapper()

    # Call the tokenize function
    map.printMap(map.computeWordFreq(map.tokenize(arg1)))