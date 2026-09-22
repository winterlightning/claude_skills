const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const html = fs.readFileSync(__dirname + '/../scripts/templates/primitives.html', 'utf8');
const script = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)][0][1];
const location = {href:'http://localhost/gallery/primitives.html',search:''};
const context = vm.createContext({URL, URLSearchParams, location,
  history:{replaceState(_a,_b,url){location.href=String(url);location.search=url.search;}}});
vm.runInContext(script.slice(0, script.indexOf('\nfor(const [k,l] of Object.entries(REASONS))')), context);
const run = value => vm.runInContext(value, context);
run(`catalog.rows=[
 {uuid:'a',category:'one',state:'generated',concept:'Container'},
 {uuid:'b',category:'two',state:'todo',concept:'Side'},
 {uuid:'c',category:'two',state:'generated',concept:'Text'},
 {uuid:'d',category:'one',state:'todo',concept:'Unmarked'}
];statuses={a:{reason:'container'},b:{reason:'combination'},c:{reason:'text_number'}};
statusesAvailable=true;readURL();`);
assert.equal(run('state.view'), 'review');
assert.equal(run('detailRows().length'),4);
run("state.reason='combinations'");
assert.equal(run("detailRows().map(r=>r.uuid).join(',')"),'a,b', 'Generated and skipped classifications both remain visible');
run("state.status='generated'");
assert.equal(run("detailRows().map(r=>r.uuid).join(',')"),'a');
run("state.reason='text_number'");
assert.equal(run("detailRows().map(r=>r.uuid).join(',')"),'c');
run("state.reason='';state.status='all';state.category='two'");
assert.equal(run('detailRows().length'),2);
run("state.category='';state.status='todo';writeURL();readURL()");
assert.equal(run('state.status'),'todo','Review TODO filter survives reload');
assert.equal(run("detailRows()[0].uuid"),'d');
location.search='?view=todo';run('readURL()');
assert.equal(run('state.view'),'todo');
assert.equal(run('detailRows().length'),1);
location.search='?view=review&reason=container&status=all';run('readURL();statusesAvailable=false');
assert.equal(run('detailRows().length'),0,'Unavailable decisions are never treated as known classifications');
console.log('Review filters, generated classifications, category scope and URL persistence passed.');
