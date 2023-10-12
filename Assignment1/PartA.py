import sys

class FreqMapper:

    def tokenize(self, file_path):
        """
        input : String file_path 

        output : List<String> tokens
        """
        try:
            
            tokens=[];
            
            #opening the file for reading 
            with open(file_path, 'r') as file:
                for line in file:

                    #extending the tokens list with the list of words from current line
                    tokens.extend(line.split())
            
            for i in range (0, len(tokens)):
                tokens[i]=tokens[i].lower()
                

            return tokens
        
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return []
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return []
        
    def computeWordFreq(self, tokenList):
        freqMap = {}
        for token in tokenList:
            if token in freqMap:
                freqMap[token] += 1
            else:
                freqMap[token] = 1
        return freqMap

    def printMap(self, freqMap):
        
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