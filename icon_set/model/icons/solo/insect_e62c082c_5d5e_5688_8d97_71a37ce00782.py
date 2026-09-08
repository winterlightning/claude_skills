"""Eye-free insect head with long paired antennae and two hooked legs. Centerline extremes (5,2)-(43,46). Mirrored quarter ellipses follow Lucide bug geometry; eyes omitted as in the source."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e62c082c-5d5e-5688-8d97-71a37ce00782'
SOURCE_PATH = 'pictographic-primitives/animals/insect_e62c082c-5d5e-5688-8d97-71a37ce00782.svg'
AUTHOR = 'gpt-6'


class BugHeadWithAntennae(Solo48):
    icon_id = 'bug-head-with-antennae'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('insect', 'head', 'antennae', 'bug', 'face', 'minimal', 'nature', 'larva')

    def build(self) -> None:
        self.add_line('forehead', (18, 18), (30, 18))
        self.add_arc('temple-r', (30, 18), (36, 24), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('cheek-r', (36, 24), (30, 38), radius_x=10, radius_y=15, sweep=True)
        self.add_arc('chin', (30, 38), (18, 38), radius_x=8, radius_y=5, sweep=True)
        self.add_arc('cheek-l', (18, 38), (12, 24), radius_x=10, radius_y=15, sweep=True)
        self.add_arc('temple-l', (12, 24), (18, 18), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('head', 'forehead', 'temple-r', 'cheek-r', 'chin', 'cheek-l', 'temple-l', closed=True)
        self.add_arc('antenna-l', (18, 18), (5, 2), radius_x=18, radius_y=20, sweep=True)
        self.relate("connect", 'head', 'antenna-l')
        self.add_arc('leg-l', (18, 38), (13, 46), radius_x=10, radius_y=10, sweep=False)
        self.relate("connect", 'head', 'leg-l')
        self.add_arc('antenna-r', (30, 18), (43, 2), radius_x=18, radius_y=20, sweep=False)
        self.relate("connect", 'head', 'antenna-r')
        self.add_arc('leg-r', (30, 38), (35, 46), radius_x=10, radius_y=10, sweep=True)
        self.relate("connect", 'head', 'leg-r')
