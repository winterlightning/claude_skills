"""An engine with two face vents and a rounded side cover. Square keyshape provides height for the separated vents. No exact Lucide match; cast corners and asymmetric ports retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd9383db2-4d70-57a0-9f02-11f604de9926'
SOURCE_PATH = 'pictographic-primitives/transportation/car engine_d9383db2-4d70-57a0-9f02-11f604de9926.svg'
SOURCE_REFERENCES = (('d9383db2-4d70-57a0-9f02-11f604de9926', 'pictographic-primitives/transportation/car engine_d9383db2-4d70-57a0-9f02-11f604de9926.svg'),)
AUTHOR = 'gpt-6'

class EngineVentLines(Solo48):
    icon_id = 'engine-vent-lines'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('engine', 'motor', 'engine block', 'car', 'mechanic', 'service', 'dashboard', 'automotive')

    def build(self) -> None:
        self.add_polyline('block',(14,15),(25,15),(34,15),(34,20),(34,36),(34,42),(18,42),(14,38),(14,34),(14,22),(14,15),closed=True)
        self.add_polyline('cap',(20,6),(25,6),(30,6))
        self.add_line('neck',(25,6),(25,15))
        self.relate('connect','neck','cap')
        self.relate('connect','neck','block')
        self.add_polyline('port',(14,22),(6,22),(6,34),(14,34))
        self.relate('connect','port','block')
        self.add_line('cover-top',(34,20),(39,20))
        self.add_arc('cover-tr',(39,20),(42,23),radius_x=3)
        self.add_line('cover-right',(42,23),(42,33))
        self.add_arc('cover-br',(42,33),(39,36),radius_x=3)
        self.add_line('cover-bottom',(39,36),(34,36))
        self.add_contour('cover','cover-top','cover-tr','cover-right','cover-br','cover-bottom')
        self.relate('connect','cover','block')
        for y in (24,33):
            self.add_line(f'vent-{y}',(22,y),(26,y))
