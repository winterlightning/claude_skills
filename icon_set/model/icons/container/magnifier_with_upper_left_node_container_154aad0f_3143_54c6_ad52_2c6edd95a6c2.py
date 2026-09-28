"""A circular magnifier with a diagonal lower-right handle and a short upper-left stalk ending in a separate small circle. Exclude all network nodes inside the lens.

Plan: Lens and terminal circles, with explicit stalk and handle joins. Deliberate diagonal asymmetry; bounds (2,2)-(62,62).
Hosting at the standard slot: add-sub32: invalid, heart-state-63: invalid, check-mark: invalid.
Construction reference: Lucide search: circular lens and attached diagonal handle."""
from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '154aad0f-3143-54c6-ad52-2c6edd95a6c2'
SOURCE_PATH = 'pictographic-primitives/programing/amazon inspector_154aad0f-3143-54c6-ad52-2c6edd95a6c2.svg'
SOURCE_ICON_IDS = ('154aad0f-3143-54c6-ad52-2c6edd95a6c2',)
AUTHOR = 'gpt-6'

class MagnifierWithUpperLeftNodeContainer(Container64):
    icon_id = 'magnifier-with-upper-left-node-container'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    categories = ('programing', 'primitives')
    aliases = ()
    keywords = ('magnifier', 'with', 'upper', 'left', 'node', 'container')

    def build(self) -> None:
        # Lens radius20 uses exact 12-16-20 diagonal attachment points.
        self.add_arc('lens-a',(22,18),(46,50),radius_x=20)
        self.add_arc('lens-b',(46,50),(22,18),radius_x=20)
        self.add_contour('lens','lens-a','lens-b',closed=True)
        self.add_arc('terminal-a',(10,11),(4,3),radius_x=5)
        self.add_arc('terminal-b',(4,3),(10,11),radius_x=5)
        self.add_contour('terminal','terminal-a','terminal-b',closed=True)
        self.add_line('stalk',(10,11),(22,18))
        self.add_line('handle',(46,50),(62,62))
        self.relate('connect','lens','stalk')
        self.relate('connect','terminal','stalk')
        self.relate('connect','lens','handle')
