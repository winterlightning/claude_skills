"""winter sport ice hockey.
Symbol plan: HRECT_L (4,8)-(44,40). Head radius5 center24,13; torso neck24,26 has exact8 centerline gap. Curved forward torso, two bent legs, diagonal stick and left puck.
Shared human_ref/full_body_ref.png controls circular head and round-ended action limbs. Supplied original controls forward hockey pose and puck.
Deliberate anatomical asymmetry preserves the supplied pose."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd95d80d0-b910-4819-8ffd-fb7a67b374db'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hockey-player-reference-d95d80d0/20260929T105554Z-thuan-mac/reference/winter sport ice hockey_d95d80d0-b910-4819-8ffd-fb7a67b374db.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hockey-player-reference-d95d80d0'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hockey', 'player', 'reference', 'd95d80d0')
    
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def bez(n,a,*segments): self.add_bezier(n,a,*segments)
        def path(n,*points,closed=False): self.add_polyline(n,*points,closed=closed)
        def contour(n,*members,closed=False): self.add_contour(n,*members,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r)
            arc(n+'b',(x+r,y),(x-r,y),r)
            contour(n,n+'a',n+'b',closed=True)


        circle('head',24,13,5)
        bez('torso',(24,26),((24,28),(29,28),(32,31)))
        path('front-leg',(32,31),(25,35),(28,40))
        path('back-leg',(32,31),(34,35),(44,40))
        path('arm',(24,26),(18,28));path('stick',(18,28),(14,38),(12,40))
        line('puck',(4,40),(4,40))
        for a,b in [('torso','front-leg'),('torso','back-leg'),('front-leg','back-leg'),('torso','arm'),('arm','stick')]:connect(a,b)
        self.mark_human_figure('player',head='head',torso='torso',torso_junction='start')

