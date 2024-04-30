#!/usr/bin/node
// Get the number of arguments passed to the script
const numArgs = process.argv.length - 2; // Subtract 2 to exclude "node" and the script name

// Check the number of arguments and print the corresponding message
if (numArgs === 0) {
  console.log('No argument');
} else if (numArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
