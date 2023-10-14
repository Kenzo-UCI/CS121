import sys
import PartA

class Relator:

    #tokenize(file_name) has runtime O(n) -> called twice -> O(n1) + O(n2)
    #computeWordFreq(tokens) has a runtime of O(n)-> called twice -> O(n1) + O(n2)
    #We then compare every token from file1 with every token in file2 
    #nested for loop -> O(n1 * n2)
    #This results in O(n1 * n2 + O(n1) + 2(On2))
    #Simplified Time Complexity: O(n1 * n2)


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

#n1-> number of tokens in file 1
#n2-> number of tokens in file 2
#main method has a time complexity of O(n1 * n2)
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
    