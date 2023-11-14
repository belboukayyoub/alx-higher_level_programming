#!/usr/bin/node
function factorial (n) {
  if (isNaN(Number(n)) || n <= 0) return 1;

  return n * factorial(n - 1);
}

console.log(factorial(Number(process.argv[2])));
