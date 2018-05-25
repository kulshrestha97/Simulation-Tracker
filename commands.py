# SIMULATION TRACKER
__author__="Rajat Kulshreshtha"

import subprocess # Package for running the commands.
import glob # Package for extracting the file names using pattern matching
import os
import re
import datetime
import time
import MySQLdb
from reportparser import textreport, htmlreport
from SQLdatabase import database
import sys
# TODO
# Script Transition is completed.
# Report Parsing is working fine.
# Database is made, connections are fine, make tables and the discussion on logic.
 
########################################################################################

# These are the commands that are needed initially, to run the vsim.
# vlib : defines the workflow (vscode)
# vmap : maps an existing library to a variable.
# vlog/vcom/ : on making the run commands.
# vsim -top : the design hierarchy that is on top.
# run step : compiling the command
# 
class commands:
    """
    Command class will have the behaviour of executing different commands that are in QuestaSim.
    """
    def __init__(self,dir):
        self.direc = dir
        
    
    def vlib(self): # Very less chance of staying till final code.
        """
        vlib can create a folder in the system file hierarchy for execution of commands.
        """
        d = self.direc
        subprocess.check_output("vlib "+d, shell = True)
       
    def vmap(self,name): # Very less chance of staying till final code.
        """
        vmap can assign a name to the library of QuestaSim
        """
        d = self.direc
        subprocess.check_output("vmap %s %s" %(name, d), shell = True)
    
    def vlog(self):
        """
        vlog compiles the verilog file and contains the way to return the top level modules. 
        
        """
        l = os.listdir(os.getcwd()+'/'+self.direc)
        query = 'vlog'
        for i in l:
            if(i.endswith('.v')):
                add = self.direc+'/'+i
                query=query+' '+add
        query = query+" +cover"
        
        # Popen opens a child program in new process
        a = subprocess.Popen(query, stdout = subprocess.PIPE)
        output = a.stdout.read()
        outen = output.decode("utf-8").encode("unicode-escape") 
        outen = str(outen)
        outen = outen.split(' ')
        module = outen[-1]
        module = module[17:]
        module = module[0:len(module)-7]
        return [query,module]
      
    def domaker(self):
        """
        domaker makes the DO file. Necessary while using the vsim command.
        \n If the do file exists, it will no longer asks you to create a do file, it uses it. 
        """
        savepath = "C:/Users/RAJAT KULSHRESHTHA/"+self.direc
        dofiles = os.listdir(savepath)
        flag = True
        dofile = input('Name the do file\n')
        inp = str()
        
        for i in dofiles:
            if(i == dofile+'.do'):
                print("Do File exists, using it.")
                flag = False
                fi = open(savepath+"/"+dofile+'.do','r')
                filist = fi.readlines()

                for j in filist:

                    if "vlog" in j:
                        tcases = j.split('+define+')[1].split('+')
                        tcases[-1] = str(tcases[-1].rstrip("\n"))
                        print("Test Cases in the do maker function: ",tcases)

                return i,tcases
            else:
                pass

        complete_path = os.path.join(savepath,dofile+'.do')
        file1 = open(complete_path,'w')
        
        while(flag == True):
            comm = input()
            if(comm=="bye"):
                print('DO file made successfully')
                break

            if(comm=="vsim"):
                comm=comm+' -coverage -c '+self.vlog()[1]
                
            if(comm.startswith("vlog")):
                inp = input('Define Test Cases using +define+\n')
                comm = self.vlog()[0]+' '+inp

            file1.write(comm)
            file1.write('\n')
            testcases = (inp.split('+')[2:])

        dofile+='.do'
        return dofile, testcases
    
    def writer(self,testcases):
        """
        Writer writes the transcript generated after each iteration.
        """
        now = datetime.datetime.now()
        ts = now.strftime('%Y-%m-%d_%H-%M')
        
        timestamp=str(ts)+self.vlog()[1]
        
        f = open('transcript', 'r')
        f1 = open(timestamp+'.txt', 'w')
        for i in f:
            
            f1.write(i)
        
        f.close()
        f1.close()
        f1 = open(timestamp+'.txt', 'r')
        a = f1.readlines()
        error = 0
        pas = 0
        
        reasons = []
        passorfail = []
        errorlist = []
        for i in a:
            if 'Error:' in i:
                error+=1
                passorfail.append('Fail')
                if 'Reason:' in i:
                    i = i.split('Reason: ')
                    i[-1] = str(i[-1].rstrip("\n"))
                    reasons.append(i[-1])
                    i[0] = str(i[0].lstrip('# Error: '))
                    errorlist.append(i[0])
                
                
            if 'PASS:' in i:
                pas+=1
                passorfail.append('Pass')
                reasons.append('--')
                errorlist.append('--')
            
        print("FAIL TEST CASES::",error)
        print("PASSED TEST CASES:: ", pas)
        print("Test Cases are", testcases)
        print("Pass Fail Status is", passorfail)
        print("Reasons ", reasons)
        print("Error List ",errorlist)
        table_values = list(zip(testcases, passorfail, errorlist, reasons))
        # print("The values for the list is: ", table_values)
        return error, pas, table_values
        
    def vsim(self):
        """
        vsim makes the simulation possible for the compiled vlog output.\n
        Generates the transcript file.
        """
        # m = self.vlog()
        do_file,testcases = self.domaker()
        print('Making Transcript file . . .')
        time.sleep(3)
        subprocess.call("vsim -do "+self.direc+"/"+do_file+" -c", shell=True)
        
        err, ps, table_values = self.writer(testcases)
        return err, ps, testcases, table_values
# Driver Program to run the project.
if __name__ == "__main__":
    
    print('\nWELCOME TO THE SIMULATION TRACKER \nBy Rajat Kulshreshtha\nIn vsim command Do not add top level module name. \nWe will extract it for you :)\n\n')
    usecase = input("Choose from the following by entering the respective number\n1. Run Simulation\n2. View the progress\n")
    if(usecase=='1'):

        cmd = commands(input('Enter your directory name\n'))
        error, pas, testcases, tabletoadd = cmd.vsim()
        modulename = cmd.vlog()[1]
        now = datetime.datetime.now()
        tm_table = now.strftime('%Y_%m_%d__%H_%M')
        tm_table = str(tm_table)
        table_name = modulename+tm_table
        report_txt = textreport()
        textreportname = input('Enter the name of text report\n')
        textvalues = (report_txt.textreportvalues(textreportname))
        report_html = htmlreport()
        htmlreportdir = input('Enter the name of folder where html report is stored\n')
        content = report_html.dataread(htmlreportdir)
        report_html.feed(content)
        htmlvalues = report_html.variables()
        base = database(server="localhost",user="root",password="",db ="reports")
        sql = "INSERT INTO TOTALREPORT "+"(TOGGLE, LINE, BRANCHES, FSM, TOTALPERCENTAGE, DESIGN_NAME, ERROR, FATAL, WARNING, PASS, TIME) "+"VALUES ("+"'"+htmlvalues['toggle']+"','"+textvalues['statement']+"','"+textvalues['branches']+"','"+textvalues['fsm']+"','"+htmlvalues['coverage']+"','"+modulename+"','"+str(error)+"','"+htmlvalues['fatal']+"','"+htmlvalues['warning']+"','"+str(pas)+"','"+tm_table+"')"
        table_command = "CREATE TABLE "+table_name+" LIKE STRUCTURE"
        table_insert = "INSERT INTO "+table_name+" (TESTCASE, RESULT, ERROR, REASON) VALUES (%s, %s, %s, %s)"
        base.masterinsert(sql)
        base.branchcreate(table_command)
        base.branchinsert(table_insert,tabletoadd)
        checkcase = input('Want to view the progress of code? (Y/N)')
        if(checkcase=='Y' or checkcase=='y'):
            subprocess.call("python app.py", shell=True)
            
        elif(checkcase=='N' or checkcase=='n'):
            sys.exit(0)            

    elif(usecase=='2'):
        subprocess.call("python app.py", shell=True)