'A crescent with a smooth concave sweep behind a rounded cloud, with two clear diagonal rain strokes; informed by Lucide cloud-moon-rain.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '93e91edf-3294-4be6-b0ea-84ff55057f87'
SOURCE_PATH = 'pictographic-primitives/weather/weather night rain_93e91edf-3294-4be6-b0ea-84ff55057f87.svg'
AUTHOR = 'gpt-6'

class MoonRainCloud(Solo48):
    icon_id = 'moon-rain-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    categories = ('weather', 'primitives')
    aliases = ()
    keywords = ('moon', 'rain', 'cloud', 'night', 'shower', 'weather')

    def build(self) -> None:
        # A rounded foreground cloud occludes the lower crescent. The two actual
        # intersection points are shared; rainfall sits nine units below the base.
        # SQUARE centerline envelope (6,6)-(42,42), with constant four-unit strokes.
        self.add_arc('cloud-left',(6,22),(14,14),radius_x=8)
        self.add_bezier('cloud-crown',(14,14),((18,14),(21,15),(22,18)))
        self.add_bezier('cloud-shoulder',(22,18),((23,21),(23,21),(23,22)))
        self.add_bezier('cloud-lobe',(23,22),((26,18),(32,20),(32,24)))
        self.add_arc('cloud-right',(32,24),(26,30),radius_x=6)
        self.add_line('cloud-base',(26,30),(14,30))
        self.add_arc('cloud-bottom',(14,30),(6,22),radius_x=8)
        self.add_contour('cloud','cloud-left','cloud-crown','cloud-shoulder','cloud-lobe','cloud-right','cloud-base','cloud-bottom',closed=True)
        self.add_bezier('moon-outer',(22,18),((22,11),(26,6),(32,6)))
        self.add_bezier('moon-inner',(32,6),((29,12),(34,16),(42,14)))
        self.add_bezier('moon-lower',(42,14),((41,20),(37,24),(32,24)))
        self.add_contour('moon','moon-outer','moon-inner','moon-lower')
        self.relate('connect','moon','cloud')
        self.add_line('rain-left',(15,39),(13,42))
        self.add_line('rain-right',(27,39),(25,42))
