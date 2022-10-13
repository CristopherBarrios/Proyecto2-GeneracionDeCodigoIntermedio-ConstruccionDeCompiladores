// Generated from c:\Users\cjrba\OneDrive\Documentos\Universidad\10-semestre\Compiladores\Proyecto2\modificando\Proyecto2Compis-main\YAPL.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class YAPLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		CLASS=10, ELSE=11, FALSE=12, FI=13, IF=14, IN=15, INHERITS=16, ISVOID=17, 
		LET=18, LOOP=19, POOL=20, THEN=21, WHILE=22, CASE=23, ESAC=24, NEW=25, 
		OF=26, NOT=27, TRUE=28, STRING=29, INT=30, TYPEID=31, OBJECTID=32, ASSIGNMENT=33, 
		CASE_ARROW=34, ADD=35, MINUS=36, MULTIPLY=37, DIVISION=38, LESS_THAN=39, 
		LESS_EQUAL=40, EQUAL=41, INTEGER_NEGATIVE=42, OPEN_COMMENT=43, CLOSE_COMMENT=44, 
		COMMENT=45, ONE_LINE_COMMENT=46, WHITESPACE=47;
	public static final int
		RULE_program = 0, RULE_programBlocks = 1, RULE_classDefine = 2, RULE_feature = 3, 
		RULE_decla = 4, RULE_formal = 5, RULE_expression = 6;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "programBlocks", "classDefine", "feature", "decla", "formal", 
			"expression"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'{'", "'}'", "'('", "','", "')'", "':'", "'@'", "'.'", 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, "'<-'", 
			"'=>'", "'+'", "'-'", "'*'", "'/'", "'<'", "'<='", "'='", "'~'", "'(*'", 
			"'*)'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, "CLASS", 
			"ELSE", "FALSE", "FI", "IF", "IN", "INHERITS", "ISVOID", "LET", "LOOP", 
			"POOL", "THEN", "WHILE", "CASE", "ESAC", "NEW", "OF", "NOT", "TRUE", 
			"STRING", "INT", "TYPEID", "OBJECTID", "ASSIGNMENT", "CASE_ARROW", "ADD", 
			"MINUS", "MULTIPLY", "DIVISION", "LESS_THAN", "LESS_EQUAL", "EQUAL", 
			"INTEGER_NEGATIVE", "OPEN_COMMENT", "CLOSE_COMMENT", "COMMENT", "ONE_LINE_COMMENT", 
			"WHITESPACE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "YAPL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public YAPLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public ProgramBlocksContext programBlocks() {
			return getRuleContext(ProgramBlocksContext.class,0);
		}
		public TerminalNode EOF() { return getToken(YAPLParser.EOF, 0); }
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(14);
			programBlocks();
			setState(15);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ProgramBlocksContext extends ParserRuleContext {
		public ProgramBlocksContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programBlocks; }
	 
		public ProgramBlocksContext() { }
		public void copyFrom(ProgramBlocksContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ClassesContext extends ProgramBlocksContext {
		public ClassDefineContext classDefine() {
			return getRuleContext(ClassDefineContext.class,0);
		}
		public ProgramBlocksContext programBlocks() {
			return getRuleContext(ProgramBlocksContext.class,0);
		}
		public ClassesContext(ProgramBlocksContext ctx) { copyFrom(ctx); }
	}
	public static class EofContext extends ProgramBlocksContext {
		public TerminalNode EOF() { return getToken(YAPLParser.EOF, 0); }
		public EofContext(ProgramBlocksContext ctx) { copyFrom(ctx); }
	}

	public final ProgramBlocksContext programBlocks() throws RecognitionException {
		ProgramBlocksContext _localctx = new ProgramBlocksContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_programBlocks);
		try {
			setState(22);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CLASS:
				_localctx = new ClassesContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(17);
				classDefine();
				setState(18);
				match(T__0);
				setState(19);
				programBlocks();
				}
				break;
			case EOF:
				_localctx = new EofContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(21);
				match(EOF);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClassDefineContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(YAPLParser.CLASS, 0); }
		public List<TerminalNode> TYPEID() { return getTokens(YAPLParser.TYPEID); }
		public TerminalNode TYPEID(int i) {
			return getToken(YAPLParser.TYPEID, i);
		}
		public TerminalNode INHERITS() { return getToken(YAPLParser.INHERITS, 0); }
		public List<FeatureContext> feature() {
			return getRuleContexts(FeatureContext.class);
		}
		public FeatureContext feature(int i) {
			return getRuleContext(FeatureContext.class,i);
		}
		public ClassDefineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classDefine; }
	}

	public final ClassDefineContext classDefine() throws RecognitionException {
		ClassDefineContext _localctx = new ClassDefineContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_classDefine);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(24);
			match(CLASS);
			setState(25);
			match(TYPEID);
			setState(28);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INHERITS) {
				{
				setState(26);
				match(INHERITS);
				setState(27);
				match(TYPEID);
				}
			}

			setState(30);
			match(T__1);
			setState(36);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OBJECTID) {
				{
				{
				setState(31);
				feature();
				setState(32);
				match(T__0);
				}
				}
				setState(38);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(39);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FeatureContext extends ParserRuleContext {
		public FeatureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_feature; }
	 
		public FeatureContext() { }
		public void copyFrom(FeatureContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class MethodContext extends FeatureContext {
		public TerminalNode OBJECTID() { return getToken(YAPLParser.OBJECTID, 0); }
		public TerminalNode TYPEID() { return getToken(YAPLParser.TYPEID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<FormalContext> formal() {
			return getRuleContexts(FormalContext.class);
		}
		public FormalContext formal(int i) {
			return getRuleContext(FormalContext.class,i);
		}
		public MethodContext(FeatureContext ctx) { copyFrom(ctx); }
	}
	public static class PropertyContext extends FeatureContext {
		public TerminalNode OBJECTID() { return getToken(YAPLParser.OBJECTID, 0); }
		public TerminalNode TYPEID() { return getToken(YAPLParser.TYPEID, 0); }
		public TerminalNode ASSIGNMENT() { return getToken(YAPLParser.ASSIGNMENT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public PropertyContext(FeatureContext ctx) { copyFrom(ctx); }
	}

	public final FeatureContext feature() throws RecognitionException {
		FeatureContext _localctx = new FeatureContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_feature);
		int _la;
		try {
			setState(67);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				_localctx = new MethodContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(41);
				match(OBJECTID);
				setState(42);
				match(T__3);
				setState(51);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==OBJECTID) {
					{
					setState(43);
					formal();
					setState(48);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__4) {
						{
						{
						setState(44);
						match(T__4);
						setState(45);
						formal();
						}
						}
						setState(50);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(53);
				match(T__5);
				setState(54);
				match(T__6);
				setState(55);
				match(TYPEID);
				setState(56);
				match(T__1);
				setState(57);
				expression(0);
				setState(58);
				match(T__2);
				}
				break;
			case 2:
				_localctx = new PropertyContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(60);
				match(OBJECTID);
				setState(61);
				match(T__6);
				setState(62);
				match(TYPEID);
				setState(65);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASSIGNMENT) {
					{
					setState(63);
					match(ASSIGNMENT);
					setState(64);
					expression(0);
					}
				}

				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclaContext extends ParserRuleContext {
		public TerminalNode OBJECTID() { return getToken(YAPLParser.OBJECTID, 0); }
		public TerminalNode TYPEID() { return getToken(YAPLParser.TYPEID, 0); }
		public TerminalNode ASSIGNMENT() { return getToken(YAPLParser.ASSIGNMENT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public DeclaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decla; }
	}

	public final DeclaContext decla() throws RecognitionException {
		DeclaContext _localctx = new DeclaContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_decla);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(69);
			match(OBJECTID);
			setState(70);
			match(T__6);
			setState(71);
			match(TYPEID);
			setState(74);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASSIGNMENT) {
				{
				setState(72);
				match(ASSIGNMENT);
				setState(73);
				expression(0);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FormalContext extends ParserRuleContext {
		public TerminalNode OBJECTID() { return getToken(YAPLParser.OBJECTID, 0); }
		public TerminalNode TYPEID() { return getToken(YAPLParser.TYPEID, 0); }
		public FormalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formal; }
	}

	public final FormalContext formal() throws RecognitionException {
		FormalContext _localctx = new FormalContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_formal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			match(OBJECTID);
			setState(77);
			match(T__6);
			setState(78);
			match(TYPEID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class LetInContext extends ExpressionContext {
		public TerminalNode LET() { return getToken(YAPLParser.LET, 0); }
		public List<DeclaContext> decla() {
			return getRuleContexts(DeclaContext.class);
		}
		public DeclaContext decla(int i) {
			return getRuleContext(DeclaContext.class,i);
		}
		public TerminalNode IN() { return getToken(YAPLParser.IN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public LetInContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class MinusContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode MINUS() { return getToken(YAPLParser.MINUS, 0); }
		public MinusContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class StringContext extends ExpressionContext {
		public TerminalNode STRING() { return getToken(YAPLParser.STRING, 0); }
		public StringContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class IsvoidContext extends ExpressionContext {
		public TerminalNode ISVOID() { return getToken(YAPLParser.ISVOID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public IsvoidContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class WhileContext extends ExpressionContext {
		public TerminalNode WHILE() { return getToken(YAPLParser.WHILE, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode LOOP() { return getToken(YAPLParser.LOOP, 0); }
		public TerminalNode POOL() { return getToken(YAPLParser.POOL, 0); }
		public WhileContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class DivisionContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode DIVISION() { return getToken(YAPLParser.DIVISION, 0); }
		public DivisionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class NegativeContext extends ExpressionContext {
		public TerminalNode INTEGER_NEGATIVE() { return getToken(YAPLParser.INTEGER_NEGATIVE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public NegativeContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class BoolNotContext extends ExpressionContext {
		public TerminalNode NOT() { return getToken(YAPLParser.NOT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BoolNotContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class LessThanContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode LESS_THAN() { return getToken(YAPLParser.LESS_THAN, 0); }
		public LessThanContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class BlockContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public BlockContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class IdContext extends ExpressionContext {
		public TerminalNode OBJECTID() { return getToken(YAPLParser.OBJECTID, 0); }
		public IdContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class MultiplyContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode MULTIPLY() { return getToken(YAPLParser.MULTIPLY, 0); }
		public MultiplyContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class IfContext extends ExpressionContext {
		public TerminalNode IF() { return getToken(YAPLParser.IF, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode THEN() { return getToken(YAPLParser.THEN, 0); }
		public TerminalNode ELSE() { return getToken(YAPLParser.ELSE, 0); }
		public TerminalNode FI() { return getToken(YAPLParser.FI, 0); }
		public IfContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class CaseContext extends ExpressionContext {
		public TerminalNode CASE() { return getToken(YAPLParser.CASE, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode OF() { return getToken(YAPLParser.OF, 0); }
		public TerminalNode ESAC() { return getToken(YAPLParser.ESAC, 0); }
		public List<TerminalNode> OBJECTID() { return getTokens(YAPLParser.OBJECTID); }
		public TerminalNode OBJECTID(int i) {
			return getToken(YAPLParser.OBJECTID, i);
		}
		public List<TerminalNode> TYPEID() { return getTokens(YAPLParser.TYPEID); }
		public TerminalNode TYPEID(int i) {
			return getToken(YAPLParser.TYPEID, i);
		}
		public List<TerminalNode> CASE_ARROW() { return getTokens(YAPLParser.CASE_ARROW); }
		public TerminalNode CASE_ARROW(int i) {
			return getToken(YAPLParser.CASE_ARROW, i);
		}
		public CaseContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class OwnMethodCallContext extends ExpressionContext {
		public TerminalNode OBJECTID() { return getToken(YAPLParser.OBJECTID, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public OwnMethodCallContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class AddContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode ADD() { return getToken(YAPLParser.ADD, 0); }
		public AddContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class NewContext extends ExpressionContext {
		public TerminalNode NEW() { return getToken(YAPLParser.NEW, 0); }
		public TerminalNode TYPEID() { return getToken(YAPLParser.TYPEID, 0); }
		public NewContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ParenthesesContext extends ExpressionContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ParenthesesContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class AssignmentContext extends ExpressionContext {
		public TerminalNode OBJECTID() { return getToken(YAPLParser.OBJECTID, 0); }
		public TerminalNode ASSIGNMENT() { return getToken(YAPLParser.ASSIGNMENT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class FalseContext extends ExpressionContext {
		public TerminalNode FALSE() { return getToken(YAPLParser.FALSE, 0); }
		public FalseContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class IntContext extends ExpressionContext {
		public TerminalNode INT() { return getToken(YAPLParser.INT, 0); }
		public IntContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class EqualContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode EQUAL() { return getToken(YAPLParser.EQUAL, 0); }
		public EqualContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class TrueContext extends ExpressionContext {
		public TerminalNode TRUE() { return getToken(YAPLParser.TRUE, 0); }
		public TrueContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class LessEqualContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode LESS_EQUAL() { return getToken(YAPLParser.LESS_EQUAL, 0); }
		public LessEqualContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class MethodCallContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode OBJECTID() { return getToken(YAPLParser.OBJECTID, 0); }
		public TerminalNode TYPEID() { return getToken(YAPLParser.TYPEID, 0); }
		public MethodCallContext(ExpressionContext ctx) { copyFrom(ctx); }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 12;
		enterRecursionRule(_localctx, 12, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(166);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				{
				_localctx = new OwnMethodCallContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(81);
				match(OBJECTID);
				setState(82);
				match(T__3);
				setState(91);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__3) | (1L << FALSE) | (1L << IF) | (1L << ISVOID) | (1L << LET) | (1L << WHILE) | (1L << CASE) | (1L << NEW) | (1L << NOT) | (1L << TRUE) | (1L << STRING) | (1L << INT) | (1L << OBJECTID) | (1L << INTEGER_NEGATIVE))) != 0)) {
					{
					setState(83);
					expression(0);
					setState(88);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__4) {
						{
						{
						setState(84);
						match(T__4);
						setState(85);
						expression(0);
						}
						}
						setState(90);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(93);
				match(T__5);
				}
				break;
			case 2:
				{
				_localctx = new IfContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(94);
				match(IF);
				setState(95);
				expression(0);
				setState(96);
				match(THEN);
				setState(97);
				expression(0);
				setState(98);
				match(ELSE);
				setState(99);
				expression(0);
				setState(100);
				match(FI);
				}
				break;
			case 3:
				{
				_localctx = new WhileContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(102);
				match(WHILE);
				setState(103);
				expression(0);
				setState(104);
				match(LOOP);
				setState(105);
				expression(0);
				setState(106);
				match(POOL);
				}
				break;
			case 4:
				{
				_localctx = new BlockContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(108);
				match(T__1);
				setState(112); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(109);
					expression(0);
					setState(110);
					match(T__0);
					}
					}
					setState(114); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__3) | (1L << FALSE) | (1L << IF) | (1L << ISVOID) | (1L << LET) | (1L << WHILE) | (1L << CASE) | (1L << NEW) | (1L << NOT) | (1L << TRUE) | (1L << STRING) | (1L << INT) | (1L << OBJECTID) | (1L << INTEGER_NEGATIVE))) != 0) );
				setState(116);
				match(T__2);
				}
				break;
			case 5:
				{
				_localctx = new LetInContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(118);
				match(LET);
				setState(119);
				decla();
				setState(124);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__4) {
					{
					{
					setState(120);
					match(T__4);
					setState(121);
					decla();
					}
					}
					setState(126);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(127);
				match(IN);
				setState(128);
				expression(20);
				}
				break;
			case 6:
				{
				_localctx = new CaseContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(130);
				match(CASE);
				setState(131);
				expression(0);
				setState(132);
				match(OF);
				setState(140); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(133);
					match(OBJECTID);
					setState(134);
					match(T__6);
					setState(135);
					match(TYPEID);
					setState(136);
					match(CASE_ARROW);
					setState(137);
					expression(0);
					setState(138);
					match(T__0);
					}
					}
					setState(142); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==OBJECTID );
				setState(144);
				match(ESAC);
				}
				break;
			case 7:
				{
				_localctx = new NewContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(146);
				match(NEW);
				setState(147);
				match(TYPEID);
				}
				break;
			case 8:
				{
				_localctx = new NegativeContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(148);
				match(INTEGER_NEGATIVE);
				setState(149);
				expression(17);
				}
				break;
			case 9:
				{
				_localctx = new IsvoidContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(150);
				match(ISVOID);
				setState(151);
				expression(16);
				}
				break;
			case 10:
				{
				_localctx = new BoolNotContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(152);
				match(NOT);
				setState(153);
				expression(8);
				}
				break;
			case 11:
				{
				_localctx = new ParenthesesContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(154);
				match(T__3);
				setState(155);
				expression(0);
				setState(156);
				match(T__5);
				}
				break;
			case 12:
				{
				_localctx = new IdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(158);
				match(OBJECTID);
				}
				break;
			case 13:
				{
				_localctx = new IntContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(159);
				match(INT);
				}
				break;
			case 14:
				{
				_localctx = new StringContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(160);
				match(STRING);
				}
				break;
			case 15:
				{
				_localctx = new TrueContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(161);
				match(TRUE);
				}
				break;
			case 16:
				{
				_localctx = new FalseContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(162);
				match(FALSE);
				}
				break;
			case 17:
				{
				_localctx = new AssignmentContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(163);
				match(OBJECTID);
				setState(164);
				match(ASSIGNMENT);
				setState(165);
				expression(1);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(210);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(208);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
					case 1:
						{
						_localctx = new MultiplyContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(168);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(169);
						match(MULTIPLY);
						setState(170);
						expression(16);
						}
						break;
					case 2:
						{
						_localctx = new DivisionContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(171);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(172);
						match(DIVISION);
						setState(173);
						expression(15);
						}
						break;
					case 3:
						{
						_localctx = new AddContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(174);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(175);
						match(ADD);
						setState(176);
						expression(14);
						}
						break;
					case 4:
						{
						_localctx = new MinusContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(177);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(178);
						match(MINUS);
						setState(179);
						expression(13);
						}
						break;
					case 5:
						{
						_localctx = new LessThanContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(180);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(181);
						match(LESS_THAN);
						setState(182);
						expression(12);
						}
						break;
					case 6:
						{
						_localctx = new LessEqualContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(183);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(184);
						match(LESS_EQUAL);
						setState(185);
						expression(11);
						}
						break;
					case 7:
						{
						_localctx = new EqualContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(186);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(187);
						match(EQUAL);
						setState(188);
						expression(10);
						}
						break;
					case 8:
						{
						_localctx = new MethodCallContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(189);
						if (!(precpred(_ctx, 25))) throw new FailedPredicateException(this, "precpred(_ctx, 25)");
						setState(192);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==T__7) {
							{
							setState(190);
							match(T__7);
							setState(191);
							match(TYPEID);
							}
						}

						setState(194);
						match(T__8);
						setState(195);
						match(OBJECTID);
						setState(196);
						match(T__3);
						setState(205);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__3) | (1L << FALSE) | (1L << IF) | (1L << ISVOID) | (1L << LET) | (1L << WHILE) | (1L << CASE) | (1L << NEW) | (1L << NOT) | (1L << TRUE) | (1L << STRING) | (1L << INT) | (1L << OBJECTID) | (1L << INTEGER_NEGATIVE))) != 0)) {
							{
							setState(197);
							expression(0);
							setState(202);
							_errHandler.sync(this);
							_la = _input.LA(1);
							while (_la==T__4) {
								{
								{
								setState(198);
								match(T__4);
								setState(199);
								expression(0);
								}
								}
								setState(204);
								_errHandler.sync(this);
								_la = _input.LA(1);
							}
							}
						}

						setState(207);
						match(T__5);
						}
						break;
					}
					} 
				}
				setState(212);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 6:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 15);
		case 1:
			return precpred(_ctx, 14);
		case 2:
			return precpred(_ctx, 13);
		case 3:
			return precpred(_ctx, 12);
		case 4:
			return precpred(_ctx, 11);
		case 5:
			return precpred(_ctx, 10);
		case 6:
			return precpred(_ctx, 9);
		case 7:
			return precpred(_ctx, 25);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\61\u00d8\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\3\2\3\2\3\2\3\3\3\3\3"+
		"\3\3\3\3\3\5\3\31\n\3\3\4\3\4\3\4\3\4\5\4\37\n\4\3\4\3\4\3\4\3\4\7\4%"+
		"\n\4\f\4\16\4(\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\7\5\61\n\5\f\5\16\5\64"+
		"\13\5\5\5\66\n\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5D"+
		"\n\5\5\5F\n\5\3\6\3\6\3\6\3\6\3\6\5\6M\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b"+
		"\3\b\3\b\3\b\7\bY\n\b\f\b\16\b\\\13\b\5\b^\n\b\3\b\3\b\3\b\3\b\3\b\3\b"+
		"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\6\bs\n\b\r\b\16\b"+
		"t\3\b\3\b\3\b\3\b\3\b\3\b\7\b}\n\b\f\b\16\b\u0080\13\b\3\b\3\b\3\b\3\b"+
		"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\6\b\u008f\n\b\r\b\16\b\u0090\3\b"+
		"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3"+
		"\b\3\b\3\b\3\b\5\b\u00a9\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3"+
		"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00c3\n\b\3"+
		"\b\3\b\3\b\3\b\3\b\3\b\7\b\u00cb\n\b\f\b\16\b\u00ce\13\b\5\b\u00d0\n\b"+
		"\3\b\7\b\u00d3\n\b\f\b\16\b\u00d6\13\b\3\b\2\3\16\t\2\4\6\b\n\f\16\2\2"+
		"\2\u00f8\2\20\3\2\2\2\4\30\3\2\2\2\6\32\3\2\2\2\bE\3\2\2\2\nG\3\2\2\2"+
		"\fN\3\2\2\2\16\u00a8\3\2\2\2\20\21\5\4\3\2\21\22\7\2\2\3\22\3\3\2\2\2"+
		"\23\24\5\6\4\2\24\25\7\3\2\2\25\26\5\4\3\2\26\31\3\2\2\2\27\31\7\2\2\3"+
		"\30\23\3\2\2\2\30\27\3\2\2\2\31\5\3\2\2\2\32\33\7\f\2\2\33\36\7!\2\2\34"+
		"\35\7\22\2\2\35\37\7!\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37 \3\2\2\2 &\7"+
		"\4\2\2!\"\5\b\5\2\"#\7\3\2\2#%\3\2\2\2$!\3\2\2\2%(\3\2\2\2&$\3\2\2\2&"+
		"\'\3\2\2\2\')\3\2\2\2(&\3\2\2\2)*\7\5\2\2*\7\3\2\2\2+,\7\"\2\2,\65\7\6"+
		"\2\2-\62\5\f\7\2./\7\7\2\2/\61\5\f\7\2\60.\3\2\2\2\61\64\3\2\2\2\62\60"+
		"\3\2\2\2\62\63\3\2\2\2\63\66\3\2\2\2\64\62\3\2\2\2\65-\3\2\2\2\65\66\3"+
		"\2\2\2\66\67\3\2\2\2\678\7\b\2\289\7\t\2\29:\7!\2\2:;\7\4\2\2;<\5\16\b"+
		"\2<=\7\5\2\2=F\3\2\2\2>?\7\"\2\2?@\7\t\2\2@C\7!\2\2AB\7#\2\2BD\5\16\b"+
		"\2CA\3\2\2\2CD\3\2\2\2DF\3\2\2\2E+\3\2\2\2E>\3\2\2\2F\t\3\2\2\2GH\7\""+
		"\2\2HI\7\t\2\2IL\7!\2\2JK\7#\2\2KM\5\16\b\2LJ\3\2\2\2LM\3\2\2\2M\13\3"+
		"\2\2\2NO\7\"\2\2OP\7\t\2\2PQ\7!\2\2Q\r\3\2\2\2RS\b\b\1\2ST\7\"\2\2T]\7"+
		"\6\2\2UZ\5\16\b\2VW\7\7\2\2WY\5\16\b\2XV\3\2\2\2Y\\\3\2\2\2ZX\3\2\2\2"+
		"Z[\3\2\2\2[^\3\2\2\2\\Z\3\2\2\2]U\3\2\2\2]^\3\2\2\2^_\3\2\2\2_\u00a9\7"+
		"\b\2\2`a\7\20\2\2ab\5\16\b\2bc\7\27\2\2cd\5\16\b\2de\7\r\2\2ef\5\16\b"+
		"\2fg\7\17\2\2g\u00a9\3\2\2\2hi\7\30\2\2ij\5\16\b\2jk\7\25\2\2kl\5\16\b"+
		"\2lm\7\26\2\2m\u00a9\3\2\2\2nr\7\4\2\2op\5\16\b\2pq\7\3\2\2qs\3\2\2\2"+
		"ro\3\2\2\2st\3\2\2\2tr\3\2\2\2tu\3\2\2\2uv\3\2\2\2vw\7\5\2\2w\u00a9\3"+
		"\2\2\2xy\7\24\2\2y~\5\n\6\2z{\7\7\2\2{}\5\n\6\2|z\3\2\2\2}\u0080\3\2\2"+
		"\2~|\3\2\2\2~\177\3\2\2\2\177\u0081\3\2\2\2\u0080~\3\2\2\2\u0081\u0082"+
		"\7\21\2\2\u0082\u0083\5\16\b\26\u0083\u00a9\3\2\2\2\u0084\u0085\7\31\2"+
		"\2\u0085\u0086\5\16\b\2\u0086\u008e\7\34\2\2\u0087\u0088\7\"\2\2\u0088"+
		"\u0089\7\t\2\2\u0089\u008a\7!\2\2\u008a\u008b\7$\2\2\u008b\u008c\5\16"+
		"\b\2\u008c\u008d\7\3\2\2\u008d\u008f\3\2\2\2\u008e\u0087\3\2\2\2\u008f"+
		"\u0090\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0092\3\2"+
		"\2\2\u0092\u0093\7\32\2\2\u0093\u00a9\3\2\2\2\u0094\u0095\7\33\2\2\u0095"+
		"\u00a9\7!\2\2\u0096\u0097\7,\2\2\u0097\u00a9\5\16\b\23\u0098\u0099\7\23"+
		"\2\2\u0099\u00a9\5\16\b\22\u009a\u009b\7\35\2\2\u009b\u00a9\5\16\b\n\u009c"+
		"\u009d\7\6\2\2\u009d\u009e\5\16\b\2\u009e\u009f\7\b\2\2\u009f\u00a9\3"+
		"\2\2\2\u00a0\u00a9\7\"\2\2\u00a1\u00a9\7 \2\2\u00a2\u00a9\7\37\2\2\u00a3"+
		"\u00a9\7\36\2\2\u00a4\u00a9\7\16\2\2\u00a5\u00a6\7\"\2\2\u00a6\u00a7\7"+
		"#\2\2\u00a7\u00a9\5\16\b\3\u00a8R\3\2\2\2\u00a8`\3\2\2\2\u00a8h\3\2\2"+
		"\2\u00a8n\3\2\2\2\u00a8x\3\2\2\2\u00a8\u0084\3\2\2\2\u00a8\u0094\3\2\2"+
		"\2\u00a8\u0096\3\2\2\2\u00a8\u0098\3\2\2\2\u00a8\u009a\3\2\2\2\u00a8\u009c"+
		"\3\2\2\2\u00a8\u00a0\3\2\2\2\u00a8\u00a1\3\2\2\2\u00a8\u00a2\3\2\2\2\u00a8"+
		"\u00a3\3\2\2\2\u00a8\u00a4\3\2\2\2\u00a8\u00a5\3\2\2\2\u00a9\u00d4\3\2"+
		"\2\2\u00aa\u00ab\f\21\2\2\u00ab\u00ac\7\'\2\2\u00ac\u00d3\5\16\b\22\u00ad"+
		"\u00ae\f\20\2\2\u00ae\u00af\7(\2\2\u00af\u00d3\5\16\b\21\u00b0\u00b1\f"+
		"\17\2\2\u00b1\u00b2\7%\2\2\u00b2\u00d3\5\16\b\20\u00b3\u00b4\f\16\2\2"+
		"\u00b4\u00b5\7&\2\2\u00b5\u00d3\5\16\b\17\u00b6\u00b7\f\r\2\2\u00b7\u00b8"+
		"\7)\2\2\u00b8\u00d3\5\16\b\16\u00b9\u00ba\f\f\2\2\u00ba\u00bb\7*\2\2\u00bb"+
		"\u00d3\5\16\b\r\u00bc\u00bd\f\13\2\2\u00bd\u00be\7+\2\2\u00be\u00d3\5"+
		"\16\b\f\u00bf\u00c2\f\33\2\2\u00c0\u00c1\7\n\2\2\u00c1\u00c3\7!\2\2\u00c2"+
		"\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5\7\13"+
		"\2\2\u00c5\u00c6\7\"\2\2\u00c6\u00cf\7\6\2\2\u00c7\u00cc\5\16\b\2\u00c8"+
		"\u00c9\7\7\2\2\u00c9\u00cb\5\16\b\2\u00ca\u00c8\3\2\2\2\u00cb\u00ce\3"+
		"\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce"+
		"\u00cc\3\2\2\2\u00cf\u00c7\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1\3\2"+
		"\2\2\u00d1\u00d3\7\b\2\2\u00d2\u00aa\3\2\2\2\u00d2\u00ad\3\2\2\2\u00d2"+
		"\u00b0\3\2\2\2\u00d2\u00b3\3\2\2\2\u00d2\u00b6\3\2\2\2\u00d2\u00b9\3\2"+
		"\2\2\u00d2\u00bc\3\2\2\2\u00d2\u00bf\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4"+
		"\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\17\3\2\2\2\u00d6\u00d4\3\2\2"+
		"\2\25\30\36&\62\65CELZ]t~\u0090\u00a8\u00c2\u00cc\u00cf\u00d2\u00d4";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}