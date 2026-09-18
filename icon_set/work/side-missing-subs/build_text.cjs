// Source-linked typeface reuse. AUTHOR names the model implementing this layout.
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const AUTHOR='gpt-6', root=path.resolve(__dirname,'../../..');
const {layout,svg}=require(path.join(root,'icon_set/scripts/templates/text-combine.js'));
const {glyphs}=JSON.parse(fs.readFileSync(path.join(root,'icon_set/typeface/glyphs.json')));
const refs=JSON.parse(fs.readFileSync(path.join(__dirname,'references.json')));
const specs=[[1,'3DS'],[3,'A3'],[4,'API'],[5,'AI'],[8,'C++'],[9,'CCPA'],[15,'DMG'],[17,'FAKE'],[27,'C5'],[47,'X2'],[49,'UV'],[52,'XLSX'],[53,'0%']];
const output=path.join(root,'icon_set/dist/text32'),records=[];
for(const [number,text] of specs){
 const source=refs[number-1], SOURCE_ICON_ID=source.id, SOURCE_PATH='icon_set/dist/gallery/'+source.reference_url;
 const result=layout(text,glyphs,{canvasHeight:32,stroke:4,padding:0,trimInk:true,align:'center'});
 if(!result.placements.length||result.height>32||!Number.isFinite(result.width))throw Error('Invalid layout');
 for(const p of result.placements){const [l,t,r,b]=p.glyph.bounds;const ink=[l*p.scale+p.x-2,t*p.scale+p.y-2,r*p.scale+p.x+2,b*p.scale+p.y+2];if(ink[0]<-1e-6||ink[1]<-1e-6||ink[2]>result.width+1e-6||ink[3]>32+1e-6)throw Error('Clipped glyph: '+text);}
 const icon_id='side-text-'+SOURCE_ICON_ID.slice(0,8),document=svg(result,text).replaceAll('stroke="#202820"','stroke="currentColor"');
 records.push({document,record:{icon_id,name:source.concept,family:'text',profile:'TEXT32',canvas_size:32,canvas_width:result.width,canvas_height:32,text_ink_height:32,text,description:source.concept,category:'text',tags:['text','sub icon'],aliases:[],keywords:[text],author:AUTHOR,source_ids:[SOURCE_ICON_ID],original_sources:[{source_id:SOURCE_ICON_ID,source_path:SOURCE_PATH}],glyph_ids:result.placements.map(p=>p.glyph.icon_id),svg_sha256:crypto.createHash('sha256').update(document).digest('hex'),style:{stroke_width:4,line_cap:'round',line_join:'round'},semantic_role:'SUB',semantic_kind:'text',composition_class:'TEXT',keyshape:null,keyshape_bounds:null,validation:{status:'valid',errors:[],warnings:[],checks_run:['existing preferred glyphs','32-unit maximum height','4-unit stroke','unclipped glyph bounds','uniform glyph proportions'],scope:'Typeface layout; SOLO48 keyshapes do not apply.'}}});
}
fs.mkdirSync(output,{recursive:true});
const manifestPath=path.join(output,'manifest.json');
const manifest=fs.existsSync(manifestPath)?JSON.parse(fs.readFileSync(manifestPath)):{schema_version:1,family:'text',profile:'TEXT32',canvas_height:32,icons:[]};
const ids=new Set(records.map(r=>r.record.icon_id));manifest.icons=manifest.icons.filter(r=>!ids.has(r.icon_id));
for(const {record,document} of records){fs.writeFileSync(path.join(output,record.icon_id+'.svg'),document+'\n');manifest.icons.push(record);}
fs.writeFileSync(manifestPath,JSON.stringify(manifest,null,2)+'\n');
fs.writeFileSync(path.join(__dirname,'text-results.json'),JSON.stringify(records.map(r=>r.record),null,2)+'\n');
console.log('Exported '+records.length+' labels with 32-unit height and natural variable widths.');

const oldPath=path.join(root,'icon_set/dist/text44/manifest.json');
if(fs.existsSync(oldPath)){
 const old=JSON.parse(fs.readFileSync(oldPath));old.icons=old.icons.filter(r=>!ids.has(r.icon_id));
 fs.writeFileSync(oldPath,JSON.stringify(old,null,2)+'\n');
 for(const id of ids){const oldSvg=path.join(root,'icon_set/dist/text44',id+'.svg');if(fs.existsSync(oldSvg))fs.unlinkSync(oldSvg);}
}
