"""Source-linked, non-production container trials from existing solo artwork.

These previews do not author SUB32 models or claim frozen-template validation.
The container remains native64; content geometry is uniformly fitted while its
stroke stays 4 units. Raster clearance estimates are explicitly review aids.
"""
from pathlib import Path
import json,copy,hashlib,io,html,collections
import xml.etree.ElementTree as ET
import numpy as np
from scipy import ndimage,signal
from PIL import Image,ImageDraw
import cairosvg
from icon_set.model.icons.registry import create
from icon_set.validation.envelope import centerline_bounds
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/container-solo-briefs/generation-results.json'
AUTHOR='gpt-6'
ROOT=Path(__file__).resolve().parents[3];PKG=ROOT/'icon_set';WORK=Path(__file__).resolve().parent
ASSETS=PKG/'assets/container-solo-trials';ASSETS.mkdir(parents=True,exist_ok=True)
NS='http://www.w3.org/2000/svg';ET.register_namespace('',NS)
S=4;N=64*S
linked={r['uuid']:r for r in json.loads((ROOT/SOURCE_PATH).read_text())}
catalog=json.loads((PKG/'dist/gallery/combinations.json').read_text())
pairs=[r for r in catalog['rows'] if r['kind']=='container' and r['sub_id'] in linked]
cache={};sources={};hosts={}
def source(family,name):
 key=family+'/'+name
 if key not in sources:
  file=PKG/'dist'/('container64' if family=='container' else 'solo48')/(name+'.svg')
  document=file.read_text();sources[key]=(document,hashlib.sha256(document.encode()).hexdigest())
 return sources[key]
def raster(document):
 return np.array(Image.open(io.BytesIO(cairosvg.svg2png(bytestring=document.encode(),output_width=N,output_height=N))).convert('RGBA'))[:,:,3]>100
def group(document,prefix,scale=1,tx=0,ty=0):
 root=ET.fromstring(document);g=ET.Element('{'+NS+'}g',{'id':prefix,'fill':'none','stroke':'currentColor','stroke-width':str(4/scale),'stroke-linecap':'round','stroke-linejoin':'round','transform':f'translate({tx:.8f} {ty:.8f}) scale({scale:.8f})'})
 for child in list(root):
  if child.tag.split('}')[-1] in ('title','metadata','desc'):continue
  c=copy.deepcopy(child)
  for e in c.iter():
   if 'id' in e.attrib:e.set('id',prefix+'-'+e.get('id'))
   if 'stroke-width' in e.attrib:e.set('stroke-width',str(4/scale))
   if e.tag.split('}')[-1] in ('path','line','polyline','polygon','rect','circle','ellipse'):
    # Resolve monochrome uploaded CSS strokes without allowing a stylesheet
    # to shrink the fixed stroke or force black paint in the dark preview.
    e.set('style',f'stroke:currentColor;stroke-width:{4/scale};stroke-linecap:round;stroke-linejoin:round;fill:none')
  g.append(c)
 return g
def document(host,sub,scale,cx,cy,bounds):
 root=ET.Element('{'+NS+'}svg',{'width':'64','height':'64','viewBox':'0 0 64 64','fill':'none','stroke':'currentColor','stroke-width':'4','stroke-linecap':'round','stroke-linejoin':'round'})
 if host:root.append(group(host,'container'))
 x0,y0,x1,y1=bounds
 root.append(group(sub,'content',scale,cx-scale*(x0+x1)/2,cy-scale*(y0+y1)/2))
 return ET.tostring(root,encoding='unicode')
def host_region(name):
 if name not in hosts:
  doc,_=source('container',name);ink=raster(doc);filled=ndimage.binary_fill_holes(ink);regions,count=ndimage.label(filled&~ink)
  areas=np.bincount(regions.ravel());areas[0]=0
  enclosed=bool(count and areas.max()>S*S*100)
  if enclosed:region=regions==areas.argmax()
  else:
   x0,y0,x1,y1=centerline_bounds(create(name).draw().primitives)
   region=np.zeros_like(ink);region[max(0,int((y0+4)*S)):min(N,int((y1-4)*S)),max(0,int((x0+4)*S)):min(N,int((x1-4)*S))]=True
  # Whiteboards beside people are open on the figure side; their closed
  # head silhouette must not be mistaken for the content area.
  board=name in ('female-teacher-with-whiteboard','teacher-presenting-at-whiteboard')
  if board:
   region=np.zeros_like(ink);region[7*S:47*S,29*S:60*S]=True;enclosed=False
  distance=ndimage.distance_transform_edt(~ink)/S
  allowed=region&(distance>=2.25)
  ys,xs=np.where(region);cx=float(xs.mean()/S) if len(xs) else 32;cy=float(ys.mean()/S) if len(ys) else 32
  hosts[name]=(doc,ink,allowed,(cx,cy),enclosed,distance)
 return hosts[name]
def combine(host_id,sub_id):
 host,ink,allowed,preferred,enclosed,distance=host_region(host_id);sub,_=source('solo',sub_id)
 bounds=centerline_bounds(create(sub_id).draw().primitives);x0,y0,x1,y1=bounds;extent=max(x1-x0,y1-y0)
 choice=None
 for size in (32,28,24):
  scale=(size-4)/extent;mask=raster(document(None,sub,scale,32,32,bounds));ys,xs=np.where(mask);top,left=ys.min(),xs.min();bottom,right=ys.max()+1,xs.max()+1;crop=mask[top:bottom,left:right]
  bad=signal.fftconvolve((~allowed).astype(float),crop[::-1,::-1].astype(float),mode='valid')
  yy,xx=np.indices(bad.shape);cx=32+(xx-left)/S;cy=32+(yy-top)/S
  cost=(cx-preferred[0])**2+(cy-preferred[1])**2
  valid=(bad<.1)&(cost<=100)&(xx%S==0)&(yy%S==0)
  if valid.any():
   score=np.where(valid,cost,np.inf);ay,ax=np.unravel_index(score.argmin(),score.shape)
   # Raster crop origin includes centered content offset; convert back to center.
   px=32+(ax-left)/S;py=32+(ay-top)/S
   choice=(scale,px,py,size,'clearance-estimate-pass' if enclosed else 'review-open-container');break
 if choice is None:choice=((28-4)/extent,round(preferred[0]),round(preferred[1]),28,'review-fit')
 scale,cx,cy,size,status=choice
 if host_id=='universal-prohibited-symbol':
  # A prohibition mark crosses its subject; off-center placement in one
  # half-circle would change the intended relationship. Keep this trial
  # centered and explicitly request review of the overlapping strokes.
  scale,cx,cy,size,status=(28-4)/extent,32,32,28,'review-fit'
 svg=document(host,sub,scale,cx,cy,bounds);mask=raster(document(None,sub,scale,cx,cy,bounds));gap=float(distance[mask].min()) if mask.any() else 0
 if gap<2:status='review-fit'
 filename=host_id+'--'+sub_id+'.svg';(ASSETS/filename).write_text(svg)
 return dict(svg_file=filename,main_key='container/'+host_id,sub_key='solo/'+sub_id,main_sha256=source('container',host_id)[1],sub_sha256=source('solo',sub_id)[1],svg_sha256=hashlib.sha256(svg.encode()).hexdigest(),status=status,estimated_clearance=round(gap,2),placement={'center':[round(cx,3),round(cy,3)],'content_ink_size':size,'scale':scale,'stroke':4},native_sub32=False)
results={}
for i,row in enumerate(pairs):
 host=row['main_icon_id'];sub=linked[row['sub_id']]['icon_id'];key=(host,sub)
 if key not in cache:cache[key]=combine(host,sub)
 results[row['id']]={**cache[key],'pair_id':row['id'],'concept':row['concept'],'main_source_id':row['main_id'],'sub_source_id':row['sub_id']}
 if i%40==0:print(f'Prepared {i+1}/{len(pairs)} pairings',flush=True)
manifest={'version':1,'kind':'container-solo-trial','author':AUTHOR,'notes':'Experimental fitting of existing solo artwork. Fixed stroke 4; native containers unchanged. Raster clearance is advisory, not SUB32 or composition validation.','results':results}
(PKG/'data/container-solo-trials.json').write_text(json.dumps(manifest,indent=2)+'\n');(WORK/'results.json').write_text(json.dumps(manifest,indent=2)+'\n')
# Portable review page with original combination and linked component identities.
e=html.escape
out=['<!doctype html><meta charset="utf-8"><title>Container pair trials</title><style>body{font:15px system-ui;max-width:1200px;margin:36px auto;padding:0 20px;background:#f5f5f0;color:#20251e}input{padding:12px;font:inherit;width:96%;margin:16px 0}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}article{padding:18px;background:white;border:1px solid #ddd;border-radius:12px}h2{font-size:16px}.images{display:flex;align-items:center;justify-content:space-around}.images img{width:64px;height:64px}.dark{background:#181818;padding:10px;border-radius:8px}.dark img{filter:invert(1)}p{font-size:13px;line-height:1.5}a{color:#356342}.review{color:#965113}[hidden]{display:none!important}</style><h1>Container pair trials</h1>']
counts=collections.Counter(r['status'] for r in results.values())
out.append(f'<p>{len(pairs)} recorded pairings · {len(cache)} distinct combinations · {len(hosts)} containers.</p><p>Trial layouts from the existing solo icons, keeping stroke 4. The original combination is on the left. These are previews, not newly authored SUB32 icons. Review labels identify crowded or open layouts.</p><input type="search" aria-label="Filter trials" placeholder="Search concept, container, icon, or review"><div class="grid">')
for r in results.values():
 ref=catalog['references'][r['pair_id']].get('reference_url');url='../../../dist/gallery/'+ref if ref else ''
 # Work folder is icon_set/work/container-pair-trials, so dist is two levels up.
 url='../../dist/gallery/'+ref if ref else ''
 trial='../../assets/container-solo-trials/'+r['svg_file'];label='Trial · clearance estimate clear' if r['status']=='clearance-estimate-pass' else 'Trial · review placement'
 out.append(f'<article data-search="{e((r["concept"]+" "+r["main_key"]+" "+r["sub_key"]+" "+label).lower())}"><h2>{e(r["concept"])}</h2><div class="images"><img alt="Original combination" src="{e(url)}"><a href="{e(trial)}"><img alt="Trial light" src="{e(trial)}"></a><a class="dark" href="{e(trial)}"><img alt="Trial dark" src="{e(trial)}"></a></div><p class="{ "review" if r["status"]!="clearance-estimate-pass" else ""}">{label}</p><p><a href="http://localhost:8000/gallery/index.html?q={r["main_key"].split("/")[1]}">{e(r["main_key"])}</a><br>+ <a href="http://localhost:8000/gallery/index.html?q={r["sub_key"].split("/")[1]}">{e(r["sub_key"])}</a></p><a href="http://localhost:8000/gallery/primitives.html?view=container&amp;q={r["pair_id"]}">Pair in Progression</a></article>')
out.append('</div><script>document.querySelector("input").oninput=e=>document.querySelectorAll("article").forEach(a=>a.hidden=!a.dataset.search.includes(e.target.value.toLowerCase()))</script>')
(WORK/'index.html').write_text(''.join(out))
unique=list(cache.items())
for start in range(0,len(unique),40):
 im=Image.new('RGB',(1200,8*130),'#eee');d=ImageDraw.Draw(im)
 for j,((host,sub),r) in enumerate(unique[start:start+40]):
  x=j%5*240;y=j//5*130
  svg=(ASSETS/r['svg_file']).read_text()
  for dx,fg,bg in [(0,'#111','#fff'),(70,'#fff','#111')]:
   d.rectangle((x+dx,y,x+dx+68,y+68),fill=bg);p=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.replace('currentColor',fg).encode(),output_width=64,output_height=64)));im.paste(p,(x+dx+2,y+2),p)
  d.text((x,y+72),str(start+j)+' '+host[:29],fill='black');d.text((x,y+86),sub[:33],fill='black');d.text((x,y+100),r['status'],fill='black')
 im.save(WORK/f'sheet-{start//40}.png')
print(json.dumps({'pairs':len(pairs),'unique':len(cache),'statuses':counts}),flush=True)
