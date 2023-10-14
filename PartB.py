import sys
import PartA

class Relator:

    #tokenize(file_name) has runtime O(n) -> called twice -> O(n1) + O(n2)
    #converting these lists to sets -> O(n1) + O(n2)
    #the intersection operation take O(min(n1, n2))
    #In total O(2n1) + O(2n2) + O(min(n1,n2))
    #This can be simplified to O(n1 + n2) time complexity


    def findCommonWords(self, fileName1, fileName2):

        mapper = PartA.FreqMapper()

        tokens1=mapper.tokenize(fileName1)
        tokens2= mapper.tokenize(fileName2)

        A = set(tokens1)
        B = set(tokens2)

        print(len(A.intersection(B)))

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
    