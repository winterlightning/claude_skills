"""locust. Revision: Smooth tapered body, oval head, prominent folded jumping leg and three ground contacts; omit tiny eye.
Construction: No useful direct Lucide match; supplied source silhouette. Preserve source-facing direction and arrangement.
Keyshape HRECT_L; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5c07b2b0-22a5-4eba-a68b-9d0f0cf7fbd8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/locust_5c07b2b0-22a5-4eba-a68b-9d0f0cf7fbd8.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='locust'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('locust',)

    def build(self):
        # Each contour owns its shape. Repeated parts share dimensions and axes.
        def path(n,start,steps,closed=False):
            p=start; members=[]
            for j,s in enumerate(steps):
                k=f'{n}-{j}';kind,q,*v=s
                if kind=='L': self.add_line(k,p,q)
                elif kind=='A': self.add_arc(k,p,q,radius_x=v[0],radius_y=v[1],sweep=v[2])
                elif kind=='C': self.add_bezier(k,p,(v[0],v[1],q))
                members.append(k);p=q
            self.add_contour(n,*members,closed=closed)
        def line(n,a,b):self.add_line(n,a,b)
        def poly(n,*p):self.add_polyline(n,*p)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def join(a,b):self.relate('connect',a,b)

        path('head',(32,22),[('A',(44,22),6,7,True),('A',(32,22),6,7,True)],True)
        line('antenna',(38,15),(31,8));join('antenna','head')
        path('body',(32,22),[('C',(4,25),(22,22),(10,21)),('C',(30,31),(6,34),(21,36)),('L',(38,29))])
        join('body','head')
        path('hind-leg',(4,40),[('L',(8,14)),('A',(12,13),3,3,True),('L',(25,28)),('L',(22,40))])
        join('hind-leg','body')
        poly('foreleg',(38,29),(39,32),(44,40));join('foreleg','head')

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)
