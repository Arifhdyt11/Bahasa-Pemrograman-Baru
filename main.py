from lexer import Lexer
from aparser import Parser


def main():
    filename = 'contoh.code'
    file = open(filename, 'r')
    lexer = Lexer(file)
    parser = Parser(lexer.tokens)

    lexer.tokenizer()
    print("TOKENS:")
    print(lexer.tokens, "\n")

    parser.build_AST()
    print("AST:")
    print(parser.AST, "\n")


if __name__ == "__main__":
    main()