'Card: four identical tangent quarter-circle corners; short identifying mark inset with clear space.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b42901ee-f812-48ee-a415-b6ce160f17ba'
SOURCE_PATH = 'pictographic-primitives/business/card_b42901ee-f812-48ee-a415-b6ce160f17ba.svg'
AUTHOR = 'gpt-6'

class CardB42901ee(Solo48):
    icon_id = 'card-b42901ee'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('business', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('card', 'business')

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
        self.add_line('detail',(30,30),(35,30))
