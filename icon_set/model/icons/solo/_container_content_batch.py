"""Shared typed shapes for user-authorized complete container content subjects."""
def path(o,n,start,*steps,closed=False):
 p=start;members=[]
 for i,s in enumerate(steps):
  name=f'{n}-{i}'
  if s[0]=='L':o.add_line(name,p,s[1])
  else:o.add_arc(name,p,s[1],radius_x=s[2],radius_y=s[3],sweep=s[4],large_arc=s[5] if len(s)>5 else False)
  p=s[1];members.append(name)
 o.add_contour(n,*members,closed=closed)
def cross(o,n,x,y,r):
 for i,p in enumerate(((x-r,y),(x+r,y),(x,y-r),(x,y+r))):o.add_line(f'{n}-{i}',(x,y),p)
def contacts(o):
 ps=list(o.primitives)
 for i,a in enumerate(ps):
  for b in ps[i+1:]:
   if {a.start,a.end}&{b.start,b.end}:o.relate('connect',a.element_id,b.element_id)
def bust(o,n,cx=18,cy=12,r=6,left=4,right=32,bottom=40):
 from ._payments_batch01 import circle
 circle(o,n+'-head',cx,cy,r)
 top=cy+r+8
 o.add_arc(n+'-shoulders',(left,bottom),(right,bottom),radius_x=(right-left)//2,radius_y=bottom-top)
def car(o,n,top=26,bottom=40):
 path(o,n,(8,bottom),('L',(8,top+5)),('L',(12,top)),('L',(36,top)),('L',(40,top+5)),('L',(40,bottom)),('L',(8,bottom)),closed=True)
 for side,x in enumerate((12,36)):
  o.add_line(n+f'-wheel-{side}',(x,bottom),(x,bottom+4));o.relate('connect',n,n+f'-wheel-{side}')
def bolt(o,n,points):o.add_polyline(n,*points)
