"""pruner. Revision: Restore curved pruning blade and two splayed handles beside a leafy stem. Reduce secondary leaf and handle outlines to maintain spacing.
Construction: Lucide scissors and sprout: distinct pivot attachments and coherent leaf contour. Preserve source-facing direction and arrangement.
Keyshape SQUARE; exact contract extremes, stroke four. No validation exceptions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='a757f97f-925d-4ec4-a7e5-e647c6df42dd'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__pruning-shears-leafy-stem/20260924T150007Z-thuan-mac/reference/pruner_a757f97f-925d-4ec4-a7e5-e647c6df42dd.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='pruning-shears-leafy-stem'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('pruner',)

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

        path('leaf',(6,23),[('C',(16,6),(6,13),(10,8)),('C',(6,23),(20,15),(16,22))],True)
        line('stem',(6,23),(6,42))
        path('blade',(31,25),[('L',(30,6)),('C',(31,25),(43,18),(39,22))],True)
        path('handle-left',(31,25),[('C',(27,30),(29,25),(28,28)),('L',(23,42))])
        path('handle-right',(31,25),[('C',(36,30),(34,25),(35,28)),('L',(42,42))])

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)
