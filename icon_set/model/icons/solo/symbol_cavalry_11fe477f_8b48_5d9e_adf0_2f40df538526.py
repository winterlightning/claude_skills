"""Standing right-facing horse with arched neck and pricked ear. Bounds (2,2)-(46,46). No useful local horse match; retain angular equine head. Far legs merged into two clear legs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '11fe477f-8b48-5d9e-adf0-2f40df538526'
SOURCE_PATH = 'pictographic-primitives/animals/symbol cavalry_11fe477f-8b48-5d9e-adf0-2f40df538526.svg'
AUTHOR = 'gpt-6'


class Horse(Solo48):
    icon_id = 'horse'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('horse', 'pony', 'stallion', 'equine', 'cavalry', 'animal', 'riding', 'profile')

    def build(self) -> None:
        self.add_polyline('head',(30,14),(36,2),(36,9),(46,19),(44,24),(36,21),(36,30))
        self.add_arc('chest',(36,30),(32,36),radius_x=8,sweep=True)
        self.add_polyline('front-leg',(32,36),(32,46),(26,46),(25,34))
        self.add_arc('belly',(25,34),(14,32),radius_x=24,sweep=True)
        self.add_polyline('rear-leg',(14,32),(10,39),(10,46),(4,46),(4,30))
        self.add_arc('rump',(4,30),(14,20),radius_x=10,sweep=True)
        self.add_line('back',(14,20),(24,20))
        self.add_arc('neck',(24,20),(30,14),radius_x=6,sweep=False)
        self.add_contour('body','chest')
        self.relate('connect','head','body')
        self.relate('connect','body','front-leg')
        self.relate('connect','front-leg','belly')
        self.relate('connect','belly','rear-leg')
        self.relate('connect','rear-leg','rump')
        self.relate('connect','rump','back')
        self.relate('connect','back','neck')
        self.relate('connect','neck','head')
        self.add_arc('tail-top',(14,20),(2,30),radius_x=12,radius_y=10,sweep=False)
        self.add_line('tail-drop',(2,30),(2,36))
        self.add_contour('tail','tail-top','tail-drop')
        self.relate('connect','tail','back')
        self.relate('connect','tail','rump')
