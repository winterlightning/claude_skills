"""Right-facing standing deer with capsule body and crown antlers. Four legs reduced to two visible legs for separation; source asymmetry retained. Lucide bird informs rounded body joins."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6ff6a0a-a017-4795-b53f-e68479e6966b'
SOURCE_PATH = 'pictographic-primitives/animals/deer body_a6ff6a0a-a017-4795-b53f-e68479e6966b.svg'
AUTHOR = 'gpt-6'


class StandingDeer(Solo48):
    icon_id = 'standing-deer'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('deer', 'stag', 'doe', 'standing', 'antlers', 'wildlife', 'forest', 'animal')

    def build(self) -> None:
        # Visible bounds: (0, 0, 48, 48); centerline inset 2.
        self.add_line('back', (12, 24), (28, 24))
        self.add_arc('shoulder', (28, 24), (34, 18), radius_x=6, radius_y=6, sweep=False)
        self.add_line('neck-back', (34, 18), (34, 12))
        self.add_line("head-1", (34, 12), (40, 12))
        self.add_line("head-2", (40, 12), (46, 18))
        self.add_line("head-3", (46, 18), (44, 24))
        self.add_line("head-4", (44, 24), (38, 24))
        self.add_line('neck-front', (38, 24), (38, 26))
        self.add_arc('chest', (38, 26), (26, 38), radius_x=12, radius_y=12, sweep=True)
        self.add_line('belly', (26, 38), (12, 38))
        self.add_arc('rump', (12,38), (12,24), radius_x=10, radius_y=7, sweep=True)
        self.add_contour('body', 'back', 'shoulder', 'neck-back', 'head-1', 'head-2', 'head-3', 'head-4', 'neck-front', 'chest', 'belly', 'rump', closed=True)
        self.add_line('leg-back', (12, 38), (12, 46))
        self.add_line('leg-front', (26, 38), (26, 46))
        self.relate("connect", 'leg-back', 'body')
        self.relate("connect", 'leg-front', 'body')
        self.add_arc('antler-left', (34, 12), (24, 2), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('antler-right', (34, 12), (44, 2), radius_x=10, radius_y=10, sweep=False)
        self.relate("connect", 'antler-left', 'body')
        self.relate("connect", 'antler-right', 'body')
        self.relate("connect", 'antler-left', 'antler-right')
