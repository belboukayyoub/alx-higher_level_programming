#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};
for (const userId in dict) {
  if (Object.hasOwnProperty.call(dict, userId)) {
    const occurrences = dict[userId];
    if (newDict[occurrences]) {
      newDict[occurrences].push(userId);
    } else {
      newDict[occurrences] = [userId];
    }
  }
}
console.log(newDict);
