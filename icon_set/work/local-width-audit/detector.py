"""Experimental contour-local width audit, not a production validation gate.

Equal-arclength sampling makes subdivisions of the same path immaterial.
Adjacent source primitives are included. Exclude only a local contour journey
of 2*stroke (8u on SOLO48), rather than entire adjacent primitive pairs.
Distances are sampled estimates; candidates are reviewed, never certified fails.
"""
import math
import numpy as np
from scipy.spatial import cKDTree
from icon_set.validation.internal_spacing import _samples
from icon_set.validation.circle_exceptions import circle_candidates
from shapely.geometry import LineString
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/design-repair/mapping.json'
AUTHOR='gpt-6'
PARAMETERS={'sample_step':0.25,'required_centerline':8.,'stroke_width':4.,'local_contour_exclusion':8.,'max_tangent_normal_dot':0.5,'minimum_narrow_run':2.,'blocking':False}

def contour_samples(primitives,step=.25):
 starts=[];vectors=[];lengths=[];names=[]
 for p in primitives:
  a,d,l=_samples(p)
  starts.extend(a);vectors.extend(d);lengths.extend(l);names.extend([p.element_id]*len(l))
 if not lengths:return None
 a=np.array(starts);v=np.array(vectors);l=np.array(lengths);end=np.cumsum(l);total=end[-1]
 n=max(2,math.ceil(total/step));s=(np.arange(n)+.5)*total/n
 idx=np.minimum(np.searchsorted(end,s),len(l)-1);frac=(s-(end-l)[idx])/l[idx]
 return a[idx]+v[idx]*frac[:,None],v[idx]/l[idx,None],s,total,np.array(names)[idx]

def analyze(icon,minimum_run=2.,step=.25):
 drawing=icon.draw();drawing.by_id();by=drawing.by_id();circles={c['element_id'] for c in circle_candidates('<svg/>',drawing)}
 found=[]
 for contour in drawing.contours:
  if contour.contour_id in circles:continue
  members=[by[n] for n in contour.members]
  samples=contour_samples(members,step)
  if samples is None:continue
  points,tangents,s,total,names=samples;n=len(s);ds=total/n
  pairs=cKDTree(points).query_pairs(8.+step,output_type='ndarray')
  if len(pairs)==0:continue
  i,j=pairs.T;travel=np.abs(s[i]-s[j]);travel=np.minimum(travel,total-travel) if contour.closed else travel
  keep=travel>=8.;i,j=i[keep],j[keep]
  if not len(i):continue
  # Directed distances: project each sample onto the opposing tiny segment.
  ii=np.r_[i,j];jj=np.r_[j,i];delta=points[ii]-points[jj]
  proj=np.clip(np.sum(delta*tangents[jj],axis=1),-ds/2,ds/2)
  targets=points[jj]+tangents[jj]*proj[:,None];r=targets-points[ii];dist=np.linalg.norm(r,axis=1)
  # Use the actual nearest nonlocal boundary, not any conveniently oriented pair.
  order=np.lexsort((dist,ii));ii=ii[order];jj=jj[order];dist=dist[order];r=r[order];targets=targets[order]
  first=np.r_[True,ii[1:]!=ii[:-1]];ii=ii[first];jj=jj[first];dist=dist[first];r=r[first];targets=targets[first]
  normal=r/np.maximum(dist[:,None],1e-12)
  opposing=(np.abs(np.sum(normal*tangents[ii],axis=1))<=.5)&(np.abs(np.sum(normal*tangents[jj],axis=1))<=.5)
  ok=(dist<8.-.01)&opposing
  valid=np.zeros(n,dtype=bool);valid[ii[ok]]=True
  distances=np.full(n,np.inf);distances[ii]=dist;dest=np.full(n,-1,dtype=int);dest[ii]=jj
  target_points=np.zeros((n,2));target_points[ii]=targets
  # Test visibility across the opening against every contour in the drawing.
  # Endpoint portions belong to the two bounding strokes and are trimmed.
  segments=[]
  for p in drawing.primitives:
   aa,dd,ll=_samples(p)
   segments.extend(LineString([u,u+v]) for u,v in zip(aa,dd))
  from shapely.strtree import STRtree
  tree=STRtree(segments) if segments else None
  for k in np.flatnonzero(valid):
   p,q=points[k],target_points[k];distance=distances[k]
   if distance<=4:continue # ink overlap, retained as a geometric candidate
   t=2.01/distance
   connector=LineString([p+(q-p)*t,q-(q-p)*t])
   if tree is not None and len(tree.query(connector,predicate='intersects')):valid[k]=False
  # Connected narrow runs follow the original contour across primitive boundaries.
  if contour.closed and np.any(~valid):
   offset=(np.flatnonzero(~valid)[0]+1)%n;indices=np.roll(np.arange(n),-offset)
  else:indices=np.arange(n)
  runs=[];run=[]
  for k in indices:
   if valid[k]:run.append(int(k))
   elif run:runs.append(run);run=[]
  if run:runs.append(run)
  for run in runs:
   length=len(run)*ds
   if length+1e-8<minimum_run:continue
   k=min(run,key=lambda k:distances[k]);other=dest[k]
   found.append({'contour':contour.contour_id,'elements':[str(names[k]),str(names[other])],
    'sustained_length':round(length,4),'centerline_distance':round(float(distances[k]),4),'ink_gap':round(float(distances[k]-4),4),
    'nearest_points':[points[k].tolist(),target_points[k].tolist()],
    'run_points':points[run].tolist(),'status':'review'})
 return {'status':'review' if found else 'pass','findings':found,'parameters':dict(PARAMETERS,sample_step=step,minimum_narrow_run=minimum_run)}
