
def Scanner(fname):


    file=open(fname,"r")
#newlines were not getting read correctly so i replaced them with random characters
    read=file.read().replace("\n","#$09")
#also concatenated a fake newline onto end so it always ended properly
    read+="#$09"
    n = 0
    j=0
    k=0
    i = 0
    tokens = "("
    while (i<len(read)):
        def Program(): #defining <program>
            print("<Program>") 
            if read[i] == "$": #if $ is found end 
                print("\t$")
            if read[i:i+4] == "read": #if read is found 
                n = i+4 # n takes i value for end of read 
                while read[n] == " ":# while n is whitespace
                    n+=1 #add 1
                if read[n].isalpha:
                    factor #call factor for n
                
                stmt_list()
            if read[i:i+5] == "write":
                n = i+5
                while read[n] == " ":
                    n+=1
                if read[n].isalpha:
                    factor
                stmt_list()
            else:
                print("none")
                
                
            print("</Program>")

        def stmt_list():
            print("\t<stmt_list>")
            stmt()
            print("\t</stmt_list>")
        def stmt():
            print("\t\t<stmt>")
            if read[i:i+4] == "read":
                print("\t\t\t<read>")
                print("\t\t\t\tread")
                print("\t\t\t</read>")
                factor()
                
            if read[i:i+5] == "write":
                print("\t\t\t<write>")
                print("\t\t\t\twrite")
                print("\t\t\t</write>")
                factor()

                
                
            print("\t\t</stmt>")
        def factor():
            
            if read[i].isalpha():
                n=i #initialize variables
                j=0
                k=n
                if read[i:i+4] == "read": #if read is found
                    n+=4 # n assinged to i+4 so i is not modified
                    if read[n] ==" ": 
                        n+=1
                        k=n
                        while read[k].isalpha():
                            
                            j+=1
                            k+=1
                if read[i:i+5] == "write":
                    n+=5
                    if read[n] == " ":
                        n+=1
                        k=n
                        while read[k].isalpha():
                            j+=1
                            k+=1

                        


                    
              
                        
            print("\t\t\t<id>")
            print ("\t\t\t\t"+read[n:n+j])
            print("\t\t\t</id>")
            
                
                

#check for space
        
        if (read[i] == " "):
            i+=1
            continue
#check for tab
        if read[i:i+2] == "\t":
            i+=2
            continue
#check for newline, \n was not being read so i replaced it with these random characters
        if read[i:i+4] == "#$09":
            i+=4
            continue
#check for $
        if (read[i] == "$"):
            Program()
            i+=1
            continue

#check for \
        if read[i] == "/":
            i+=1
#for comment of //
            if read[i] == "/":
                while(read[i:i+4] != "#$09"):
                    i+=1
                i+=4
                continue
#for comment of /*
            if read[i] == "*":
                i+=1
                while (i<len(read)):
                    if read[i] == "*" and read[i+1] == "/":
                        i+=2
                        break
                    i+=1
                if i<len(read):
                    continue
                else:
                    print("error.")
                    break
#for division symbol
            else:
                tokens+="div, "
                continue
#for left parenthesis

        if read[i] == "(":
            tokens+="lparen, "
            i+=1
            continue
#for right parenthesis
        if read[i] == ")":
            tokens+="rparen, "
            i+=1
            continue
#for plus
        if read[i] == "+":
            tokens+="plus, "
            i+=1
            continue
#for minus
        if read[i] == "-":
            tokens+="minus, "
            i+=1
            continue
#for times
        if read[i] == "*":
            tokens+="times, "
            i+=1
            continue
#for assign (:=)
        if read[i] == ":":
            i+=1
            if read[i] == "=":
                tokens+="assign, "
                i+=1
                continue
            else:
                print("error.")
                break
#for .number
        if read[i] == ".":
            i+=1
            if read[i].isdigit():
                while read[i].isdigit():
                    i+=1
                tokens+="number, "
                continue
            else:
                print("error.")
                break
#for number.number and number
        if read[i].isdigit():
            while(i<len(read) and read[i].isdigit()):
                i+=1
            if i<len(read) and read[i]==".":
                i+=1
                if read[i].isdigit():
                    print(tokens)
                    while read[i].isdigit():
                        i+=1
                    tokens+="number, "
                    continue
                else:
                    print("error.")
                    break
            else:
                tokens+="number, "
                continue
#for ids, checks for if id is read or write before checking for id
        if (read[i].isalpha()):
            if read[i:i+4] == "read":
                Program()
                tokens+="read, "
                
                i+=4
                continue
            if read[i:i+5] == "write":
                Program()
                tokens+="write, "
                i+=5
                continue
            else:
                while read[i].isalpha():
                    i+=1
                tokens+="id, "
                continue
        else:
            print("error.")
            break
#checks to make sure it went thru whole file before printing tokens
    if(i==len(read)):
        tokens=tokens[0:len(tokens)-2]
        #tokens+=")."
        #print(tokens)








#function call change txt file to txt file you want      
Scanner("sample.txt")
