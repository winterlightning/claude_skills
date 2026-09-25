# Complete geometry repair; parent preserved.
'Filament shortened and doubled pipe/foot runs replaced by one tangent radius-8 support bend. Lucide lightbulb informs simple glass and filament. VRECT_L bounds retained; bent support remains asymmetric.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a36c6af9-3860-579c-aa1b-a5f68c4f1845'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/steampunk decoration lamp_a36c6af9-3860-579c-aa1b-a5f68c4f1845.svg'
AUTHOR = 'gpt-6'

class PipeMountedLightBulb(Solo48):
    icon_id = 'pipe-mounted-light-bulb'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    categories = ('primitives', 'decoration')
    aliases = ()
    keywords = ('lamp', 'bulb', 'pipe', 'light', 'filament', 'steampunk', 'fixture')

    def build(self) -> None:
        self.add_arc('dome', (16, 16), (40, 16), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('shoulder-r', (40, 16), (34, 28), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_line('socket-r', (34, 28), (34, 34))
        self.add_line('socket-base-r', (34, 34), (28, 34))
        self.add_line('socket-base-l', (28, 34), (22, 34))
        self.add_line('socket-l', (22, 34), (22, 28))
        self.add_arc('shoulder-l', (22, 28), (16, 16), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_contour('bulb', 'dome', 'shoulder-r', 'socket-r', 'socket-base-r', 'socket-base-l', 'socket-l', 'shoulder-l', closed=True)
        self.add_line('filament', (28, 15), (28, 20))
        # One tangent support bend ending in the flat foot; no doubled run.
        self.add_line('pipe-top', (28, 34), (28, 36))
        self.add_arc('pipe-bend', (28, 36), (20, 44), radius_x=8)
        self.add_line('foot', (20, 44), (8, 44))
        self.add_contour('support', 'pipe-top', 'pipe-bend', 'foot')
        self.relate('connect', 'support', 'bulb')
