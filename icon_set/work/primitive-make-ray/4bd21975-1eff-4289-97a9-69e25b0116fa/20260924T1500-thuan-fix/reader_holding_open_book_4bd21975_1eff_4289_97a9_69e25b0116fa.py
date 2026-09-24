"""newspaper read man. Revision: Restore angular open pages and separate rounded hands; keep circular upper head visible above book. Omit facial marks and hidden chin/torso.
Construction: Shared human_ref/user.svg: rounded cranium. Torso/chin hidden by book; no detached stick-figure torso is emitted. Preserve source-facing direction and arrangement.
Keyshape SQUARE; exact contract extremes, stroke four. No validation exceptions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4bd21975-1eff-4289-97a9-69e25b0116fa'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__reader-holding-open-book/20260924T150007Z-thuan-mac/reference/newspaper read man_4bd21975-1eff-4289-97a9-69e25b0116fa.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='reader-holding-open-book'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('newspaper', 'read', 'man')

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

        path('head',(14,18),[('L',(14,16)),('A',(34,16),10,10,True),('L',(34,18))])
        poly('book-top',(10,30),(10,26),(24,30),(38,26),(38,30))
        path('book-bottom',(10,38),[('L',(10,40)),('L',(24,42)),('L',(38,40)),('L',(38,38))])
        line('spine',(24,30),(24,42))
        path('left-hand',(10,30),[('A',(10,38),4,4,True),('A',(10,30),4,4,True)],True)
        path('right-hand',(38,30),[('A',(38,38),4,4,True),('A',(38,30),4,4,True)],True)

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)
