// Existing-glyph layouts for this source-linked batch; no replacement glyphs.
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const root=path.resolve(__dirname,'../../..');
const {layout,svg}=require(path.join(root,'icon_set/scripts/templates/text-combine.js'));
const {glyphs}=JSON.parse(fs.readFileSync(path.join(root,'icon_set/typeface/glyphs.json')));
const refs=JSON.parse(fs.readFileSync(path.join(__dirname,'icons.json')));
const specs=[[1,'?'],[2,'∈'],[3,'%'],[14,'¥'],[21,'°F'],[31,'ॐ'],[38,'PM\n2.5'],[39,'T'],[41,'+\n-'],[43,'16:9']];
const records=[],unresolved=[];const output=path.join(__dirname,'generated-text');fs.mkdirSync(output,{recursive:true});
for(const [number,text] of specs){
 const source=refs[number-1];
 try{
  const result=layout(text,glyphs,{canvasHeight:number===39?20:44,stroke:4,padding:0,trimInk:true,align:'center'});
  if(number===39){result.width=44;result.height=44;result.decorations.push({kind:'paragraph-line',x1:2,x2:42,y:30},{kind:'paragraph-line',x1:2,x2:42,y:42});}
  for(const p of result.placements){const [l,t,r,b]=p.glyph.bounds;const ink=[l*p.scale+p.x-2,t*p.scale+p.y-2,r*p.scale+p.x+2,b*p.scale+p.y+2];if(ink[0]<-1e-6||ink[1]<-1e-6||ink[2]>result.width+1e-6||ink[3]>44+1e-6)throw Error('Clipped glyph');}
  const icon_id='container-content-text-'+source.id.slice(0,8),document=svg(result,text);
  fs.writeFileSync(path.join(output,icon_id+'.svg'),document+'\n');
  records.push({icon_id,number,name:source.name,text,source_id:source.id,source_path:source.reference,author:'gpt-6',width:result.width,height:result.height,stroke:4,glyph_ids:result.placements.map(p=>p.glyph.icon_id),line_scales:result.placements.map(p=>p.scale),file:icon_id+'.svg',validation:'Existing glyphs; total ink bounds at most 44 units high; effective stroke 4; natural proportions preserved.'});
 }catch(e){unresolved.push({number,name:source.name,source_id:source.id,text,reason:e.message});}
}
fs.writeFileSync(path.join(output,'manifest.json'),JSON.stringify({icons:records,unresolved},null,2)+'\n');
const published=path.join(root,'icon_set/dist/text44');fs.mkdirSync(published,{recursive:true});
const icons=records.map(r=>{
 const document=fs.readFileSync(path.join(output,r.file),'utf8');fs.writeFileSync(path.join(published,r.file),document);
 return {icon_id:r.icon_id,name:r.name,family:'text',profile:'TEXT44',canvas_size:44,canvas_width:r.width,canvas_height:44,text:r.text,description:r.name,category:'text',tags:['text','sub icon'],aliases:[],keywords:[r.text],author:r.author,source_ids:[r.source_id],original_sources:[{source_id:r.source_id,source_path:path.relative(root,r.source_path)}],glyph_ids:r.glyph_ids,svg_sha256:crypto.createHash('sha256').update(document).digest('hex'),style:{stroke_width:4,line_cap:'round',line_join:'round'},semantic_role:'SUB',semantic_kind:'text',composition_class:'TEXT',keyshape:null,keyshape_bounds:null,validation:{status:'valid',errors:[],warnings:[],checks_run:['existing glyphs','44-unit ink bounds','4-unit stroke'],scope:'Typeface layout; not SOLO48 geometric validation.'}};
});
fs.writeFileSync(path.join(published,'manifest.json'),JSON.stringify({schema_version:1,family:'text',profile:'TEXT44',canvas_height:44,icons},null,2)+'\n');
console.log(JSON.stringify({generated:records.length,unresolved},null,2));
