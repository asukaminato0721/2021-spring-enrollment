/*
  鞋带的系法为依次从左边 / 右边 / 左边 / 右边穿孔。 
一个数组可以看作为一条鞋带。按照系鞋带的方式对数组进行转换。
  1,2,3,4,5,6,7,8,9,10
   转换后为 
    转换后为   1,3,5,7,9,10,8,6,4,2
*/

let a = readline()
  .split(",")
  .map((x) => +x);
// 这题过了 60%
let len = a.length;
let odd = [];
let even = [];
for (let i = 0; i < len; i++) {
  if (i % 2 === 0) {
    even.push(a[i]);
  }
  if (i % 2 === 1) {
    odd.push(a[i]);
  }
}
odd.reverse();
console.log([...even, ...odd].join(","));
