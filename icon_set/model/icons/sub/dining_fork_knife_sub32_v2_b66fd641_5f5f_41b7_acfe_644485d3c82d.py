"""Complete source composition; see the accompanying visual and validation evidence."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.sub._base import Sub32
SOURCE_ICON_ID = 'b66fd641-5f5f-41b7-acfe-644485d3c82d'
SOURCE_PATH = 'pictographic-primitives/symbol/fork and knife_b66fd641-5f5f-41b7-acfe-644485d3c82d.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('three-tined fork', 'rounded fork bowl with central tine continuing into handle', 'upright curved knife blade with heel', 'long knife handle')

class Drawing(Sub32):
    variant_of = 'dining-fork-knife-sub32'
    variant_label = 'Uniform 4px readability repair'
    REPAIR_PLAN = {'concept': 'Dining Fork and Knife', 'core_parts': ['three-tined fork', 'rounded fork bowl with central tine continuing into handle', 'upright curved knife blade with heel', 'long knife handle'], 'flexible_parts': 'Coordinates and proportions only; no parts removed.', 'repair': 'Wider knife blade opens its counter; fork stays three-tined with equal 6-unit spacing.'}
    icon_id = 'dining-fork-knife-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    keywords = ('dining', 'fork', 'and', 'knife')

    def build(self):
        self.add_line('fork-left', (2, 2), (2, 10))
        self.add_arc('fork-bottom-left', (2, 10), (8, 16), radius_x=6, sweep=False)
        self.add_arc('fork-bottom-right', (8, 16), (14, 10), radius_x=6, sweep=False)
        self.add_line('fork-right', (14, 10), (14, 2))
        self.add_contour('fork-cup', 'fork-left', 'fork-bottom-left', 'fork-bottom-right', 'fork-right')
        self.add_line('fork-center', (8, 2), (8, 16))
        self.add_line('fork-handle', (8, 16), (8, 30))
        self.relate('connect', 'fork-bottom-left', 'fork-center', 'fork-handle')
        self.relate('connect', 'fork-bottom-right', 'fork-center', 'fork-handle')
        self.add_line('knife-back', (20, 2), (20, 18))
        self.add_bezier('knife-edge', (20, 2), ((27, 7), (30, 12), (30, 18)))
        self.add_line('knife-heel', (30, 18), (20, 18))
        self.add_contour('blade', 'knife-edge', 'knife-heel')
        self.add_line('knife-handle', (20, 18), (20, 30))
        self.relate('connect', 'knife-back', 'knife-edge')
        self.relate('connect', 'knife-back', 'knife-heel', 'knife-handle')
