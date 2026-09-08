"""Round spectacles with an arched bridge. HRECT_S extremes (2,14)-(46,34). Lucide glasses informs paired lens arcs and bridge; lenses are slightly tall to fit the keyshape. Tiny temples retained as short stubs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '136a421d-0aa5-57f0-bc5e-ab9d19e5eca4'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/glasses retro_136a421d-0aa5-57f0-bc5e-ab9d19e5eca4.svg'
AUTHOR = 'astra-chatgpt'


class RoundSpectacles(Solo48):
    icon_id = 'round-spectacles'
    keyshape = Keyshape.HRECT_S
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('glasses', 'spectacles', 'eyewear', 'round glasses', 'retro', 'vision', 'optician', 'accessory')

    def build(self) -> None:
        self.add_arc('lens-left-0', (21, 24), (12, 34), radius_x=9, radius_y=10, sweep=True)
        self.add_arc('lens-left-1', (12, 34), (3, 24), radius_x=9, radius_y=10, sweep=True)
        self.add_arc('lens-left-2', (3, 24), (12, 14), radius_x=9, radius_y=10, sweep=True)
        self.add_arc('lens-left-3', (12, 14), (21, 24), radius_x=9, radius_y=10, sweep=True)
        self.add_contour('lens-left', 'lens-left-0', 'lens-left-1', 'lens-left-2', 'lens-left-3', closed=True)
        self.add_arc('lens-right-0', (45, 24), (36, 34), radius_x=9, radius_y=10, sweep=True)
        self.add_arc('lens-right-1', (36, 34), (27, 24), radius_x=9, radius_y=10, sweep=True)
        self.add_arc('lens-right-2', (27, 24), (36, 14), radius_x=9, radius_y=10, sweep=True)
        self.add_arc('lens-right-3', (36, 14), (45, 24), radius_x=9, radius_y=10, sweep=True)
        self.add_contour('lens-right', 'lens-right-0', 'lens-right-1', 'lens-right-2', 'lens-right-3', closed=True)
        self.add_arc('bridge', (21, 24), (27, 24), radius_x=3, radius_y=3, sweep=True)
        self.add_line('temple-left', (2, 24), (3, 24))
        self.add_line('temple-right', (45, 24), (46, 24))
        self.relate("connect", 'bridge', 'lens-left')
        self.relate("connect", 'bridge', 'lens-right')
        self.relate("connect", 'temple-left', 'lens-left')
        self.relate("connect", 'temple-right', 'lens-right')
