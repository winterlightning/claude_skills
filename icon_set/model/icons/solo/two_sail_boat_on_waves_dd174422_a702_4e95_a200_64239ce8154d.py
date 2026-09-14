"""Two-Sail Boat on Waves. Narrow triangular port sail and curved starboard sail over a broad hull; omit extra wave rows.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide sailboat: shared central mast and coherent sail contours. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dd174422-a702-4e95-a200-64239ce8154d'
SOURCE_PATH = 'pictographic-primitives/recreation/sailing boat water_dd174422-a702-4e95-a200-64239ce8154d.svg'
AUTHOR = 'gpt-6'


class TwoSailBoatOnWaves(Solo48):
    icon_id = 'two-sail-boat-on-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('two', 'sail', 'boat', 'on', 'waves')

    def build(self) -> None:
        self.add_line('port-sail-1', (24, 6), (10, 25))
        self.add_line('port-sail-2', (10, 25), (24, 25))
        self.add_line('port-sail-3', (24, 25), (24, 6))
        self.add_contour('port-sail', 'port-sail-1', 'port-sail-2', 'port-sail-3', closed=True)
        self.add_arc('starboard-edge', (24, 6), (42, 25), radius_x=25, radius_y=25, sweep=True)
        self.add_line('starboard-foot', (42, 25), (24, 25))
        self.add_contour('starboard', 'starboard-edge', 'starboard-foot', closed=False)
        self.relate("connect", 'port-sail', 'starboard')
        self.add_line('mast', (24, 25), (24, 34))
        self.relate("connect", 'port-sail', 'mast')
        self.relate("connect", 'starboard', 'mast')
        self.add_line('hull-1', (6, 34), (24, 34))
        self.add_line('hull-2', (24, 34), (42, 34))
        self.add_line('hull-3', (42, 34), (35, 42))
        self.add_line('hull-4', (35, 42), (13, 42))
        self.add_line('hull-5', (13, 42), (6, 34))
        self.add_contour('hull', 'hull-1', 'hull-2', 'hull-3', 'hull-4', 'hull-5', closed=True)
        self.relate("connect", 'hull', 'mast')
