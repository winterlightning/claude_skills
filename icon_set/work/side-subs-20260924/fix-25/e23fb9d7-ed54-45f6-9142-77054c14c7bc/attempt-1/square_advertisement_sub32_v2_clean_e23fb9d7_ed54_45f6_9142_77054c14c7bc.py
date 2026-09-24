"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = 'e23fb9d7-ed54-45f6-9142-77054c14c7bc'
SOURCE_PATH = 'pictographic-primitives/other/rectangle ad text_e23fb9d7-ed54-45f6-9142-77054c14c7bc.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rounded square frame', 'uppercase A', 'uppercase D')
class Drawing(Sub32):
    icon_id = 'square-advertisement-sub32-v2-clean'
    variant_of = 'square-advertisement-sub32-v2'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Square Advertisement Icon', 'core_parts': ('rounded square frame', 'uppercase A', 'uppercase D'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Widen the A counter and preserve a separate D, using grid-fitted approved glyph centerlines.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-d-uppercase')
    def build(self):
        self.box('frame',2,2,30,30,2)
        self.add_line('text-A-0-0-0-0',(7, 24),(10, 9))
        self.primitives.append(Bezier('text-A-0-0-1-0',Point(*(10, 9)),Point(*(11, 9)),(((10, 8), (11, 8), (11, 9)),)))
        self.add_line('text-A-0-0-1-1',(11, 9),(14, 24))
        self.add_contour('glyph-A-0-0-1',*['text-A-0-0-1-0', 'text-A-0-0-1-1'],closed=False)
        self.add_line('text-A-0-1-0-0',(8, 17),(13, 17))
        self.add_line('text-D-0-0-0-0',(20, 8),(22, 8))
        self.primitives.append(Bezier('text-D-0-0-0-1',Point(*(22, 8)),Point(*(22, 24)),(((26, 8), (26, 24), (22, 24)),)))
        self.add_contour('glyph-D-0-0-0',*['text-D-0-0-0-0', 'text-D-0-0-0-1'],closed=False)
        self.add_line('text-D-0-0-1-0',(22, 24),(20, 24))
        self.add_line('text-D-0-0-1-1',(20, 24),(20, 8))
        self.add_contour('glyph-D-0-0-1',*['text-D-0-0-1-0', 'text-D-0-0-1-1'],closed=False)

    def box(self,name,left,top,right,bottom,r):
        points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        for i,a in enumerate(points):
            b=points[(i+1)%8]
            if i%2:self.add_arc(f'{name}-{i}',a,b,radius_x=r)
            else:self.add_line(f'{name}-{i}',a,b)
        self.add_contour(name,*[f'{name}-{i}' for i in range(8)],closed=True)

