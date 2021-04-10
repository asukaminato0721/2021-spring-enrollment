//   给定一组括号，判断其配对是否正确，括号允许嵌套。
let a = "()(())()";
while (a.includes("()")) {
  a = a.replace("()", "");
}
console.log(a === "" ? "yes" : "no");
