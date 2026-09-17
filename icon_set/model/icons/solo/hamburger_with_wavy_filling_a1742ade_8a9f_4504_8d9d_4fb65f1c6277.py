"""Classic Fast Food Hamburger."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a1742ade-8a9f-4504-8d9d-4fb65f1c6277'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/double burger_a1742ade-8a9f-4504-8d9d-4fb65f1c6277.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hamburger-with-wavy-filling'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('hamburger', 'burger', 'bun', 'filling', 'fast food', 'sandwich', 'meal')

    def build(self):
        # Plan: Domed bun, regular wavy filling, open lower bun. Lucide sandwich layer separation. Small sesame marks omitted, shared horizontal center. Envelope (4,8)-(44,40).
        self.add_arc('top',(4,17),(44,17),radius_x=20,radius_y=9)
        self.add_line('base',(44,17),(4,17));self.add_contour('upper-bun','top','base',closed=True)
        for i in range(4):
         x=4+10*i;y=29 if i%2==0 else 25
         self.add_bezier(f'wave-{i}',(x,27),((x+3,y),(x+7,y),(x+10,27)))
        self.add_contour('filling',*[f'wave-{i}' for i in range(4)])
        self.add_bezier('lower-l',(4,37),((4,39),(7,40),(10,40)))
        self.add_line('lower-base',(10,40),(38,40))
        self.add_bezier('lower-r',(38,40),((41,40),(44,39),(44,37)))
        self.add_contour('lower-bun','lower-l','lower-base','lower-r')
