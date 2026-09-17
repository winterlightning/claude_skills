(async()=>{
  const nav=document.querySelector('.site-nav');
  // Keep every page's tabs, order, and active state in one place.
  const links=[["home.html", "Home"], ["icon-laboratory.html", "Design Document"], ["icons.html", "Icon"], ["preview.html", "Preview"], ["index.html", "Icon review"], ["experiment.html", "Experiment"], ["ai-review.html", "AI quality review"], ["primitives.html", "Progression"], ["upload.html", "Upload icon"], ["api.html", "API"]];
  const page=location.pathname.split('/').pop()||'home.html';
  const current=({'text-combine.html':'experiment.html','generate.html':'index.html','reviewers.html':'index.html','failures.html':'index.html','concept-dictionary.html':'primitives.html'})[page]||page;
  if(nav){
    nav.replaceChildren(...links.map(([href,label])=>{
      const link=document.createElement('a');
      link.href=href;link.textContent=label;
      if(href===current)link.setAttribute('aria-current','page');
      return link;
    }));
  }
  let auth=document.getElementById('siteAuth');
  if(nav&&!auth){auth=document.createElement('a');auth.id='siteAuth';auth.className='auth-link';auth.href='login.html';nav.append(auth);}
  if(auth){
    if(page==='login.html')auth.setAttribute('aria-current','page');
    auth.setAttribute('aria-label','Log in');auth.title='Log in';
    auth.replaceChildren();
    const icon=document.createElementNS('http://www.w3.org/2000/svg','svg');
    icon.setAttribute('viewBox','0 0 24 24');icon.setAttribute('width','20');icon.setAttribute('height','20');icon.setAttribute('fill','none');icon.setAttribute('stroke','currentColor');icon.setAttribute('stroke-width','1.8');icon.setAttribute('stroke-linecap','round');icon.setAttribute('stroke-linejoin','round');icon.setAttribute('aria-hidden','true');
    const path=document.createElementNS('http://www.w3.org/2000/svg','path');path.setAttribute('d','M14 4h5v16h-5M3 12h12M10 7l5 5-5 5');icon.append(path);auth.append(icon,document.createTextNode('Log in'));
  }
  try{
    const response=await fetch('/api/auth/session');
    if(!response.ok)throw Error();
    const {user}=await response.json();
    document.body.classList.toggle('guest',!user);
    if(user&&auth){
      const button=document.createElement('button');button.className='auth-link';button.textContent=user+' · Log out';
      button.onclick=async()=>{button.disabled=true;try{const result=await fetch('/api/auth/logout',{method:'POST',headers:{'Content-Type':'application/json'},body:'{}'});if(!result.ok)throw Error();location.assign('home.html');}catch{button.textContent='Retry log out';button.disabled=false;}};
      auth.replaceWith(button);
    }
    const fix=document.getElementById('fixForm');
    if(!user&&fix){const link=document.createElement('a');link.href='login.html';link.textContent='Log in as an admin to generate a revised icon.';fix.parentElement.append(link);}
  }catch{document.body.classList.add('guest');}
})();
