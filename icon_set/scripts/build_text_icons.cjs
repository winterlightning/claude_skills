#!/usr/bin/env node
/* Export text-family artwork using the Experiment / Typeface layout engine. */
'use strict';
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const {layout,svg}=require('./templates/text-combine.js');
const root=path.resolve(__dirname,'../..'),specPath=path.join(root,'icon_set/data/container-text-icons.json');
const spec=JSON.parse(fs.readFileSync(specPath,'utf8'));
const {glyphs}=JSON.parse(fs.readFileSync(path.join(root,spec.geometry_source),'utf8'));
const {development_assets}=JSON.parse(require('node:child_process').execFileSync(process.env.PYTHON_BIN||'python3',['-m','icon_set.scripts.workspace'],{cwd:root,encoding:'utf8'}));
const output=process.argv[2]?path.resolve(process.argv[2]):path.join(development_assets,'text28');
if(fs.existsSync(path.join(output,'..','release.json')))throw Error('Cannot write text exports into a production release.');
if(spec.family!=='text'||spec.canvas_height!==28)throw Error('Text family requires a 28-unit canvas height.');
const records=[],ids=new Set();
const mixed=spec.icons.filter(i=>i.motif).map(item=>({item,result:layout(item.text,glyphs,{canvasHeight:28,stroke:4,padding:0,trimInk:true,align:item.line_align||'center'})}));
const rendered=mixed.length?JSON.parse(require('node:child_process').execFileSync('python3',[path.join(__dirname,'build_text_motifs.py')],{input:JSON.stringify(mixed),maxBuffer:20*1024*1024,encoding:'utf8'})):[];
const motifs=new Map(mixed.map((x,i)=>[x.item.icon_id,rendered[i]]));
for(const item of spec.icons){
 if(!/^[a-z][a-z0-9-]+$/.test(item.icon_id)||ids.has(item.icon_id))throw Error('Invalid or duplicate icon ID');
 ids.add(item.icon_id);
 const result=layout(item.text,glyphs,{canvasHeight:28,stroke:4,padding:0,trimInk:true,underline:item.underline,align:item.line_align||'center'});
 if(!result.placements.length||result.height!==28||result.stroke!==4||!Number.isFinite(result.width))throw Error('Empty or invalid text export');
 for(const p of result.placements){
  const [l,t,r,b]=p.glyph.bounds,h=result.stroke/2,e=1e-7;
  if(l*p.scale+p.x-h < -e || t*p.scale+p.y-h < -e || r*p.scale+p.x+h > result.width+e || b*p.scale+p.y+h > 28+e)throw Error('Clipped glyph: '+item.icon_id);
 }
 const motif=motifs.get(item.icon_id);
 const document=motif?motif.document:svg(result,item.text).replaceAll('stroke="#202820"','stroke="currentColor"');
 const record={icon_id:item.icon_id,name:item.name,description:item.text,tags:['text','sub icon',...(item.motif?['text composition']:[]),...item.text.split(/\s+/)],aliases:[],keywords:[item.text],category:'text',family:'text',profile:motif?'TEXT_COMPOSITION':'TEXT28',canvas_size:motif?motif.height:28,canvas_width:motif?motif.width:result.width,canvas_height:motif?motif.height:28,text_ink_height:28,keyshape:null,keyshape_bounds:null,semantic_role:'SUB',semantic_kind:'text',composition_class:'TEXT',style:{stroke_width:result.stroke,line_cap:'round',line_join:'round'},text:item.text,underline:item.underline,author:item.author,source_ids:[item.source_id],original_sources:[{source_id:item.source_id,source_path:item.source_path}],glyph_ids:result.placements.map(p=>p.glyph.icon_id),svg_sha256:crypto.createHash('sha256').update(document).digest('hex'),svg_path:path.relative(path.join(root,'icon_set'),path.join(output,item.icon_id+'.svg')),validation:{status:'valid',errors:[],warnings:[],checks_run:['existing typeface glyphs','28-unit canvas height','4-unit effective stroke','glyph ink bounds','uniform aspect ratio'],scope:'Typeface layout validation; geometric icon-profile rules do not apply to text.'}};
 if(motif){record.motif=item.motif;record.composition_class='TEXT_COMPOSITION';record.description=item.name;record.validation.checks_run=['existing typeface glyphs','redrawn non-text motif','28-unit text ink height','tight combined ink bounds','4-unit effective stroke','uniform aspect ratio'];record.validation.scope='Text composition bounds; not a native SUB32 primitive.';}
 records.push({record,document});
}
// Validate the entire batch before writing its manifest or any artwork.
fs.mkdirSync(output,{recursive:true});
for(const {record,document} of records)fs.writeFileSync(path.join(output,record.icon_id+'.svg'),document+'\n');
fs.writeFileSync(path.join(output,'manifest.json'),JSON.stringify({schema_version:1,family:'text',profile:'TEXT28',canvas_height:28,geometry_policy:'existing-typeface-proportions',icons:records.map(r=>r.record)},null,2)+'\n');
console.log(`Exported ${records.length} text-family icons; lettering ink height is 28 units (mixed compositions expand to include non-text details). ${spec.unresolved.length} unresolved references recorded in ${specPath}.`);
