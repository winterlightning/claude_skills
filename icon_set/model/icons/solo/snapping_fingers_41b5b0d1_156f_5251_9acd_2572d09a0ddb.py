"""A snapping hand with smooth palm and rounded diagonal raised finger, thumb and tucked finger tips. Envelope (6,6)-(42,42). Intentional diagonal gesture, matching rounded finger caps.
Construction reference: Lucide hand: coherent palm curve and rounded fingertip construction; human-reference vocabulary.
Omissions: One folded finger crease omitted to preserve clear interior."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '41b5b0d1-156f-5251-9acd-2572d09a0ddb'
SOURCE_PATH = 'pictographic-primitives/wayfinding/hand snapping finger_41b5b0d1-156f-5251-9acd-2572d09a0ddb.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='snapping-fingers'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/wayfinding"
    aliases=()
    keywords=('hand', 'snapping', 'finger')
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        line=self.add_line; poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path('hand',(10,29),[('L',(14,19)),('C',(20,21),(16,16),(22,17)),('L',(18,27)),('L',(35,11)),('C',(42,14),(40,6),(42,10)),('C',(40,18),(42,16),(41,17)),('L',(29,29)),('C',(34,34),(35,26),(39,30)),('L',(29,39)),('C',(22,42),(27,41),(24,42)),('C',(10,29),(15,42),(8,36))],True)
        line('snap-up',(19,6),(19,9));line('snap-left',(6,8),(8,10))
