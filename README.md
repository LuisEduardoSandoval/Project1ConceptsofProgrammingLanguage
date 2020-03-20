# Project1ConceptsofProgrammingLanguage
problem :  write a scanner using imperative langauge, 

requirements: scan function, pointer not EOF, scans current pointer input file.
i.e: ID -> letter letter*, token type abc would be ID, otherwise returning error
"longest possible token rule" scanner deals with read and write.

command line invocation: scanner<inputfile name>
i.e.
/* 
foo
	bar */
*
five 5
file: scanner foo.txt
output(read,times, id, number)
DO NOT OUPUT COMMENT:

assign-> :=
plus-> +
minus -> -
times-> *
div->/ 
lparen-> (
rparen-> )
id ->letter ( letter| digit)* except read write 
number -> digit digit* | digit* (. digit | digit . ) digit*

comment -> /* (non-* | * non-/)*  */ 
global variable
word position: position of word 
scanner psuedo code:

function: scanner //missing number, etc..

input: <file.txt>

while there is more to read in <file.txt>
	read a word
	assign word to current_char 

if cur_char ∈ {' '}/ignore whitespace
	getnextword:

if cur_char ∈ {'/'}    //note this does not take into account the dfa will need to be modified
	word position + 1 // cannot call getnextword , as it would call scanner 
	if cur_char ∈ {'*'}
		while( cur_char != */)
			getnextword:// comment line
		if(cur_char == '*/')
			output:comment
		getnextword:
		else
			output: "error"
			exit

		
else 
		output: "division"
		getnextword:
if cur_char ∈ {:=}
	output: "assign"
	getnextword:
if cur_char ∈ {+}
	output: "plus"
	getnextword():
if cur_char ∈ {-}
	output: "minus"
	getnextword():

getnextword() psuedo code
function name: getnextword()
input: none

for current word position
	word position +1
	scanner(<input file.txt>) // call scanner 
	if end of file
		end
	
