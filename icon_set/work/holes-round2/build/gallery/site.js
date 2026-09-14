(async()=>{
  const nav=document.querySelector('.site-nav');
  const page=location.pathname.split('/').pop();
  const current=['generate.html','login.html'].includes(page)?'index.html':page;
  nav?.querySelectorAll('a').forEach(a=>{if(a.getAttribute('href')===current)a.setAttribute('aria-current','page');});
  try{
    const response=await fetch('/api/auth/session');
    if(!response.ok)throw Error();
    const {user}=await response.json();
    document.body.classList.toggle('guest',!user);
    const auth=document.getElementById('siteAuth');
    if(user&&auth){
      const button=document.createElement('button');button.className='auth-link';button.textContent=user+' · Log out';
      button.onclick=async()=>{button.disabled=true;try{const result=await fetch('/api/auth/logout',{method:'POST',headers:{'Content-Type':'application/json'},body:'{}'});if(!result.ok)throw Error();location.assign('home.html');}catch{button.textContent='Retry log out';button.disabled=false;}};
      auth.replaceWith(button);
    }
    const fix=document.getElementById('fixForm');
    if(!user&&fix){const link=document.createElement('a');link.href='login.html';link.textContent='Log in as an admin to generate a revised icon.';fix.parentElement.append(link);}
  }catch{document.body.classList.add('guest');}
})();
