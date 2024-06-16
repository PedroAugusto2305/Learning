// externo
const minimist = require('minimist');
const args = minimist(process.argv.slice(2));

// interno
const sum = require('./sum.js').sum;

const a = parseInt(args['a']);
const b = parseInt(args['b']);

sum(a, b);