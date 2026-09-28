from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '46fff59c-84bf-4526-bd9b-33201133c81c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__baby-bottle-with-handles/20260926T085631Z-thuan-mac/reference/milk bottle handle_46fff59c-84bf-4526-bd9b-33201133c81c.svg'
AUTHOR = "claude-opus-5-5"

class BabyBottleWithHandles(Solo48):
    icon_id = 'baby-bottle-with-handles'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'babies'
    categories = ('babies', 'primitives')
    aliases = ()
    keywords = ('bottle', 'handles', 'baby', 'milk', 'feeding', 'sippy', 'teat', 'infant')

    def build(self) -> None:
        # Symbol plan: a feeding bottle on the 45-degree axis (lower-left base,
        # teat to the upper right), mirrored about that axis. Frame:
        # P(a, b) = (14 + a + b, 34 - a + b); a runs along the bottle, b across.
        #   body    a 0..16, walls b = -7 / +7 (19.8 apart), rounded base corners
        #   collar  a 16..22, a band 8.5 thick above the separator line
        #   teat    3/4-circle bulb r4 on the collar top, b -2..2
        #   handles 3/4-circle lobes r5 on both walls, a 4..9, integer centres
        # Every part meets the outline at a shared split point (no crossings).
        # SQUARE centerline extrema: handle x 6, teat x 42 / y 6, handle y 42.
        def P(a, b):
            return (14 + a + b, 34 - a + b)

        self.add_arc('base-left', P(0, -4), P(3, -7), radius_x=4, sweep=True)
        self.add_line('wall-left-base', P(3, -7), P(4, -7))
        self.add_line('wall-left-low', P(4, -7), P(9, -7))
        self.add_line('wall-left', P(9, -7), P(16, -7))
        self.add_line('collar-left', P(16, -7), P(20, -7))
        self.add_arc('collar-corner-left', P(20, -7), P(22, -5), radius_x=3, sweep=True)
        self.add_line('collar-top-left', P(22, -5), P(22, -2))
        self.add_line('collar-top', P(22, -2), P(22, 2))
        self.add_line('collar-top-right', P(22, 2), P(22, 5))
        self.add_arc('collar-corner-right', P(22, 5), P(20, 7), radius_x=3, sweep=True)
        self.add_line('collar-right', P(20, 7), P(16, 7))
        self.add_line('wall-right', P(16, 7), P(9, 7))
        self.add_line('wall-right-low', P(9, 7), P(4, 7))
        self.add_line('wall-right-base', P(4, 7), P(3, 7))
        self.add_arc('base-right', P(3, 7), P(0, 4), radius_x=4, sweep=True)
        self.add_line('base', P(0, 4), P(0, -4))
        self.add_contour('bottle', 'base-left', 'wall-left-base', 'wall-left-low', 'wall-left', 'collar-left',
                         'collar-corner-left', 'collar-top-left', 'collar-top', 'collar-top-right',
                         'collar-corner-right', 'collar-right', 'wall-right', 'wall-right-low',
                         'wall-right-base', 'base-right', 'base', closed=True)
        self.add_line('collar-seam', P(16, -7), P(16, 7))
        self.add_arc('teat', P(22, -2), P(22, 2), radius_x=4, large_arc=True, sweep=True)
        self.add_arc('handle-left', P(4, -7), P(9, -7), radius_x=5, large_arc=True, sweep=True)
        self.add_arc('handle-right', P(9, 7), P(4, 7), radius_x=5, large_arc=True, sweep=True)
        for part in ('collar-seam', 'teat', 'handle-left', 'handle-right'):
            self.relate('connect', 'bottle', part)
