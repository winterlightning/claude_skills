"""Three jellyfish arranged in a staggered group. Centerline extremes (2,2)-(46,46). No useful Lucide jellyfish match. Each bell keeps three tentacles. Angles reduced to keep the group readable."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9bdc48d-a72f-41ce-9b7a-6a465d1111ed'
SOURCE_PATH = 'pictographic-primitives/animals/jellyfish group_c9bdc48d-a72f-41ce-9b7a-6a465d1111ed.svg'
AUTHOR = 'gpt-6'


class JellyfishGroup(Solo48):
    icon_id = 'jellyfish-group'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('jellyfish', 'group', 'three', 'swarm', 'sea', 'ocean', 'marine', 'bloom')

    def build(self) -> None:
        self.add_arc('bell-0-dome', (2, 8), (24, 8), radius_x=11, radius_y=6, sweep=True)
        self.add_line('bell-0-rim-r', (24, 8), (20, 8))
        self.add_line('bell-0-rim-mr', (20, 8), (13, 8))
        self.add_line('bell-0-rim-ml', (13, 8), (6, 8))
        self.add_line('bell-0-rim-l', (6, 8), (2, 8))
        self.add_contour('bell-0', 'bell-0-dome', 'bell-0-rim-r', 'bell-0-rim-mr', 'bell-0-rim-ml', 'bell-0-rim-l', closed=True)
        self.add_line('tentacle-0-0', (6, 8), (4, 17))
        self.relate("connect", 'bell-0', 'tentacle-0-0')
        self.add_line('tentacle-0-1', (13, 8), (11, 17))
        self.relate("connect", 'bell-0', 'tentacle-0-1')
        self.add_line('tentacle-0-2', (20, 8), (18, 17))
        self.relate("connect", 'bell-0', 'tentacle-0-2')
        self.add_arc('bell-1-dome', (24, 23), (46, 23), radius_x=11, radius_y=6, sweep=True)
        self.add_line('bell-1-rim-r', (46, 23), (42, 23))
        self.add_line('bell-1-rim-mr', (42, 23), (35, 23))
        self.add_line('bell-1-rim-ml', (35, 23), (28, 23))
        self.add_line('bell-1-rim-l', (28, 23), (24, 23))
        self.add_contour('bell-1', 'bell-1-dome', 'bell-1-rim-r', 'bell-1-rim-mr', 'bell-1-rim-ml', 'bell-1-rim-l', closed=True)
        self.add_line('tentacle-1-0', (28, 23), (28, 29))
        self.relate("connect", 'bell-1', 'tentacle-1-0')
        self.add_line('tentacle-1-1', (35, 23), (35, 29))
        self.relate("connect", 'bell-1', 'tentacle-1-1')
        self.add_line('tentacle-1-2', (42, 23), (42, 29))
        self.relate("connect", 'bell-1', 'tentacle-1-2')
        self.add_arc('bell-2-dome', (2, 37), (24, 37), radius_x=11, radius_y=6, sweep=True)
        self.add_line('bell-2-rim-r', (24, 37), (20, 37))
        self.add_line('bell-2-rim-mr', (20, 37), (13, 37))
        self.add_line('bell-2-rim-ml', (13, 37), (6, 37))
        self.add_line('bell-2-rim-l', (6, 37), (2, 37))
        self.add_contour('bell-2', 'bell-2-dome', 'bell-2-rim-r', 'bell-2-rim-mr', 'bell-2-rim-ml', 'bell-2-rim-l', closed=True)
        self.add_line('tentacle-2-0', (6, 37), (4, 46))
        self.relate("connect", 'bell-2', 'tentacle-2-0')
        self.add_line('tentacle-2-1', (13, 37), (11, 46))
        self.relate("connect", 'bell-2', 'tentacle-2-1')
        self.add_line('tentacle-2-2', (20, 37), (18, 46))
        self.relate("connect", 'bell-2', 'tentacle-2-2')
