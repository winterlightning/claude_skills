"""A human-headed sphinx with a nemes and reclining lion body. HRECT_XL extremes (2,5)-(46,43). Preserve asymmetric body and extended paws; omit face marks, toes and tail curl. No useful local Lucide subject match."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c701c596-0404-4be0-8228-3ddc825a28fa'
SOURCE_PATH = 'pictographic-primitives/culture/batch-03/sphinx_c701c596-0404-4be0-8228-3ddc825a28fa.svg'


class GreatSphinx(Solo48):
    icon_id = 'great-sphinx'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture/objects"
    aliases = ()
    keywords = ('sphinx', 'egyptian', 'giza', 'pharaoh', 'lion', 'monument', 'ancient', 'mythology')

    def build(self) -> None:
        self.add_line('flap-outer-left',(12,35),(2,29))
        self.add_line('headdress-left',(2,29),(4,18))
        self.add_arc('headdress-top',(4,18),(36,18),radius_x=16,radius_y=13)
        self.add_line('headdress-right',(36,18),(38,29))
        self.add_line('flap-outer-right',(38,29),(28,35))
        self.add_contour('headdress','flap-outer-left','headdress-left','headdress-top','headdress-right','flap-outer-right')
        self.add_line('face-top',(12,14),(28,14))
        self.add_line('face-right',(28,14),(28,21))
        self.add_arc('chin',(28,21),(12,21),radius_x=8)
        self.add_line('face-left',(12,21),(12,14))
        self.add_contour('face','face-top','face-right','chin','face-left',closed=True)
        self.add_line('flap-left',(12,21),(12,35))
        self.add_line('flap-right',(28,21),(28,35))
        for flap in ('flap-left','flap-right'):
            self.relate('connect','face',flap)
            self.relate('connect','headdress',flap)
        self.add_arc('haunch',(38,29),(46,37),radius_x=8)
        self.add_line('body-right',(46,37),(46,43))
        self.add_line('base',(46,43),(2,43))
        self.add_arc('paw',(2,43),(10,35),radius_x=8)
        self.add_line('paw-top',(10,35),(12,35))
        self.add_contour('body','haunch','body-right','base','paw','paw-top')
        self.relate('connect','body','headdress')
        self.relate('connect','body','flap-left')
