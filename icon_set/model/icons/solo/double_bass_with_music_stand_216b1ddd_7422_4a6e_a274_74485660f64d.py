"""Upright waisted bass at left and music stand at right. Two physical subjects; no modifier. Omit strings, head pegs and page text. Extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '216b1ddd-7422-4a6e-a274-74485660f64d'
SOURCE_PATH = 'pictographic-primitives/music/contrabass sheet_216b1ddd-7422-4a6e-a274-74485660f64d.svg'
AUTHOR = 'gpt-6'

class DoubleBassWithMusicStand(Solo48):
    icon_id = 'double-bass-with-music-stand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "music"
    categories = ("primitives", "music")
    aliases = ()
    keywords = ('contrabass', 'double-bass', 'music-stand', 'orchestra', 'string', 'instrument', 'sheet-music')

    def build(self):
        axis=14
        self.add_bezier('bass',(14,18), ((8,18),(8,22),(10,26)), ((12,29),(6,29),(6,34)), ((6,39),(10,42),(14,42)), ((18,42),(22,39),(22,34)), ((22,29),(16,29),(18,26)), ((20,22),(20,18),(14,18)))
        self.add_contour('bass-outline','bass',closed=True)
        self.add_line('neck',(14,6),(14,18))
        self.relate('connect','neck','bass-outline')
        self.add_polyline('desk',(30,14),(42,14),(42,24),(36,24),(30,24),closed=True)
        self.add_line('stand',(36,24),(36,36))
        self.add_polyline('tripod',(30,42),(36,36),(42,42))
        self.relate('connect','stand','desk')
        self.relate('connect','stand','tripod')
