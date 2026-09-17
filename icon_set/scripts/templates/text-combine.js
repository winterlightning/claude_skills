(function(root){
'use strict';
function layout(text,glyphs,{xHeight=36,capHeight=52,tracking=6,lineGap=16,stroke=4,padding=16,underline=false,strikethrough=false,canvasHeight=null,align='left',trimInk=false}={}){
  if(![xHeight,capHeight,tracking,lineGap,stroke,padding].every(Number.isFinite)||xHeight<=0||capHeight<=0||tracking<0||lineGap<0||stroke<=0||padding<0)throw Error('Invalid text dimensions.');
  if(canvasHeight!==null){
    if(!Number.isFinite(canvasHeight)||canvasHeight<=0)throw Error('Invalid canvas height.');
    // Fit geometry and spacing, keeping stroke in final canvas units.
    const measure=factor=>layout(text,glyphs,{xHeight:xHeight*factor,capHeight:capHeight*factor,tracking:tracking*factor,lineGap:lineGap*factor,padding:padding*factor,stroke,underline,strikethrough,align,trimInk});
    let low=1e-9,high=1;
    if(measure(low).height>=canvasHeight)throw Error('This stroke and line count cannot fit the locked canvas height.');
    while(measure(high).height<canvasHeight)high*=2;
    for(let i=0;i<60;i++){
      const mid=(low+high)/2;
      if(measure(mid).height>canvasHeight)high=mid;else low=mid;
    }
    const fitted=measure(low);fitted.height=canvasHeight;
    return fitted;
  }
  text=text.replace(/\r\n?/g,'\n');
  if(text.length>200)throw Error('Please use 200 characters or fewer.');
  const map=new Map(glyphs.filter(g=>g.preferred).map(g=>[g.character,g]));
  const missing=[...new Set([...text].filter(c=>c!==' '&&c!=='\n'&&!map.has(c)))];
  if(missing.length)throw Error('Unsupported characters: '+missing.map(c=>JSON.stringify(c)).join(', ')+'. Use uppercase or lowercase letters, digits, keyboard punctuation, spaces and line breaks.');
  let top=-capHeight-stroke/2,bottom=stroke/2;
  const placements=[],lines=[];
  for(const [lineIndex,lineText] of text.split('\n').entries()){
    let cursor=0,hasGlyphs=false;
    for(const c of lineText){
      if(c===' '){cursor+=xHeight*.55;continue;}
      hasGlyphs=true;
      const g=map.get(c),scale=(g.kind==='digit'||g.kind==='uppercase'?capHeight:xHeight)/g.body_height;
      const width=(g.bounds[2]-g.bounds[0])*scale+stroke;
      const x=cursor+stroke/2-g.bounds[0]*scale,y=-g.baseline*scale;
      top=Math.min(top,g.bounds[1]*scale+y-stroke/2);
      bottom=Math.max(bottom,g.bounds[3]*scale+y+stroke/2);
      placements.push({glyph:g,scale,x,y,width,lineIndex});
      cursor+=width+tracking;
    }
    if(lineText.length&&lineText.at(-1)!==' ')cursor-=tracking;
    lines.push({width:cursor,hasGlyphs});
  }
  // Keep the underline clear of descenders and include it in the line box.
  const underlineY=bottom+Math.max(stroke,xHeight*.12)+stroke/2;
  if(underline&&placements.length)bottom=underlineY+stroke/2;
  const decorations=[];
  // Use a shared line box covering all ascenders, dots and descenders.
  // Empty lines keep their full advance and every line starts at the same left edge.
  const offset=padding-top,lineAdvance=bottom-top+lineGap;
  for(const [index,line] of lines.entries()){
    line.baseline=offset+index*lineAdvance;
    line.bodyTop=line.baseline-xHeight;
    if(line.hasGlyphs){
      const x1=padding+stroke/2,x2=padding+line.width-stroke/2;
      if(underline)decorations.push({kind:'underline',x1,x2,y:line.baseline+underlineY,lineIndex:index});
      if(strikethrough)decorations.push({kind:'strikethrough',x1,x2,y:line.baseline-xHeight/2,lineIndex:index});
    }
  }
  for(const p of placements){p.x+=padding;p.y+=lines[p.lineIndex].baseline;}
  const result={placements,lines,decorations,lineAdvance,width:Math.max(2*padding+Math.max(...lines.map(l=>l.width)),2*padding+1),height:bottom-top+2*padding+(lines.length-1)*lineAdvance,baseline:offset,bodyTop:offset-xHeight,stroke};
  if(!['left','center','right'].includes(align))throw Error('Invalid line alignment.');
  if(align!=='left'){
    const longest=Math.max(...lines.map(l=>l.width));
    for(let i=0;i<lines.length;i++){
      const shift=(longest-lines[i].width)/(align==='center'?2:1);
      for(const p of placements)if(p.lineIndex===i)p.x+=shift;
      for(const d of decorations)if(d.lineIndex===i){d.x1+=shift;d.x2+=shift;}
    }
  }
  if(trimInk&&placements.length){
    const half=stroke/2,boxes=placements.map(p=>{
      const [l,t,r,b]=p.glyph.bounds;
      return [l*p.scale+p.x-half,t*p.scale+p.y-half,r*p.scale+p.x+half,b*p.scale+p.y+half];
    });
    for(const d of decorations)boxes.push([d.x1-half,d.y-half,d.x2+half,d.y+half]);
    const left=Math.min(...boxes.map(b=>b[0])),top=Math.min(...boxes.map(b=>b[1]));
    const right=Math.max(...boxes.map(b=>b[2])),bottom=Math.max(...boxes.map(b=>b[3]));
    for(const p of placements){p.x-=left;p.y-=top;}
    for(const line of lines){line.baseline-=top;line.bodyTop-=top;}
    for(const d of decorations){d.x1-=left;d.x2-=left;d.y-=top;}
    result.baseline-=top;result.bodyTop-=top;
    result.width=right-left;result.height=bottom-top;
  }
  return result;
}
function escapeXML(s){return s.replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&apos;'}[c]));}
function svg(result,text,guides=false){
  const {width,height,stroke}=result;
  let inner='';
  if(guides)for(const {baseline,bodyTop} of result.lines)inner+=`<rect x="0" y="${bodyTop}" width="${width}" height="${baseline-bodyTop}" fill="#e7eee7"/><path d="M0 ${bodyTop}H${width}M0 ${baseline}H${width}" stroke="#8caa92" stroke-width="1" stroke-dasharray="4 4"/>`;
  for(const p of result.placements){
    inner+=`<g transform="translate(${p.x} ${p.y}) scale(${p.scale})">`;
    // Inverse stroke scaling keeps the composition's weight uniform, including exports.
    for(const d of p.glyph.paths)inner+=`<path d="${escapeXML(d)}" fill="none" stroke="#202820" stroke-width="${stroke/p.scale}" stroke-linecap="round" stroke-linejoin="round"/>`;
    inner+='</g>';
  }
  for(const d of result.decorations||[])inner+=`<line data-effect="${d.kind}" x1="${d.x1}" x2="${d.x2}" y1="${d.y}" y2="${d.y}" stroke="#202820" stroke-width="${stroke}" stroke-linecap="round"/>`;
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" role="img" aria-label="${escapeXML(text)}"><title>${escapeXML(text)}</title>${inner}</svg>`;
}
const api={layout,svg};
if(typeof module!=='undefined'&&module.exports)module.exports=api;
root.Typeface=api;
if(typeof document==='undefined')return;
const data=JSON.parse(document.getElementById('glyphData').textContent),$=id=>document.getElementById(id);
let current=null;
function update(){
  try{current=layout($('words').value,data.glyphs,{xHeight:Number($('height').value),capHeight:Number($('height').value)*52/36,tracking:Number($('spacing').value),lineGap:Number($('lineSpacing').value),stroke:Number($('strokeWidth').value),underline:$('underline').checked,strikethrough:$('strikethrough').checked,canvasHeight:$('lockHeight').checked?28:null,padding:$('lockHeight').checked?0:16,trimInk:$('lockHeight').checked,align:'center'});
    $('output').innerHTML=svg(current,$('words').value,$('guides').checked);
    $('status').textContent=($('lockHeight').checked?'Visible ink locked at 28 units high, without padding; width follows the text. ':'')+'Bodies share the shaded height. Ascenders rise above it; descenders fall below the baseline.';
    $('download').disabled=!current.placements.length;
  }catch(e){current=null;$('output').replaceChildren();$('status').textContent=e.message;$('download').disabled=true;}
}
for(const id of ['words','height','spacing','lineSpacing','strokeWidth','guides','underline','strikethrough','lockHeight'])$(id).addEventListener('input',update);
$('download').onclick=()=>{
 if(!current)return;
 const url=URL.createObjectURL(new Blob([svg(current,$('words').value)],{type:'image/svg+xml'}));
 const a=document.createElement('a');a.href=url;a.download='combined-text.svg';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
};
for(const g of data.glyphs){const option=document.createElement('option');option.value=g.icon_id;option.textContent=g.character+(g.preferred?'':' (large source)');$('inspect').append(option);}
function inspect(){
 const g=data.glyphs.find(g=>g.icon_id===$('inspect').value);if(!g)return;
 const paths=g.paths.map(d=>`<path d="${escapeXML(d)}"/>`).join('');
 const [vx,vy,vw,vh]=g.preview_box||[0,0,48,48];
 $('bodyPreview').innerHTML=`<svg viewBox="${vx} ${vy} ${vw} ${vh}" role="img" aria-label="Body region of ${escapeXML(g.character)}"><rect x="${vx}" y="${g.body_top}" width="${vw}" height="${g.body_height}" fill="#e7eee7"/><path d="M${vx} ${g.body_top}H${vx+vw}M${vx} ${g.baseline}H${vx+vw}" stroke="#8caa92" stroke-width=".4" stroke-dasharray="1 1"/><g fill="none" stroke="#202820" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">${paths}</g></svg>`;
 $('metrics').textContent=`Body height ${g.body_height.toFixed(1)} · top ${g.body_top.toFixed(1)} · baseline ${g.baseline.toFixed(1)}. `+(['authored-body-band','source-body-band'].includes(g.measurement)?'Body region measured from the source letter.':'Measured from '+(g.measurement==='closed-body-contour'?'the closed bowl.':'the natural letter strokes.'));
}
$('inspect').onchange=inspect;$('inspect').value='letter-b';inspect();update();
})(typeof globalThis!=='undefined'?globalThis:this);
