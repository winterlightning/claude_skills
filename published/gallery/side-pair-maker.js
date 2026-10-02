/* Side pair from a combination primitive (primitives.html review cards). A reference classified as a
   combination is not a published side pair, so it never reached the side page. Pick its main (a solo icon)
   and its sub (a sub icon) from pictures, prefilled from the classification's briefs; when no icon fits yet,
   type the name of the one to draw. Save puts the pair on the side page (filter "From review"), where it is
   combined like every other pair. From D1: the pair (GET /api/combinations), its icons (POST /api/combinations/parts),
   a new pair (POST /api/combinations/pair), candidates (GET /api/combinations/candidates); a new side is saved with a
   build composed in this browser (side-pairs-data.js). */
(function(){
const POSITIONS={br:'Bottom-right',bl:'Bottom-left',tr:'Top-right',tl:'Top-left',ri:'Right',le:'Left',bo:'Bottom',to:'Top'};
const ROLES={main:{label:'Main icon',family:'solo',hint:'A 48×48 solo icon',example:'eye'},sub:{label:'Sub icon',family:'sub',hint:'A 32×32 sub icon',example:'light bulb'}};
const STATUS={needs_both:['Needs main + sub drawn','todo'],needs_main:['Needs main drawn','todo'],needs_sub:['Needs sub drawn','todo'],
              waiting:['On the side page','drawn'],generated:['Combined','generated']};
const TRACK='primitives.html?view=side&side=made';
// Open forms by primitive uuid; they survive the page's re-renders, and the page does not refresh while one is open.
const forms=new Map();
// The last save's confirmation per card, shown until the next change.
const notices=new Map();
// Saved pairs by primitive uuid (GET /api/combinations?q=), read once per card.
let pairs=null,pairsLoading=null;

// A published pair (side page) is addressed by its pair id, a combination primitive by its uuid.
const target=row=>row.published?{pair_id:row.uuid}:{uuid:row.uuid};
function el(tag,cls,text){const n=document.createElement(tag);if(cls)n.className=cls;if(text!==undefined)n.textContent=text;return n;}
function button(text,cls){const b=el('button',cls||'',text);b.type='button';return b;}
async function readJSON(response,fallback){let data={};try{data=await response.json();}catch{}if(!response.ok)throw Error(data.error||fallback);return data;}
// The side pair of a reference as the old list gave it: {row: {id, position, mains, subs}, status}.
function pairEntry(item){
  const part=role=>item.parts.find(p=>p.role===role)||{},m=part('main'),s=part('sub');
  const icon=p=>p.icon?[{icon:p.icon.split('/')[1],family:p.icon.split('/')[0],model_key:p.icon,
    preview_url:'/api/icon-artwork/svg?'+new URLSearchParams({icon:p.icon,...(p.current_sha?{v:p.current_sha.slice(0,12)}:{})})}]:[];
  const status=!m.icon&&!s.icon?'needs_both':!m.icon?'needs_main':!s.icon?'needs_sub':item.state==='built'?'generated':'waiting';
  return {row:{id:item.reference_id,position:s.position,mains:icon(m),subs:icon(s),generated:item.icon?{at:item.icon.svg_sha256}:null,
               main_name:m.icon?null:m.draw_name||null,sub_name:s.icon?null:s.draw_name||null,
               forms:{main:m.form?.model_key||(m.form?m.form.family+'/'+m.form.icon:null),sub:s.form?.model_key||(s.form&&!s.form.native_text?s.form.family+'/'+s.form.icon:null)}},
          status,main:m.icon?{preview_url:icon(m)[0].preview_url}:null,sub:s.icon?{preview_url:icon(s)[0].preview_url}:null};
}
const pairRequests=new Map();
function loadPair(uuid,rerender){
  if(pairRequests.has(uuid))return pairRequests.get(uuid);
  const request=fetch('/api/combinations?'+new URLSearchParams({kind:'side',size:String(window.SideData?.size()||64),q:uuid,limit:'5',forms:'1'}),{cache:'no-store'})
    .then(r=>r.ok?r.json():{items:[]}).catch(()=>({items:[]}))
    .then(data=>{pairs??=new Map();const item=data.items.find(i=>i.reference_id===uuid);if(item)pairs.set(uuid,pairEntry(item));else pairs.delete(uuid);rerender();});
  pairRequests.set(uuid,request);return request;
}
function loadPairs(rerender,uuid){pairs??=new Map();return uuid?loadPair(uuid,rerender):Promise.resolve();}
function combinedURL(uuid,version){return 'combination-previews/'+encodeURIComponent(uuid)+'.svg'+(version?'?v='+encodeURIComponent(version):'');}
function link(text,href){const a=el('a','',text);a.href=href;return a;}
const iconName=i=>i?.icon?.replace(/-/g,' ')||'';
// What a saved pair uses for a part: its icon's name, or the name of the icon still to draw.
const partName=(r,role)=>r[role+'s']?.length?iconName(r[role+'s'][0]):'to draw: '+(r[role+'_name']||'?');

// Icons that can be the main (solo) or sub (sub) of a 64 side pair, approved first (GET /api/combinations/candidates).
// A phrase with no match (a brief name, "Idea lightbulb") is looked up word by word, longest first.
async function findCandidates(role,query){
  const ask=async q=>(await readJSON(await fetch('/api/combinations/candidates?'+new URLSearchParams({role,size:String(window.SideData?.size()||64),q}),{cache:'no-store'}),'Search failed.'))
    .map(c=>({key:c.key,icon_id:c.key.split('/')[1],name:c.name,approved:c.review==='approve',
              preview_url:'/api/icon-artwork/svg?'+new URLSearchParams({icon:c.key,v:(c.svg_sha256||'').slice(0,12)})}));
  let found=await ask(query.trim());
  if(found.length||!query.trim())return found;
  const seen=new Map();
  for(const word of query.toLowerCase().split(/[^a-z0-9]+/).filter(w=>w.length>2).sort((a,b)=>b.length-a.length))
    for(const c of await ask(word))if(!seen.has(c.key))seen.set(c.key,c);
  return [...seen.values()].slice(0,40);
}
function candidateButton(form,role,c,rerender){
  const b=button('','side-pair-candidate'+(!form.draw[role]&&form[role]===c.key?' chosen':''));b.title=c.icon_id+(c.build_failed?' · fails the build check':'')+(c.approved?' · approved':'');
  if(c.preview_url){const img=el('img');img.src=c.preview_url;img.alt='';img.loading='lazy';b.append(img);}
  b.append(el('span','',c.name||c.icon_id));
  if(c.approved)b.append(el('span','badge generated','Approved'));else if(c.build_failed)b.append(el('span','badge failed','Fails'));
  b.onclick=()=>{form[role]=c.key;form.chosen[role]=c;form.draw[role]=null;form.focus=null;rerender();};
  return b;
}
function roleField(form,role,rerender){
  const info=ROLES[role],box=el('div','side-pair-role');
  box.append(el('strong','',info.label),el('span','muted',' · '+info.hint));
  if(form.draw[role]!==null){
    // No icon fits yet: the pair keeps the name of the one to draw, and waits for it.
    const picked=el('div','side-pair-chosen to-draw'),name=el('input');
    name.value=form.draw[role];name.maxLength=120;name.placeholder='Name of the '+role+' icon to draw';name.setAttribute('aria-label','Name of the '+role+' icon to draw');
    name.oninput=()=>{form.draw[role]=name.value;};
    picked.append(el('span','','To draw:'),name);
    const back=button('Pick an existing icon instead');back.onclick=()=>{form.draw[role]=null;rerender();};
    box.append(picked,back);return box;
  }
  // The chosen icon, shown as its picture and name: picked by clicking a result, never typed.
  const chosen=form.chosen[role],picked=el('div','side-pair-chosen');
  if(chosen){if(chosen.preview_url){const img=el('img');img.src=chosen.preview_url;img.alt='';picked.append(img);}
    picked.append(el('span','',chosen.name||chosen.icon_id));picked.title=chosen.icon_id||'';}
  else picked.append(el('span','muted','Nothing chosen yet: click an icon below.'));
  const search=el('input');search.type='search';search.value=form.queries[role];search.placeholder='Search by name, e.g. '+info.example;
  search.setAttribute('aria-label','Search '+info.label.toLowerCase());
  // The page re-renders the card when results arrive: keep typing in the same box.
  if(form.focus===role)requestAnimationFrame(()=>{search.focus();const end=search.value.length;search.setSelectionRange(end,end);});
  let timer;search.oninput=()=>{form.queries[role]=search.value;form.focus=role;clearTimeout(timer);timer=setTimeout(async()=>{
    const query=search.value;
    try{const candidates=await findCandidates(role,query);if(form.queries[role]===query){form.candidates[role]=candidates;rerender();}}catch(error){form.message=error.message;rerender();}
  },250);};
  const list=el('div','side-pair-candidates'),candidates=form.candidates[role]||[];
  if(candidates.length)list.append(...candidates.map(c=>candidateButton(form,role,c,rerender)));
  else list.append(el('span','muted',form.queries[role]?'No '+info.family+' icon matches “'+form.queries[role]+'”.':'Type a name to search.'));
  const none=button('None of these: it needs drawing','side-pair-none');
  none.onclick=()=>{form.draw[role]=form.brief[role]||form.queries[role]||'';form.focus=null;rerender();};
  box.append(picked,search,list,none);
  return box;
}

const post=async(url,body,fallback)=>readJSON(await fetch(url,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}),fallback);
// Save the pair in D1: make it (a primitive's first save), pick its icons, and save a changed side with a build
// composed in this browser (the side is stored with the pair's build). → {pair, status} or {removed}.
async function savePair(row,body){
  const id=row.uuid;
  if(body.remove){
    const saved=pairs?.get(id);
    if(row.published&&saved){for(const role of ['main','sub'])if(saved.row.forms[role])await post('/api/combinations/parts',{reference_id:id,role,icon:saved.row.forms[role],size:window.SideData?.size()||64},'Could not restore the published icons.');}
    else await post('/api/combinations/pair',{reference_id:id,remove:true},'Could not remove the side pair.');
    return {removed:true};
  }
  if(!pairs?.has(id))await post('/api/combinations/pair',{reference_id:id,position:body.position||'br'},'Could not make the side pair.');
  for(const role of ['main','sub']){
    if(body[role])await post('/api/combinations/parts',{reference_id:id,role,icon:body[role],size:window.SideData?.size()||64},'Could not save the '+role+'.');
    // No icon fits yet: the part keeps the name of the one to draw (shown on the side page until one is picked).
    else if(body[role+'_name']!==undefined)await post('/api/combinations/parts',{reference_id:id,role,draw_name:body[role+'_name']||null,size:window.SideData?.size()||64},'Could not save the '+role+' to draw.');
  }
  let got=await window.SideData?.refresh(id);
  const sub=got?.item.parts.find(p=>p.role==='sub');
  if(got&&body.position&&sub?.position!==body.position&&got.item.parts.every(p=>p.icon||p.form?.native_text)){
    const composed=await SideData.compose(id,{position:body.position});const [built]=await SideData.build([composed.request]);
    if(!built?.ok)throw Error(built?.error||'Could not save the side.');got=await SideData.refresh(id);
  }
  const entry=got?pairEntry(got.item):null;
  if(entry)pairs.set(id,entry);
  return entry?{pair:entry.row,status:entry.status}:{pair:{id,position:body.position,mains:[],subs:[]},status:'needs_both'};
}
async function send(row,form,body,rerender,working){
  form.busy=true;form.focus=null;form.message=working;rerender();
  try{return await savePair(row,body);}
  catch(error){form.message=error.message;return null;}
  finally{form.busy=false;rerender();}
}
function pairBody(form){
  const part=role=>form.draw[role]!==null?{[role+'_name']:form.draw[role].trim()}:form[role]&&form[role]!==form.saved?.[role]?{[role]:form[role]}:{};
  return {...part('main'),...part('sub'),position:form.position};
}
function remember(row,data){if(data.pair&&!pairs?.has(row.uuid))pairs?.set(row.uuid,{row:data.pair,status:data.status});}

function formSection(row,form,rerender){
  const box=el('div','side-pair-form');
  if(!form.loaded){box.append(el('p','muted','Finding the main and sub icons…'));return box;}
  box.append(roleField(form,'main',rerender),roleField(form,'sub',rerender));
  const label=el('label','','Sub position ');const select=el('select');
  select.append(new Option('Choose…',''),...Object.entries(POSITIONS).map(([k,v])=>new Option(v,k)));select.value=form.position||'';
  select.onchange=()=>{form.position=select.value;rerender();};label.append(select);box.append(label);
  if(form.sub_position==='center')box.append(el('p','muted','Classified as center: a side pair needs one of the eight side positions.'));
  const actions=el('div','side-pair-actions'),save=button('Save','primary'),close=button('Close');
  save.disabled=form.busy;
  save.onclick=async()=>{
    const data=await send(row,form,pairBody(form),rerender,'Saving…');
    if(data){remember(row,data);forms.delete(row.uuid);
      // On the side page the row redraws itself from the saved pair.
      if(form.onSaved){form.onSaved(data);return;}
      const saved=el('span','',data.status==='waiting'?'Saved to Side combination. Combine it there. ':'Saved to Side combination. It waits there until the '+(data.status==='needs_both'?'main and sub are':data.status==='needs_main'?'main is':'sub is')+' drawn. ');
      notices.set(row.uuid,saved);rerender();}
  };
  close.onclick=()=>{forms.delete(row.uuid);rerender();};
  actions.append(save,close);
  if(pairs?.has(row.uuid)){
    // Removing a published pair's change brings back its published main / sub, icon and layout.
    const remove=button(row.published?'Use published main / sub':'Remove pair');remove.disabled=form.busy;
    remove.onclick=async()=>{if(await send(row,form,{remove:true},rerender,'Removing…')){pairs.delete(row.uuid);form.version=null;
      if(form.onSaved){forms.delete(row.uuid);form.onSaved({removed:true});return;}
      form.message='Removed.';rerender();}};
    actions.append(remove);
  }
  box.append(actions);
  return box;
}

async function openForm(row,rerender){
  await loadPairs(()=>{},row.uuid);
  const saved=pairs?.get(row.uuid);const r=saved?.row;notices.delete(row.uuid);
  const form={uuid:row.uuid,target:target(row),loaded:false,busy:false,message:'',main:'',sub:'',position:r?.position||row.position||'',version:null,
              queries:{main:'',sub:''},candidates:{main:[],sub:[]},chosen:{main:null,sub:null},draw:{main:null,sub:null},brief:{main:'',sub:''},saved:{}};
  // A saved pair opens as it was saved: its icons.
  for(const role of ['main','sub']){const i=r?.[role+'s']?.[0];
    if(i){form[role]=form.saved[role]=i.model_key;form.chosen[role]={key:i.model_key,icon_id:i.icon,name:iconName(i),preview_url:saved?.[role]?.preview_url||i.preview_url};}
    else if(r?.[role+'_name'])form.draw[role]=r[role+'_name'];}
  forms.set(row.uuid,form);rerender();
  try{
    // The searches start from the primitive's classification briefs, or a published pair's icon names.
    const statuses=await fetch('/api/primitives/status',{cache:'no-store'}).then(x=>x.ok?x.json():{}).catch(()=>({}));
    const status=statuses[row.uuid]||{},brief=b=>typeof b==='string'?(()=>{try{return JSON.parse(b);}catch{return {name:b};}})():b;
    for(const role of ['main','sub']){
      const name=brief(status[role+'_brief'])?.name||(row.current?.[role]?.name)||(r?.[role+'s']?.[0]?iconName(r[role+'s'][0]):'');
      form.queries[role]=form.brief[role]=name||'';form.candidates[role]=await findCandidates(role,form.queries[role]);
      // A published pair opens with what it uses now; a new pair with the best match of the brief name.
      const now=!r&&row.current?.[role];
      if(now){form[role]=now.key;form.chosen[role]=now;}
      else if(!r&&form.candidates[role][0]){form[role]=form.candidates[role][0].key;form.chosen[role]=form.candidates[role][0];}
    }
    const codes={'bottom-right':'br','bottom-left':'bl','top-right':'tr','top-left':'tl',right:'ri',left:'le',bottom:'bo',top:'to'};
    form.position||=codes[status.sub_position]||'';form.sub_position=status.sub_position;
  }catch(error){form.message=error.message;}
  form.loaded=true;rerender();
}

// The card section: where the saved pair stands, and a form to make or change it.
function section(row,rerender){
  if(!pairRequests.has(row.uuid))loadPairs(rerender,row.uuid);
  const box=el('section','component-brief side-pair'),saved=pairs?.get(row.uuid),form=forms.get(row.uuid);
  const head=el('div','side-pair-head');head.append(el('strong','','Side pair'));
  if(saved){const [label,tone]=STATUS[saved.status]||STATUS.waiting;head.append(el('span','badge '+tone,label));}
  box.append(head);
  if(saved){
    const r=saved.row;box.append(el('p','','Main: '+partName(r,'main')+' · Sub: '+partName(r,'sub')+' · '+(POSITIONS[r.position]||'position not set')));
    if(!form&&saved.status==='generated'){const img=el('img','side-pair-result');img.src=combinedURL(row.uuid,r.generated?.at);img.alt=row.concept+' — combined';img.loading='lazy';box.append(img);}
  }else if(!form)box.append(el('p','muted','Not on the Side combination page yet. Pick its main and sub icons to save it.'));
  if(form)box.append(formSection(row,form,rerender));
  else{const open=button(saved?'Change side pair':'Make side pair','brief-edit login-only');open.onclick=()=>openForm(row,rerender);box.append(open);}
  if(form?.message){const m=el('p','side-pair-message',form.message);m.setAttribute('role','status');box.append(m);}
  if(!form&&notices.has(row.uuid)){const m=el('p','side-pair-message');m.setAttribute('role','status');
    m.append(notices.get(row.uuid),link('Open it →','primitives.html?view=side&q='+encodeURIComponent(row.uuid)));box.append(m);}
  if(saved||form)box.append(link('All saved side pairs →',TRACK));
  return box;
}

// The side page's control for a saved pair: a button, then the picker; `onSaved` runs after a save.
function editor(row,rerender,onSaved){
  const box=el('div','component-brief side-pair side-pair-editor'),form=forms.get(row.uuid);
  if(form){form.onSaved=onSaved;box.append(formSection(row,form,rerender));
    if(form.message){const m=el('p','side-pair-message',form.message);m.setAttribute('role','status');box.append(m);}}
  else{const open=button('Change main / sub','login-only');open.onclick=()=>openForm(row,rerender);box.append(open);}
  return box;
}

window.SidePairMaker={section,editor,editing:()=>forms.size>0};
})();
