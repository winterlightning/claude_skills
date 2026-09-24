"""powder. Revision: Broaden the powder mound and smooth its rounded peak; retain lid band and jar occlusion. Omit lid overhang.
Construction: No useful direct Lucide match; supplied source silhouette. Preserve source-facing direction and arrangement.
Keyshape SQUARE; exact contract extremes, stroke four. No validation exceptions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='05ec6a05-5792-40e2-930e-254cb25d815c'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__powder-jar-and-small-heap/20260924T150007Z-thuan-mac/reference/powder_05ec6a05-5792-40e2-930e-254cb25d815c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='powder-jar-and-small-heap'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('powder',)

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

        path('lid',(10,6),[('L',(30,6)),('A',(34,10),4,4,True),('L',(34,14)),('L',(6,14)),('L',(6,10)),('A',(10,6),4,4,True)],True)
        path('jar',(6,14),[('L',(6,36)),('A',(10,40),4,4,False),('L',(13,40))])
        line('right-wall',(34,14),(34,19))
        path('heap',(25,42),[('A',(22,38),4,4,True),('L',(28,30)),('C',(36,30),(31,26),(33,26)),('L',(41,37)),('C',(38,42),(43,40),(42,42)),('L',(25,42))],True)

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)
