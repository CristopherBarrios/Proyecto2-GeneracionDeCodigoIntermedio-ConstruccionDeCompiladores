##################################
# Cristopher Barrios
# COMPILADORES 
##################################
# gui.py
##################################

from flask import Flask, render_template, request, session
from antlr4 import *
import antlr4
from YAPLLexer import YAPLLexer
from YAPLListener import YAPLListener
from YAPLParser import YAPLParser
from antlr4.tree.Trees import Trees
from YAPLVisitor import YAPLVisitor
import visitor as Visitor
import sistema_de_tipos as tables
import sys
import intermediate as inter

app  = Flask(__name__)
app.secret_key = "compis:D"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#session.get no truena

# inicio
print("start everything")


#program = open('z_int_code_tests/all.decaf', 'r+')
#program = open('z_semantic_tests/param.decaf', 'r+')
# text = program.read()
# program.close()
# text = antlr4.InputStream(text)
# lexer =YAPLLexer(text)
# stream = CommonTokenStream(lexer)
# parser =YAPLParser(stream)
# tree = parser.program()
# printer =YAPLListener()
# walker = ParseTreeWalker()
# walker.walk(printer, tree)
# #print(Trees.toStringTree(tree, None, parser))
# visitonator = Visitor.MyYAPLVisitor()
# visitonator.visit(tree)



@app.route('/')
def home():
    errors = []
    return render_template("home.html")

@app.route('/', methods = ["POST"])
def get_code():
    errors = []
    code = ""
    code = request.form["codigo"]
    session.code = code
    print("errores", errors)
    if code!= " ":
        text = antlr4.InputStream(code)
        lexer = YAPLLexer(text)
        stream = CommonTokenStream(lexer)
        parser = YAPLParser(stream)
        tree = parser.program()
        printer =YAPLListener()
        walker = ParseTreeWalker()
        walker.walk(printer, tree)
        visitonator = Visitor.MyYAPLVisitor()
        visitonator.visit(tree)
        errors = visitonator.ERRORS
        if len(errors) > 0:
            intercode = ""
        else:
            intermedio = inter.Inter(visitonator.total_scopes,visitonator.clases,visitonator.metodos,visitonator.ownmethod,visitonator.property,visitonator.formal,visitonator.assignment,visitonator.methodcall,visitonator.ifCount,visitonator.equal,visitonator.lessequal,visitonator.lessthan,visitonator.minus,visitonator.add,visitonator.division,visitonator.multiply,visitonator.whileCount,visitonator.declaration,visitonator.letin,visitonator.void,visitonator.negative,visitonator.boolnot,visitonator.case,visitonator.new,visitonator.string,visitonator.valor,visitonator.block,visitonator.id,visitonator.parentheses,visitonator.fals,visitonator.integer,visitonator.truet,visitonator.instr,visitonator.outstring,visitonator.outint)
            intermedio.visit(tree)
            intercode = intermedio.line.split("\n")
    else:
        errors = []
    return render_template("home.html", errors = errors, code = code, intercode=intercode)




if __name__ == "__main__":
    app.run(host='localhost', port = 5000, debug = True)