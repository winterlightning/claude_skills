"""Fidget spinner: rejected outline is angular and lacks all three outer bearing holes. Restore smooth three-lobe outline and bearings. Rebuild as three circular bearing lobes joined to a central axle, omitting the crowded extra rim.
Symbol plan: Three equal circular bearings with shared central axle; no useful exact Lucide match.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c9d7e3a6-e7cd-53ad-8f0d-95595a117f13'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-armed-fidget-spinner-batch-017-10/20260929T115456Z-thuan-mac/reference/toys fidget spinner_c9d7e3a6-e7cd-53ad-8f0d-95595a117f13.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'three-armed-fidget-spinner-batch-017-10'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('three', 'armed', 'fidget', 'spinner', 'batch', '017', '10')

    def build(self):

        def path(n,start,steps,closed=False):
            point=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L': self.add_line(m,point,end)
                elif kind=='A': self.add_arc(m,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(m,point,(args[0],args[1],end))
                point=end; members.append(m)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        for n,x,y in [('top',24,12),('left',12,36),('right',36,36)]:circle(n,x,y,6)
        line('top-arm',(24,18),(24,24));line('left-arm',(24,24),(12,30));line('right-arm',(24,24),(36,30))
        join('top-arm','top');join('left-arm','left');join('right-arm','right')
        join('top-arm','left-arm');join('top-arm','right-arm');join('left-arm','right-arm')
