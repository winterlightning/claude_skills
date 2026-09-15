'Horizontal menu: three evenly spaced native-size dots, centred within a tangent rounded frame.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5094fde9-e2bf-5105-b3e2-9fe5c51241c7'
SOURCE_PATH = 'pictographic-primitives/interface-essential/navigation menu horizontal_5094fde9-e2bf-5105-b3e2-9fe5c51241c7.svg'
AUTHOR = 'gpt-6'

class NavigationMenuHorizontal(Solo48):
    icon_id = 'navigation-menu-horizontal'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'menu', 'horizontal', 'interface-essential')

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

        for i,x in enumerate((15,24,33)):
            self.add_dot(f'dot-{i}',(x,24))
