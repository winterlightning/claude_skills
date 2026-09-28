"""pheasant. Revision: Round head and breast, restore a graceful raised tail and bent legs with feet. Omit tiny eye and internal wing detail.
Construction: Lucide bird: coherent rounded breast and purposeful directional silhouette. Preserve source-facing direction and arrangement.
Keyshape SQUARE; exact contract extremes, stroke four. No validation exceptions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='7ec3f373-1143-413c-9c5d-6a91026ab479'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__pheasant-raised-tail/20260924T142504Z-thuan-mac/reference/pheasant_7ec3f373-1143-413c-9c5d-6a91026ab479.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='pheasant-raised-tail'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('pheasant',)

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

        path('body',(6,15),[('C',(15,6),(9,11),(9,6)),('C',(21,16),(21,6),(21,11)),('C',(28,25),(21,21),(25,22)),('C',(33,30),(30,27),(32,29)),('C',(29,35),(34,33),(31,35)),('C',(19,35),(26,37),(22,37)),('C',(12,26),(14,33),(12,30)),('L',(12,20)),('A',(6,15),6,5,False)])
        path('tail',(28,25),[('L',(42,6)),('C',(33,30),(41,17),(38,25))]);join('tail','body')
        poly('leg-left',(19,35),(16,42),(12,42));poly('leg-right',(29,35),(29,42),(25,42));join('leg-left','body');join('leg-right','body')

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)
