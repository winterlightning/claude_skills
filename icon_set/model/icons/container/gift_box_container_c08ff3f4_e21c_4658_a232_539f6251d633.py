"""Gift box following user reference: broad bow on lid, empty box face.
SQUARE visible extremes (0,0)-(64,64), native 4-unit stroke.
User clipboard b296dcc9-5ef6-4656-8612-b557f0b5702d is the visual reference.
Lucide gift informs geometric construction. Bow bases share the lid edge
without duplicate strokes. The plain lid is eight units high on centerlines.
Paired symbols measured separately; native 32 does not fit. 24-unit prototypes are measured separately.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (gift-box-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = 'c08ff3f4-e21c-4658-a232-539f6251d633'
SOURCE_PATH = 'pictographic-primitives/rewards/gift box_c08ff3f4-e21c-4658-a232-539f6251d633.svg'
AUTHOR = 'claude-opus-5-5'


class GiftBoxContainer(Container64):
    icon_id = 'gift-box-container'
    keyshape = Keyshape.SQUARE
    category = 'rewards'
    categories = ('rewards', 'primitives')
    aliases = ()
    keywords = ('gift', 'box', 'container')

    def build(self) -> None:
        # A smaller bow (6..14) on a slimmer lid (14..22) so the box below runs 22..58 and holds a symbol of 24 with
        # a 4 px gap (was 18). Mirrored about x = 32.
        self.add_line('lid-0', (10, 14), (22, 14))
        self.add_arc('lid-1', (54, 14), (58, 18), radius_x=4)
        self.add_arc('lid-2', (58, 18), (54, 22), radius_x=4)
        self.add_line('lid-3', (54, 22), (10, 22))
        self.add_arc('lid-4', (10, 22), (6, 18), radius_x=4)
        self.add_arc('lid-5', (6, 18), (10, 14), radius_x=4)
        self.add_line('lid-6', (42, 14), (54, 14))
        self.add_line('box-0', (10, 22), (10, 52))
        self.add_arc('box-1', (10, 52), (16, 58), radius_x=6, sweep=False)
        self.add_line('box-2', (16, 58), (48, 58))
        self.add_arc('box-3', (48, 58), (54, 52), radius_x=6, sweep=False)
        self.add_line('box-4', (54, 52), (54, 22))
        self.add_bezier('bow-left-0', (32, 14), ((29, 9), (24, 6), (21, 6)), ((18, 6), (17, 8), (17, 10)), ((17, 12), (19, 14), (22, 14)))
        self.add_line('bow-left-1', (22, 14), (32, 14))
        self.add_bezier('bow-right-0', (32, 14), ((35, 9), (40, 6), (43, 6)), ((46, 6), (47, 8), (47, 10)), ((47, 12), (45, 14), (42, 14)))
        self.add_line('bow-right-1', (42, 14), (32, 14))
        self.add_contour('lid', 'lid-6', 'lid-1', 'lid-2', 'lid-3', 'lid-4', 'lid-5', 'lid-0')
        self.add_contour('bow-left', 'bow-left-0', 'bow-left-1', closed=True)
        self.add_contour('bow-right', 'bow-right-0', 'bow-right-1', closed=True)
        self.add_contour('box', 'box-0', 'box-1', 'box-2', 'box-3', 'box-4')
        self.relate('connect', 'box', 'lid')
        self.relate('connect', 'bow-left', 'lid')
        self.relate('connect', 'bow-right', 'lid')
        self.relate('connect', 'bow-left', 'bow-right')
