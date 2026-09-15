"""Diagonal waisted bass body with long neck and headstock; omit fine f-holes, endpin and peg bars. Smooth opposed bouts follow Lucide guitar construction. Extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '084164fe-fde8-45f3-af63-b15e617e7641'
SOURCE_PATH = 'pictographic-primitives/music/contrabass_084164fe-fde8-45f3-af63-b15e617e7641.svg'
AUTHOR = 'gpt-6'

class DoubleBassDiagonal(Solo48):
    icon_id = 'double-bass-diagonal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/music"
    aliases = ()
    keywords = ('contrabass', 'double-bass', 'string', 'instrument', 'orchestra', 'cello', 'music')

    def build(self):
        self.add_bezier('body',(28,16), ((24,12),(18,13),(18,19)), ((18,23),(16,25),(12,23)), ((8,21),(6,26),(6,30)), ((6,37),(11,42),(18,42)), ((25,42),(29,37),(26,33)), ((23,29),(26,27),(30,27)), ((37,27),(35,19),(28,16)))
        self.add_contour('outline','body',closed=True)
        self.add_line('neck',(28,16),(38,6))
        self.add_line('head',(38,6),(42,10))
        self.relate('connect','neck','outline')
        self.relate('connect','neck','head')
