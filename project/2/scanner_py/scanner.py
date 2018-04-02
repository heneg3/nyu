import tok1

# Give the lexer some input
with open('TEST_EXHAUSTIVE', 'r') as inf:
    tok1.lexer.input(inf.read(-1))
# lexer.input(data)

with open('TEST_EXHAUSTIVE_OUTPUT','w') as f:
  f.write("token\t" +  "token\t" + "token\n")
  f.write("number\t" + "name\t"   + "value\n")
# Tokenize

print "token\t" +  "token\t" + "token"

while True:
    tok = tok1.lexer.token()
    if not tok: 
      print "FOUND EOF" 
      break      # No more input
    tok.lexpos = tok1.token_dictionary[tok.type]
    with open('TEST_EXHAUSTIVE_OUTPUT','a') as f:
      f.write(str(tok.lexpos) + '\t\t' + str(tok.type) + '\t\t' + '"'+str(tok.value)+'"' + '\n') 

    print str(tok.lexpos) + '\t' + str(tok.type) + '\t' + '"'+str(tok.value)+'"'