'Type G outlet: shorten the three slots inside a symmetric rounded frame to retain their familiar arrangement and clear margins.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c0411cd9-5038-475a-aa2f-c63811150a34'
SOURCE_PATH = 'icons-json/electronics/power outlet type g_c0411cd9-5038-475a-aa2f-c63811150a34.json'
AUTHOR = 'gpt-6'

class PowerOutletTypeG(Solo48):
    icon_id = 'power-outlet-type-g'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('power', 'outlet', 'type', 'g', 'electronics')

    def build(self) -> None:
        # A shared corner radius keeps all four turns tangent to their walls.
        left, top, right, bottom, radius = 6, 6, 42, 42, 4
        self.add_line('frame-top', (left+radius,top), (right-radius,top))
        self.add_arc('frame-tr', (right-radius,top), (right,top+radius), radius_x=radius)
        self.add_line('frame-right', (right,top+radius), (right,bottom-radius))
        self.add_arc('frame-br', (right,bottom-radius), (right-radius,bottom), radius_x=radius)
        self.add_line('frame-bottom', (right-radius,bottom), (left+radius,bottom))
        self.add_arc('frame-bl', (left+radius,bottom), (left,bottom-radius), radius_x=radius)
        self.add_line('frame-left', (left,bottom-radius), (left,top+radius))
        self.add_arc('frame-tl', (left,top+radius), (left+radius,top), radius_x=radius)
        self.add_contour('frame', *('frame-'+part for part in ('top','tr','right','br','bottom','bl','left','tl')), closed=True)

        self.add_line('earth',(24,15),(24,21))
        self.add_line('left',(15,31),(19,31))
        self.add_line('right',(29,31),(33,31))
