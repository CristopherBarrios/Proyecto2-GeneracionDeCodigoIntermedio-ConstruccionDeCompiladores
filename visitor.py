##################################
# Cristopher Barrios
# COMPILADORES 
##################################
# visitor.py
##################################

import sistema_de_tipos as tables
import classes as lista
from classes import Clase, In
from YAPLVisitor import YAPLVisitor
from functions import *

DEFAULT_TYPES = {
    'int': 4,
    'boolean': 4,
    'char': 4,
}

class MyYAPLVisitor(YAPLVisitor):

    def __init__(self):
        YAPLVisitor.__init__(self)
        self.class_ids = -1
        self.method_ids = -1
        self.symbols_ids = 0
        self.offset = 0
        self.instantiable_ids = 0
        self.ERRORS = []
        global_scope = tables.Scope()
        self.scopes = []

        self.clases = []
        self.metodos = []
        self.ownmethod = []
        self.property = []
        self.formal = []
        self.assignment = []
        self.methodcall = []
        self.ifCount = []
        self.equal = []
        self.lessequal = []
        self.lessthan = []
        self.minus = []
        self.add = []
        self.division = []
        self.multiply = []
        self.whileCount = []
        self.declaration = []
        self.letin = []
        self.void = []
        self.negative = []
        self.boolnot = []
        self.case = []
        self.new = []
        self.string = []
        self.valor = []
        self.block = []
        self.id = []
        self.parentheses = []
        self.fals = []
        self.integer = []
        self.truet = []
        self.instr = []
        self.outstring = []
        self.outint = []

        self.total_scopes = {}
        self.printidorClases = {}

        

    def visitProgram(self, ctx):
        self.ERRORS = []
        self.visitChildren(ctx)

        contador = []
        for clas in self.clases:
            contador.append(clas.get_instance("Main"))
        if "Main" not in contador:
            new_error = tables.Error("Main class not defined", ctx.start.line, ctx.start.column)
            self.ERRORS.append(new_error)

        # contador = []
        # for met in self.metodos:
        #         contador.append(met.get_instance("main"))
        # if "main" not in contador:
        #     new_error = tables.Error("main method not defined", ctx.start.line, ctx.start.column)
        #     self.ERRORS.append(new_error)

        if len(self.clases) != 0:
            for x in self.clases:
                self.total_scopes[x.name] = x
            for y in self.metodos:
                self.total_scopes[y.name] = y

        
        if "Main" in contador:
            contador = []
            for meto in self.total_scopes["Main"].params:
                if "id" in dir(meto):
                    contador.append(meto.get_instance("main"))
            if "main" not in contador:
                new_error = tables.Error("main method not defined", ctx.start.line, ctx.start.column)
                self.ERRORS.append(new_error)

        if "main" in contador:
            contador = []
            if "bloc" in dir(self.total_scopes["main"].expr): 
                for corredor in self.total_scopes["main"].expr.bloc:
                    if "expr" in dir(corredor) and "expr1" in dir(corredor) and "expr2" in dir(corredor) and "name" in dir(corredor) and "type" in dir(corredor):
                        contador.append(corredor.name)
                if "main" not in contador:
                    new_error = tables.Error("No se encuentra (new Main).main(); en main", ctx.start.line, ctx.start.column)
                    self.ERRORS.append(new_error)
            else:
                new_error = tables.Error("No se encuentra { } en main", ctx.start.line, ctx.start.column)
                self.ERRORS.append(new_error)

        for scopeClass in self.clases:
            n = buscar_n_elemento(self.total_scopes, scopeClass.name)
            if n > 1:
                new_error = tables.Error("Hay clases repetidas", ctx.start.line, ctx.start.column)
                self.ERRORS.append(new_error)

        for scopeMetodo in self.metodos:
            n = buscar_n_elemento(self.total_scopes, scopeMetodo.name)
            if n > 1:
                new_error = tables.Error("Hay metodos repetidos", ctx.start.line, ctx.start.column)
                self.ERRORS.append(new_error)


        printidor(self.clases,self.metodos,self.ownmethod,self.property,self.formal,self.assignment,self.methodcall,self.ifCount,self.equal,self.lessequal,self.lessthan,self.minus,self.add,self.division,self.multiply,self.whileCount,self.declaration,self.letin,self.void,self.negative,self.boolnot,self.case,self.new,self.string,self.valor,self.block,self.id,self.parentheses,self.fals,self.integer,self.truet,self.instr,self.outstring,self.outint)

        return 0


    def visitClasses(self, ctx):
        class_list = [self.visit(ctx.classDefine())]
        programB = self.visit(ctx.programBlocks())


    def visitEof(self, ctx):
        return self.visitChildren(ctx)
    
    
    def visitClassDefine(self, ctx):
        class_name = ctx.TYPEID(0).getText()
        self.class_ids += 1

        parent = None
        if len(ctx.TYPEID()) > 1:
            parent = ctx.TYPEID(1).getText()

        features = []
        for f in ctx.feature():
            feature = self.visit(f)
            features.append(feature)

        for met in self.clases:
            if class_name == met.name:
                new_error = tables.Error("Ya se ha declarado esta clase " + str(class_name), ctx.start.line, ctx.start.column)
                self.ERRORS.append(new_error)

        clase = lista.Clase(class_name,parent,self.class_ids,features)
        self.clases.append(clase)

        if ctx.INHERITS():
            if class_name == "Main":
                if parent != "IO":
                    new_error = tables.Error("La clase Main no puede heredar de ninguna otra clase ", ctx.start.line, ctx.start.column)
                    self.ERRORS.append(new_error)
            if class_name == parent:
                    new_error = tables.Error("La clase no puede heredar de la misma clase ", ctx.start.line, ctx.start.column)
                    self.ERRORS.append(new_error)

        return clase


    def visitMethod(self, ctx):
        name = ctx.OBJECTID().getText()
        type = None;expr=None
        if ctx.TYPEID():
            type = ctx.TYPEID().getText()
        self.method_ids += 1

        for meto in self.metodos:
            if name == meto.name:
                self.method_ids -= 1
                return 0

        formalParams = []
        for f in ctx.formal():
            formalParam = self.visit(f)
            formalParams.append(formalParam)

        if ctx.expression():
            expr = self.visit(ctx.expression())

        metodo = lista.Method(name,self.method_ids,type,formalParams,expr)
        self.metodos.append(metodo)

        if name == "main":
            if ctx.formal():
                new_error = tables.Error("El metodo main no puede contener parametros formales ", ctx.start.line, ctx.start.column)
                self.ERRORS.append(new_error)              

        if name == type or type == None:
            new_error = tables.Error("No se puede encontrar type en metodo ", ctx.start.line, ctx.start.column)
            self.ERRORS.append(new_error)

        return metodo


    def visitProperty(self, ctx):
        name = ctx.OBJECTID().getText()
        type = ctx.TYPEID().getText()

        if ctx.ASSIGNMENT() is None:
            propiedad = lista.Property(name,type,None)
            self.property.append(propiedad)
            return propiedad

        expr = self.visit(ctx.expression())

        propiedad = lista.Property(name,type,expr)
        self.property.append(propiedad)
        return propiedad

        #return self.visitChildren(ctx)


    def visitDecla(self, ctx):
        name = ctx.OBJECTID().getText()
        type = ctx.TYPEID().getText()

        if ctx.ASSIGNMENT() is None:
            declaration = lista.Decla(name,type,None)
            self.declaration.append(declaration)
            return declaration

        expr = self.visit(ctx.expression())

        declaration = lista.Decla(name,type,expr)
        self.declaration.append(declaration)
        return declaration
        #return self.visitChildren(ctx)


    def visitFormal(self, ctx):
        name = ctx.OBJECTID().getText()
        type = ctx.TYPEID().getText()

        formal = lista.Formal(name,type)
        self.formal.append(formal)

        return formal

        #return self.visitChildren(ctx)


    def visitLetIn(self, ctx):
        let = self.visit(ctx.decla(0))
        let1 = None
        if ctx.decla(1) is not None:
            let1 = self.visit(ctx.decla(1))
        expr = self.visit(ctx.expression())

        letin = lista.LetIn(let,let1,expr)
        self.letin.append(letin)

        return letin

        #return self.visitChildren(ctx)


    def visitMinus(self, ctx):
        Le = self.visit(ctx.expression(0))
        Ri = self.visit(ctx.expression(1))

        minus = lista.Minus(Le,Ri)
        self.minus.append(minus)

        return minus
        #return self.visitChildren(ctx)


    def visitString(self, ctx):
        stri = ctx.STRING().getText()
        striLoop = stri
        list_valus = []
        if "\\n" in stri:
            id = "\\n"
            striLoop = idTexto(id,stri,striLoop,self.valor,list_valus)

        if "\\t" in stri:
            id = "\\t"
            striLoop = idTexto(id,stri,striLoop,self.valor,list_valus)


        string = lista.String(striLoop,stri,list_valus)
        self.string.append(string)

        return string


    def visitIsvoid(self, ctx):
        vo = self.visit(ctx.expression())

        void = lista.Isvoid(vo)
        self.void.append(void)

        return void

        #return self.visitChildren(ctx)


    def visitWhile(self, ctx):
        expWhile = self.visit(ctx.expression(0))
        expLoop = self.visit(ctx.expression(1))

        if type(expWhile).__name__ == "Add" or type(expWhile).__name__ == "Division" or type(expWhile).__name__ == "Multiply" or type(expWhile).__name__ == "Minus":
            new_error = tables.Error("While tiene que ser booleano", ctx.start.line, ctx.start.column)
            self.ERRORS.append(new_error)

        whileCount = lista.WhileCount(expWhile,expLoop)
        self.whileCount.append(whileCount)

        return whileCount
        #return self.visitChildren(ctx)


    def visitDivision(self, ctx):
        Le = self.visit(ctx.expression(0))
        Ri = self.visit(ctx.expression(1))

        division = lista.Division(Le,Ri)
        self.division.append(division)

        return division
        #return self.visitChildren(ctx)


    def visitNegative(self, ctx):
        ne = self.visit(ctx.expression())

        negative = lista.Negative(ne)
        self.negative.append(negative)

        return negative
        #return self.visitChildren(ctx)


    def visitBoolNot(self, ctx):
        bn = self.visit(ctx.expression())

        boolnot = lista.BoolNot(bn)
        self.boolnot.append(boolnot)

        return boolnot
        #return self.visitChildren(ctx)


    def visitLessThan(self, ctx):
        Le = self.visit(ctx.expression(0))
        Ri = self.visit(ctx.expression(1))

        lessthan = lista.LessThan(Le,Ri)
        self.lessthan.append(lessthan)

        return lessthan
        #return self.visitChildren(ctx)


    def visitBlock(self, ctx):
        expr = []
        for e in ctx.expression():
            expre = self.visit(e)
            expr.append(expre)

        block = lista.Block(expr)
        self.block.append(block)

        return block
        #return self.visitChildren(ctx)


    def visitId(self, ctx):
        name = ctx.OBJECTID().getText()

        id = lista.Id(name)
        self.id.append(id)

        return id
        #return self.visitChildren(ctx)


    def visitMultiply(self, ctx):
        Le = self.visit(ctx.expression(0))
        Ri = self.visit(ctx.expression(1))

        multiply = lista.Multiply(Le,Ri)
        self.multiply.append(multiply)

        return multiply

        #return self.visitChildren(ctx)


    def visitIf(self, ctx):
        exprIf = self.visit(ctx.expression(0))
        exprThen = self.visit(ctx.expression(1))
        exprElse = self.visit(ctx.expression(2))

        if type(exprIf).__name__ == "Add" or type(exprIf).__name__ == "Division" or type(exprIf).__name__ == "Multiply" or type(exprIf).__name__ == "Minus":
            new_error = tables.Error("If tiene que ser booleano", ctx.start.line, ctx.start.column)
            self.ERRORS.append(new_error)
            
        ifcount = lista.IfCount(exprIf,exprThen,exprElse)
        self.ifCount.append(ifcount)

        return ifcount
        #return self.visitChildren(ctx)


    def visitCase(self, ctx):
        exprCase = self.visit(ctx.expression(0))

        Of = []
        for f in ctx.OBJECTID():
            name = f.getText()
            Of.append(name)
            
        type = []
        exprCaseArrow = []


        for t in ctx.TYPEID():
            name = t.getText()
            type.append(name)

        for i in range(1, len(ctx.expression())):
            exprCaseArrow.append(self.visit(ctx.expression(i)))
        
        case = lista.Case(exprCase,Of,type,exprCaseArrow)
        self.case.append(case)

        return case
        #return self.visitChildren(ctx)


    def visitOwnMethodCall(self, ctx):
        instance = "self"
        method = ctx.OBJECTID().getText()

        arguments = []
        for f in ctx.expression():
            argumen = self.visit(f)
            arguments.append(argumen)
        
        if method == "in_string" or method == "in_int":
            instr = lista.In(method)
            self.instr.append(instr)
            return instr
        
        if method == "out_string":
            outstring = lista.OutString(arguments)
            self.outstring.append(outstring)
            return outstring

        if method == "out_int":
            outint = lista.OutInt(arguments)
            self.outint.append(outint)
            return outint

        OwnMeth = lista.OwnMethod(method,arguments)
        self.ownmethod.append(OwnMeth)
        return OwnMeth


    def visitAdd(self, ctx):
        Le = self.visit(ctx.expression(0))
        Ri = self.visit(ctx.expression(1))

        # print(type(Le).__name__)
        # print(type(Ri).__name__)

        # if type(Le).__name__ == "Id":
        #     print("awebo perro")
        # if type(Ri).__name__ == "Id":
        #     print("awebo perro")

        # if type(Le).__name__ == "Int":
        #     print("awebo perro")
        # if type(Ri).__name__ == "Int":
        #     print("awebo perro")

        add = lista.Add(Le,Ri)
        self.add.append(add)

        return add
        #return self.visitChildren(ctx)


    def visitNew(self, ctx):
        type = ctx.TYPEID().getText()

        new = lista.New(type)
        self.new.append(new)

        return new

        #return self.visitChildren(ctx)


    def visitParentheses(self, ctx):
        expr = self.visit(ctx.expression())

        parentheses = lista.Parentheses(expr)
        self.parentheses.append(parentheses)

        return parentheses
        #return self.visitChildren(ctx)


    def visitAssignment(self, ctx):
        name = ctx.OBJECTID().getText()
        expr = self.visit(ctx.expression())

        assignement = lista.Assignment(name,expr)
        self.assignment.append(assignement)

        return assignement
        #return self.visitChildren(ctx)


    def visitFalse(self, ctx):
        false = ctx.FALSE().getText()

        fals = lista.FalseCount(false)
        self.fals.append(fals)

        return fals
        #return self.visitChildren(ctx)


    def visitInt(self, ctx):
        int = ctx.INT().getText()

        integer = lista.Int(int)
        self.integer.append(integer)

        return integer
        #return self.visitChildren(ctx)


    def visitEqual(self, ctx):
        Le = self.visit(ctx.expression(0))
        Ri = self.visit(ctx.expression(1))

        equal = lista.Equal(Le,Ri)
        self.equal.append(equal)

        return equal
        #return self.visitChildren(ctx)


    def visitTrue(self, ctx):
        true = ctx.TRUE().getText()

        truet = lista.TrueCount(true)
        self.truet.append(truet)

        return truet
        #return self.visitChildren(ctx)


    def visitLessEqual(self, ctx):
        Le = self.visit(ctx.expression(0))
        Ri = self.visit(ctx.expression(1))

        lessequal = lista.LessEqual(Le,Ri)
        self.lessequal.append(lessequal)

        return lessequal
        #return self.visitChildren(ctx)


    def visitMethodCall(self, ctx):
        name = ctx.OBJECTID().getText()
        type = None; expr1 = None; expr2 = None
        
        if ctx.TYPEID() is not None:
            type = ctx.TYPEID().getText()

        expr = self.visit(ctx.expression(0))

        if ctx.expression(1) is not None:
            expr1 = self.visit(ctx.expression(1))

        if ctx.expression(2) is not None:
            expr2 = self.visit(ctx.expression(2))

        if name == "in_string" or name == "in_int":
            instr = lista.In(name)
            self.instr.append(instr)
            return instr
        
        if name == "out_string":
            outstring = lista.OutString(expr,expr1,expr2)
            self.outstring.append(outstring)
            return outstring

        if name == "out_int":
            outint = lista.OutInt(expr,expr1,expr2)
            self.outint.append(outint)
            return outint
        methodcall = lista.MethodCall(name,type,expr,expr1,expr2)
        self.methodcall.append(methodcall)

        return methodcall
        #return self.visitChildren(ctx)