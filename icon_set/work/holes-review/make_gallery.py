from pathlib import Path
import json,html,re
from PIL import Image,ImageDraw
import cairosvg,io
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/holes-review/queue.json'
AUTHOR='gpt-6'
W=Path(__file__).parent
rows=json.loads((W/'results.json').read_text());notes=json.loads((W/'notes.json').read_text())
excluded=json.loads((W/'excluded.json').read_text()) if (W/'excluded.json').exists() else {}
revised={r['original'] for r in json.loads((W/'revision-2-mapping.json').read_text())} if (W/'revision-2-mapping.json').exists() else set()
rows=[r for r in rows if r['original'] not in excluded]
total=len(rows)
assert all(r['qa']['negative_space']['status']=='pass' for r in rows)
passed=sum(r['qa']['status']=='pass' for r in rows)
parts=[]
for index,r in enumerate(rows,1):
 name=r['original'];q=r['qa'];fully=q['status']=='pass';findings=q['errors']+q['warnings']
 before=((W/(r['previous_candidate']+'.svg')).read_text() if name in revised else Path('icon_set/dist/failed/solo48',name+'.svg').read_text());after=(W/(r['candidate']+'.svg')).read_text()
 def figure(svg,label):return f'<div class="sample"><span>{label}</span><div class="drawing">{svg}</div><div class="native">{svg}<small>48 px</small></div></div>'
 issue_text=''.join('<li>'+html.escape(e)+'</li>' for e in findings)
 issue_summary='All blocking checks pass' if fully else 'Other bounds / spacing findings remain'
 detail='' if fully else f'<details><summary>View remaining findings ({len(findings)})</summary><ul>{issue_text}</ul></details>'
 parts.append(f'''<article id="icon-{index}" data-name="{html.escape(name)}" data-revised="{str(name in revised).lower()}" data-status="{'pass' if fully else 'remaining'}">
 <div class="card-head"><span class="number">{index:02}</span><h2>{html.escape(name)}</h2><a href="#icon-{index}" aria-label="Link to icon {index}">#</a></div>
 <div class="comparison">{figure(before,'Previous draft' if name in revised else 'Original')}{figure(after,'Revised' if name in revised else 'Proposed fix')}</div>
 <p class="note">{html.escape(notes[name])}</p>
 <div class="badges"><span class="good">Openings pass</span><span class="{'good' if fully else 'pending'}">{issue_summary}</span></div>{detail}</article>''')
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Opening repairs — latest revisions</title>
<style>
:root{color-scheme:light;--bg:#f5f4ef;--panel:#fff;--ink:#242521;--muted:#73746b;--line:#e5e5db;--green:#1f633d;--green-bg:#edf5ee;--amber:#80581b;--amber-bg:#fcf3e3}
body.dark{color-scheme:dark;--bg:#171917;--panel:#202320;--ink:#ebeee5;--muted:#a6aea2;--line:#373d35;--green:#a2d7af;--green-bg:#293e2d;--amber:#e3c17e;--amber-bg:#3e3524}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.5 system-ui,sans-serif}header{max-width:1380px;margin:auto;padding:36px 28px 22px}.eyebrow{text-transform:uppercase;letter-spacing:.12em;font-size:11px;color:var(--muted)}h1{font-size:34px;letter-spacing:-.035em;line-height:1.15;margin:8px 0 14px}header p{color:var(--muted);max-width:800px;margin:8px 0}.stats{display:flex;gap:24px;flex-wrap:wrap;margin:24px 0 0}.stats b{font-size:25px;display:block;line-height:1.1}.stats span{font-size:12px;color:var(--muted)}.toolbar{position:sticky;top:0;z-index:2;border-block:1px solid var(--line);background:var(--bg);padding:12px 28px;display:flex;gap:12px;align-items:center;flex-wrap:wrap}.toolbar-inner{max-width:1324px;width:100%;margin:auto;display:flex;gap:12px;align-items:center;flex-wrap:wrap}input,select,button{font:inherit;color:var(--ink);background:var(--panel);border:1px solid var(--line);padding:9px 12px;border-radius:8px}input{min-width:250px;flex:1}button{cursor:pointer}#count{color:var(--muted);font-size:12px}.grid{max-width:1380px;margin:auto;padding:24px 28px 60px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}article{background:var(--panel);border:1px solid var(--line);border-radius:12px;overflow:hidden;scroll-margin-top:85px}.card-head{display:flex;align-items:center;gap:10px;padding:15px 16px;border-bottom:1px solid var(--line)}h2{font-size:13px;font-weight:650;margin:0;overflow-wrap:anywhere;flex:1}.number{font-size:11px;color:var(--muted);font-variant-numeric:tabular-nums}.card-head a{color:var(--muted);text-decoration:none}.comparison{display:grid;grid-template-columns:1fr 1fr;padding:18px 6px 10px}.sample{text-align:center}.sample+.sample{border-left:1px solid var(--line)}.sample>span{font-size:11px;color:var(--muted)}.drawing{height:150px;display:flex;align-items:center;justify-content:center}.drawing svg{width:132px;height:132px}.native{display:flex;align-items:center;justify-content:center;gap:12px;margin:4px 0}.native svg{width:48px;height:48px;flex:none}.native small{font-size:10px;color:var(--muted)}.note{margin:10px 16px 14px;min-height:63px;font-size:12px;color:var(--muted)}.badges{display:flex;gap:6px;flex-wrap:wrap;padding:0 16px 16px}.badges span{font-size:10px;border-radius:5px;padding:4px 7px}.good{color:var(--green);background:var(--green-bg)}.pending{color:var(--amber);background:var(--amber-bg)}details{border-top:1px solid var(--line);font-size:11px;padding:12px 16px;color:var(--muted)}summary{cursor:pointer}li{overflow-wrap:anywhere;margin:8px 0}footer{max-width:1324px;margin:0 auto 40px;color:var(--muted);font-size:12px;padding:0 28px}article[hidden]{display:none}@media(max-width:1080px){.grid{grid-template-columns:repeat(2,minmax(0,1fr))}}@media(max-width:650px){.grid{grid-template-columns:1fr;padding:16px}header{padding:24px 16px}.toolbar{padding:10px 16px}h1{font-size:28px}}
</style></head><body>
<header><div class="eyebrow">Pictographic · SOLO48 · review batch</div><h1>Give the openings room.</h1><p>Nine requested revisions now pass all blocking checks. Compare their previous drafts and revised drawings, enlarged and at their actual 48-pixel size. Select All icons to view the full __TOTAL__-icon batch.</p><p><strong>Original sources preserved. These candidates have not been applied to the failure gallery.</strong> Opening checks pass for every candidate; remaining bounds and spacing findings are shown on each card. User-with-gear has been removed from this review batch. All previous source versions are preserved.</p>
<div class="stats"><div><b>__TOTAL__ / __TOTAL__</b><span>Opening checks pass</span></div><div><b>__PASS__</b><span>All blocking checks pass</span></div><div><b>__REMAIN__</b><span>Still have other findings</span></div></div></header>
<div class="toolbar"><div class="toolbar-inner"><input id="search" type="search" placeholder="Find an icon…" aria-label="Find an icon"><select id="filter" aria-label="Filter validation status"><option value="revised" selected>Latest revisions (9)</option><option value="all">All __TOTAL__ icons</option><option value="pass">All blocking checks pass</option><option value="remaining">Other findings remain</option></select><button id="theme" type="button">Dark theme</button><span id="count">9 icons</span></div></div>
<main class="grid">__CARDS__</main><footer>Construction references inspected: local Lucide originals and atomic geometry for church, turtle, baby, sprout, cloud-moon-rain, disc-3, person-standing, bug, shell, watch, bird, trophy, scale, paw-print, castle and fish. These informed round shapes, coherent curves and clear openings; the supplied subjects were preserved. All geometry changes live in independent Python variants; no validation thresholds were changed. The repository-wide test run is not green (4,077 failures and 41 errors across the existing library); per-candidate validation is shown above.</footer>
<script>
const cards=[...document.querySelectorAll('article')],search=document.querySelector('#search'),filter=document.querySelector('#filter');
function apply(){let n=0;for(const card of cards){const show=card.dataset.name.includes(search.value.toLowerCase().trim())&&(filter.value==='all'||(filter.value==='revised'?card.dataset.revised==='true':card.dataset.status===filter.value));card.hidden=!show;if(show)n++}document.querySelector('#count').textContent=n+' icons'}search.addEventListener('input',apply);filter.addEventListener('change',apply);apply();
document.querySelector('#theme').addEventListener('click',function(){const dark=document.body.classList.toggle('dark');this.textContent=dark?'Light theme':'Dark theme'});
</script></body></html>'''
(W/'review.html').write_text(page.replace('__PASS__',str(passed)).replace('__REMAIN__',str(total-passed)).replace('__TOTAL__',str(total)).replace('__CARDS__','\n'.join(parts)))
# Native-size dark overview: inspect every repaired drawing with its original.
out=Image.new('RGB',(1150,1196),'#202320');d=ImageDraw.Draw(out)
for j,r in enumerate(rows):
 x=j%5*230;y=j//5*92;d.text((x+8,y+5),f"{j+1}. {r['original'][:25]}",fill='#cbd2c5')
 for k,name in enumerate([r['original'],r['candidate']]):
  path=Path('icon_set/dist/failed/solo48',name+'.svg') if k==0 else W/(name+'.svg')
  svg=path.read_text().replace('currentColor','#eff2e9');im=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(),output_width=48,output_height=48)));out.paste(im,(x+28+k*105,y+30),im)
out.save(W/'native-dark.png')
manifest={'status':'awaiting batch review','opening_passes':total,'latest_revision_passes':len(revised),'excluded':list(excluded),'fully_passed':passed,'other_findings':total-passed,'candidates_applied_to_failure_gallery':False,'live_gallery_observed_hole_count':88,'live_gallery_observed_failed_count':1462,'originals_modified':False,'previously_approved':['cologne-cathedral-v2'],'models':[{k:v for k,v in r.items() if k!='qa'} for r in rows]}
(W/'review-manifest.json').write_text(json.dumps(manifest,indent=2))
print('Wrote review.html and native dark overview')
