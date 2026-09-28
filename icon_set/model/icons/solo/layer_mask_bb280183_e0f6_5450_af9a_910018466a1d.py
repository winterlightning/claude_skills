"""Layer mask (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb280183-e0f6-5450-af9a-910018466a1d'
SOURCE_PATH = 'pictographic-primitives/design/layer mask_bb280183-e0f6-5450-af9a-910018466a1d.svg'
AUTHOR = 'gpt-6'

class LayerMask(Solo48):
    icon_id = 'layer-mask'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('layer', 'mask', 'design')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('sym-e0', (15, 24), (33, 24), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('sym-e1', (33, 24), (15, 24), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('sym-e2', (12, 6), (6, 11), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('sym-e3', (6, 11), (6, 13))
        self.add_line('sym-e5', (6, 13), (6, 14))
        self.add_line('sym-e6', (6, 14), (6, 24))
        self.add_line('sym-e7', (6, 24), (6, 34))
        self.add_line('sym-e8', (6, 34), (6, 35))
        self.add_line('sym-e10', (6, 35), (6, 37))
        self.add_arc('sym-e11', (6, 37), (12, 42), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('sym-e12', (12, 42), (24, 42))
        self.add_line('sym-e13', (24, 42), (36, 42))
        self.add_arc('sym-e14', (36, 42), (42, 37), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('sym-e15', (42, 37), (42, 35))
        self.add_line('sym-e17', (42, 35), (42, 34))
        self.add_line('sym-e18', (42, 34), (42, 24))
        self.add_line('sym-e19', (42, 24), (42, 14))
        self.add_line('sym-e20', (42, 14), (42, 13))
        self.add_line('sym-e22', (42, 13), (42, 11))
        self.add_arc('sym-e23', (42, 11), (36, 6), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('sym-e24', (36, 6), (24, 6))
        self.add_line('sym-e25', (24, 6), (12, 6))
        self.add_contour('sym-c0', *('sym-e0', 'sym-e1'), closed=True)
        self.add_contour('sym-c1', *('sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25'), closed=True)
