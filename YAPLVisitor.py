# Generated from YAPL.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YAPLParser import YAPLParser
else:
    from YAPLParser import YAPLParser

# This class defines a complete generic visitor for a parse tree produced by YAPLParser.

class YAPLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by YAPLParser#program.
    def visitProgram(self, ctx:YAPLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#classes.
    def visitClasses(self, ctx:YAPLParser.ClassesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#eof.
    def visitEof(self, ctx:YAPLParser.EofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#classDefine.
    def visitClassDefine(self, ctx:YAPLParser.ClassDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#method.
    def visitMethod(self, ctx:YAPLParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#property.
    def visitProperty(self, ctx:YAPLParser.PropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#decla.
    def visitDecla(self, ctx:YAPLParser.DeclaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#formal.
    def visitFormal(self, ctx:YAPLParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#letIn.
    def visitLetIn(self, ctx:YAPLParser.LetInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#minus.
    def visitMinus(self, ctx:YAPLParser.MinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#string.
    def visitString(self, ctx:YAPLParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#isvoid.
    def visitIsvoid(self, ctx:YAPLParser.IsvoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#while.
    def visitWhile(self, ctx:YAPLParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#division.
    def visitDivision(self, ctx:YAPLParser.DivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#negative.
    def visitNegative(self, ctx:YAPLParser.NegativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#boolNot.
    def visitBoolNot(self, ctx:YAPLParser.BoolNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#lessThan.
    def visitLessThan(self, ctx:YAPLParser.LessThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#block.
    def visitBlock(self, ctx:YAPLParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#id.
    def visitId(self, ctx:YAPLParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#multiply.
    def visitMultiply(self, ctx:YAPLParser.MultiplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#if.
    def visitIf(self, ctx:YAPLParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#case.
    def visitCase(self, ctx:YAPLParser.CaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#ownMethodCall.
    def visitOwnMethodCall(self, ctx:YAPLParser.OwnMethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#add.
    def visitAdd(self, ctx:YAPLParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#new.
    def visitNew(self, ctx:YAPLParser.NewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#parentheses.
    def visitParentheses(self, ctx:YAPLParser.ParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#assignment.
    def visitAssignment(self, ctx:YAPLParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#false.
    def visitFalse(self, ctx:YAPLParser.FalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#int.
    def visitInt(self, ctx:YAPLParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#equal.
    def visitEqual(self, ctx:YAPLParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#true.
    def visitTrue(self, ctx:YAPLParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#lessEqual.
    def visitLessEqual(self, ctx:YAPLParser.LessEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#methodCall.
    def visitMethodCall(self, ctx:YAPLParser.MethodCallContext):
        return self.visitChildren(ctx)



del YAPLParser