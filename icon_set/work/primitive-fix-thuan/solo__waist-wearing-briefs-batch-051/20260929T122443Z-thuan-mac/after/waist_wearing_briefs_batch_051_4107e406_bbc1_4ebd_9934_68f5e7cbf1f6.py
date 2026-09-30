"""The rejected waist had straight angular sides and a triangular crotch. Restore the curved waist, bowed waistband and two rounded leg openings from the original. No written feedback.
Symbol plan: Original waist; paired cubic sides and mirrored leg openings.
Keyshape VRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4107e406-bbc1-4ebd-9934-68f5e7cbf1f6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__waist-wearing-briefs-batch-051/20260929T122443Z-thuan-mac/reference/girdle_4107e406-bbc1-4ebd-9934-68f5e7cbf1f6.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'waist-wearing-briefs-batch-051'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('waist', 'wearing', 'briefs', 'batch', '051')

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

        path('left',(12,4),[('C',(14,18),(15,10),(16,13)),('C',(10,26),(13,22),(11,24)),('C',(8,34),(9,28),(8,31)),('L',(8,44))])
        path('right',(36,4),[('C',(34,18),(33,10),(32,13)),('C',(38,26),(35,22),(37,24)),('C',(40,34),(39,28),(40,31)),('L',(40,44))])
        path('band',(10,26),[('C',(38,26),(19,28),(29,28))])
        # Side band attaches at exactly authored points on the waist curves.
        path('leg-left',(8,34),[('C',(20,44),(14,34),(19,39))])
        path('leg-right',(40,34),[('C',(28,44),(34,34),(29,39))])
        join('left','leg-left');join('right','leg-right');join('left','band');join('right','band')
