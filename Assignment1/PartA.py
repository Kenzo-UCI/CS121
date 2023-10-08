import sys


def tokenize(file_path):
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

        return tokens
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []
        
if __name__ == "__main__":

    #Check for correct number of arguments, always one extra
    if len(sys.argv) != 2 :
        print("Format : python PartA.py <file_path>")
        sys.exit(1)

    #store the argument 
    arg1 = sys.argv[1]

    # Call the tokenize function
    print(tokenize(arg1))