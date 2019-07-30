import os

class text_parser(object):

    def __init__(self,textFile,func,verbose = True):
        self.textFile = textFile
        self.verbose = verbose
        
    


    def parse_file(self,func):

        fh = open(self.textFile)
        
        while True:

            line = fh.readline()
            words = line.split()
            func(words)

            if not line:
                break
    
    
class directory_parser(object):

    def __init__(self,directory,verbose = True):
        self.directory = directory
        self.verbose = verbose
       
    


    def parse_directory(self,list_of_functions):
        
        directory = os.fsencode(self.directory)

        for file in sorted(os.listdir(directory)):
            
            filename = os.fsdecode(file)

            fh = open(  directory +file)

            if os.fsdecode(filename).endswith(".txt"):

                if self.verbose: 
                    print ("processing file : " + filename)
                    print()
            
                while True:
                    line = None
                    try:
                        line = fh.readline()

                        words = line.split()
                        for func in list_of_functions:

                            func(words)
                    except:
                        
                        if self.verbose:
                            print("error parsing line")
                            continue
                        else:
                            continue
                    
                    if not line:
                        break




