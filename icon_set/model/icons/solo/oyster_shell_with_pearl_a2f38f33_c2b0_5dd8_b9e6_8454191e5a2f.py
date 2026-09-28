"""An open oyster cradles a circular pearl on the lower rim. Mirrored about x=24. The local Lucide shell is a spiral, so it is not a useful subject match; use coherent circular lobes and an elliptical bowl. Omit the two inner ridge lines to protect pearl clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2f38f33-c2b0-5dd8-b9e6-8454191e5a2f'
SOURCE_PATH = 'pictographic-primitives/products/business pearl_a2f38f33-c2b0-5dd8-b9e6-8454191e5a2f.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'oyster-shell-with-pearl'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "products"
    categories = ("primitives", "products")
    aliases = ()
    keywords = ('pearl', 'oyster', 'shell', 'clam', 'jewel', 'treasure', 'value', 'sea')

    def build(self):
        # SQUARE centerline extremes (6, 6, 42, 42).

        # Mirrored three-lobed valve; pearl touches the shared lower-valve rim.
        self.add_arc('left-lobe',(6,24),(14,16),radius_x=8)
        self.add_arc('crown',(14,16),(34,16),radius_x=10)
        self.add_arc('right-lobe',(34,16),(42,24),radius_x=8)
        self.add_arc('right-shoulder',(42,24),(36,32),radius_x=6,radius_y=8)
        self.add_arc('left-shoulder',(12,32),(6,24),radius_x=6,radius_y=8)
        self.add_contour('upper-valve','left-shoulder','left-lobe','crown','right-lobe','right-shoulder')
        self.add_polyline('rim',(6,32),(12,32),(24,32),(36,32),(42,32))
        self.relate('connect','rim','upper-valve')
        self.add_arc('bowl',(42,32),(6,32),radius_x=18,radius_y=10)
        self.relate('connect','bowl','rim')
        self.add_arc('pearl-upper-left',(18,26),(24,20),radius_x=6)
        self.add_arc('pearl-upper-right',(24,20),(30,26),radius_x=6)
        self.add_arc('pearl-lower-right',(30,26),(24,32),radius_x=6)
        self.add_arc('pearl-lower-left',(24,32),(18,26),radius_x=6)
        self.add_contour('pearl','pearl-upper-left','pearl-upper-right','pearl-lower-right','pearl-lower-left',closed=True)
        self.relate('connect','pearl','rim')
