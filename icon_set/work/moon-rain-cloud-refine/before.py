# Review candidate; original preserved.
"""A crescent moon rises behind the upper-right side of an open-bottom cloud. Three parallel diagonal rain strokes fall toward the lower left beneath the foreground cloud.

Reduced secondary lobes and rain count; preserved rightward crescent behind a lower-left cloud.
Construction reference: Lucide moon and cloud: coherent overlapping silhouettes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '93e91edf-3294-4be6-b0ea-84ff55057f87'
SOURCE_PATH = 'pictographic-primitives/weather/weather night rain_93e91edf-3294-4be6-b0ea-84ff55057f87.svg'
AUTHOR = 'gpt-6'

class MoonRainCloud(Solo48):
    icon_id = 'moon-rain-cloud'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/weather'
    aliases = ()
    keywords = ('moon', 'rain', 'cloud', 'night', 'shower', 'weather')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_arc('cloud-dome',(16, 30),(28, 22),radius_x=12,radius_y=8,large_arc=True,sweep=True)
        self.add_bezier('cloud-right-upper',(28,22),((32,22),(34,24),(34,26)))
        self.add_bezier('cloud-right-lower',(34,26),((34,28),(31,30),(28,30)))
        self.add_line('cloud-base',(28, 30),(16, 30))
        self.add_bezier('moon-outer',(28, 22),*(((26.95163751, 17.45649811), (28.21742765, 12.59730588), (31.23554653, 9.579187)), ((34.31708176, 8), (39.58108387, 8), (44, 8))))
        self.add_bezier('moon-inner',(44,8),((40,8),(40,11),(40,15)),((40,19),(41,21),(44,22)))
        self.add_line('moon-tip',(44,22),(34,26))
        self.add_line('rain-left',(16, 39),(15, 40))
        self.add_line('rain-right',(29, 39),(28, 40))
        self.add_contour('cloud',*('cloud-dome', 'cloud-right-upper', 'cloud-right-lower', 'cloud-base'),closed=True)
        self.add_contour('moon',*('moon-outer', 'moon-inner', 'moon-tip'),closed=False)
        self.relate('connect',*('moon', 'cloud'))
