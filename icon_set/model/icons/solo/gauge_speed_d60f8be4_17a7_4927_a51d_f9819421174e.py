"""An open speed dial has three rays and a teardrop needle pointing northeast. SQUARE extremes (6,6)-(42,42). Lucide gauge informs the open dial and diagonal needle; source teardrop and external rays retained. Intentional asymmetry expresses the reading."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd60f8be4-17a7-4927-a51d-f9819421174e'
SOURCE_PATH = 'pictographic-primitives/symbol/gauge_d60f8be4-17a7-4927-a51d-f9819421174e.svg'
AUTHOR = 'gpt-6'


class GaugeSpeed(Solo48):
    icon_id = 'gauge-speed'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('gauge', 'speed', 'speedometer', 'performance', 'dashboard', 'meter', 'fast', 'dial')

    def build(self) -> None:
        self.add_arc('dial-left',(6,40),(26,20),radius_x=20)
        self.add_arc('dial-top',(26,20),(38,24),radius_x=20)
        self.add_contour('dial','dial-left','dial-top')
        self.add_line('ray-left',(8,10),(12,14))
        self.add_line('ray-top',(24,6),(24,10))
        self.add_line('ray-right',(42,6),(38,10))
        self.add_line('needle-right',(32,30),(26,42))
        self.add_arc('needle-base',(26,42),(20,36),radius_x=6)
        self.add_line('needle-left',(20,36),(32,30))
        self.add_contour('needle','needle-right','needle-base','needle-left',closed=True)
