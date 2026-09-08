"""Left-facing orca head with swept dorsal and pectoral fins; small eye patch reduced to circular mark."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c6bf4ca-1470-5ea8-84b1-028297d70465'
SOURCE_PATH = 'pictographic-primitives/animals/orca whale head_2c6bf4ca-1470-5ea8-84b1-028297d70465.svg'
AUTHOR = 'gpt-6'


class OrcaHead(Solo48):
    icon_id = 'orca-head'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('orca', 'head')

    def build(self) -> None:
        # Centerline extremes from HRECT_XL: (0, 3, 48, 45)
        self.add_arc('forehead', (2, 23), (18, 12), radius_x=16, radius_y=11, sweep=True, large_arc=False)
        self.add_arc('back', (18, 12), (30, 15), radius_x=24, radius_y=24, sweep=False, large_arc=False)
        self.add_arc('dorsal-front', (30, 15), (43, 5), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_arc('dorsal-back', (43, 5), (41, 24), radius_x=22, radius_y=22, sweep=False, large_arc=False)
        self.add_line('rear', (41, 24), (46, 43))
        self.add_line('fin-bottom', (46, 43), (30, 37))
        self.add_arc('jaw', (30, 37), (2, 23), radius_x=36, radius_y=36, sweep=True, large_arc=False)
        self.add_contour('outline', 'forehead', 'back', 'dorsal-front', 'dorsal-back', 'rear', 'fin-bottom', 'jaw', closed=True)
        self.add_arc('patch-top', (17, 24), (23, 24), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('patch-bottom', (23, 24), (17, 24), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('patch', 'patch-top', 'patch-bottom', closed=True)
        self.add_line('pectoral', (30, 37), (32, 28))
        self.relate("connect", 'outline', 'pectoral')
