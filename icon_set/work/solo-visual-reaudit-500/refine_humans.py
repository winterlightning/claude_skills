from humans import *
import math

def current(n):
 r=next(r for r in records if r['number']==n);return r,create(r['icon_id']).draw()

if __name__=='__main__':
 for n,spec in specs.items():
  r,d=current(n);head,body,old,s,c,radius=spec;vx,vy=c[0]-s[0],c[1]-s[1]
  bounds=create(r['icon_id']).keyshape_bounds();limits=[bounds[0]+2,bounds[1]+2,bounds[2]-2,bounds[3]-2];pm={}
  for p in d.primitives:
   if not isinstance(p,Line) or s not in [p.start.as_tuple(),p.end.as_tuple()]:continue
   other=p.end.as_tuple() if p.start.as_tuple()==s else p.start.as_tuple();dot=vx*(other[0]-s[0])+vy*(other[1]-s[1])
   if dot<=0:continue
   trials=[]
   for dx in range(-8,9):
    for dy in range(-8,9):
     q=(other[0]+dx,other[1]+dy)
     if not (limits[0]<=q[0]<=limits[2] and limits[1]<=q[1]<=limits[3]):continue
     if other[0] in (limits[0],limits[2]) and dx:continue
     if other[1] in (limits[1],limits[3]) and dy:continue
     if vx*(q[0]-s[0])+vy*(q[1]-s[1])<=0:trials.append((dx*dx+dy*dy,q))
   if trials:pm[other]=min(trials)[1]
  if pm:save(n,emit(d,{}, {},pm),r['reason']+' Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.');print('  points',pm)
