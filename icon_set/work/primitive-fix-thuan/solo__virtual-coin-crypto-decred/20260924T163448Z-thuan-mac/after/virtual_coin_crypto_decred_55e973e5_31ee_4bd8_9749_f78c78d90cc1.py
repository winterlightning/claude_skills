"""Decred coin with a circular rim and balanced opposing curved logo strokes.
Plan: Decred coin with a circular rim and balanced opposing curved logo strokes.
Construction: No useful exact local Lucide match; source silhouette rebuilt from coherent curves.
Omissions: No symbol component omitted; opposing strokes share one rotated definition."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='55e973e5-31ee-4bd8-9749-f78c78d90cc1'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__virtual-coin-crypto-decred/20260924T163448Z-thuan-mac/reference/virtual coin crypto decred_55e973e5-31ee-4bd8-9749-f78c78d90cc1.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='virtual-coin-crypto-decred'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('virtual', 'coin', 'crypto', 'decred')

    def build(self):
        def path(name,start,steps,closed=False):
            p=start; members=[]
            for j,(kind,q,*args) in enumerate(steps):
                n=f'{name}-{j}'
                if p==q: continue
                if kind=='L': self.add_line(n,p,q)
                elif kind=='A': self.add_arc(n,p,q,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(n,p,(args[0],args[1],q))
                p=q;members.append(n)
            self.add_contour(name,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False):self.add_polyline(n,*p,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        circle('rim',24,24,20)
        for n,side in [('left',1),('right',-1)]:
         p=lambda x,y:(24+side*(x-24),24+side*(y-24))
         path(n,p(16,16),[('L',p(20,20)),('L',p(17,20)),('C',p(13,24),p(13,20),p(13,22)),('C',p(19,30),p(13,28),p(15,30))])
