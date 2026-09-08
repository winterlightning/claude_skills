"""A low left-facing whale with a pectoral fin and forked water spout."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '769eae2e-e0b1-5885-a663-304ba6167b21'
SOURCE_PATH = 'pictographic-primitives/animals/whale body_769eae2e-e0b1-5885-a663-304ba6167b21.svg'
AUTHOR = 'gpt-6'


class SpoutingWhale(Solo48):
    icon_id = 'spouting-whale'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('whale', 'spout', 'blow', 'water', 'sea', 'ocean', 'marine', 'mammal')

    def build(self) -> None:
        # Visible keyshape extremes: (0, 0, 48, 48).
        self.add_arc("forehead",(2,29),(16,25),radius_x=26)
        self.add_line("back",(16,25),(32,25))
        self.add_arc("tail-rise",(32,25),(38,19),radius_x=6,sweep=False)
        self.add_line('fluke-1', (38, 19), (34, 13))
        self.add_line('fluke-2', (34, 13), (40, 15))
        self.add_line('fluke-3', (40, 15), (46, 7))
        self.add_line('fluke-4', (46, 7), (46, 26))
        self.add_arc("rump",(46,26),(34,42),radius_x=12,radius_y=16)
        self.add_line('fin-1', (34, 42), (36, 46))
        self.add_line('fin-2', (36, 46), (25, 43))
        self.add_line('fin-3', (25, 43), (18, 36))
        self.add_arc("belly",(25,43),(2,29),radius_x=26)
        self.add_contour("outline","forehead","back","tail-rise","fluke-1","fluke-2","fluke-3","fluke-4","rump","fin-1","fin-2")
        self.add_contour("underside","belly")
        self.relate("connect","outline","underside")
        self.add_contour("pectoral-fin","fin-3")
        self.relate("connect","outline","pectoral-fin")
        self.relate("connect","underside","pectoral-fin")
        self.add_arc("spray-left",(6,2),(14,10),radius_x=8)
        self.add_arc("spray-right",(14,10),(22,2),radius_x=8)
        self.add_contour("spray","spray-left","spray-right")
        self.add_line("spout-stem",(14,10),(14,17))
        self.relate("connect","spray","spout-stem")
