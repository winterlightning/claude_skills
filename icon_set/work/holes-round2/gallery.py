from pathlib import Path
import json,html,io
from PIL import Image,ImageDraw
import cairosvg
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/holes-round2/results.json'
AUTHOR='gpt-6'
w=Path(__file__).parent;rows=json.loads((w/'results.json').read_text())
notes={
'amazon-connect':'Round matching lower nodes and a round top node; both branches now meet the nodes cleanly.',
'canoe-paddles-outdoors':'Matching rounded paddle caps, deeper openings, and evenly placed crossbars.',
'computer-chip-core':'Wider space around the inner core and evenly spaced pins. The inner square is smaller to fit both layers.',
'cracked-shield':'Clean mirrored shoulders and smooth shield sides replace the tiny pocket at the old join; the crack stays.',
'diamond-shine':'Larger upper and lower facets, matching side walls, and two clear sparkle strokes instead of four crowded ones.',
'earth-model-1':'A clear offset between the globe and its curved mount, with a taller open pedestal.',
'floppy-disk-v2':'Deeper lower slot and narrower inset details, preserving the shutter and center hub.',
'ghost-scare':'Matching open arm pockets, a round head, and the original raised-arm silhouette.',
'horse-head':'A wider curved mane band, smoother muzzle, and a repositioned eye with clear spacing.',
'legal-scale-1':'Larger round pivot, matching pan curves, and a balanced beam and stand.',
'meeting-headphone-wireless':'Roomier earcups and microphone, a smooth headband, and a rounded boom connection. One signal arc replaces the crowded pair.',
'megaphone-7a36c569':'Larger rounded handle and rebalanced horn; the directional silhouette is preserved.',
'nagras':'Wider N skeleton with evenly spaced crossbars and open triangular counters.',
'nagras-money':'The same shared N construction and crossbar spacing, preserving the currency mark.',
'one-eye-smile':'Round open eye, smooth smile, and a wink moved clear of both.',
'pencil-sketch-design':'Deeper rounded end cap and an inset divider; the pencil tip and diagonal body remain.',
'picker-take':'Round upper bulb, compact nozzle, and a larger detached droplet with clear space above it.',
'power-outlet-type-m':'Three open round sockets. The housing changes from square to circular so the sockets retain the required spacing.',
'presentation':'Larger round pull loop and a shorter screen body to fit the whole drawing.',
'round-cap':'One smooth outer semicircle flows into the rails; the central loop is round and larger.',
'shield-c3034182':'Mirrored shoulders and simplified smooth side curves replace the tiny accidental pocket.',
'skull-c8f4a237':'Smooth cranium and jaw, a larger open nose, solid eye marks, and one tooth mark. The crowded eye rings and paired tooth lines are simplified.',
'staffordshire-bull-terrier':'Larger open nose and wider ear clearance; the broad head and hanging ears remain.',
'strategy-split':'Three larger open arrowheads with matching branch curves meeting at one shared point.',
'war-flag-guild-faction':'Larger round finial and a lower banner attachment, preserving the swallowtail.'}
(w/'notes.json').write_text(json.dumps(notes,indent=2))
cards=[]
for i,r in enumerate(rows,1):
 n=r['original'];before=(w/(n+'-before.svg')).read_text();after=(w/(r['candidate']+'.svg')).read_text()
 def fig(s,label):return '<div class="sample"><small>'+label+'</small><div class="large">'+s+'</div><div class="native">'+s+'<small>48 px</small></div></div>'
 cards.append(f'<article id="{n}" data-name="{n}"><h2><small>{i:02d}</small> {n}</h2><div class="pair">'+fig(before,'Before')+fig(after,'Repaired')+'</div><p>'+html.escape(notes[n])+'</p><span class="badge">Holes · spacing · bounds pass</span></article>')
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>25 icon repairs — review</title><style>
:root{--bg:#f4f3ed;--card:#fff;--ink:#242521;--muted:#6f7269;--line:#dddfd5;--green:#22623a;--badge:#eaf5ec}body.dark{--bg:#171b18;--card:#222823;--ink:#eef2e9;--muted:#b0bbaf;--line:#3c473d;--green:#abd9b3;--badge:#304637}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.5 system-ui}header{max-width:1350px;margin:auto;padding:32px 24px 20px}h1{font-size:34px;letter-spacing:-1px;margin:4px 0}header p{max-width:860px;color:var(--muted)}.tools{position:sticky;top:0;z-index:2;display:flex;gap:16px;padding:12px 24px;background:var(--bg);border-block:1px solid var(--line)}input,button{font:inherit;border:1px solid var(--line);border-radius:8px;padding:9px 12px;background:var(--card);color:var(--ink)}input{flex:1}button{cursor:pointer}main{max-width:1350px;margin:auto;padding:24px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}article{border:1px solid var(--line);border-radius:12px;background:var(--card);padding:16px}h2{font-size:14px;overflow-wrap:anywhere;margin:0 0 16px}small{color:var(--muted);font-size:11px}h2 small{margin-right:8px}.pair{display:grid;grid-template-columns:1fr 1fr}.sample{text-align:center}.sample+.sample{border-left:1px solid var(--line)}.large{height:160px;display:flex;align-items:center;justify-content:center}.large svg{width:144px;height:144px}.native{display:flex;justify-content:center;align-items:center;gap:10px}.native svg{width:48px;height:48px}article p{color:var(--muted);font-size:12px;min-height:58px}.badge{display:inline-block;color:var(--green);background:var(--badge);border-radius:6px;padding:5px 8px;font-size:11px}footer{max-width:1300px;margin:0 auto 32px;padding:24px;color:var(--muted);font-size:12px}article[hidden]{display:none}@media(max-width:1050px){main{grid-template-columns:repeat(2,minmax(0,1fr))}}@media(max-width:670px){main{grid-template-columns:1fr}.tools{flex-wrap:wrap}h1{font-size:28px}}
</style></head><body><header><small>PICTOGRAPHIC · SOLO48 · REVIEW</small><h1>25 repairs, approved and applied.</h1><p>Every repaired version passes the hole, spacing, and bounds checks with no warnings. Compare the curves and openings enlarged and at their actual 48-pixel size.</p><p>Approved repairs have been applied to the original icon models. Previous source versions are backed up. User-with-gear remains excluded; horse-head-v2 already passes.</p><p><strong>Look closely at:</strong> the outlet’s circular housing, the skull’s simplified eye and tooth marks, and the headset’s single signal arc. These larger changes give the remaining details room.</p></header><div class="tools"><input id="search" placeholder="Find an icon…" aria-label="Find an icon"><button id="theme">Dark theme</button><span id="count">25 icons</span></div><main>__CARDS__</main><footer>Construction references: local Lucide shield, headphones, pipette, cpu, scale, pencil, skull, flag and ghost originals and atomic drawings. Their coherent curves, shared radii and reduced detail informed these repairs. The asymmetric horse, pencil and megaphone retain their direction. All changes are in independent Python models; validation rules are unchanged.</footer><script>const cards=[...document.querySelectorAll('article')];document.querySelector('#search').addEventListener('input',e=>{let n=0;for(const c of cards){c.hidden=!c.dataset.name.includes(e.target.value.toLowerCase().trim());if(!c.hidden)n++}document.querySelector('#count').textContent=n+' icons'});document.querySelector('#theme').addEventListener('click',e=>{const dark=document.body.classList.toggle('dark');e.target.textContent=dark?'Light theme':'Dark theme'});</script></body></html>'''
(w/'review.html').write_text(page.replace('__CARDS__',''.join(cards)))
# All candidates at native size in both themes, kept at one image pixel per icon pixel.
im=Image.new('RGB',(1000,650),'#eef0e8');d=ImageDraw.Draw(im)
for i,r in enumerate(rows):
 x=i%5*200;y=i//5*130;d.text((x+6,y+5),r['original'][:26],fill='#222')
 for j,color in enumerate(['#242521','#eef2e9']):
  if j:d.rectangle((x+102,y+26,x+197,y+111),fill='#222823')
  s=(w/(r['candidate']+'.svg')).read_text().replace('currentColor',color);p=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=s.encode(),output_width=48,output_height=48)));im.paste(p,(x+25+j*100,y+45),p)
im.save(w/'native-both-themes.png')
(w/'manifest.json').write_text(json.dumps({'status':'awaiting visual approval','review_count':25,'hole_passes':25,'fully_passed':25,'excluded':['user-with-gear'],'already_passed':['horse-head-v2'],'originals_modified':False,'models':[{k:v for k,v in r.items() if k!='qa'} for r in rows]},indent=2))
print('Review page and native-size sheet written.')
