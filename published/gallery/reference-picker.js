// Reference images (SVG or PNG) attached to feedback and generation briefs.
// Files upload as soon as they are chosen; forms send only the returned ids.
(()=>{
  const API='../api/reference-images',MAX=4,LIMITS={png:2*1024*1024,svg:1024*1024};

  function el(tag,className,text){const node=document.createElement(tag);if(className)node.className=className;if(text!=null)node.textContent=text;return node;}

  function thumb(ref){
    const figure=el('figure','reference-thumb'),link=el('a'),img=el('img');
    img.src=API+'?id='+encodeURIComponent(ref.id);img.alt='Reference: '+ref.name;img.loading='lazy';
    link.href=img.src;link.target='_blank';link.rel='noopener';link.title='Open '+ref.name;link.append(img);
    figure.append(link,el('figcaption','',ref.name));
    return figure;
  }

  function referenceThumbs(refs){
    const strip=el('div','reference-strip');
    for(const ref of refs||[])strip.append(thumb(ref));
    return strip;
  }

  function readBase64(file){
    return new Promise((resolve,reject)=>{const reader=new FileReader();reader.onload=()=>resolve(String(reader.result).split(',',2)[1]||'');reader.onerror=()=>reject(Error('Could not read '+file.name+'.'));reader.readAsDataURL(file);});
  }

  function ReferencePicker(container,{id,label='Reference images (optional, SVG or PNG)',onChange=()=>{}}={}){
    let refs=[],pending=0,epoch=0;
    const wrap=el('div','reference-picker'),input=el('input'),list=el('div','reference-strip'),status=el('p','reference-status');
    input.type='file';input.multiple=true;input.accept='.svg,.png,image/svg+xml,image/png';
    if(id)input.id=id;
    const caption=el('label','',label);if(id)caption.htmlFor=id;
    status.setAttribute('role','status');
    wrap.append(caption,input,list,status);container.append(wrap);

    function draw(){
      list.replaceChildren();
      for(const ref of refs){
        const figure=thumb(ref),remove=el('button','reference-remove','Remove');
        remove.type='button';remove.setAttribute('aria-label','Remove '+ref.name);
        remove.onclick=()=>{refs=refs.filter(item=>item.id!==ref.id);draw();onChange();};
        figure.append(remove);list.append(figure);
      }
      input.disabled=refs.length+pending>=MAX;
    }

    input.onchange=async()=>{
      const files=[...input.files],started=epoch;input.value='';
      for(const file of files){
        if(started!==epoch)return;
        if(refs.length+pending>=MAX){status.textContent='Attach up to '+MAX+' reference images.';break;}
        const kind=/\.png$/i.test(file.name)||file.type==='image/png'?'png':/\.svg$/i.test(file.name)||file.type==='image/svg+xml'?'svg':'';
        if(!kind){status.textContent=file.name+' is not an SVG or PNG file.';continue;}
        if(file.size>LIMITS[kind]){status.textContent=file.name+' is too large ('+kind.toUpperCase()+' limit '+LIMITS[kind]/1048576+' MB).';continue;}
        pending++;draw();status.textContent='Uploading '+file.name+'…';
        try{
          const response=await fetch(API,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name:file.name,data:await readBase64(file)})});
          const result=await response.json().catch(()=>({}));
          if(!response.ok)throw Error(result.error||('Could not upload '+file.name+'.'));
          if(started===epoch&&!refs.some(ref=>ref.id===result.id))refs.push(result);
          if(started===epoch)status.textContent='';
        }catch(error){if(started===epoch)status.textContent=error.message;}
        finally{if(started===epoch){pending--;draw();onChange();}}
      }
    };

    const picker={
      element:wrap,
      ids:()=>refs.map(ref=>ref.id),
      items:()=>refs.map(ref=>({...ref})),
      busy:()=>pending>0,
      set(list){epoch++;pending=0;refs=(list||[]).slice(0,MAX);status.textContent='';draw();},
      clear(){picker.set([]);},
    };
    draw();
    return picker;
  }

  window.ReferencePicker=ReferencePicker;
  window.referenceThumbs=referenceThumbs;
})();
