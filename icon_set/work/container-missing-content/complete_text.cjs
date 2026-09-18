// SOURCE_ICON_IDs are preserved per layout in the input and output manifests.
// AUTHOR: gpt-6; source: container-missing-content/icons.json.
const fs=require('fs'),path=require('path'),cp=require('child_process');
const root=path.resolve(__dirname,'../../..');
const {layout}=require(path.join(root,'icon_set/scripts/templates/text-combine.js'));
const {glyphs}=JSON.parse(fs.readFileSync(path.join(root,'icon_set/typeface/glyphs.json')));
const specs=[{number:7,text:'...',motif:'ellipsis',result:layout('...',glyphs,{stroke:4,padding:0,trimInk:true,tracking:16})},{number:21,text:'F',motif:'degree',result:layout('F',glyphs,{canvasHeight:32,stroke:4,padding:0,trimInk:true})},{number:19,text:'$',motif:'car',result:layout('$',glyphs,{canvasHeight:32,stroke:4,padding:0,trimInk:true})}];
cp.execFileSync('python3',[path.join(__dirname,'complete_text.py')],{input:JSON.stringify(specs),stdio:['pipe','inherit','inherit']});
