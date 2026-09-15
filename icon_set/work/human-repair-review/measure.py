from audit import *
import numpy as np
from scipy.spatial import cKDTree

def samples(p,n=1024):
 if isinstance(p,Line):return np.linspace(p.start.as_tuple(),p.end.as_tuple(),n)
 if isinstance(p,Bezier):return np.array(p.sample(n))
 g=arc_geometry(p);ts=np.linspace(g.start_angle,g.start_angle+g.delta_angle,n);return np.stack([g.center_x+g.radius_x*np.cos(ts),g.center_y+g.radius_y*np.sin(ts)],axis=1)
def gap(by,heads,torsos):
 if not torsos:return None
 a=np.concatenate([samples(by[k]) for k in heads]);b=np.concatenate([samples(by[k]) for k in torsos]);dist,idx=cKDTree(a).query(b);j=int(dist.argmin());return dict(ink_gap=float(dist[j]-4),head_point=a[idx[j]].tolist(),body_point=b[j].tolist())
if __name__=='__main__':
 audit=json.loads((OUT/'audit.json').read_text());source={x['row']['icon_id']:x for x in rows}
 for a in audit:
  i=load(source[a['icon_id']]);by=i.draw().by_id()
  for f in a['figures']:f['measured']=gap(by,f['head_members'],f['torso_members'])
  if a['type']!='stick-figure':print(a['number'],a['type'],[(f['head'],f['measured']) for f in a['figures']])
 (OUT/'audit.json').write_text(json.dumps(audit,indent=2))
