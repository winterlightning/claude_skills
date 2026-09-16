(async()=>{
  const nav=document.querySelector('.site-nav');
  if(nav&&!nav.querySelector('a[href="reviewers.html"]')){const link=document.createElement('a');link.href='reviewers.html';link.textContent='Reviewers';const review=nav.querySelector('a[href="index.html"]');if(review)review.after(link);else nav.append(link);}
  const page=location.pathname.split('/').pop();
  const current=['generate.html','login.html'].includes(page)?'index.html':page;
  nav?.querySelectorAll('a').forEach(a=>{if(a.getAttribute('href')===current)a.setAttribute('aria-current','page');});
  let auth=document.getElementById('siteAuth');
  if(nav&&!auth){auth=document.createElement('a');auth.id='siteAuth';auth.className='auth-link';auth.href='login.html';nav.append(auth);}
  if(auth){
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
