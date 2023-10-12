import sys
import PartA

class Relator:

    #In the file1 
    #Let 'l1' be the number of lines 
    #Let 'c1' be the number of character on a line
    #Let 'n1' be the number of tokens 

    #In the file2
    #Let 'l2' be the number of lines 
    #Let 'c2' be the number of character on a line
    #Let 'n2' be the number of tokens 

    #Calling tokenize of file1 takes O(l1 c1 + n1) time.
    #Calling tokenize of file1 takes O(l2 c2 + n2) time.

    #Calling computeWordFreq on file1 take O(n1) time.
    #Calling computeWordFreq on file2 take O(n2) time. 

    #Then we convert each word to lower case whch is O(n) time.
    #This results in a final time complexity of O(lc+n).

    #For every token in file while we loop through every token in file 2
    #This gives us O(n1 n2) time complexity.

    #Therefore we get total time complexity of O(l1 c1 + n1) + O(l2 c2 + n2) + O(n1 n2)
    #If we take l, c, n to be the upper limits
    # then we get time complexity of O(l + c + n) + O(n^2)
    #The number of tokens will probably dominate giving us O(n^2) time complexity

    def findCommonWords(self, fileName1, fileName2):

        mapper = PartA.FreqMapper()

        tokens1=mapper.tokenize(fileName1)
        tokens2= mapper.tokenize(fileName2)

        map1=mapper.computeWordFreq(tokens1)
        map2=mapper.computeWordFreq(tokens2)

        counter=0;

        for token1 in map1.keys():
            for token2 in map2.keys():
                if token1 == token2:
                    counter+=1

        print(counter)



if __name__ == "__main__":

    #Check for correct number of arguments, always one extra
    if len(sys.argv) != 3 :
        print("Format : python PartB.py <file_path> <file_path>")
        sys.exit(1)

    #store the argument 
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]

    rel = Relator()
    rel.findCommonWords(arg1, arg2)
    