#[derive(PartialEq)]
pub enum Token {
    Number(String),
    OpAdd,
    OpMul,
    OpenParentheses,
    CloseParentheses,
}

pub fn tokenise(text: &str) -> Vec<Token> {
    let mut tokens = Vec::new();

    let mut i = 0;
    'outer: while i < text.len() {
        let c = text.chars().nth(i).unwrap();

        while c == ' ' {
            i += 1;
            continue 'outer;
        }
        if c == '(' {
            tokens.push(Token::OpenParentheses);
        } else if c == ')' {
            tokens.push(Token::CloseParentheses);
        } else if c == '+' {
            tokens.push(Token::OpAdd);
        } else if c == '*' {
            tokens.push(Token::OpMul);
        } else {
            let mut num_as_string = String::from("");
            num_as_string.push(c);

            loop {
                let c_or_end = text.chars().nth(i + 1);
                if i + 1 == text.len() || c_or_end.unwrap() == ' ' || c_or_end.unwrap() == ')' {
                    break;
                }
                num_as_string.push(c_or_end.unwrap());
                i += 1;
            }

            tokens.push(Token::Number(num_as_string));
        }
        i += 1;
    }

    tokens
}
