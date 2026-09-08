"""A standing stag with an upright head and forked antlers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e94fd1b4-129e-4102-9c4f-84126a4d1b78'
SOURCE_PATH = 'pictographic-primitives/animals/deer body_e94fd1b4-129e-4102-9c4f-84126a4d1b78.svg'
AUTHOR = 'gpt-6'


class StandingStag(Solo48):
    icon_id = 'standing-stag'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('deer', 'stag', 'antlers', 'standing', 'buck', 'wildlife', 'forest', 'animal')

    def build(self) -> None:
        # Centerline extremes: (2,2)-(46,46).
        self.add_polyline("body", (6,46),(8,26),(30,26),(32,16),(40,16),(46,22),(38,24),(38,46))
        self.add_polyline("belly", (8,36),(28,36),(30,46))
        self.relate("connect","body","belly")
        self.add_line("tail",(8,26),(2,20))
        self.relate("connect","tail","body")
        self.add_polyline("antler",(36,16),(30,10),(28,2))
        self.relate("connect","antler","body")
        self.add_polyline("tine",(30,10),(40,8),(42,2))
        self.relate("connect","antler","tine")
