use crate::day_18_parser as parser;

pub fn evaluate(node: parser::Node) -> i64 {
    match node {
        parser::Node::Number(num) => num,
        parser::Node::OpAdd(left, right) => evaluate(*left) + evaluate(*right),
        parser::Node::OpMul(left, right) => evaluate(*left) * evaluate(*right),
    }
}
