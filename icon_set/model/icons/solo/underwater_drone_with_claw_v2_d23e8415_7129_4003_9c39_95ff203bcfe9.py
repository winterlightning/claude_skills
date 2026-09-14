"""Smooth waterline, flat stern and a clearly open curved pincer. The arm is lowered 10 units below the hull; source establishes the submersible and manipulator, with no exact Lucide counterpart."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd23e8415-7129-4003-9c39-95ff203bcfe9'
SOURCE_PATH = 'pictographic-primitives/war/underwater drone 1_d23e8415-7129-4003-9c39-95ff203bcfe9.svg'
AUTHOR = 'gpt-6'

class UnderwaterDroneWithClawV2(Solo48):
    icon_id = 'underwater-drone-with-claw-v2'
    variant_of = 'underwater-drone-with-claw'
    variant_label = 'Clearer construction and spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('underwater', 'drone', 'with', 'claw')

    def build(self):

        def L(n,a,b): self.add_line(n,a,b)
        def P(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def A(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def J(a,b): self.relate('connect',a,b)
        def C(n,x,y,r):
            A(n+'-upper',(x-r,y),(x+r,y),r)
            A(n+'-lower',(x+r,y),(x-r,y),r)
            self.add_contour(n,n+'-upper',n+'-lower',closed=True)

        A('water-a',(6,8),(18,8),6,2)
        A('water-b',(18,8),(30,8),6,2,s=False)
        A('water-c',(30,8),(42,8),6,2)
        self.add_contour('water','water-a','water-b','water-c')
        L('hull-top',(14,20),(30,20))
        A('nose-top',(30,20),(34,24),4)
        A('nose-bottom',(34,24),(30,28),4)
        L('hull-bottom-r',(30,28),(22,28))
        L('hull-bottom-l',(22,28),(14,28))
        L('stern-low',(14,28),(14,24))
        L('stern-high',(14,24),(14,20))
        self.add_contour('hull','hull-top','nose-top','nose-bottom','hull-bottom-r','hull-bottom-l','stern-low','stern-high',closed=True)
        P('tail',(6,18),(14,24),(6,30));J('tail','hull')
        P('arm',(22,28),(22,38),(36,38));J('arm','hull')
        A('claw-top',(42,34),(36,38),6,4,s=False)
        A('claw-bottom',(36,38),(42,42),6,4,s=False)
        self.add_contour('claw','claw-top','claw-bottom');J('claw','arm')
