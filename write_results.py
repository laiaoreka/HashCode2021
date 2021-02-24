### write & save file ###
##HOW TO USE:
#1.- from write_results import newFile
#2.- init newFile ->> nf = newFile()
#       optional name: nf = newFile('testing.txt')
#       automatically new file is created and closed
#3.- insert line ->> nf.wrtie_line('line string here')
#4.- get file name ->> nf.namefile

import traceback, datetime

class newFile:
    def write_line(self, line_string ):
        try:
            self.open_file()
            self.nf.write('%s\n'%line_string)
            print('line inserted: %s'%line_string)
            self.close_file()
        except:
            print("WRITE FAILED!!!")
            print(traceback.format_exc())
            
        return
        
    def close_file(self ):
        try:
            self.nf.close()
            print('file closed')
        except:
            print("CLOSE FAILED!!!")
            print(traceback.format_exc())
        return
        
    def open_file(self):
        
        try:
            self.nf = open(self.namefile, "a" )
            print('file open: %s'%self.namefile)
            ret = True
        except:
            print("OPEN FAILED!!!")
            print(traceback.format_exc())
            ret = False
        
        return ret
    
    def create_new_file(self):
        
        try:
            self.nf = open(self.namefile, "w" )
            print('file created: %s'%self.namefile)
            ret = True
        except:
            print("Created FAILED!!!")
            print(traceback.format_exc())
            ret = False
        
        self.close_file()
        return ret

    def __init__(self, wnf=0):
        
        if wnf==0:
            now = datetime.datetime.now()
            wnf = '%s%sresults.txt'%(now.hour,now.minute)
        
        self.namefile = wnf
        
        self.create_new_file()
        return
