// Run with: node icon_set/tests/test_progression_container_main.cjs
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const context = vm.createContext({});
vm.runInContext(fs.readFileSync(__dirname + '/../scripts/templates/progression-combinations.js', 'utf8'), context);
const run = source => vm.runInContext(source, context);
run(`
const solo={icon_id:'old-solo',key:'solo/old-solo'};
const container={icon_id:'native',key:'container/native'};
combinationCatalog={references:{main:{generated:[solo]},sub:{generated:[{key:'sub/plus'}]},pair:{generated:[]}}};
const row={kind:'container',id:'pair',main_id:'main',sub_id:'sub'};
`);
assert.equal(run('combinationMain(row).generated.length'), 0, 'Legacy solo link is not a container main');
assert.equal(run('combinationState(row)'), 'partial');
run('row.main_generated=[container]');
assert.equal(run('combinationState(row)'), 'ready');
assert.equal(run('combinationMain(row).generated[0].icon_id'), 'native');
assert.equal(run('combinationCatalog.references.main.generated[0].icon_id'), 'old-solo', 'Shared source is preserved');
run('row.main_generated=[];combinationCatalog.references.main.generated.push(container)');
assert.equal(run('combinationState(row)'), 'partial', 'An unavailable mapped build does not fall back');
run("row.kind='side'");
assert.equal(run('combinationMain(row).generated.length'), 2, 'Side roles retain their artwork');
console.log('Container main family, coverage, and role isolation checks passed.');
run(`
combinationCatalog.references.other={concept:'Alias',generated:[]};
combinationCatalog.references.main.concept='Main';
const groupRows=[
 {kind:'container',main_id:'main',main_icon_id:'window',main_generated:[container]},
 {kind:'container',main_id:'other',main_icon_id:'window',main_generated:[container]},
 {kind:'container',main_id:'main',main_icon_id:'badge',main_generated:[container]},
 {kind:'container',main_id:'main',main_generated:[]},
 {kind:'container',main_id:'other',main_generated:[]}
];
`);
assert.equal(run('containerGroups(groupRows).length'),4);
assert.equal(run("containerGroups(groupRows).find(g=>g.iconId==='window').rows.length"),2);
assert.equal(run('containerGroups(groupRows).reduce((n,g)=>n+g.rows.length,0)'),5);
assert.equal(run('containerGroups(groupRows)[0].title'),'Alias');
console.log('Container grouping, shared mappings, and missing-main isolation checks passed.');
