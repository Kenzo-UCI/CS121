import sys

class FreqMapper:

 
    #Let 'n' be the number of bytes in the file 
    #The while loop goes through each character in the file
    #This results in a time complexity O(n).

    def tokenize(self, file_path):
        """
        input : String with the file name  

        output : List of String with tokens
        """
        try:
            
            tokens=[]
            tempWord=""
            #opening the file for reading 
            file = open(file_path, "rb")
            byte = file.read(1)
            while byte:
                #if we have reached the end of line and there is something left in the tempWord buffer append it
                if byte == b'\n':
                    if tempWord != "":
                        tokens.append(tempWord)
                        tempWord=""
                    byte = file.read(1)
                    continue
                try:
                    char = str(byte, 'utf-8')
                except UnicodeDecodeError as e:
                    byte = file.read(1)
                    continue
                if char.isalnum():
                    #convert each word to lower case so same words with different Casing
                    char = char.lower()
                    tempWord+=char;
                elif tempWord != "":
                    tokens.append(tempWord)
                    tempWord=""
                byte = file.read(1)

            file. close()

            if(tempWord != ""):
                tokens.append(tempWord);
            
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
            print(f"|{word}|->{count}")

# The main method calls three functions each of which have O(n) time complexity
# O(3n) = O(n) runtime complexity
if __name__ == "__main__":

    #Check for correct number of arguments, always one extra
    if len(sys.argv) != 2 :
        print("Format : python PartA.py <file_path>")
        sys.exit(1)

    #store the argument 
    arg1 = sys.argv[1]


    mapper = FreqMapper()

    # Call the tokenize function
    mapper.printMap(mapper.computeWordFreq(mapper.tokenize(arg1)))
    