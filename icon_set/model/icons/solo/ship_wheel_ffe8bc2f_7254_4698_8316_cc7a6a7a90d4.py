'Nautical Ship Steering Wheel.\n\nSymbol plan: Eight evenly radiating wheel spokes join in a solid central hub; the hollow hub is reduced to the joined stroke center.\nKeyshape: CIRCLE; authored on SOLO48, not scaled from source.\nLucide: ship-wheel.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ffe8bc2f-7254-4698-8316-cc7a6a7a90d4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/steering wheel_ffe8bc2f-7254-4698-8316-cc7a6a7a90d4.svg'
AUTHOR = 'gpt-6'

class ShipWheel(Solo48):
    icon_id = 'ship-wheel'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('ship', 'wheel')

    def build(self):
        # Eight evenly radiating wheel spokes join in a solid central hub; the hollow hub is reduced to the joined stroke center.
        axis_x = 24
        p_4_24 = (4, 24)
        p_10_10 = (10, 10)
        p_10_24 = (10, 24)
        p_10_38 = (10, 38)
        p_24_4 = (24, 4)
        p_24_24 = (24, 24)
        p_24_44 = (24, 44)
        p_38_10 = (2 * axis_x - p_10_10[0], p_10_10[1])
        p_38_24 = (2 * axis_x - p_10_24[0], p_10_24[1])
        p_38_38 = (2 * axis_x - p_10_38[0], p_10_38[1])
        p_44_24 = (2 * axis_x - p_4_24[0], p_4_24[1])
        self.add_arc('rim-1', p_10_24, p_38_24, radius_x=14, radius_y=14, sweep=True)
        self.add_arc('rim-2', p_38_24, p_10_24, radius_x=14, radius_y=14, sweep=True)
        self.add_contour('rim', 'rim-1', 'rim-2', closed=True)
        self.add_line('n-1', p_24_24, p_24_4)
        self.add_contour('n', 'n-1', closed=False)
        self.relate("connect", 'n', 'rim')
        self.add_line('s-1', p_24_24, p_24_44)
        self.add_contour('s', 's-1', closed=False)
        self.relate("connect", 's', 'rim')
        self.add_line('w-1', p_24_24, p_4_24)
        self.add_contour('w', 'w-1', closed=False)
        self.relate("connect", 'w', 'rim')
        self.add_line('e-1', p_24_24, p_44_24)
        self.add_contour('e', 'e-1', closed=False)
        self.relate("connect", 'e', 'rim')
        self.add_line('nw-1', p_24_24, p_10_10)
        self.add_contour('nw', 'nw-1', closed=False)
        self.relate("connect", 'nw', 'rim')
        self.add_line('ne-1', p_24_24, p_38_10)
        self.add_contour('ne', 'ne-1', closed=False)
        self.relate("connect", 'ne', 'rim')
        self.add_line('sw-1', p_24_24, p_10_38)
        self.add_contour('sw', 'sw-1', closed=False)
        self.relate("connect", 'sw', 'rim')
        self.add_line('se-1', p_24_24, p_38_38)
        self.add_contour('se', 'se-1', closed=False)
        self.relate("connect", 'se', 'rim')
