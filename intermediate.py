##################################
# Cristopher Barrios
# COMPILADORES 
##################################
# intermediate.py
##################################

from operator import methodcaller
from types import MethodType
from YAPLVisitor import YAPLVisitor
from classes import MethodCall
from functions import *

DEFAULT_TYPES = {
    'Int': 4,
    'Bool': 1,
    'String': 1,
}

class Inter(YAPLVisitor):

    def __init__(self, scopes,clases,metodos,ownmethod,property,formal,assignment,methodcall,ifcount,equal,lessequal,lessthan,minus,add,division,multiply,whileCount,declaration,letin,void,negative,boolnot,case,new,string,valor,block,id,parentheses,fals,integer,truet,instr,outstring,outint):
        YAPLVisitor.__init__(self)
        self.tree = None
        self.og_registers = ["t0", "t1","t2", "t3", "t4", "t5", "t6", "t7", "t8","t9","t10","t11", "t12","t13", "t14", "t15", "t16", "t17", "t18", "t19","t20","t21","t22", "t23", "t24", "t25", "t26", "t27", "t28","t29","t30", "t31","t32", "t33", "t34", "t35", "t36", "t37", "t38","t39","t40", "t41","t42", "t43", "t44", "t45", "t46", "t47", "t48","t49","t50", "t51","t52", "t53", "t54", "t55", "t56", "t57", "t58","t59","t60", "t61","t62", "t63", "t64", "t65", "t66", "t67", "t68","t69","t70", "t71","t72", "t73", "t74", "t75", "t76", "t77", "t78","t79","t80", "t81","t82", "t83", "t84", "t85", "t86", "t87", "t88","t89","t90", "t91","t92", "t93", "t94", "t95", "t96", "t97", "t98","t99","t100","t100", "t101","t102", "t103", "t104", "t105", "t106", "t107", "t108","t109","t110","t111", "t112","t113", "t114", "t115", "t116", "t117", "t118", "t119","t120","t121","t122", "t123", "t124", "t125", "t126", "t127", "t128","t129","t130", "t131","t132", "t133", "t134", "t135", "t136", "t137", "t138","t139","t140", "t141","t142", "t143", "t144", "t145", "t146", "t147", "t148","t149","t150", "t151","t152", "t153", "t154", "t155", "t156", "t157", "t158","t159","t160", "t161","t162", "t163", "t164", "t165", "t166", "t167", "t168","t169","t170", "t171","t172", "t173", "t174", "t175", "t176", "t177", "t178","t179","t180", "t181","t182", "t183", "t184", "t185", "t186", "t187", "t188","t189","t190", "t191","t192", "t193", "t194", "t195", "t196", "t197", "t198","t199","t200"]
        #self.og_registers = ["r0", "r1","r2", "r3", "r4", "r5", "r6", "r7", "r8","r9","r10"]
        self.registers = self.og_registers[::-1]
        self.line = ""
        self.label = 0
        self.scope_ids = 0
        self.lets = []
        self.strprint = []

        self.scope_actual = ["global"]
        self.scopes = scopes
        # self.method_actual = ["global"]
        self.method_actual = []
        self.class_actual = []

        self.clases = clases
        self.metodos = metodos
        self.ownmethod = ownmethod
        self.property = property
        self.formal = formal
        self.assignment = assignment
        self.methodcall = methodcall
        self.ifCount = ifcount
        self.equal = equal
        self.lessequal = lessequal
        self.lessthan = lessthan
        self.minus = minus
        self.add = add
        self.division = division
        self.multiply = multiply
        self.whileCount = whileCount
        self.declaration = declaration
        self.letin = letin
        self.void = void
        self.negative = negative
        self.boolnot = boolnot
        self.case = case
        self.new = new
        self.string = string
        self.valor = valor
        self.block = block
        self.id = id
        self.parentheses = parentheses
        self.fals = fals
        self.integer = integer
        self.truet = truet
        self.instr = instr
        self.outstring = outstring
        self.outint = outint

        self.cumulative = 0


    def visitProgram(self, ctx):
        return self.visitChildren(ctx)


    def visitEof(self, ctx):
        return self.visitChildren(ctx)


    def visitProperty(self, ctx):
        return self.visitChildren(ctx)


    def visitBlock(self, ctx):
        return self.visitChildren(ctx)


    def visitParentheses(self, ctx):
        return self.visit(ctx.expression())


    def visitFormal(self, ctx):
        return self.visitChildren(ctx)


    def visitClasses(self, ctx):
        self.visit(ctx.classDefine())
        self.visit(ctx.programBlocks())
        #return self.visitChildren(ctx)


    def visitClassDefine(self, ctx):
        class_name = ctx.TYPEID(0).getText()
        self.class_actual.append(class_name)
        start = class_name +": \n"
        #actual = self.scopes[self.class_actual[-1]]
        #start += "class begin " + str(actual.get_size())  + "\n"
        self.line += start
        self.visitChildren(ctx)
        self.class_actual.pop()
        end = "class end \n"
        self.line += end
        

    def visitMethod(self, ctx):
        name = ctx.OBJECTID().getText()
        #self.scope_ids +=1
        self.method_actual.append(name)
        start = name +": \n"
        actual = self.scopes[self.method_actual[-1]]
        start += "func begin " + str(actual.get_size())  + "\n"
        self.line += start
        self.visitChildren(ctx)
        end = "func end \n"
        self.line += end
        self.method_actual.pop()

        return 0
        #return self.visitChildren(ctx)


    def visitAdd(self, ctx):
        Le = self.visit(ctx.expression(0))
        Ri = self.visit(ctx.expression(1))

        register = self.registers.pop()
        operation = register + " = " + str(Le) + " " + ctx.ADD().getText() + " " + str(Ri)

        if Ri in self.og_registers:
            self.registers.append(Ri)
        if Le in self.og_registers:
            self.registers.append(Le)
            
        self.line += operation + "\n"
        return register
        #return self.visitChildren(ctx)


    def visitMinus(self, ctx):
        Le = self.visit(ctx.expression(0))
        Ri = self.visit(ctx.expression(1))

        register = self.registers.pop()
        operation = register + " = " + str(Le) + " " + ctx.MINUS().getText() + " " + str(Ri)

        if Ri in self.og_registers:
            self.registers.append(Ri)
        if Le in self.og_registers:
            self.registers.append(Le)

        self.line += operation + "\n"
        return register
        #return self.visitChildren(ctx)


    def visitMultiply(self, ctx):
        Le = self.visit(ctx.expression(0))
        Ri = self.visit(ctx.expression(1))

        register = self.registers.pop()
        operation = register + " = " + str(Le) + " " + ctx.MULTIPLY().getText() + " " + str(Ri)

        if Ri in self.og_registers:
            self.registers.append(Ri)
        if Le in self.og_registers:
            self.registers.append(Le)

        self.line += operation + "\n"
        return register
        #return self.visitChildren(ctx)


    def visitDivision(self, ctx):
        Le = self.visit(ctx.expression(0))
        Ri = self.visit(ctx.expression(1))

        register = self.registers.pop()
        operation = register + " = " + str(Le) + " " + ctx.DIVISION().getText() + " " + str(Ri)

        if Ri in self.og_registers:
            self.registers.append(Ri)
        if Le in self.og_registers:
            self.registers.append(Le)

        self.line += operation + "\n"
        return register
        #return self.visitChildren(ctx)


    def visitEqual(self, ctx):
        Le = self.visit(ctx.expression(0))
        Ri = self.visit(ctx.expression(1))

        register = self.registers.pop()
        operation = register + " = " + str(Le) + " " + ctx.EQUAL().getText() + " " + str(Ri)

        if Ri in self.og_registers:
            self.registers.append(Ri)
        if Le in self.og_registers:
            self.registers.append(Le)

        self.line += operation + "\n"
        return register
        #return self.visitChildren(ctx)


    def visitLessEqual(self, ctx):
        Le = self.visit(ctx.expression(0))
        Ri = self.visit(ctx.expression(1))

        register = self.registers.pop()
        operation = register + " = " + str(Le) + " " + ctx.LESS_EQUAL().getText() + " " + str(Ri)

        if Ri in self.og_registers:
            self.registers.append(Ri)
        if Le in self.og_registers:
            self.registers.append(Le)

        self.line += operation + "\n"
        return register
        #return self.visitChildren(ctx)


    def visitLessThan(self, ctx):
        Le = self.visit(ctx.expression(0))
        Ri = self.visit(ctx.expression(1))

        register = self.registers.pop()
        operation = register + " = " + str(Le) + " " + ctx.LESS_THAN().getText() + " " + str(Ri)

        if Ri in self.og_registers:
            self.registers.append(Ri)
        if Le in self.og_registers:
            self.registers.append(Le)

        self.line += operation + "\n"
        return register
        #return self.visitChildren(ctx)


    def visitString(self, ctx):
        string = ctx.STRING().getText()
        register = self.registers.pop()
        operation = register + " = " + string
        if string in self.og_registers:
            self.registers.append(string)
        self.line += operation + "\n"
        self.strprint.append(len(string))
        return register


    def visitInt(self, ctx):
        num = ctx.INT().getText()
        register = self.registers.pop()
        operation = register + " = " + num
        if num in self.og_registers:
            self.registers.append(num)
        self.line += operation + "\n"
        self.strprint.append(len(num))
        return register
        #return self.visitChildren(ctx)


    def visitNegative(self, ctx):
        ne = self.visit(ctx.expression())
        Negat = ctx.INTEGER_NEGATIVE().getText() + str(ne)
        register = self.registers.pop()
        operation = register + " = " + Negat
        if ne in self.og_registers:
            self.registers.append(ne)
        self.line += operation + "\n"
        return register
        #return self.visitChildren(ctx)


    def visitIsvoid(self, ctx):
        ne = self.visit(ctx.expression())
        Negat = ctx.ISVOID().getText() + str(ne)
        register = self.registers.pop()
        operation = register + " = " + Negat
        if ne in self.og_registers:
            self.registers.append(ne)
        self.line += operation + "\n"
        return register
        #return self.visitChildren(ctx)


    def visitBoolNot(self, ctx):
        ne = self.visit(ctx.expression())
        Negat = ctx.NOT().getText() + str(ne)
        register = self.registers.pop()
        operation = register + " = " + Negat
        if ne in self.og_registers:
            self.registers.append(ne)
        self.line += operation + "\n"
        return register
        #return self.visitChildren(ctx)


    def visitNew(self, ctx):
        type = ctx.TYPEID().getText()
        register = self.registers.pop()
        operation = register + " = " + "allocate byte_size " + type
        if type in self.og_registers:
            self.registers.append(type)
        self.line += operation + "\n"
        return register


    def visitFalse(self, ctx):
        false = "0"
        register = self.registers.pop()
        self.line += register + " = " + "Bool " + str(false) + "\n"
        if register in self.og_registers:
            self.registers.append(register)
        return register
        #return self.visitChildren(ctx)


    def visitTrue(self, ctx):
        true = "1"
        register = self.registers.pop()
        self.line +=  register + " = " + "Bool " + str(true) + "\n"
        if register in self.og_registers:
            self.registers.append(register)
        return register
        #return self.visitChildren(ctx)


    def visitWhile(self, ctx):
        self.scope_ids += 1
        self.scope_actual.append("while" + str(self.scope_ids))
        start_label = "L" + str(self.label)
        while_line = start_label + ":\n"
        self.label += 1
        self.line += while_line
        register = self.visit(ctx.expression(0))
        true_label = "L" + str(self.label)
        self.label += 1
        while_cont1 = "IfW " + str(register) + " Goto " + str(true_label) +"\n"
        if register in self.og_registers:
            self.registers.append(register)
        self.line += while_cont1
        self.line += "Goto " + "L_END_WHILE" + "\n"
        self.line += true_label + ":\n"
        self.visit(ctx.expression(1))
        while_loop = "Goto " + start_label + "\n"
        self.line += while_loop
        self.line += "L_END_WHILE" + "\n"
        self.scope_actual.pop()
        return 0
        #return self.visitChildren(ctx)


    def visitIf(self, ctx):
        self.scope_ids += 1
        name = "if" + str(self.scope_ids)
        self.scope_actual.append(name)
        register = self.visit(ctx.expression(0))
        salto = "L" + str(self.label)
        self.label += 1
        if_line = "IfZ " + str(register) + " Goto " + str(salto) + "\n"
        if register in self.og_registers:
            self.registers.append(register)
        self.line += if_line
        self.line += "Goto " + "L" + str(self.label) + "\n"
        self.line += salto + ":\n"
        self.visit(ctx.expression(1))
        end = ""
        if ctx.expression(2):
            #end_line = salto + ": \n"
            end = "L_END_IF"
            self.line += "Goto " + end + "\n"
            elsee = "L" + str(self.label)
            self.line += elsee + ":\n"
            self.visit(ctx.expression(2))
            self.label += 1
        else:
            end_line = "L" + str(self.label) + ":\n"
            self.line += end_line
        if len(end) > 0:
            self.line += end + "\n"
        self.scope_actual.pop()
        return 0
        #return self.visitChildren(ctx)


    def visitLetIn(self, ctx):
        self.scope_ids += 1
        self.scope_actual.append("let" + str(self.scope_ids))
        start_label = "L" + str(self.label)
        let_line = start_label + ":\n"
        self.label += 1
        self.line += let_line
        let = self.visit(ctx.decla(0))
        true_label = "L" + str(self.label)
        self.label += 1
        let_cont1 = "IfL " + str(let) + " Goto " + str(true_label) + "\n"
        if let in self.og_registers:
            self.registers.append(let)
        if ctx.decla(1):
            let1 = self.visit(ctx.decla(1))
        self.line += let_cont1
        self.line += "Goto " + "L_END_LET" + "\n"
        self.line += true_label + ":\n"
        self.visit(ctx.expression())
        let_loop = "Goto " + start_label + "\n"
        self.line += let_loop
        self.line += "L_END_LET" + "\n"
        self.scope_actual.pop()
        return 0
        #return self.visitChildren(ctx)


    def visitCase(self, ctx):
        self.scope_ids += 1
        self.scope_actual.append("case" + str(self.scope_ids))
        start_label = "L" + str(self.label)
        let_line = start_label + ":\n"
        self.label += 1
        self.line += let_line
        exprCase = self.visit(ctx.expression(0))
        true_label = "L" + str(self.label)
        self.label += 1
        let_cont1 = "IfC " + str(exprCase) + " Goto " + str(true_label) + "\n"
        if exprCase in self.og_registers:
            self.registers.append(exprCase)
        self.line += let_cont1
        self.line += "Goto " + "L_END_CASE" + "\n"
        self.line += true_label + ":\n"
        for f,t,i in zip(ctx.OBJECTID(),ctx.TYPEID(),range(1, len(ctx.expression()))):
            name = f.getText()
            type = t.getText()
            self.line += "Obj " + name + "\n"
            self.line += "Type " + type + "\n"
            expr = self.visit(ctx.expression(i))
        #self.visit(ctx.expression())
        let_loop = "Goto " + start_label + "\n"
        self.line += let_loop
        self.line += "L_END_CASE" + "\n"
        self.scope_actual.pop()
        return 0
        #return self.visitChildren(ctx)


    def visitOwnMethodCall(self, ctx):
        method = ctx.OBJECTID().getText()
        
        # if method == "in_string" or method == "in_int":
        #     return self.visitChildren(ctx)
        # if method == "out_string":
        #     return self.visitChildren(ctx)
        # if method == "out_int":
        #     return self.visitChildren(ctx)

        if ctx.expression(1) or ctx.expression(0):
            for arg in ctx.expression():
               
                param = self.visit(arg)
                self.line += "push param " + str(param) + "\n"
        register = self.registers.pop()
        self.line += register + " = _MCall " + method + "\n"
        if method == "in_string" or method == "in_int" or method == "out_string" or method == "out_int":
            if self.strprint != []:   
                popparams = self.strprint.pop()
                self.line += "PopParams" + " " + str(popparams) + "\n"
        if register in self.og_registers:
            self.registers.append(register)

        return register

        #return self.visitChildren(ctx)


    def visitMethodCall(self, ctx):
        name = ctx.OBJECTID().getText()

        if ctx.TYPEID():
            type = ctx.TYPEID().getText()

        if ctx.expression(0) :
            expr2 = self.visit(ctx.expression(0))
            self.line += "param " + str(expr2) + "\n"
            if expr2 in self.og_registers:
                self.registers.append(expr2)

        if ctx.expression(1) :
            expr2 = self.visit(ctx.expression(1))
            self.line += "push param " + str(expr2) + "\n"
            if expr2 in self.og_registers:
                self.registers.append(expr2)

        if ctx.expression(2):
            expr2 = self.visit(ctx.expression(2))
            self.line += "push param " + str(expr2) + "\n"
            if expr2 in self.og_registers:
                self.registers.append(expr2)

        # if ctx.expression():
        #     for arg in ctx.expression():
        #         param = self.visit(arg)
        #         self.line += "push param " + str(param) + "\n"
        #         if param in self.og_registers:
        #             self.registers.append(param)

        register = self.registers.pop()
        self.line += register + " = _MCall " + name + "\n"
        if register in self.og_registers:
            self.registers.append(register)
            #expr1 = self.visit(ctx.expression(0))

        if name == "in_string" or name == "in_int":
            return self.visitChildren(ctx)
        if name == "out_string":
            return self.visitChildren(ctx)
        if name == "out_int":
            return self.visitChildren(ctx)

        return register
        #return self.visitChildren(ctx)


    def visitId(self, ctx):
        name = ctx.OBJECTID().getText()
        for nombre in self.property:
            if nombre.get_property_name(name) == name:
                if nombre.get_expression() != None:

                    offset = 0
                    for scope in self.class_actual:
                        actualScope = self.scopes[scope]
                        if symbol := actualScope.get_symbol(name):
                            break

                    sName = actualScope.name[0] + str(actualScope.scope_ids)
                    value  = sName + "[" + str(offset) + "]"
                    equal = str(value) + " = " + str(symbol) + "\n"
                    if symbol == None:
                        return value

                    self.line += equal
                    return equal
                else:

                    offset = 0
                    for scope in self.class_actual[::-1]:
                        actualScope = self.scopes[scope]
                        if symbol := actualScope.get_symbol(name):
                            break

                    for symbol in actualScope.params:
                        if symbol.name == name:
                            break
                        else:
                            if symbol.type in DEFAULT_TYPES:
                                offset += DEFAULT_TYPES[symbol.type]

                    sName = actualScope.name[0] + str(actualScope.scope_ids)
                    value  = sName + "[" + str(offset) + "]"
                    return value


        for form in self.formal:
            if form.name  == name:
                    offset = 0
                    for scope in self.method_actual[::-1]:
                        actualScope = self.scopes[scope]
                        if symbol := actualScope.get_symbol(name):
                            break

                    for symbol in actualScope.formalParams:
                        if symbol.name == name:
                            break
                        else:
                            if symbol.type in DEFAULT_TYPES:
                                offset += DEFAULT_TYPES[symbol.type]

                    sName = actualScope.name[0] + str(actualScope.id)
                    value  = sName + "[" + str(offset) + "]"

                    # for l in self.lets:
                    #     if value in l:
                    #         offset += DEFAULT_TYPES[symbol.type]
                    #         value  = sName + "[" + str(offset) + "]"
                    #         break
                    return value

        for decl in self.letin:
            if decl.name.name == name:
                    offset = 0
                    for scope in self.method_actual[::-1]:
                        actualScope = self.scopes[scope]
                        break

                    for decl in self.letin:
                        if decl.name.name == name:
                            break
                        else:
                            if decl.name.type in DEFAULT_TYPES:
                                offset += DEFAULT_TYPES[decl.name.type]

                    sName = "l" + actualScope.name[0] + str(actualScope.id)
                    value  = sName + "[" + str(offset) + "]"

                    for l in self.lets:
                        if name in l:
                            value = l[1]
                            break
                    return value


    def visitAssignment(self, ctx):
        name = ctx.OBJECTID().getText()
        for nombre in self.property:
            if nombre.get_property_name(name) == name:
                if nombre.get_expression() != None:
                    offset = 0
                    for scope in self.class_actual:
                        actualScope = self.scopes[scope]
                        if symbol := actualScope.get_symbol(name):
                            break

                    sName = actualScope.name[0] + str(actualScope.scope_ids)
                    value  = sName + "[" + str(offset) + "]"
                    break

                else:
                    offset = 0
                    for scope in self.class_actual:
                        actualScope = self.scopes[scope]
                        if symbol := actualScope.get_symbol(name):
                            break

                    for symbol in actualScope.params:
                        if symbol.name == name:
                            break
                        else:
                            if symbol.type in DEFAULT_TYPES:
                                offset += DEFAULT_TYPES[symbol.type]

                    sName = actualScope.name[0] + str(actualScope.scope_ids)
                    value  = sName + "[" + str(offset) + "]"
                    break

        for decl in self.letin:
            if decl.name.name == name:
                    offset = 0
                    for scope in self.method_actual[::-1]:
                        actualScope = self.scopes[scope]
                        break

                    for decl in self.letin:
                        if decl.name.name == name:
                            break
                        else:
                            if decl.name.type in DEFAULT_TYPES:
                                offset += DEFAULT_TYPES[decl.name.type]

                    sName = "l" + actualScope.name[0] + str(actualScope.id)
                    value  = sName + "[" + str(offset) + "]"

                    for l in self.lets:
                        if name in l:
                            value = l[1]
                            break
                    self.lets.append([name, value])

                    # for n in self.scope_actual[::-1]:
                    #     if "let" in n:
                    #         self.scope_actual.append(name)
                    break
        expr = self.visit(ctx.expression())

        equal = str(value) + " = " + str(expr) + "\n"
        self.line += equal
        return equal
        #return self.visitChildren(ctx)


    def visitDecla(self, ctx):
        name = ctx.OBJECTID().getText()
        for nombre in self.property:
            if nombre.get_property_name(name) == name:
                if nombre.get_expression() != None:
                    offset = 0
                    for scope in self.class_actual:
                        actualScope = self.scopes[scope]
                        if symbol := actualScope.get_symbol(name):
                            break

                    sName = actualScope.name[0] + str(actualScope.scope_ids)
                    value  = sName + "[" + str(offset) + "]"
                    break

                else:
                    offset = 0
                    for scope in self.class_actual:
                        actualScope = self.scopes[scope]
                        if symbol := actualScope.get_symbol(name):
                            break

                    for symbol in actualScope.params:
                        if symbol.name == name:
                            break
                        else:
                            if symbol.type in DEFAULT_TYPES:
                                offset += DEFAULT_TYPES[symbol.type]

                    sName = actualScope.name[0] + str(actualScope.scope_ids)
                    value  = sName + "[" + str(offset) + "]"
                    break

        for decl in self.letin:
            if decl.name.name == name:
                    offset = 0
                    for scope in self.method_actual[::-1]:
                        actualScope = self.scopes[scope]
                        break

                    for decl in self.letin:
                        if decl.name.name == name:
                            break
                        else:
                            if decl.name.type in DEFAULT_TYPES:
                                offset += DEFAULT_TYPES[decl.name.type]

                    sName = "l" + actualScope.name[0] + str(actualScope.id)
                    value  = sName + "[" + str(offset) + "]"

                    for l in self.lets:
                        if name in l:
                            value = l[1]
                            break
                    self.lets.append([name, value])
                    break

        type = ctx.TYPEID().getText()

        if ctx.expression():
            expr = self.visit(ctx.expression())
            register = self.registers.pop()
            operation = register + " = " + str(value) + " " + " = " + " " + str(expr)
            if expr in self.og_registers:
                self.registers.append(expr)
            if value in self.og_registers:
                self.registers.append(value)
            self.line += operation + "\n"
            return register

        return value