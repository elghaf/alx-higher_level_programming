#!/usr/bin/node
// Random ps

const lang = 'C is fun';

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(lang);
  }
}
