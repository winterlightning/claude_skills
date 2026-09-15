(()=>{
  const names={landing:'Landing page',dashboard:'Dashboard',application:'Application',slides:'Presentation',...Object.fromEntries(Object.entries(PreviewUsageTemplates).map(([id,t])=>[id,t.name]))};
  const descriptions={landing:'Feature cards, navigation, and a hero with personality.',dashboard:'Navigation, metrics, and activity. Small cues that make data easier to read.',application:'Everyday actions and project cards with a shared visual language.',slides:'A presentation slide sample: bold ideas, simple diagrams, and recognizable symbols.'};
  const uses={landing:['ecology-leaf','upright-rocket-round-window','flash','nodes-connected-angle','security-shield','arrow-right-1','globe'],dashboard:['bars-chart','folder','nodes-connected-angle','notification-bell','cog','check-circle','ecology-leaf','upright-rocket-round-window'],application:['folder','zoom-in-magnifying-glass','check-circle','document','cup','user-reference','ecology-leaf','nodes-connected-angle','cog'],slides:['upright-rocket-round-window','globe','flash','nodes-connected-angle','ecology-leaf']};
  const $=id=>document.getElementById(id);let icons=[],example='landing',accent='green',width='desktop';const sceneIcons=new Map();
  function render(){
    const p=new URLSearchParams(location.search);example=Object.hasOwn(names,p.get('example'))?p.get('example'):'landing';accent=['green','blue','plum'].includes(p.get('accent'))?p.get('accent'):'green';width=p.get('width')==='mobile'?'mobile':'desktop';
    for(const [key,value] of Object.entries({example,accent,width}))document.querySelectorAll(`[data-${key}]`).forEach(b=>{if(b.tagName==='BUTTON')b.setAttribute('aria-pressed',String(b.dataset[key]===value));});
    $('exampleName').textContent=names[example];$('exampleDescription').textContent=descriptions[example]||PreviewUsageTemplates[example]?.description;$('previewStage').dataset.width=width;$('previewStage').dataset.example=example;
    const src=`preview-scene.html?example=${example}&accent=${accent}`;if($('exampleFrame').getAttribute('src')!==src)$('exampleFrame').src=src;
    $('exampleFrame').title=names[example]+' usage example';$('openExample').href=src;renderUsedIcons();
  }
  function renderUsedIcons(){
    $('usedIcons').replaceChildren();
    for(const id of sceneIcons.get(example)||uses[example]||[]){const icon=icons.find(i=>i.icon_id===id);if(!icon)continue;const a=document.createElement('a');a.className='used-icon';a.href='index.html?q='+encodeURIComponent(id);a.title='Inspect '+icon.name;const img=document.createElement('img');img.src=icon.preview_url;img.alt='';const label=document.createElement('span');label.textContent=icon.name.replaceAll('-',' ');a.append(img,label);$('usedIcons').append(a);}
  }
  window.addEventListener('message',event=>{
    if(event.origin!==location.origin||event.source!==$('exampleFrame').contentWindow)return;
    const data=event.data;if(data?.type!=='preview-icons-used'||data.example!==example||!Array.isArray(data.ids))return;
    sceneIcons.set(example,data.ids.filter(id=>typeof id==='string'));renderUsedIcons();
  });
  for(const [index,[id,template]] of Object.entries(PreviewUsageTemplates).entries()){
    const button=document.createElement('button');button.dataset.example=id;button.setAttribute('aria-pressed','false');
    const number=document.createElement('span');number.textContent=String(index+5).padStart(2,'0');const name=document.createElement('strong');name.textContent=template.name;const subtitle=document.createElement('small');subtitle.textContent=template.subtitle;button.append(number,name,subtitle);document.querySelector('.example-picker').append(button);
  }
  for(const key of ['example','accent','width'])document.querySelectorAll(`button[data-${key}]`).forEach(b=>b.onclick=()=>{const u=new URL(location.href);u.searchParams.set(key,b.dataset[key]);history.pushState(null,'',u);render();});
  window.addEventListener('popstate',()=>render());render();
  loadApprovedPreviewIcons().then(approved=>{icons=approved;render();if(!icons.length)$('previewStatus').textContent='No approved icons are available yet.';}).catch(()=>{$('previewStatus').textContent='Could not verify approved icons. Reload the page to try again.';});
})();
