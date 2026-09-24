"""beetle. Revision: Restore oval wing case with central seam, bent mirrored legs and distinct rounded head. Omit tiny antenna hooks.
Construction: Lucide bug: mirror leg pairs around an oval divided shell. Preserve source-facing direction and arrangement.
Keyshape SQUARE; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c2f25e0c-a7a3-42f1-a324-58dcfcc899f6'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/beetle_c2f25e0c-a7a3-42f1-a324-58dcfcc899f6.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='oval-beetle-with-six-bent-legs'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/misc'
    aliases=()
    keywords=('beetle',)

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

        path('shell',(24,18),[('A',(34,28),10,10,True),('L',(34,32)),('A',(24,42),10,10,True),('A',(14,32),10,10,True),('L',(14,28)),('A',(24,18),10,10,True)],True)
        line('seam',(24,18),(24,42))
        path('head',(16,22),[('L',(16,18)),('A',(32,18),8,8,True),('L',(32,22))]);join('head','shell')
        for s,label in [(-1,'left'),(1,'right')]:
            poly('antenna-'+label,(24,10),(24+s*7,6));join('antenna-'+label,'head')
            poly(label+'-upper',(24+s*8,22),(24+s*18,18),(24+s*18,14));join(label+'-upper','shell');join(label+'-upper','head')
            line(label+'-middle',(24+s*10,30),(24+s*18,30));join(label+'-middle','shell')
            poly(label+'-lower',(24+s*8,38),(24+s*16,40),(24+s*18,42));join(label+'-lower','shell')

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)
