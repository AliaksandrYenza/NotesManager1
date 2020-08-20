#from main import command_selector

class FileWorker():

    def __init__(self):
        pass

    #C:\02_MYPROJECTS\PY\VSCode\python01\tel_dict\file.txt
    def file_reader(self, name):
        '''
        Read str from file
        Input: file name - str
        Output: dic{} of info
        '''
        dic = {}
        with open(str(name)) as inf:
            for line in inf:
                key, value = line.split()
                dic[key] = str(value)
        return dic


    def save_dic(self, dic, name):
        with open(name, 'w+') as ouf:
            for key, val in dic.items():
                ouf.write('{}: {}\n'.format(key,val))
        return dic

    
    def back_go(self,dic):
        main.command_selector()


    def key_check(self, dic):
        while True:
            k = input("Input key: ")
            if k not in dic.keys():
                print("no key find try again ")
                continue
            else:
                print("hey key okey")
                break
        return k



    def edit_value_by_key(self,dic):
        while True:
            k = self.key_check(dic)
            v = input("Input value \n*!* if u will start value with plus (+) its mean u wanna add smth *!*\n --->")
            if v[0] == "+":
                dic[k] += v
                break
            else:
                dic[k] = v
                break
        return dic

    
    def add_key(self, dic):
        while True:
            k = input("Input key:")
            if k in dic.keys():
                print("this key DONE already \n write 1 if u wanna edit the key")
                continue
            else:
                dic[k] = input("value for key - {k}".format(k = k))
                break
        return dic


    def clean_value(self, dic):
        while True:
            k = self.key_check(dic)
            if k:
                dic[k] = ""
                print("key {k} clean!".format(k = k))
                break
        return dic

    
    def del_key_value(self, dic):
        while True:
            k = self.key_check(dic)
            if k:
                del dic[k]
                break
        return dic


    def cut_copy_value(self, dic):
        while True:
            print("from key")
            k = self.key_check(dic)
            while k:
                print("to key")
                k_to = self.key_check(dic)
                if k_to:
                    dic[k_to] = dic[k]
                    print("cut paste DONE!")
                    break
                else:
                    print("err _to key")
                    continue
            else:
                print("err _from key")
                continue
            break
        return dic



    def actions_with_dates(self, dic, file_name):
        print("ok, file read, so wat next ? ")
        #fdgdf = input()
        while True:   
            print("from file:\n{d}".format(d = dic))
            print(" 1 - edit value by key\n 2 - add key ( with value which def = '') \n 3 - del value \n 4 - del key and value \n 5 - cut value from key1 to key2 \n 0 back ")
            action = input()
            if action == "1":


                try:
                    dic = self.edit_value_by_key(dic)
                    print("value edited ! ")
                    continue
                    #return new_dic
                    
                except:
                    print("smth wrong from edit value by key")
                    continue


            elif action == "2":
                try:
                    dic = self.add_key(dic)
                    print("key added")
                    continue
                except:
                    print("smth wrong from add key")
                    continue


            elif action == "3":
                try:
                    dic = self.clean_value(dic)
                    print("value cleaned")
                    continue
                except:
                    print("smth wrong from clean value")
                    continue


            elif action == "4":
                try:
                    dic = self.del_key_value(dic)
                    print("value + key deleted")
                    continue

                except:
                    print("smth wrong from del key")
                    continue


            elif action == "5":
                try:
                    dic = self.cut_copy_value(dic)
                    print("value copyed")
                    continue

                except:
                    print("smth wrong from del key")
                    continue

            elif action == "6":
                while True:
                    sub_act = input("1 - save in same file\n2 - save in the other file")
                    if sub_act == "1":
                        try:
                            self.save_dic(dic, file_name)
                            print("Saved in {f} file".format(f = file_name))
                            break
                        except :
                            print("error with saving into {f}".format(f = file_name))
                            continue
                    elif sub_act == '2':
                        file_name = input("file for save: ")
                        try:
                            self.save_dic(dic, file_name)
                            print("Saved in {f} file".format(f = file_name))
                            break
                        except :
                            print("error saving in z {f}".format(f = file_name))
                            continue
                    else:
                        print("try again to choose how to save file")
                        continue
                '''try:
                    save_dic(dic)
                    print("Saved!")
                    continue
                except :
                    print("smth wrong from save f")
                    continue
                        '''

            elif action == "0":
                break


            else:
                print("Uncorrect command plz try again")
                continue





        #save
