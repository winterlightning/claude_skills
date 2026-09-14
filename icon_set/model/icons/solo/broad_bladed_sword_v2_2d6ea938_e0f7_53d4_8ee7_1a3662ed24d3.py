"""Aligned blade, grip and pommel; 11-unit blade width. Lucide sword informed the perpendicular guard and flat pommel; the tiny round pommel is replaced by a bar."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2d6ea938-e0f7-53d4-8ee7-1a3662ed24d3'
SOURCE_PATH = 'pictographic-primitives/war/antique sword_2d6ea938-e0f7-53d4-8ee7-1a3662ed24d3.svg'
AUTHOR = 'gpt-6'

class BroadBladedSwordV2(Solo48):
    icon_id = 'broad-bladed-sword-v2'
    variant_of = 'broad-bladed-sword'
    variant_label = 'Clearer construction and spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('broad', 'bladed', 'sword')

    def build(self):

        def L(n,a,b): self.add_line(n,a,b)
        def P(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def A(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def J(a,b): self.relate('connect',a,b)
        def C(n,x,y,r):
            A(n+'-upper',(x-r,y),(x+r,y),r)
            A(n+'-lower',(x+r,y),(x-r,y),r)
            self.add_contour(n,n+'-upper',n+'-lower',closed=True)

        # Shared blade/grip axis x+y=48; guard and pommel run perpendicular to it.
        P('blade',(15,25),(32,8),(42,6),(40,16),(23,33))
        P('guard',(11,21),(15,25),(19,29),(23,33),(27,37));J('guard','blade')
        L('grip',(19,29),(9,39));J('grip','guard')
        P('pommel',(6,36),(9,39),(12,42));J('pommel','grip')
