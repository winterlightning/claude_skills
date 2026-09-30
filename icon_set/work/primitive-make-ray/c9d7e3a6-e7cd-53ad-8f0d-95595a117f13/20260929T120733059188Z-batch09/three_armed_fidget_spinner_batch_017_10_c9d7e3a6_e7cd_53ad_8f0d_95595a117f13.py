"""Fidget spinner: rejected outline is angular and lacks all three outer bearing holes. Restore smooth three-lobe outline and bearings. Restore smooth three-lobed body and four bearing marks; small holes simplify to dots for spacing.
Symbol plan: Mirrored smooth lobes and spaced bearing marks; no useful exact Lucide match.
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

        path('spinner',(15,15),[('A',(33,15),9,9,True),('C',(35,24),(30,19),(31,23)),('C',(42,33),(41,24),(42,29)),('A',(33,42),9,9,True),('C',(24,37),(29,42),(27,39)),('C',(15,42),(21,39),(19,42)),('A',(6,33),9,9,True),('C',(13,24),(6,29),(7,24)),('C',(15,15),(17,23),(18,19))],True)
        for n,x,y in [('top',24,15),('left',15,33),('right',33,33),('hub',24,26)]:self.add_dot(n,(x,y))
