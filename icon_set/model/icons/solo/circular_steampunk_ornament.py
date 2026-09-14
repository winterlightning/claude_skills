# Review candidate; original preserved.
"""Circular mechanical ornament with offset ring, spokes and a loose wavy trace. CIRCLE radius 22 around (24,24). No useful exact Lucide match; continuous circular arcs guide construction. Deliberately asymmetric interior; tiny stray mark omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b930fde9-bd19-41b6-bfa5-0da26c21f3c9'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/steampunk decoration_b930fde9-bd19-41b6-bfa5-0da26c21f3c9.svg'
AUTHOR = 'gpt-6'

class CircularSteampunkOrnament(Solo48):
    icon_id = 'circular-steampunk-ornament'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/decoration'
    aliases = ()
    keywords = ('disc', 'steampunk', 'ornament', 'circle', 'ring', 'spokes', 'abstract')

    def build(self) -> None:
        """Opening repair: Restored a circular rim and rebalanced the inner wavy trace to remove crossing pockets."""
        self.add_arc('disc-a', (4, 24), (44, 24), sweep=True, large_arc=False, radius_x=20, radius_y=20)
        self.add_arc('disc-b', (44, 24), (4, 24), sweep=True, large_arc=False, radius_x=20, radius_y=20)
        self.add_contour('disc', 'disc-a', 'disc-b', closed=True)
        self.add_arc('hub-a', (22, 21), (30, 21), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('hub-b', (30, 21), (22, 21), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('hub', 'hub-a', 'hub-b', closed=True)
        self.add_line('spoke-ne', (30, 21), (44, 24))
        self.relate('connect', 'spoke-ne', 'hub')
        self.relate('connect', 'spoke-ne', 'disc')
        self.add_line('spoke-top', (26, 17), (24, 4))
        self.relate('connect', 'spoke-top', 'hub')
        self.relate('connect', 'spoke-top', 'disc')
        self.add_line('spoke-se', (30, 21), (34, 29))
        self.relate('connect', 'spoke-se', 'hub')
        self.add_arc('wave-a', (13, 20), (13, 24), radius_x=8, sweep=False)
        self.add_arc('wave-b', (13, 24), (15, 29), radius_x=6, sweep=True)
        self.add_contour('wave', 'wave-a', 'wave-b')

        self.relate('connect', 'spoke-ne', 'spoke-se')
