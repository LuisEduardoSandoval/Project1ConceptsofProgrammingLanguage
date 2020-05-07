import sys
def Scanner(fname):
    file=open(fname,"r")
#newlines were not getting read correctly so i replaced them with random characters
    read=file.read().replace("\n","#$09")
#also concatenated a fake newline onto end so it always ended properly
#the program function will be called everytime a token has been found therefore a tree will be generated
#for every token
    read+="#$09"
    i = 0
    tokens = "("
    while (i<len(read)):
        def Program():
            
            print("<Program>")
            stmt_list()
            print("</Program>")
            sys.exit("compiled")

            
        def stmt_list():
            print("\t<Stmt_List>")
            stmt()            

    
            #stmt_list()
            print("\t</Stmt_List>")

        def stmt():
            n = 0
            stmt_l = False
            print("\t\t<stmt>")
            if read[i].isalpha:
                if read[i:i+4] != "read":
                    if read[i:i+5] != "write":
                        if read[i].isdigit() == False:
                            expr(i)
                            #print("Why man")
            
            if read[i:i+4] == "read":
                read_()
                n=0
                while read[i+n+4] == " ":
                    n+=1
                #print(n)
                if read[i+n+4].isalpha():
                    stmt_l = True
                if read[i+n+4].isdigit():
                    print("error read value")
                    
                    


            if read[i:i+5] == "write":
                write_()
                n=0
                while read[i+n+5] == " ":
                    n+=1
                if read[i+n+5].isalpha():
                    stmt_1 = True
                    expr(i+n+5)
                if read[i+n+5].isdigit():
                    stmt_1 = True
                    expr(i+n+5)
                

            
            if read[i+n+4].isalpha(): # checks a previous statement list to see if a new statment is an id
                id_(i+n+4)

                

            
            if read[i].isalpha() == False:
                expr(i)
                
            print("\t\t</stmt>")
            if stmt_l == True:
                print("\t\t<stmt_list>")
                print("\t\t</stmt_list>")
            #stmt_list()



        def expr(i):
            print("\t\t\t<expr>")
            term(i)
            if read[i] == "+":
                
                term_tail(i)
                
            if read[i] == "-":
                #print("<expr>")
                term_tail(i)
                #print("</expr>")
            print("\t\t\t</expr>")
            

        def term(i):
            print("\t\t\t\t<term>")
            factor(i)
            print("\t\t\t\t</term>")
        def term_tail(i):
            n = 0
            j=1
            if read[i] == "+":
                print("\t\t\t\t<term_tail>")
                add_op(i)
                while read[i+j] == " ":
                    j+=1
                
                if read[i+j].isdigit():
                    #print("calling term")
                   
                    term(i+j)
                    
                print("\t\t\t\t</term_tail>")


                    
            if read[i] == "-":
                print("\t\t\t\t<term_tail>")
                add_op(i)
                while read[i+j] == " ":
                    j+=1
                if read[i+j].isdigit():
                    term(i+j)
                print("\t\t\t\t</term_tail>")
                
        def factor(i):
            n = 0
            j = 0
            k = 0
            l = 0
            #print(read[i])
            if read[i] == "(":
                print("lparen")
                while read[i+j] == " ":
                    j+=1
                if read[i+l].isdigit():
                    l+=1
                if read[i+l] == ")":
                    
                    expr(i+j)
                    print("rparen")
            if read[i].isdigit():
                print("\t\t\t\t\t<factor>")
                while read[i+j].isdigit():
                    j+=1
                print("\t\t\t\t\t<number>")
                print("\t\t\t\t\t\t"+read[i:i+j])
                print("\t\t\t\t\t</number>")
                print("\t\t\t\t\t</factor>")
                if read[i+j] == "+":
                    term_tail(i+j) #calls term tail for operator
                if read[i+j] == "-":
                    term_tail(i+j)
                

            elif read[i].isalpha():
                print("\t\t\t\t\t<factor>")
                print("\t\t\t\t\t<id>")
                while read[i+k].isalpha():
                    k+=1
                print("\t\t\t\t\t\t"+read[i:i+k])
                print("\t\t\t\t\t<id>")
                print("\t\t\t\t\t</factor>")

        def id_(i):
            n = i
            j = 0
            while read[n].isalpha():
                n+=1
                j+=1
            
            
            
            print("\t\t\t<id>")
            #while read[n].isalpha:
                #n+=1
            print("\t\t\t\t\t"+read[i:i+j])
            print("\t\t\t</id>")

        def read_():
            print("\t\t\t<read>")
            print("\t\t\t\tread")
            print("\t\t\t</read>")
        def write_():
            print("\t\t\t<write>")
            print("\t\t\t\twrite")
            print("\t\t\t</write>")
        def mult_op(i):
            if read[i+n] == "*":
                print("<times_operation>")
                print("</times_operation>")
            if read[i+n] == "/":
                print("<Div_operation>")
                print("</Div_operation>")
        def add_op(i):
            n=0
            if read[i+n] == "+":
                print("\t\t\t\t\tadd operation")
            if read[i+n] == "-":
                print("\t\t\t\t\t<minus Operation>")
            
            
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
            Program()
            i+=1
            continue
#for minus
        if read[i] == "-":
            tokens+="minus, "
            Program()
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
            Program()
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
        tokens+=")."
        print(tokens)

#function call change txt file to txt file you want      
Scanner("sample.txt")
