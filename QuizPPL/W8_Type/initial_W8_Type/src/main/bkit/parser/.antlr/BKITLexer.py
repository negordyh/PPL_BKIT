# Generated from c:\Users\Hydrogen\Downloads\BK-eL\HK201\Ass201\PPL\Ass2\initial_ass2\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u021a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\2")
        buf.write("\5\2\u0098\n\2\3\2\6\2\u009b\n\2\r\2\16\2\u009c\7\2\u009f")
        buf.write("\n\2\f\2\16\2\u00a2\13\2\3\2\3\2\3\2\3\2\3\2\3\3\6\3\u00aa")
        buf.write("\n\3\r\3\16\3\u00ab\3\3\3\3\3\4\6\4\u00b1\n\4\r\4\16\4")
        buf.write("\u00b2\3\4\7\4\u00b6\n\4\f\4\16\4\u00b9\13\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3%\3")
        buf.write("%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write("+\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3")
        buf.write(";\3<\3<\3<\5<\u0196\n<\3=\3=\7=\u019a\n=\f=\16=\u019d")
        buf.write("\13=\3=\5=\u01a0\n=\3>\3>\3>\7>\u01a5\n>\f>\16>\u01a8")
        buf.write("\13>\3>\6>\u01ab\n>\r>\16>\u01ac\3>\7>\u01b0\n>\f>\16")
        buf.write(">\u01b3\13>\3?\3?\3?\7?\u01b8\n?\f?\16?\u01bb\13?\3?\6")
        buf.write("?\u01be\n?\r?\16?\u01bf\3?\7?\u01c3\n?\f?\16?\u01c6\13")
        buf.write("?\3@\3@\5@\u01ca\n@\3@\5@\u01cd\n@\3A\3A\5A\u01d1\nA\3")
        buf.write("B\3B\5B\u01d5\nB\3B\3B\3C\3C\5C\u01db\nC\3D\3D\3D\3D\3")
        buf.write("D\7D\u01e2\nD\fD\16D\u01e5\13D\3D\3D\3D\3E\3E\3E\3F\3")
        buf.write("F\3F\3F\3F\7F\u01f2\nF\fF\16F\u01f5\13F\3F\3F\3G\3G\3")
        buf.write("G\7G\u01fc\nG\fG\16G\u01ff\13G\3G\3G\3G\5G\u0204\nG\3")
        buf.write("G\3G\3H\3H\3H\3I\3I\3I\3I\5I\u020f\nI\3I\6I\u0212\nI\r")
        buf.write("I\16I\u0213\7I\u0216\nI\fI\16I\u0219\13I\2\2J\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}")
        buf.write("@\177A\u0081\2\u0083\2\u0085B\u0087C\u0089\2\u008bD\u008d")
        buf.write("E\u008fF\u0091G\3\2\27\3\2,,\5\2\13\f\16\17\"\"\3\2c|")
        buf.write("\7\2))\62;C\\aac|\3\2\63;\3\2\62;\4\2ZZzz\3\2\62\62\4")
        buf.write("\2\63;CH\4\2\62;CH\4\2QQqq\3\2\639\3\2\629\4\2GGgg\4\2")
        buf.write("--//\7\2\n\f\16\17$$))^^\3\2))\3\2$$\t\2$$^^ddhhppttv")
        buf.write("v\n\2$$))^^ddhhppttvv\7\2\n\13\16\16$$))^^\2\u0237\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\3\u0093\3\2\2\2\5\u00a9\3\2\2\2\7\u00b0")
        buf.write("\3\2\2\2\t\u00ba\3\2\2\2\13\u00bf\3\2\2\2\r\u00c5\3\2")
        buf.write("\2\2\17\u00ce\3\2\2\2\21\u00d1\3\2\2\2\23\u00d6\3\2\2")
        buf.write("\2\25\u00dd\3\2\2\2\27\u00e5\3\2\2\2\31\u00eb\3\2\2\2")
        buf.write("\33\u00f2\3\2\2\2\35\u00fb\3\2\2\2\37\u00ff\3\2\2\2!\u0108")
        buf.write("\3\2\2\2#\u010b\3\2\2\2%\u0115\3\2\2\2\'\u011c\3\2\2\2")
        buf.write(")\u0121\3\2\2\2+\u0125\3\2\2\2-\u012b\3\2\2\2/\u0130\3")
        buf.write("\2\2\2\61\u0136\3\2\2\2\63\u013c\3\2\2\2\65\u013e\3\2")
        buf.write("\2\2\67\u0140\3\2\2\29\u0143\3\2\2\2;\u0145\3\2\2\2=\u0148")
        buf.write("\3\2\2\2?\u014a\3\2\2\2A\u014d\3\2\2\2C\u014f\3\2\2\2")
        buf.write("E\u0152\3\2\2\2G\u0154\3\2\2\2I\u0156\3\2\2\2K\u0159\3")
        buf.write("\2\2\2M\u015c\3\2\2\2O\u015f\3\2\2\2Q\u0162\3\2\2\2S\u0164")
        buf.write("\3\2\2\2U\u0166\3\2\2\2W\u0169\3\2\2\2Y\u016c\3\2\2\2")
        buf.write("[\u0170\3\2\2\2]\u0173\3\2\2\2_\u0176\3\2\2\2a\u017a\3")
        buf.write("\2\2\2c\u017e\3\2\2\2e\u0180\3\2\2\2g\u0182\3\2\2\2i\u0184")
        buf.write("\3\2\2\2k\u0186\3\2\2\2m\u0188\3\2\2\2o\u018a\3\2\2\2")
        buf.write("q\u018c\3\2\2\2s\u018e\3\2\2\2u\u0190\3\2\2\2w\u0195\3")
        buf.write("\2\2\2y\u019f\3\2\2\2{\u01a1\3\2\2\2}\u01b4\3\2\2\2\177")
        buf.write("\u01c7\3\2\2\2\u0081\u01ce\3\2\2\2\u0083\u01d2\3\2\2\2")
        buf.write("\u0085\u01da\3\2\2\2\u0087\u01dc\3\2\2\2\u0089\u01e9\3")
        buf.write("\2\2\2\u008b\u01ec\3\2\2\2\u008d\u01f8\3\2\2\2\u008f\u0207")
        buf.write("\3\2\2\2\u0091\u020a\3\2\2\2\u0093\u0094\7,\2\2\u0094")
        buf.write("\u0095\7,\2\2\u0095\u00a0\3\2\2\2\u0096\u0098\7,\2\2\u0097")
        buf.write("\u0096\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u009a\3\2\2\2")
        buf.write("\u0099\u009b\n\2\2\2\u009a\u0099\3\2\2\2\u009b\u009c\3")
        buf.write("\2\2\2\u009c\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009f")
        buf.write("\3\2\2\2\u009e\u0097\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0")
        buf.write("\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a3\3\2\2\2")
        buf.write("\u00a2\u00a0\3\2\2\2\u00a3\u00a4\7,\2\2\u00a4\u00a5\7")
        buf.write(",\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\b\2\2\2\u00a7\4")
        buf.write("\3\2\2\2\u00a8\u00aa\t\3\2\2\u00a9\u00a8\3\2\2\2\u00aa")
        buf.write("\u00ab\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2")
        buf.write("\u00ac\u00ad\3\2\2\2\u00ad\u00ae\b\3\2\2\u00ae\6\3\2\2")
        buf.write("\2\u00af\u00b1\t\4\2\2\u00b0\u00af\3\2\2\2\u00b1\u00b2")
        buf.write("\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3")
        buf.write("\u00b7\3\2\2\2\u00b4\u00b6\t\5\2\2\u00b5\u00b4\3\2\2\2")
        buf.write("\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3")
        buf.write("\2\2\2\u00b8\b\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00bb")
        buf.write("\7D\2\2\u00bb\u00bc\7q\2\2\u00bc\u00bd\7f\2\2\u00bd\u00be")
        buf.write("\7{\2\2\u00be\n\3\2\2\2\u00bf\u00c0\7D\2\2\u00c0\u00c1")
        buf.write("\7t\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4")
        buf.write("\7m\2\2\u00c4\f\3\2\2\2\u00c5\u00c6\7E\2\2\u00c6\u00c7")
        buf.write("\7q\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca")
        buf.write("\7k\2\2\u00ca\u00cb\7p\2\2\u00cb\u00cc\7w\2\2\u00cc\u00cd")
        buf.write("\7g\2\2\u00cd\16\3\2\2\2\u00ce\u00cf\7F\2\2\u00cf\u00d0")
        buf.write("\7q\2\2\u00d0\20\3\2\2\2\u00d1\u00d2\7G\2\2\u00d2\u00d3")
        buf.write("\7n\2\2\u00d3\u00d4\7u\2\2\u00d4\u00d5\7g\2\2\u00d5\22")
        buf.write("\3\2\2\2\u00d6\u00d7\7G\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9")
        buf.write("\7u\2\2\u00d9\u00da\7g\2\2\u00da\u00db\7K\2\2\u00db\u00dc")
        buf.write("\7h\2\2\u00dc\24\3\2\2\2\u00dd\u00de\7G\2\2\u00de\u00df")
        buf.write("\7p\2\2\u00df\u00e0\7f\2\2\u00e0\u00e1\7D\2\2\u00e1\u00e2")
        buf.write("\7q\2\2\u00e2\u00e3\7f\2\2\u00e3\u00e4\7{\2\2\u00e4\26")
        buf.write("\3\2\2\2\u00e5\u00e6\7G\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8")
        buf.write("\7f\2\2\u00e8\u00e9\7K\2\2\u00e9\u00ea\7h\2\2\u00ea\30")
        buf.write("\3\2\2\2\u00eb\u00ec\7G\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee")
        buf.write("\7f\2\2\u00ee\u00ef\7H\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1")
        buf.write("\7t\2\2\u00f1\32\3\2\2\2\u00f2\u00f3\7G\2\2\u00f3\u00f4")
        buf.write("\7p\2\2\u00f4\u00f5\7f\2\2\u00f5\u00f6\7Y\2\2\u00f6\u00f7")
        buf.write("\7j\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9\7n\2\2\u00f9\u00fa")
        buf.write("\7g\2\2\u00fa\34\3\2\2\2\u00fb\u00fc\7H\2\2\u00fc\u00fd")
        buf.write("\7q\2\2\u00fd\u00fe\7t\2\2\u00fe\36\3\2\2\2\u00ff\u0100")
        buf.write("\7H\2\2\u0100\u0101\7w\2\2\u0101\u0102\7p\2\2\u0102\u0103")
        buf.write("\7e\2\2\u0103\u0104\7v\2\2\u0104\u0105\7k\2\2\u0105\u0106")
        buf.write("\7q\2\2\u0106\u0107\7p\2\2\u0107 \3\2\2\2\u0108\u0109")
        buf.write("\7K\2\2\u0109\u010a\7h\2\2\u010a\"\3\2\2\2\u010b\u010c")
        buf.write("\7R\2\2\u010c\u010d\7c\2\2\u010d\u010e\7t\2\2\u010e\u010f")
        buf.write("\7c\2\2\u010f\u0110\7o\2\2\u0110\u0111\7g\2\2\u0111\u0112")
        buf.write("\7v\2\2\u0112\u0113\7g\2\2\u0113\u0114\7t\2\2\u0114$\3")
        buf.write("\2\2\2\u0115\u0116\7T\2\2\u0116\u0117\7g\2\2\u0117\u0118")
        buf.write("\7v\2\2\u0118\u0119\7w\2\2\u0119\u011a\7t\2\2\u011a\u011b")
        buf.write("\7p\2\2\u011b&\3\2\2\2\u011c\u011d\7V\2\2\u011d\u011e")
        buf.write("\7j\2\2\u011e\u011f\7g\2\2\u011f\u0120\7p\2\2\u0120(\3")
        buf.write("\2\2\2\u0121\u0122\7X\2\2\u0122\u0123\7c\2\2\u0123\u0124")
        buf.write("\7t\2\2\u0124*\3\2\2\2\u0125\u0126\7Y\2\2\u0126\u0127")
        buf.write("\7j\2\2\u0127\u0128\7k\2\2\u0128\u0129\7n\2\2\u0129\u012a")
        buf.write("\7g\2\2\u012a,\3\2\2\2\u012b\u012c\7V\2\2\u012c\u012d")
        buf.write("\7t\2\2\u012d\u012e\7w\2\2\u012e\u012f\7g\2\2\u012f.\3")
        buf.write("\2\2\2\u0130\u0131\7H\2\2\u0131\u0132\7c\2\2\u0132\u0133")
        buf.write("\7n\2\2\u0133\u0134\7u\2\2\u0134\u0135\7g\2\2\u0135\60")
        buf.write("\3\2\2\2\u0136\u0137\7G\2\2\u0137\u0138\7p\2\2\u0138\u0139")
        buf.write("\7f\2\2\u0139\u013a\7F\2\2\u013a\u013b\7q\2\2\u013b\62")
        buf.write("\3\2\2\2\u013c\u013d\7?\2\2\u013d\64\3\2\2\2\u013e\u013f")
        buf.write("\7-\2\2\u013f\66\3\2\2\2\u0140\u0141\7-\2\2\u0141\u0142")
        buf.write("\7\60\2\2\u01428\3\2\2\2\u0143\u0144\7/\2\2\u0144:\3\2")
        buf.write("\2\2\u0145\u0146\7/\2\2\u0146\u0147\7\60\2\2\u0147<\3")
        buf.write("\2\2\2\u0148\u0149\7,\2\2\u0149>\3\2\2\2\u014a\u014b\7")
        buf.write(",\2\2\u014b\u014c\7\60\2\2\u014c@\3\2\2\2\u014d\u014e")
        buf.write("\7^\2\2\u014eB\3\2\2\2\u014f\u0150\7^\2\2\u0150\u0151")
        buf.write("\7\60\2\2\u0151D\3\2\2\2\u0152\u0153\7\'\2\2\u0153F\3")
        buf.write("\2\2\2\u0154\u0155\7#\2\2\u0155H\3\2\2\2\u0156\u0157\7")
        buf.write("(\2\2\u0157\u0158\7(\2\2\u0158J\3\2\2\2\u0159\u015a\7")
        buf.write("~\2\2\u015a\u015b\7~\2\2\u015bL\3\2\2\2\u015c\u015d\7")
        buf.write("?\2\2\u015d\u015e\7?\2\2\u015eN\3\2\2\2\u015f\u0160\7")
        buf.write("#\2\2\u0160\u0161\7?\2\2\u0161P\3\2\2\2\u0162\u0163\7")
        buf.write(">\2\2\u0163R\3\2\2\2\u0164\u0165\7@\2\2\u0165T\3\2\2\2")
        buf.write("\u0166\u0167\7>\2\2\u0167\u0168\7?\2\2\u0168V\3\2\2\2")
        buf.write("\u0169\u016a\7@\2\2\u016a\u016b\7?\2\2\u016bX\3\2\2\2")
        buf.write("\u016c\u016d\7?\2\2\u016d\u016e\7\61\2\2\u016e\u016f\7")
        buf.write("?\2\2\u016fZ\3\2\2\2\u0170\u0171\7>\2\2\u0171\u0172\7")
        buf.write("\60\2\2\u0172\\\3\2\2\2\u0173\u0174\7@\2\2\u0174\u0175")
        buf.write("\7\60\2\2\u0175^\3\2\2\2\u0176\u0177\7>\2\2\u0177\u0178")
        buf.write("\7?\2\2\u0178\u0179\7\60\2\2\u0179`\3\2\2\2\u017a\u017b")
        buf.write("\7@\2\2\u017b\u017c\7?\2\2\u017c\u017d\7\60\2\2\u017d")
        buf.write("b\3\2\2\2\u017e\u017f\7*\2\2\u017fd\3\2\2\2\u0180\u0181")
        buf.write("\7+\2\2\u0181f\3\2\2\2\u0182\u0183\7}\2\2\u0183h\3\2\2")
        buf.write("\2\u0184\u0185\7\177\2\2\u0185j\3\2\2\2\u0186\u0187\7")
        buf.write("]\2\2\u0187l\3\2\2\2\u0188\u0189\7_\2\2\u0189n\3\2\2\2")
        buf.write("\u018a\u018b\7=\2\2\u018bp\3\2\2\2\u018c\u018d\7.\2\2")
        buf.write("\u018dr\3\2\2\2\u018e\u018f\7<\2\2\u018ft\3\2\2\2\u0190")
        buf.write("\u0191\7\60\2\2\u0191v\3\2\2\2\u0192\u0196\5y=\2\u0193")
        buf.write("\u0196\5{>\2\u0194\u0196\5}?\2\u0195\u0192\3\2\2\2\u0195")
        buf.write("\u0193\3\2\2\2\u0195\u0194\3\2\2\2\u0196x\3\2\2\2\u0197")
        buf.write("\u019b\t\6\2\2\u0198\u019a\t\7\2\2\u0199\u0198\3\2\2\2")
        buf.write("\u019a\u019d\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019c\3")
        buf.write("\2\2\2\u019c\u01a0\3\2\2\2\u019d\u019b\3\2\2\2\u019e\u01a0")
        buf.write("\7\62\2\2\u019f\u0197\3\2\2\2\u019f\u019e\3\2\2\2\u01a0")
        buf.write("z\3\2\2\2\u01a1\u01a2\7\62\2\2\u01a2\u01a6\t\b\2\2\u01a3")
        buf.write("\u01a5\t\t\2\2\u01a4\u01a3\3\2\2\2\u01a5\u01a8\3\2\2\2")
        buf.write("\u01a6\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01aa\3")
        buf.write("\2\2\2\u01a8\u01a6\3\2\2\2\u01a9\u01ab\t\n\2\2\u01aa\u01a9")
        buf.write("\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac")
        buf.write("\u01ad\3\2\2\2\u01ad\u01b1\3\2\2\2\u01ae\u01b0\t\13\2")
        buf.write("\2\u01af\u01ae\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af")
        buf.write("\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2|\3\2\2\2\u01b3\u01b1")
        buf.write("\3\2\2\2\u01b4\u01b5\7\62\2\2\u01b5\u01b9\t\f\2\2\u01b6")
        buf.write("\u01b8\t\t\2\2\u01b7\u01b6\3\2\2\2\u01b8\u01bb\3\2\2\2")
        buf.write("\u01b9\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bd\3")
        buf.write("\2\2\2\u01bb\u01b9\3\2\2\2\u01bc\u01be\t\r\2\2\u01bd\u01bc")
        buf.write("\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf")
        buf.write("\u01c0\3\2\2\2\u01c0\u01c4\3\2\2\2\u01c1\u01c3\t\16\2")
        buf.write("\2\u01c2\u01c1\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4\u01c2")
        buf.write("\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5~\3\2\2\2\u01c6\u01c4")
        buf.write("\3\2\2\2\u01c7\u01c9\5w<\2\u01c8\u01ca\5\u0081A\2\u01c9")
        buf.write("\u01c8\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cc\3\2\2\2")
        buf.write("\u01cb\u01cd\5\u0083B\2\u01cc\u01cb\3\2\2\2\u01cc\u01cd")
        buf.write("\3\2\2\2\u01cd\u0080\3\2\2\2\u01ce\u01d0\7\60\2\2\u01cf")
        buf.write("\u01d1\5y=\2\u01d0\u01cf\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1")
        buf.write("\u0082\3\2\2\2\u01d2\u01d4\t\17\2\2\u01d3\u01d5\t\20\2")
        buf.write("\2\u01d4\u01d3\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d6")
        buf.write("\3\2\2\2\u01d6\u01d7\5y=\2\u01d7\u0084\3\2\2\2\u01d8\u01db")
        buf.write("\5-\27\2\u01d9\u01db\5/\30\2\u01da\u01d8\3\2\2\2\u01da")
        buf.write("\u01d9\3\2\2\2\u01db\u0086\3\2\2\2\u01dc\u01e3\7$\2\2")
        buf.write("\u01dd\u01e2\5\u0089E\2\u01de\u01e2\n\21\2\2\u01df\u01e0")
        buf.write("\t\22\2\2\u01e0\u01e2\t\23\2\2\u01e1\u01dd\3\2\2\2\u01e1")
        buf.write("\u01de\3\2\2\2\u01e1\u01df\3\2\2\2\u01e2\u01e5\3\2\2\2")
        buf.write("\u01e3\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e6\3")
        buf.write("\2\2\2\u01e5\u01e3\3\2\2\2\u01e6\u01e7\7$\2\2\u01e7\u01e8")
        buf.write("\bD\3\2\u01e8\u0088\3\2\2\2\u01e9\u01ea\7^\2\2\u01ea\u01eb")
        buf.write("\t\24\2\2\u01eb\u008a\3\2\2\2\u01ec\u01f3\7$\2\2\u01ed")
        buf.write("\u01f2\5\u0089E\2\u01ee\u01f2\n\21\2\2\u01ef\u01f0\t\22")
        buf.write("\2\2\u01f0\u01f2\t\23\2\2\u01f1\u01ed\3\2\2\2\u01f1\u01ee")
        buf.write("\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f2\u01f5\3\2\2\2\u01f3")
        buf.write("\u01f1\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f6\3\2\2\2")
        buf.write("\u01f5\u01f3\3\2\2\2\u01f6\u01f7\bF\4\2\u01f7\u008c\3")
        buf.write("\2\2\2\u01f8\u01fd\7$\2\2\u01f9\u01fc\5\u0089E\2\u01fa")
        buf.write("\u01fc\n\21\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fa\3\2\2")
        buf.write("\2\u01fc\u01ff\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fe")
        buf.write("\3\2\2\2\u01fe\u0203\3\2\2\2\u01ff\u01fd\3\2\2\2\u0200")
        buf.write("\u0201\7^\2\2\u0201\u0204\n\25\2\2\u0202\u0204\t\26\2")
        buf.write("\2\u0203\u0200\3\2\2\2\u0203\u0202\3\2\2\2\u0204\u0205")
        buf.write("\3\2\2\2\u0205\u0206\bG\5\2\u0206\u008e\3\2\2\2\u0207")
        buf.write("\u0208\13\2\2\2\u0208\u0209\bH\6\2\u0209\u0090\3\2\2\2")
        buf.write("\u020a\u020b\7,\2\2\u020b\u020c\7,\2\2\u020c\u0217\3\2")
        buf.write("\2\2\u020d\u020f\7,\2\2\u020e\u020d\3\2\2\2\u020e\u020f")
        buf.write("\3\2\2\2\u020f\u0211\3\2\2\2\u0210\u0212\n\2\2\2\u0211")
        buf.write("\u0210\3\2\2\2\u0212\u0213\3\2\2\2\u0213\u0211\3\2\2\2")
        buf.write("\u0213\u0214\3\2\2\2\u0214\u0216\3\2\2\2\u0215\u020e\3")
        buf.write("\2\2\2\u0216\u0219\3\2\2\2\u0217\u0215\3\2\2\2\u0217\u0218")
        buf.write("\3\2\2\2\u0218\u0092\3\2\2\2\u0219\u0217\3\2\2\2!\2\u0097")
        buf.write("\u009c\u00a0\u00ab\u00b2\u00b7\u0195\u019b\u019f\u01a6")
        buf.write("\u01ac\u01b1\u01b9\u01bf\u01c4\u01c9\u01cc\u01d0\u01d4")
        buf.write("\u01da\u01e1\u01e3\u01f1\u01f3\u01fb\u01fd\u0203\u020e")
        buf.write("\u0213\u0217\7\b\2\2\3D\2\3F\3\3G\4\3H\5")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BLOCKCOM = 1
    WS = 2
    ID = 3
    BODY = 4
    BREAK = 5
    CONTINUE = 6
    DO = 7
    ELSE = 8
    ELSEIF = 9
    ENDBODY = 10
    ENDIF = 11
    ENDFOR = 12
    ENDWHILE = 13
    FOR = 14
    FUNCTION = 15
    IF = 16
    PARAMETER = 17
    RETURN = 18
    THEN = 19
    VAR = 20
    WHILE = 21
    TRUE = 22
    FALSE = 23
    ENDDO = 24
    ASSIGN = 25
    ADD = 26
    ADD_DOT = 27
    SUB = 28
    SUB_DOT = 29
    MUL = 30
    MUL_DOT = 31
    DIV = 32
    DIV_DOT = 33
    MOD = 34
    NOT = 35
    AND = 36
    OR = 37
    EQ = 38
    NOT_EQ_INT = 39
    LT = 40
    GT = 41
    LTE = 42
    GTE = 43
    NOT_EQ_FLOAT = 44
    LT_DOT = 45
    GT_DOT = 46
    LTE_DOT = 47
    GTE_DOT = 48
    LB = 49
    RB = 50
    LP = 51
    RP = 52
    LSB = 53
    RSB = 54
    SEMI = 55
    COMMA = 56
    COLON = 57
    DOT = 58
    INTLIT = 59
    DEC = 60
    Hexa = 61
    Octal = 62
    FLOATLIT = 63
    BOOLEAN = 64
    STRINGLIT = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67
    ERROR_CHAR = 68
    UNTERMINATED_COMMENT = 69

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
            "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'True'", "'False'", "'EndDo'", "'='", "'+'", "'+.'", "'-'", 
            "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", 
            "'<.'", "'>.'", "'<=.'", "'>=.'", "'('", "')'", "'{'", "'}'", 
            "'['", "']'", "';'", "','", "':'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "BLOCKCOM", "WS", "ID", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
            "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
            "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "TRUE", 
            "FALSE", "ENDDO", "ASSIGN", "ADD", "ADD_DOT", "SUB", "SUB_DOT", 
            "MUL", "MUL_DOT", "DIV", "DIV_DOT", "MOD", "NOT", "AND", "OR", 
            "EQ", "NOT_EQ_INT", "LT", "GT", "LTE", "GTE", "NOT_EQ_FLOAT", 
            "LT_DOT", "GT_DOT", "LTE_DOT", "GTE_DOT", "LB", "RB", "LP", 
            "RP", "LSB", "RSB", "SEMI", "COMMA", "COLON", "DOT", "INTLIT", 
            "DEC", "Hexa", "Octal", "FLOATLIT", "BOOLEAN", "STRINGLIT", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "BLOCKCOM", "WS", "ID", "BODY", "BREAK", "CONTINUE", "DO", 
                  "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", 
                  "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", 
                  "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", "ASSIGN", "ADD", 
                  "ADD_DOT", "SUB", "SUB_DOT", "MUL", "MUL_DOT", "DIV", 
                  "DIV_DOT", "MOD", "NOT", "AND", "OR", "EQ", "NOT_EQ_INT", 
                  "LT", "GT", "LTE", "GTE", "NOT_EQ_FLOAT", "LT_DOT", "GT_DOT", 
                  "LTE_DOT", "GTE_DOT", "LB", "RB", "LP", "RP", "LSB", "RSB", 
                  "SEMI", "COMMA", "COLON", "DOT", "INTLIT", "DEC", "Hexa", 
                  "Octal", "FLOATLIT", "FLDECIMAL", "FLEXPONENT", "BOOLEAN", 
                  "STRINGLIT", "ESC", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[66] = self.STRINGLIT_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
            actions[70] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.text = self.text[1:-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise ErrorToken(self.text)

     


