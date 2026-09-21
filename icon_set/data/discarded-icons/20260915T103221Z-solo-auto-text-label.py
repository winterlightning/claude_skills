"""AUTO reflowed as AU / TO to preserve legible rounded capitals. HRECT_L ink (6,6)-(42,42). Lucide type informs lettering; triangular A and rounded U/O improve native reading."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f89489d3-928e-4d8e-8a13-9ff760315c90'
SOURCE_PATH = 'pictographic-primitives/transportation/automatic drive gear_f89489d3-928e-4d8e-8a13-9ff760315c90.svg'
AUTHOR = 'gpt-6'

class AutoTextLabel(Solo48):
    icon_id = 'auto-text-label'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('auto', 'automatic', 'gear', 'transmission', 'car', 'dashboard', 'text', 'label')

    def build(self) -> None:
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.
        self.add_polyline('a-outline',(4, 20),(4, 17),(12,8),(18,17),(20,20))
        self.add_line('a-bar',(4, 17),(18,17))
        self.relate('connect','a-outline','a-bar')
        self.add_line('u-left',(30,8),(30,13))
        self.add_arc('u-bottom',(30,13),(44, 13),radius_x=7,sweep=False)
        self.add_line('u-right',(44, 13),(44, 8))
        self.add_contour('u','u-left','u-bottom','u-right')
        self.add_polyline('t-bar',(4, 29),(12,29),(20,29))
        self.add_line('t-stem',(12,29),(12,40))
        self.relate('connect','t-bar','t-stem')
        self.add_line('o-top',(33,29),(41,29))
        self.add_arc('o-tr',(41,29),(44, 32),radius_x=3)
        self.add_line('o-right',(44, 32),(44, 37))
        self.add_arc('o-br',(44, 37),(41,40),radius_x=3)
        self.add_line('o-bottom',(41,40),(33,40))
        self.add_arc('o-bl',(33,40),(30,37),radius_x=3)
        self.add_line('o-left',(30,37),(30,32))
        self.add_arc('o-tl',(30,32),(33,29),radius_x=3)
        self.add_contour('o','o-top','o-tr','o-right','o-br','o-bottom','o-bl','o-left','o-tl',closed=True)
