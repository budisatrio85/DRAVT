const PythonShell = require('python-shell').PythonShell;
text = "What is the capital of France?"
let options = {
  args: text.split(' ')
};
PythonShell.run('assistant_dengue.py', options).then(messages=>{
  console.log(`${messages}`);
});