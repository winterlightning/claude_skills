"""Read-only checks of existing non-text combination exports against source geometry."""
import io,json,hashlib,base64,sys,xml.etree.ElementTree as ET
from pathlib import Path
from collections import Counter
import numpy as np
from svgpathtools import Document,Arc
import cairosvg
from PIL import Image
from scipy.ndimage import label,binary_fill_holes
OUT=Path('icon_set/work/nontext-sub-audit');OUT.mkdir(exist_ok=True)
inv=json.load(open('icon_set/work/combination-sub-review/inventory.json'));manifest=json.load(open('icon_set/data/combination-sub32.json'));selected=set(sys.argv[1:]);results=[]
if selected and (OUT/'results.json').exists():results=[r for r in json.loads((OUT/'results.json').read_text())['rows'] if r['key'] not in selected]
def bounds(paths):
 boxes=[p.bbox() for p in paths if len(p)]
 return [min(b[0] for b in boxes),min(b[2] for b in boxes),max(b[1] for b in boxes),max(b[3] for b in boxes)]
def raster(svg,scale):
 return np.array(Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(),scale=scale))).convert('RGBA'))[:,:,3]>128
def topology(mask):
 padded=np.pad(mask,2);return [label(mask,structure=np.ones((3,3)))[1],label(binary_fill_holes(padded)^padded)[1]]
def uri(doc):return 'data:image/svg+xml;base64,'+base64.b64encode(doc.encode()).decode()
for key,a in sorted(inv['assets'].items()):
 if a['family']=='text' or (selected and key not in selected):continue
 row=dict(key=key,name=a['name'],errors=[],warnings=[])
 try:
  rec=manifest[key.split('/',1)[1]];file=Path(rec['svg']);svg=file.read_text();root=ET.fromstring(svg);paths=[p for p in Document(io.StringIO(svg)).paths() if len(p)]
  row['export']=str(file);row['source']=a['source_path'];source=Path(a['source_path']).read_text()
  if hashlib.sha256(source.encode()).hexdigest()!=rec['source_sha256']:row['errors'].append('stale_source')
  if [float(root.get('width')),float(root.get('height'))]!=[32,32] or list(map(float,root.get('viewBox').split()))!=[0,0,32,32]:row['errors'].append('canvas')
  sw=float(root.get('stroke-width'));row['stroke']=sw
  if sw!=4 or root.get('stroke-linecap')!='round' or root.get('stroke-linejoin')!='round':row['errors'].append('stroke_style')
  b=bounds(paths);ink=[b[0]-sw/2,b[1]-sw/2,b[2]+sw/2,b[3]+sw/2];row['ink_bounds']=ink
  if min(ink)<-1e-6 or max(ink)>32+1e-6:row['errors'].append('clipping')
  if abs(max(ink[2]-ink[0],ink[3]-ink[1])-32)>1e-6:row['errors'].append('ink_extent')
  off_points=[];off_radii=[]
  for pi,p in enumerate(paths):
   for si,s in enumerate(p):
    for attr in ('start','end','control','control1','control2'):
     if hasattr(s,attr):
      z=getattr(s,attr)
      if abs(z.real-round(z.real))>1e-6 or abs(z.imag-round(z.imag))>1e-6:off_points.append([pi,si,attr,[z.real,z.imag]])
    if isinstance(s,Arc) and (abs(s.radius.real-round(s.radius.real))>1e-6 or abs(s.radius.imag-round(s.radius.imag))>1e-6):off_radii.append([pi,si,[s.radius.real,s.radius.imag]])
  if off_points:row['errors'].append('fractional_points');row['off_grid_points']=off_points
  if off_radii:row['errors'].append('fractional_radii');row['off_grid_radii']=off_radii
  # Build a proportional 32-ink reference WITHOUT calling the snapping/export function.
  original=[p for p in Document(io.StringIO(source)).paths() if len(p)];l,t,r,bot=bounds(original);scale=28/max(r-l,bot-t);shift=complex(16-(l+r)*scale/2,16-(t+bot)*scale/2)
  pre=ET.Element('svg',xmlns='http://www.w3.org/2000/svg',width='32',height='32',viewBox='0 0 32 32',fill='none',stroke='black',**{'stroke-width':'4','stroke-linecap':'round','stroke-linejoin':'round'})
  for p in original:ET.SubElement(pre,'path',d=p.scaled(scale).translated(shift).d())
  before=ET.tostring(pre,encoding='unicode');mb,ma=raster(before,8),raster(svg,8);tb,ta=topology(mb),topology(ma)
  row['topology_8x']=[tb,ta];row['ink_difference']=round(1-np.logical_and(mb,ma).sum()/max(1,np.logical_or(mb,ma).sum()),4)
  if tb!=ta:
   high=[topology(raster(before,16)),topology(raster(svg,16))];row['topology_16x']=high
   row['warnings'].append('parts_or_openings_changed' if high[0]!=high[1] else 'raster_sensitive_detail')
  if len(paths)!=len(original):row['warnings'].append('path_count_changed')
  if row['ink_difference']>.20:row['warnings'].append('large_ink_difference')
  row.update(before_uri=uri(before),after_uri=uri(svg))
 except Exception as e:row['errors'].append('check_error');row['exception']=repr(e)
 results.append(row)
 if len(results)%100==0:print('Checked',len(results),flush=True)
summary=dict(total=len(results),basic_pass=sum(not r['errors'] for r in results),basic_fail=sum(bool(r['errors']) for r in results),needs_visual_review=sum(bool(r['warnings']) for r in results),flagged=sum(bool(r['errors'] or r['warnings']) for r in results),errors=dict(Counter(e for r in results for e in r['errors'])),warnings=dict(Counter(e for r in results for e in r['warnings'])))
(OUT/'results.json').write_text(json.dumps(dict(summary=summary,rows=results),indent=2));print(json.dumps(summary,indent=2))
