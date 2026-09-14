"""Left-facing orca head with swept dorsal and pectoral fins; small eye patch reduced to circular mark."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c6bf4ca-1470-5ea8-84b1-028297d70465'
SOURCE_PATH = 'pictographic-primitives/animals/orca whale head_2c6bf4ca-1470-5ea8-84b1-028297d70465.svg'
AUTHOR = 'gpt-6'


class OrcaHead(Solo48):
    icon_id = 'orca-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('orca', 'head')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_bezier('forehead', (6, 23), *(((6, 17.85456916), (10.74880085, 13.28442643), (18, 12)),))
        self.add_arc('back', (18, 12), (30, 15), radius_x=24, radius_y=24, large_arc=False, sweep=False)
        self.add_arc('dorsal-front', (30, 15), (42, 6), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('dorsal-back', (42, 6), (41, 24), radius_x=22, radius_y=22, large_arc=False, sweep=False)
        self.add_line('rear', (41, 24), (42, 42))
        self.add_line('fin-bottom', (42, 42), (30, 37))
        self.add_arc('jaw', (30, 37), (6, 23), radius_x=36, radius_y=36, large_arc=False, sweep=True)
        self.add_line('pectoral', (30, 37), (32, 28))
        self.add_contour('outline', *('forehead', 'back', 'dorsal-front', 'dorsal-back', 'rear', 'fin-bottom', 'jaw'), closed=True)
        self.relate('connect', *('outline', 'pectoral'))
        self.add_line('patch',(20,24),(23,24))
