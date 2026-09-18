const fs=require('fs'),path=require('path');const root=process.cwd(),dir=__dirname;
const {layout,svg}=require(path.join(root,'icon_set/scripts/templates/text-combine.js'));
const {glyphs}=JSON.parse(fs.readFileSync('icon_set/typeface/glyphs.json'));
const rows=JSON.parse(fs.readFileSync(path.join(dir,'before-audit.json'))).filter(x=>x.attention);
const metas={};for(const folder of ['text28','text32','text44']){const file=`icon_set/dist/${folder}/manifest.json`;if(fs.existsSync(file))for(const m of JSON.parse(fs.readFileSync(file)).icons)metas[m.icon_id]=m;}
const specs=[];for(const r of rows){const id=r.key.split('/')[1],m=metas[id];if(!m)throw Error(id);const underline=['text-mercury-chemical-symbol-8f36140b','text-silver-chemical-element-symbol-a8aa1719','text-underlined-letters-rg-a2b4d767'].includes(id);
const text=m.text.replace(/\s*\n\s*/g,' ').trim();const result=layout(text,glyphs,{canvasHeight:underline?26:32,stroke:4,padding:0,trimInk:true,tracking:12});
fs.writeFileSync(path.join(dir,id+'.raw.svg'),svg(result,text));specs.push({id,key:r.key,name:r.name,text,underline,source:r.source,old:r.export,glyph_ids:m.glyph_ids});}
fs.writeFileSync(path.join(dir,'specs.json'),JSON.stringify(specs,null,2));
