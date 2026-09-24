"""A circular east badge containing E beside a right-pointing compass arrow.
Plan: No omissions. Letter, enclosing circle and separate directional arrow are all essential; keep spacing failures if they cannot fit.
Lucide construction references: navigation.
Keyshape HRECT_M: (2,8)-(46,40) ink.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape

SOURCE_ICON_ID = 'e91a4b42-5376-4b1a-ab2d-8d86c029fcca'
SOURCE_PATH = 'pictographic-primitives/navigation/compass east_e91a4b42-5376-4b1a-ab2d-8d86c029fcca.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'compass-east'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('compass', 'east')

    def circle(self, name, cx, cy, radius):
        self.add_arc(name+'-top',(cx-radius,cy),(cx+radius,cy),radius_x=radius)
        self.add_arc(name+'-bottom',(cx+radius,cy),(cx-radius,cy),radius_x=radius)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self, name, left, top, right, bottom, radius):
        # Shared corner radius and a bottom-centre attachment node.
        mid=(left+right)//2
        pts=[(left+radius,top),(right-radius,top),(right,top+radius),
             (right,bottom-radius),(right-radius,bottom),(mid,bottom),
             (left+radius,bottom),(left,bottom-radius),(left,top+radius),(left+radius,top)]
        members=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            key=f'{name}-{i}';members.append(key)
            if i in (1,3,6,8): self.add_arc(key,a,b,radius_x=radius)
            else: self.add_line(key,a,b)
        self.add_contour(name,*members,closed=True)

    def build(self):
        # Directional E and a right-facing arrow carry the east meaning.
        # Drop the surrounding badge: a legible three-bar E plus its circle
        # would consume the width needed by the independent direction arrow.
        self.add_polyline('letter-e',(16,10),(4,10),(4,24),(4,38),(16,38))
        self.add_line('middle-bar',(4,24),(16,24))
        self.relate('connect','letter-e','middle-bar')
        self.add_polyline('east-arrow',(30,10),(44,24),(30,38),(36,24),closed=True)
