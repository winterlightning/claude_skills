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
        self.add_arc("forehead",(6,29),(16,25),radius_x=26)
        self.add_line("back",(16,25),(32,25))
        self.add_bezier('tail-rise',(32,25),((33,25),(34,24),(34,22)))
        self.add_line('fluke-1',(34,22),(28,10))
        self.add_line('fluke-2',(28,10),(36,14))
        self.add_line('fluke-3',(36,14),(42,7))
        self.add_line('fluke-4', (42, 7), (42, 26))
        self.add_bezier('rump', (42, 26), *(((42, 33.11339482), (39.04103628, 39.63648956), (34, 42)),))
        self.add_line('fin-1', (34, 42), (36, 42))
        self.add_line('fin-2', (36, 42), (25, 42))
        self.add_line('fin-3', (25, 42), (18, 36))
        self.add_arc("belly",(25,42),(6,29),radius_x=26)
        self.add_contour("outline","forehead","back","tail-rise","fluke-1","fluke-2","fluke-3","fluke-4","rump","fin-1","fin-2")
        self.add_contour("underside","belly")
        self.relate("connect","outline","underside")
        self.add_contour("pectoral-fin","fin-3")
        self.relate("connect","outline","pectoral-fin")
        self.relate("connect","underside","pectoral-fin")
        self.add_bezier('spray-left', (6, 6), *(((9.2325716, 6), (12.39737339, 7.16125546), (14, 10)),))
        self.add_bezier('spray-right',(14,10),((15,8),(18,6),(20,6)))
        self.add_contour("spray","spray-left","spray-right")
        self.add_line("spout-stem",(14,10),(14,17))
        self.relate("connect","spray","spout-stem")
