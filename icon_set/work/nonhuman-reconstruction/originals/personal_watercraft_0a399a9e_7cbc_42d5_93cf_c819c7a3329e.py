"""Personal Watercraft. Left-facing riderless craft retains handlebar, stepped seat and bow; omit decorative waves.
Keyshape HRECT_L, visible extremes (2, 6, 46, 42); centerline envelope inset by 2.
Construction: Lucide caravan: coherent side silhouette and tangent quarter-circle stern. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a399a9e-7cbc-42d5-93cf-c819c7a3329e'
SOURCE_PATH = 'pictographic-primitives/recreation/jet ski_0a399a9e-7cbc-42d5-93cf-c819c7a3329e.svg'
AUTHOR = 'gpt-6'


class PersonalWatercraft(Solo48):
    icon_id = 'personal-watercraft'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('personal', 'watercraft')

    def build(self) -> None:
        self.add_line('upper-1', (4, 29), (16, 8))
        self.add_line('upper-2', (16, 8), (24, 8))
        self.add_contour('upper', 'upper-1', 'upper-2', closed=False)
        self.add_line('seat-1', (11, 18), (19, 18))
        self.add_line('seat-2', (19, 18), (24, 25))
        self.add_line('seat-3', (24, 25), (36, 25))
        self.add_arc('stern', (36, 25), (44, 33), radius_x=8, radius_y=8, sweep=True)
        self.add_line('tail', (44, 33), (42, 40))
        self.add_contour('seat-shell', 'seat-1', 'seat-2', 'seat-3', 'stern', 'tail', closed=False)
        self.relate("connect", 'upper', 'seat-shell')
        self.add_line('hull-1', (4, 29), (12, 40))
        self.add_contour('hull', 'hull-1', closed=False)
        self.relate("connect", 'upper', 'hull')
        self.add_line('deck', (4, 29), (44, 33))
        self.relate("connect", 'deck', 'upper')
        self.relate("connect", 'deck', 'seat-shell')
