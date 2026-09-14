"""Corner-first experiment; production validation is unchanged."""
from pathlib import Path
import sys,json,math,hashlib,inspect,time
import numpy as np
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import get_context
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.validation.internal_spacing import _samples
from icon_set.model.icons.registry import factories
from shapely.geometry import LineString
from shapely.strtree import STRtree
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/model/icons/solo/'
AUTHOR='gpt-6'
W=Path(__file__).parent
XS=[8.,12.,16.]
REGISTRY={}

def path_points(primitives):
 result=[]
 for p in primitives:
  a,d,l=_samples(p)
  if len(l):
   result.extend(a.tolist());last=(a[-1]+d[-1]).tolist()
 if result:result.append(last)
 return np.array(result)
def arclength(points):return np.r_[0,np.cumsum(np.linalg.norm(np.diff(points,axis=0),axis=1))]
def at(points,s,x):
 x=min(x,float(s[-1]));i=min(int(np.searchsorted(s,x,side='right')-1),len(points)-2);i=max(0,i)
 return points[i]+(points[i+1]-points[i])*(x-s[i])/max(1e-12,s[i+1]-s[i])
def nearest(p,points):
 a=points[:-1];v=np.diff(points,axis=0);l2=np.sum(v*v,axis=1);t=np.clip(np.sum((p-a)*v,axis=1)/np.maximum(l2,1e-12),0,1)
 q=a+t[:,None]*v;dist=np.linalg.norm(q-p,axis=1);i=np.argmin(dist);return float(dist[i]),q[i]
def get_arms(members,closed):
 # Smooth joins merge: merely splitting a straight or curved side adds no corner.
 m=len(members);parts=[path_points([p]) for p in members]
 if any(len(p)<2 for p in parts):return []
 corners=[]
 for i in range(m if closed else m-1):
  j=(i+1)%m;a=parts[i][-2]-parts[i][-1];b=parts[j][1]-parts[j][0]
  cosine=np.clip(np.dot(a,b)/np.linalg.norm(a)/np.linalg.norm(b),-1,1);angle=math.degrees(math.acos(cosine))
  if angle<165:corners.append((i,angle))
 stops={i for i,_ in corners};found=[]
 for i,angle in corners:
  left=[];k=i
  while True:
   left.append(k);prev=(k-1)%m
   if (not closed and k==0) or prev in stops or prev==i:break
   k=prev
  right=[];k=(i+1)%m
  while True:
   right.append(k)
   if k in stops or (not closed and k==m-1) or (k+1)%m==(i+1)%m:break
   k=(k+1)%m
  # A closed contour with only one detected corner meets itself: no independent arms.
  if set(left)&set(right):continue
  a=path_points([members[k] for k in reversed(left)])[::-1]
  b=path_points([members[k] for k in right])
  found.append((a,b,angle,[members[i].element_id,members[(i+1)%m].element_id]))
 return found

def analyze(icon,xs=XS):
 drawing=icon.draw();by=drawing.by_id();lines=[]
 for p in drawing.primitives:
  pts=path_points([p])
  if len(pts)>1:lines.append(LineString(pts))
 tree=STRtree(lines) if lines else None
 records=[]
 for contour in drawing.contours:
  for a,b,angle,names in get_arms([by[n] for n in contour.members],contour.closed):
   sa,sb=arclength(a),arclength(b);measurements={}
   for x in xs:
    probes=[];blocked=False
    for arm,s,opposite in [(a,sa,b),(b,sb,a)]:
     p=at(arm,s,x);distance,q=nearest(p,opposite)
     if distance>.001:
      # Check the centerline connector is not hidden by a third boundary.
      v=q-p;connector=LineString([p+v*.001,q-v*.001]);blocked|=bool(len(tree.query(connector,predicate='crosses'))) if tree else False
     probes.append({'point':p.tolist(),'target':q.tolist(),'distance':distance,'walked':min(x,float(s[-1]))})
    short=min(sa[-1],sb[-1])<x-1e-6
    width=min(p['distance'] for p in probes)
    if blocked:status='occluded-review'
    elif not short:status='narrow' if width<7.99 else 'clear'
    else:
     # Inspect the whole short feature; report separately from an actual X probe.
     maxima=[]
     for arm,s,opposite in [(a,sa,b),(b,sb,a)]:
      limit=min(x,float(s[-1]));positions=np.linspace(0,limit,max(2,math.ceil(limit/.25)+1));maxima.append(max(nearest(at(arm,s,t),opposite)[0] for t in positions))
     status='short-narrow' if min(maxima)<7.99 else 'short-opens'
    measurements[str(int(x))]={'status':status,'ink_gap':round(width-4,4),'centerline_distance':round(width,4),'short_side':bool(short),'probes':probes}
   records.append({'contour':contour.contour_id,'corner':a[0].tolist(),'angle':round(angle,2),'elements':names,'side_lengths':[round(float(sa[-1]),3),round(float(sb[-1]),3)],'measurements':measurements})
 return records

def one(entry):
 ident,path,digest=entry
 try:
  obj=REGISTRY[ident]();svg=obj.to_svg();p=ROOT/'icon_set/dist/qa/solo'/ident/'metrics.json';base=json.loads(p.read_text()) if p.exists() else {};match=base.get('svg_sha256')==hashlib.sha256(svg.encode()).hexdigest()
  return {'id':ident,'baseline':base.get('status') if match else 'unmatched','corners':analyze(obj),'source_unchanged':hashlib.sha256(Path(path).read_bytes()).hexdigest()==digest}
 except Exception as e:return {'id':ident,'error':str(e)}
if __name__=='__main__':
 REGISTRY=factories();inventory=[]
 for ident,cls in sorted(REGISTRY.items()):
  if cls.family=='solo':
   p=Path(inspect.getsourcefile(cls));inventory.append((ident,str(p),hashlib.sha256(p.read_bytes()).hexdigest()))
 (W/'inventory.json').write_text(json.dumps(inventory));start=time.time();rows=[]
 with ProcessPoolExecutor(max_workers=4,mp_context=get_context('fork')) as pool:
  for i,r in enumerate(pool.map(one,inventory,chunksize=8),1):
   rows.append(r)
   if i%500==0:print(i,'/',len(inventory),round(time.time()-start),flush=True)
 (W/'results.json').write_text(json.dumps(rows));summary={'total':len(rows),'errors':[r for r in rows if 'error' in r],'seconds':round(time.time()-start,1),'changed':sum(r.get('source_unchanged')==False for r in rows),'unmatched':sum(r.get('baseline')=='unmatched' for r in rows),'settings':{'sample_step':.25,'corner_turn_min_degrees':15,'required_centerline':8,'X':XS,'short_rule':'Either side cannot open to 8u anywhere before X or its next corner; report separately.'},'counts':{}}
 for x in ['8','12','16']:
  groups={}
  for label,allowed in [('full_x_narrow',{'narrow'}),('short_narrow',{'short-narrow'}),('combined',{'narrow','short-narrow'}),('occluded',{'occluded-review'})]:
   rs=[r for r in rows if any(c['measurements'][x]['status'] in allowed for c in r.get('corners',[]))];groups[label]={'icons':len(rs),'currently_pass':sum(r['baseline']=='pass' for r in rs)}
  summary['counts'][x]=groups
 (W/'summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2),flush=True)
