def let_check_synoyms(lit):
    final_list = []
    list_of_key = [list(i)[0] for i in lit]
    
    

    for i in range(len(lit)):
        present= False
        for j in range(len(final_list)):
             if list_of_key[i] in final_list[j] or lit[i][list_of_key[i]] in final_list[j]:
                if list_of_key[i] in final_list[j]:
                    final_list[j].append(lit[i][list_of_key[i]])
                    present = True 
                else:
                    final_list[j].append(list_of_key[i])
                   
                    present = True
        
        if present == False:
             print(list_of_key[i],lit[i][list_of_key[i]])
             
             final_list.append([list_of_key[i],lit[i][list_of_key[i]]])
             
            
            
    print(final_list,'this is')


let_check_synoyms([{'a':2},{'a':3},{'v':4},{4:'w'}])
           
