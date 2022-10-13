# Generated from YAPL.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YAPLParser import YAPLParser
else:
    from YAPLParser import YAPLParser

# This class defines a complete listener for a parse tree produced by YAPLParser.
class YAPLListener(ParseTreeListener):

    # Enter a parse tree produced by YAPLParser#program.
    def enterProgram(self, ctx:YAPLParser.ProgramContext):
        pass

    # Exit a parse tree produced by YAPLParser#program.
    def exitProgram(self, ctx:YAPLParser.ProgramContext):
        pass


    # Enter a parse tree produced by YAPLParser#classes.
    def enterClasses(self, ctx:YAPLParser.ClassesContext):
        pass

    # Exit a parse tree produced by YAPLParser#classes.
    def exitClasses(self, ctx:YAPLParser.ClassesContext):
        pass


    # Enter a parse tree produced by YAPLParser#eof.
    def enterEof(self, ctx:YAPLParser.EofContext):
        pass

    # Exit a parse tree produced by YAPLParser#eof.
    def exitEof(self, ctx:YAPLParser.EofContext):
        pass


    # Enter a parse tree produced by YAPLParser#classDefine.
    def enterClassDefine(self, ctx:YAPLParser.ClassDefineContext):
        pass

    # Exit a parse tree produced by YAPLParser#classDefine.
    def exitClassDefine(self, ctx:YAPLParser.ClassDefineContext):
        pass


    # Enter a parse tree produced by YAPLParser#method.
    def enterMethod(self, ctx:YAPLParser.MethodContext):
        pass

    # Exit a parse tree produced by YAPLParser#method.
    def exitMethod(self, ctx:YAPLParser.MethodContext):
        pass


    # Enter a parse tree produced by YAPLParser#property.
    def enterProperty(self, ctx:YAPLParser.PropertyContext):
        pass

    # Exit a parse tree produced by YAPLParser#property.
    def exitProperty(self, ctx:YAPLParser.PropertyContext):
        pass


    # Enter a parse tree produced by YAPLParser#decla.
    def enterDecla(self, ctx:YAPLParser.DeclaContext):
        pass

    # Exit a parse tree produced by YAPLParser#decla.
    def exitDecla(self, ctx:YAPLParser.DeclaContext):
        pass


    # Enter a parse tree produced by YAPLParser#formal.
    def enterFormal(self, ctx:YAPLParser.FormalContext):
        pass

    # Exit a parse tree produced by YAPLParser#formal.
    def exitFormal(self, ctx:YAPLParser.FormalContext):
        pass


    # Enter a parse tree produced by YAPLParser#letIn.
    def enterLetIn(self, ctx:YAPLParser.LetInContext):
        pass

    # Exit a parse tree produced by YAPLParser#letIn.
    def exitLetIn(self, ctx:YAPLParser.LetInContext):
        pass


    # Enter a parse tree produced by YAPLParser#minus.
    def enterMinus(self, ctx:YAPLParser.MinusContext):
        pass

    # Exit a parse tree produced by YAPLParser#minus.
    def exitMinus(self, ctx:YAPLParser.MinusContext):
        pass


    # Enter a parse tree produced by YAPLParser#string.
    def enterString(self, ctx:YAPLParser.StringContext):
        pass

    # Exit a parse tree produced by YAPLParser#string.
    def exitString(self, ctx:YAPLParser.StringContext):
        pass


    # Enter a parse tree produced by YAPLParser#isvoid.
    def enterIsvoid(self, ctx:YAPLParser.IsvoidContext):
        pass

    # Exit a parse tree produced by YAPLParser#isvoid.
    def exitIsvoid(self, ctx:YAPLParser.IsvoidContext):
        pass


    # Enter a parse tree produced by YAPLParser#while.
    def enterWhile(self, ctx:YAPLParser.WhileContext):
        pass

    # Exit a parse tree produced by YAPLParser#while.
    def exitWhile(self, ctx:YAPLParser.WhileContext):
        pass


    # Enter a parse tree produced by YAPLParser#division.
    def enterDivision(self, ctx:YAPLParser.DivisionContext):
        pass

    # Exit a parse tree produced by YAPLParser#division.
    def exitDivision(self, ctx:YAPLParser.DivisionContext):
        pass


    # Enter a parse tree produced by YAPLParser#negative.
    def enterNegative(self, ctx:YAPLParser.NegativeContext):
        pass

    # Exit a parse tree produced by YAPLParser#negative.
    def exitNegative(self, ctx:YAPLParser.NegativeContext):
        pass


    # Enter a parse tree produced by YAPLParser#boolNot.
    def enterBoolNot(self, ctx:YAPLParser.BoolNotContext):
        pass

    # Exit a parse tree produced by YAPLParser#boolNot.
    def exitBoolNot(self, ctx:YAPLParser.BoolNotContext):
        pass


    # Enter a parse tree produced by YAPLParser#lessThan.
    def enterLessThan(self, ctx:YAPLParser.LessThanContext):
        pass

    # Exit a parse tree produced by YAPLParser#lessThan.
    def exitLessThan(self, ctx:YAPLParser.LessThanContext):
        pass


    # Enter a parse tree produced by YAPLParser#block.
    def enterBlock(self, ctx:YAPLParser.BlockContext):
        pass

    # Exit a parse tree produced by YAPLParser#block.
    def exitBlock(self, ctx:YAPLParser.BlockContext):
        pass


    # Enter a parse tree produced by YAPLParser#id.
    def enterId(self, ctx:YAPLParser.IdContext):
        pass

    # Exit a parse tree produced by YAPLParser#id.
    def exitId(self, ctx:YAPLParser.IdContext):
        pass


    # Enter a parse tree produced by YAPLParser#multiply.
    def enterMultiply(self, ctx:YAPLParser.MultiplyContext):
        pass

    # Exit a parse tree produced by YAPLParser#multiply.
    def exitMultiply(self, ctx:YAPLParser.MultiplyContext):
        pass


    # Enter a parse tree produced by YAPLParser#if.
    def enterIf(self, ctx:YAPLParser.IfContext):
        pass

    # Exit a parse tree produced by YAPLParser#if.
    def exitIf(self, ctx:YAPLParser.IfContext):
        pass


    # Enter a parse tree produced by YAPLParser#case.
    def enterCase(self, ctx:YAPLParser.CaseContext):
        pass

    # Exit a parse tree produced by YAPLParser#case.
    def exitCase(self, ctx:YAPLParser.CaseContext):
        pass


    # Enter a parse tree produced by YAPLParser#ownMethodCall.
    def enterOwnMethodCall(self, ctx:YAPLParser.OwnMethodCallContext):
        pass

    # Exit a parse tree produced by YAPLParser#ownMethodCall.
    def exitOwnMethodCall(self, ctx:YAPLParser.OwnMethodCallContext):
        pass


    # Enter a parse tree produced by YAPLParser#add.
    def enterAdd(self, ctx:YAPLParser.AddContext):
        pass

    # Exit a parse tree produced by YAPLParser#add.
    def exitAdd(self, ctx:YAPLParser.AddContext):
        pass


    # Enter a parse tree produced by YAPLParser#new.
    def enterNew(self, ctx:YAPLParser.NewContext):
        pass

    # Exit a parse tree produced by YAPLParser#new.
    def exitNew(self, ctx:YAPLParser.NewContext):
        pass


    # Enter a parse tree produced by YAPLParser#parentheses.
    def enterParentheses(self, ctx:YAPLParser.ParenthesesContext):
        pass

    # Exit a parse tree produced by YAPLParser#parentheses.
    def exitParentheses(self, ctx:YAPLParser.ParenthesesContext):
        pass


    # Enter a parse tree produced by YAPLParser#assignment.
    def enterAssignment(self, ctx:YAPLParser.AssignmentContext):
        pass

    # Exit a parse tree produced by YAPLParser#assignment.
    def exitAssignment(self, ctx:YAPLParser.AssignmentContext):
        pass


    # Enter a parse tree produced by YAPLParser#false.
    def enterFalse(self, ctx:YAPLParser.FalseContext):
        pass

    # Exit a parse tree produced by YAPLParser#false.
    def exitFalse(self, ctx:YAPLParser.FalseContext):
        pass


    # Enter a parse tree produced by YAPLParser#int.
    def enterInt(self, ctx:YAPLParser.IntContext):
        pass

    # Exit a parse tree produced by YAPLParser#int.
    def exitInt(self, ctx:YAPLParser.IntContext):
        pass


    # Enter a parse tree produced by YAPLParser#equal.
    def enterEqual(self, ctx:YAPLParser.EqualContext):
        pass

    # Exit a parse tree produced by YAPLParser#equal.
    def exitEqual(self, ctx:YAPLParser.EqualContext):
        pass


    # Enter a parse tree produced by YAPLParser#true.
    def enterTrue(self, ctx:YAPLParser.TrueContext):
        pass

    # Exit a parse tree produced by YAPLParser#true.
    def exitTrue(self, ctx:YAPLParser.TrueContext):
        pass


    # Enter a parse tree produced by YAPLParser#lessEqual.
    def enterLessEqual(self, ctx:YAPLParser.LessEqualContext):
        pass

    # Exit a parse tree produced by YAPLParser#lessEqual.
    def exitLessEqual(self, ctx:YAPLParser.LessEqualContext):
        pass


    # Enter a parse tree produced by YAPLParser#methodCall.
    def enterMethodCall(self, ctx:YAPLParser.MethodCallContext):
        pass

    # Exit a parse tree produced by YAPLParser#methodCall.
    def exitMethodCall(self, ctx:YAPLParser.MethodCallContext):
        pass



del YAPLParser