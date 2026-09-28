"""acupuncture head. Revision: Restore two outlined pin heads with shorter diagonal needles, smooth the head silhouette and jaw. Omit eye and ear.
Construction: Shared human_ref/user.svg: round cranium; source needles interrupt scalp, no detached body. Preserve source-facing direction and arrangement.
Keyshape SQUARE; exact contract extremes, stroke four. No validation exceptions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='e69ebb9e-0aa1-49b0-95da-1293457f990b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__profile-head-two-acupuncture-needles/20260924T150007Z-thuan-mac/reference/acupuncture head_e69ebb9e-0aa1-49b0-95da-1293457f990b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='profile-head-two-acupuncture-needles'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('acupuncture', 'head')

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

        circle('pin-upper',14,9,3);circle('pin-left',9,25,3)
        path('head',(19,42),[('L',(19,39)),('C',(16,36),(19,38),(17,37))])
        path('face',(29,13),[('A',(38,22),9,9,True),('L',(42,30)),('L',(37,31)),('L',(37,34)),('A',(31,40),6,6,True),('L',(31,42))])
        line('needle-upper',(14,12),(20,18));line('needle-left',(12,25),(17,27))

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)
