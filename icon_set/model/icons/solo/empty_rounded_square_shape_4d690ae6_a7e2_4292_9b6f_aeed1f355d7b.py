"""Empty Rounded Square Shape.

Symbol plan: Single rounded rectangle, equal four corner radii; bilateral symmetry. Centerline extremes (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4d690ae6-a7e2-4292-9b6f-aeed1f355d7b'
SOURCE_PATH = 'pictographic-primitives/other/horizontal rectangle_4d690ae6-a7e2-4292-9b6f-aeed1f355d7b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'empty-rounded-square-shape-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('empty', 'rounded', 'square', 'shape')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-b', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-a', name+'-b', closed=True)

    def rounded_box(self, name, left, top, right, bottom, r):
        self.add_line(name+'-top', (left+r,top), (right-r,top))
        self.add_arc(name+'-tr', (right-r,top), (right,top+r), radius_x=r)
        self.add_line(name+'-right', (right,top+r), (right,bottom-r))
        self.add_arc(name+'-br', (right,bottom-r), (right-r,bottom), radius_x=r)
        self.add_line(name+'-bottom', (right-r,bottom), (left+r,bottom))
        self.add_arc(name+'-bl', (left+r,bottom), (left,bottom-r), radius_x=r)
        self.add_line(name+'-left', (left,bottom-r), (left,top+r))
        self.add_arc(name+'-tl', (left,top+r), (left+r,top), radius_x=r)
        self.add_contour(name, *(name+'-'+part for part in ('top','tr','right','br','bottom','bl','left','tl')), closed=True)

    def build(self):
        self.rounded_box('outline',4,8,44,40,4)
