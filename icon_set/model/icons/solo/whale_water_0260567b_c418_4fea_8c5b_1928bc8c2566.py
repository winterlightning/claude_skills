"""An open whale back with a raised notched tail and detached forked spout."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0260567b-c418-4fea-8c5b-1928bc8c2566'
SOURCE_PATH = 'pictographic-primitives/animals/whale water_0260567b-c418-4fea-8c5b-1928bc8c2566.svg'
AUTHOR = 'gpt-6'


class WhaleTailWithSpout(Solo48):
    icon_id = 'whale-tail-with-spout'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('whale', 'tail', 'spout', 'water', 'sea', 'ocean', 'marine', 'minimal')

    def build(self) -> None:
        # Visible keyshape extremes: (0, 3, 48, 45).
        self.add_arc("head",(2,43),(14,31),radius_x=12)
        self.add_arc("back",(14,31),(28,36),radius_x=22)
        self.add_arc("tail-neck",(28,36),(38,25),radius_x=11,sweep=False)
        self.add_arc("fluke-left",(38,25),(34,13),radius_x=12)
        self.add_line('notch-1', (34, 13), (40, 17))
        self.add_line('notch-2', (40, 17), (46, 13))
        self.add_arc("fluke-right",(46,13),(42,25),radius_x=20)
        self.add_line("tail-stem",(42,25),(40,39))
        self.add_contour("whale","head","back","tail-neck","fluke-left","notch-1","notch-2","fluke-right","tail-stem")
        self.add_arc("spray-left",(2,13),(10,13),radius_x=4,radius_y=8)
        self.add_arc("spray-right",(10,13),(18,13),radius_x=4,radius_y=8)
        self.add_contour("spray","spray-left","spray-right")
        self.add_line("spout-stem",(10,13),(10,22))
        self.relate("connect","spray","spout-stem")
