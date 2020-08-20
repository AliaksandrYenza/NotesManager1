import os
import time
from infoFromFile import FileWorker

#main
def directory_transit():
    while True:
        print("\n\n============ Your currently directory ============")
        print("\t {prg}".format(prg = os.path.join(os.path.abspath(os.curdir))))
        
        print("\n====================================================")
        flag, com = command_selector()
        if  flag == False:
            print("was writen 0, so its mean cancel command selector")
            print("What do you want next ? \n 0 - exit programm \n 1 - continue \n --->")
            command = input()
            if command == "0":
                break
            elif command == "1":
                continue
            else:
                print("unknown command so I guess u wanna continue))")
                continue
        elif flag == True:
            print("DONE!")
            print("\n\nReading file {file}".format( file = com))
            '''
            while True:
                time.sleep(2)
                print("*", end="")
            '''
            
            fw = FileWorker()
            dic = fw.file_reader(str(com))
            fw.actions_with_dates(dic, str(com))
            continue




def command_selector():
    '''
    Select what the command from cmd - path u wanna
    Input: cmd command
    Ouput: Flag, full path to file like string / "" ( from file )
    '''

    while True:
        print("\n========= Files and Folders into this path =========")
        print(os.listdir())
        print("\n================= Select command =================")
        print("Go into the folder - cd *folder_name\nGo out (back) - back\nJsut write file name for open (.txt only yet)\ninput 0 for cancel \n-->", end= "")
        com = input().split()
        if com[0].lower() == 'cd':            #cd go ahead
            try:
                os.chdir(os.path.join(os.path.abspath(os.curdir), com[-1]))
                continue
            except OSError:
                print(" ! ! ! \tcd path broken \nOS ERROR")
                continue
        elif com[0].lower() == 'back':        #go back to the path
            os.chdir("..")
            continue
        elif com[0] in os.listdir():        #its file gp into file
            if os.path.isfile("".join(com)): #create full path
                full_path = os.path.join(os.path.abspath(os.curdir)) +"\\"+ com[0]
                #print("full_path = {name}, type = {type}".format(name = full_path, type = type(full_path)))
                return True, full_path      # we have file and gonna continue work with it
                break
            else:
                print("Incorrect type of file")
                continue
        elif com[0] == '0':
            return False, ""            #if input 0 = u wanna come back
            break
        else:
            print("unknown command, try again ")
            continue


if __name__ == "__main__":
    directory_transit()
