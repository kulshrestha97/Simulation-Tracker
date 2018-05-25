# Report Parsing Tool for SIMULATION TRACKER

__author__="Rajat Kulshreshtha"
import os
import re
from html.parser import HTMLParser

class textreport:
    """
    Text Report Class has the functionality to parse the myreport.txt file for the values needed. 
    """
    def __init__(self):
        self.path = os.getcwd()

    
    def search(self):
        """
        Gives the list of files that are present in the current working directory.
        """
        self.files = list(os.listdir(self.path))
        return self.files
    def currpath(self):
        """
        Auxilary Function. Returns the path from __init__.
        """
        return self.path
    
    def textreportvalues(self, report):
        """
        Parses the values from the Generated Text Report.
        """
        filelist = []
        lines = None
        self.search()
        for i in self.files:
            if i == (report+'.txt'):
                filelist.append(self.path+"\\"+i)
        for i in filelist:
            textfile = open(i,'r')
            lines = textfile.readlines()
        replace = []
        replace2 = []
        for line in lines:
            replace.append(re.sub(r'\n',',',line))
        
        for line in replace:
            replace2.append(re.sub(r'[ ]{2,}',',',line))
        
        listoflist = []
        for i in replace2:
            i=i.split(',')
            listoflist.append(i)
        
        listoflist = listoflist[14:]
        
        for i in listoflist:
            if(i[1]=="Stmts"):
                statement = i[5]
            if(i[1]=="Branches"):
                branches = i[5]
            if(i[1]=="FSMs"):
                fsm = i[2]
    
        return {'statement':statement, 'branches':branches, 'fsm':fsm}
    
class htmlreport(HTMLParser):
    """
    htmlreport class has the behaviour of generating values from the coverage summary html file.
    """
    lsdata = list()
    def dataread(self,folder):
        """
        Provides the functionality to read data from html report.
        """
        directory = os.getcwd()+"\\"+folder+"\\covsummary.html"
        with open(directory, 'r') as f:
            data = f.read()
        return data
    
    def handle_data(self, data):
        """
        Gives the parsed data in the form of list.
        """
        self.lsdata.append(data)
        
    def variables(self):
        """
        Gives the numeric values that are present in the list, in the form of a dictionary.
        """

        for i in range(0,len(self.lsdata)):
            if(self.lsdata[i]=="Passed:"):
                passed = self.lsdata[i+1]

            if(self.lsdata[i]=="Error:"):
                error = self.lsdata[i+1]

            if(self.lsdata[i]=="Fatal:"):
                fatal = self.lsdata[i+1]

            if(self.lsdata[i]=="Warning:"):
                warning = self.lsdata[i+1] 

            if(self.lsdata[i]=="Total Coverage:"):
                coverage = self.lsdata[i+2]

            if(self.lsdata[i]=="Toggles"):
                toggles = self.lsdata[i+6]
            
        
        return {'passed':passed, 'error':error, 'fatal':fatal, 'warning':warning, 'coverage':coverage,'toggle':toggles}
            
#if __name__=="__main__":
#    
#    direct = input('Add your report directory\n')
#    rep = textreport(direct)
#    textvalues = rep.textreportvalues()
#    print(textvalues)
#
#    parser = htmlreport()
#    content = parser.dataread(direct)
#    parser.feed(content)
#    # print(parser.lsdata)
#    htmlvalues = parser.variables()
#    print(htmlvalues)

    

    
    
  
    

        