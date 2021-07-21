use crate::day_18_tokeniser as tokeniser;

pub enum Node {
    Number(i64),
    OpAdd(Box<Node>, Box<Node>),
    OpMul(Box<Node>, Box<Node>),
}

fn _has_greater_than_or_eq_precendence(left: &tokeniser::Token, right: &tokeniser::Token) -> bool {
    return *left == tokeniser::Token::OpAdd || *right == tokeniser::Token::OpMul;
}

fn _parse(tokens: Vec<tokeniser::Token>) -> Vec<tokeniser::Token> {
    let token_iter = &mut tokens.into_iter().peekable();
    let mut operator_stack: Vec<tokeniser::Token> = Vec::new();
    let mut output_stack: Vec<tokeniser::Token> = Vec::new();

    while token_iter.peek().is_some() {
        let next_token = token_iter.next().unwrap();
        match next_token {
            tokeniser::Token::Number(_) => output_stack.push(next_token),
            tokeniser::Token::OpAdd | tokeniser::Token::OpMul => {
                loop {
                    let stack_top = operator_stack.last();
                    if stack_top.is_none() || *stack_top.unwrap() == tokeniser::Token::OpenParentheses {
                        break;
                    }
                    /*
                    should_shift_to_output logic:
                                      curr is Mul     curr is Add
                    stack top is Add     True           True
                    stack top is Mul     True           False
                    */
                    if _has_greater_than_or_eq_precendence(&next_token, stack_top.unwrap()) {
                        break;
                    }
                    output_stack.push(operator_stack.pop().unwrap());
                }

                operator_stack.push(next_token);
            },
            tokeniser::Token::OpenParentheses => operator_stack.push(next_token),
            tokeniser::Token::CloseParentheses => {
                loop {
                    let next = operator_stack.pop().unwrap();
                    if next == tokeniser::Token::OpenParentheses {
                        break;
                    }
                    output_stack.push(next);
                }
            },
        }
    }
    while operator_stack.len() > 0 {
        output_stack.push(operator_stack.pop().unwrap());
    }
    output_stack
}

fn _build_ast(output_stack: &mut Vec<tokeniser::Token>) -> Node {
    let current = output_stack.pop().unwrap();

    return match current {
        tokeniser::Token::Number(num_as_string) => {
            let num: i64;
            num = num_as_string.parse().unwrap();
            Node::Number(num)
        },
        tokeniser::Token::OpAdd => {
            let left = _build_ast(output_stack);
            let right = _build_ast(output_stack);
            Node::OpAdd(Box::new(left), Box::new(right))
        },
        tokeniser::Token::OpMul => {
            let left = _build_ast(output_stack);
            let right = _build_ast(output_stack);
            Node::OpMul(Box::new(left), Box::new(right))
        },
        _ => panic!("there shouldn't be another type of token on the output stack"),
    };
}

pub fn parse(tokens: Vec<tokeniser::Token>) -> Node {
    _build_ast(&mut _parse(tokens))
}
