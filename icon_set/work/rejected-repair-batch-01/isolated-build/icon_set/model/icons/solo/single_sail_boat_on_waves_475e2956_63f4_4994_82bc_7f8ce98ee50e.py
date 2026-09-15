"""Single-Sail Boat on Waves. Single straight-edged port sail above a hull; reduce the two source wave rows to one baseline.
Keyshape VRECT_L, visible extremes (6, 2, 42, 46); centerline envelope inset by 2.
Construction: Lucide sailboat: sail/mast/hull hierarchy with genuine mast attachments. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '475e2956-63f4-4994-82bc-7f8ce98ee50e'
SOURCE_PATH = 'pictographic-primitives/recreation/sailing boat water_475e2956-63f4-4994-82bc-7f8ce98ee50e.svg'
AUTHOR = 'gpt-6'


class SingleSailBoatOnWaves(Solo48):
    icon_id = 'single-sail-boat-on-waves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('single', 'sail', 'boat', 'on', 'waves')

    def build(self) -> None:
        self.add_line('sail-1', (27, 4), (9, 24))
        self.add_line('sail-2', (9, 24), (27, 24))
        self.add_line('sail-3', (27, 24), (27, 4))
        self.add_contour('sail', 'sail-1', 'sail-2', 'sail-3', closed=True)
        self.add_line('mast', (27, 24), (27, 32))
        self.relate("connect", 'sail', 'mast')
        self.add_line('hull-1', (8, 32), (27, 32))
        self.add_line('hull-2', (27, 32), (40, 32))
        self.add_line('hull-3', (40, 32), (34, 44))
        self.add_line('hull-4', (34, 44), (14, 44))
        self.add_line('hull-5', (14, 44), (8, 32))
        self.add_contour('hull', 'hull-1', 'hull-2', 'hull-3', 'hull-4', 'hull-5', closed=True)
        self.relate("connect", 'mast', 'hull')
        self.add_line('water-left', (8, 44), (14, 44))
        self.add_line('water-right', (34, 44), (40, 44))
        self.relate("connect", 'water-left', 'hull')
        self.relate("connect", 'water-right', 'hull')
