"""A swimming plesiosaur with a long neck and two paddles."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '33faf7f8-ee12-57c0-825a-cc1487bf0c4f'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur plesiosaur_33faf7f8-ee12-57c0-825a-cc1487bf0c4f.svg'
AUTHOR = 'gpt-6'


class Plesiosaur(Solo48):
    icon_id = 'plesiosaur'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('plesiosaur', 'dinosaur', 'marine', 'swimming', 'prehistoric', 'reptile', 'sea', 'extinct')

    def build(self) -> None:
        # Centerline extremes: (2,2)-(46,46).
        self.add_arc("head",(8,12),(8,2),radius_x=6,radius_y=5)
        self.add_line("crown",(8,2),(12,2))
        self.add_arc("nape",(12,2),(18,8),radius_x=6)
        self.add_line("neck",(18,8),(20,24))
        self.add_arc("back",(20,24),(38,28),radius_x=18,radius_y=8)
        self.add_line("tail-1",(38,28),(46,36))
        self.add_line("tail-2",(46,36),(36,36))
        self.add_line("tail-3",(36,36),(36,46))
        self.add_arc("rear-paddle",(36,46),(28,36),radius_x=8,radius_y=10)
        self.add_line("belly",(28,36),(20,36))
        self.add_line("front-paddle-tip",(20,36),(16,46))
        self.add_arc("front-paddle",(16,46),(10,36),radius_x=6,radius_y=10)
        self.add_line("throat",(10,36),(8,12))
        self.add_contour("reptile","head","crown","nape","neck","back","tail-1","tail-2","tail-3","rear-paddle","belly","front-paddle-tip","front-paddle","throat",closed=True)
