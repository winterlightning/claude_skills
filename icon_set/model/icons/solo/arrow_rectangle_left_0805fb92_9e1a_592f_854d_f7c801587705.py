'Left chevron in a rounded rectangle: equal corner radii and centered chevron; Lucide chevron construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0805fb92-9e1a-592f-854d-f7c801587705'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow rectangle left_0805fb92-9e1a-592f-854d-f7c801587705.svg'
AUTHOR = 'gpt-6'

class ArrowRectangleLeft(Solo48):
    icon_id = 'arrow-rectangle-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'rectangle', 'left', 'arrows')

    def build(self) -> None:
        # A shared corner radius keeps all four turns tangent to their walls.
        left, top, right, bottom, radius = 4, 8, 44, 40, 4
        self.add_line('outline-top', (left+radius,top), (right-radius,top))
        self.add_arc('outline-tr', (right-radius,top), (right,top+radius), radius_x=radius)
        self.add_line('outline-right', (right,top+radius), (right,bottom-radius))
        self.add_arc('outline-br', (right,bottom-radius), (right-radius,bottom), radius_x=radius)
        self.add_line('outline-bottom', (right-radius,bottom), (left+radius,bottom))
        self.add_arc('outline-bl', (left+radius,bottom), (left,bottom-radius), radius_x=radius)
        self.add_line('outline-left', (left,bottom-radius), (left,top+radius))
        self.add_arc('outline-tl', (left,top+radius), (left+radius,top), radius_x=radius)
        self.add_contour('outline', *('outline-'+part for part in ('top','tr','right','br','bottom','bl','left','tl')), closed=True)
        self.add_polyline('chevron',(27,17),(20,24),(27,31))
