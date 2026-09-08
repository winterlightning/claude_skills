"""Circular mechanical ornament with offset ring, spokes and a loose wavy trace. CIRCLE radius 22 around (24,24). No useful exact Lucide match; continuous circular arcs guide construction. Deliberately asymmetric interior; tiny stray mark omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b930fde9-bd19-41b6-bfa5-0da26c21f3c9'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/steampunk decoration_b930fde9-bd19-41b6-bfa5-0da26c21f3c9.svg'
AUTHOR = 'gpt-6'


class CircularSteampunkOrnament(Solo48):
    icon_id = 'circular-steampunk-ornament'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('disc', 'steampunk', 'ornament', 'circle', 'ring', 'spokes', 'abstract')

    def build(self) -> None:
        self.add_arc('disc-a', (2, 24), (46, 24), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_arc('disc-b', (46, 24), (2, 24), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_contour('disc', 'disc-a', 'disc-b', closed=True)
        self.add_arc('hub-a', (22, 21), (30, 21), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('hub-b', (30, 21), (22, 21), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('hub', 'hub-a', 'hub-b', closed=True)
        self.add_line('spoke-ne', (30, 21), (46, 24))
        self.relate('connect', 'spoke-ne', 'hub')
        self.relate('connect', 'spoke-ne', 'disc')
        self.add_line('spoke-top', (26, 17), (24, 2))
        self.relate('connect', 'spoke-top', 'hub')
        self.relate('connect', 'spoke-top', 'disc')
        self.add_line('spoke-se', (30, 21), (35, 30))
        self.relate('connect', 'spoke-se', 'hub')
        self.add_arc('wave-a', (12, 15), (12, 25), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('wave-b', (12, 25), (18, 37), radius_x=8, radius_y=8, sweep=False, large_arc=False)
        self.add_arc('wave-c', (18, 37), (27, 38), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_contour('wave', 'wave-a', 'wave-b', 'wave-c', closed=False)
