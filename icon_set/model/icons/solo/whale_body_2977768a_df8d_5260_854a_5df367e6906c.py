"""A left-facing whale with a rounded body, raised tail and forked water spout."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2977768a-df8d-5260-854a-5df367e6906c'
SOURCE_PATH = 'pictographic-primitives/animals/whale body_2977768a-df8d-5260-854a-5df367e6906c.svg'
AUTHOR = 'gpt-6'


class WhaleWithSpout(Solo48):
    icon_id = 'whale-with-spout'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('whale', 'spout', 'water', 'sea', 'ocean', 'marine', 'tail', 'mammal')

    def build(self) -> None:
        # Visible keyshape extremes: (0, 0, 48, 48).
        self.add_arc("back",(2,31),(16,19),radius_x=14,radius_y=12)
        self.add_arc("saddle",(16,19),(35,24),radius_x=18,sweep=False)
        self.add_line("tail-neck",(35,24),(36,16))
        self.add_arc("tail-left",(36,16),(34,6),radius_x=12)
        self.add_line('fluke-1', (34, 6), (40, 11))
        self.add_line('fluke-2', (40, 11), (46, 6))
        self.add_arc("tail-right",(46,6),(43,19),radius_x=30)
        self.add_arc("rump",(43,19),(25,46),radius_x=27)
        self.add_arc("belly",(25,46),(2,31),radius_x=23,radius_y=15)
        self.add_contour("whale","back","saddle","tail-neck","tail-left","fluke-1","fluke-2","tail-right","rump","belly",closed=True)
        self.add_dot("eye",(11,30))
        self.add_arc("spray-left",(8,2),(16,10),radius_x=8)
        self.add_arc("spray-right",(16,10),(24,2),radius_x=8)
        self.add_contour("spout","spray-left","spray-right")
