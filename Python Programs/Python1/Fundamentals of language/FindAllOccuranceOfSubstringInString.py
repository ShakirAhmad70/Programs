def findAllOccurance(s, subs):
    i = s.find(subs)
    if i == -1:
        print("Substrin Not Found...!>")
    else:
        print("Matching Indices are: [ ",end='')
        printstr = ''
        while(i <= len(s)):
            i = s.find(subs,i,len(s))
            if i == -1:
                break
            printstr = printstr + str(i) + ", "
            i = i + len(subs)
        print(printstr[:len(printstr)-2],end='')
        print(' ]')
        

findAllOccurance("abcabcascabcabcaddabcabc","abc")