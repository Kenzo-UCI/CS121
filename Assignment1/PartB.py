import sys
import PartA

class Relator:

    def findCommonWords(self, fileName1, fileName2):

        mapper = PartA.FreqMapper()

        tokens1=mapper.tokenize(fileName1)
        tokens2= mapper.tokenize(fileName2)

        map1=mapper.computeWordFreq(tokens1)
        map2=mapper.computeWordFreq(tokens2)

        print("list 1= ", tokens1)
        print("list 2= ", tokens2)

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
    