# Lexer

## Parsing

### Token List
````rs
<KEYWORD, fn> <IDENTIFIER, simple_sum> <LPAREN, (> <IDENTIFIER, a> <TT_COLON, :>

<KEYWORD, number> <TT_COMA, ,> <IDENTIFIER, b> <TT_COLON, :> <KEYWORD, number> <RPAREN, )>

< KEYWORD, do> <KEYWORD, return> <IDENTIFIER, a> <TT_PLUS, +> <IDENTIFIER, b> <KEYWORD, end>

````

### Lang Design

````rs
fn simple_sum (a: number, b: number) do
    return a + b
end
````

