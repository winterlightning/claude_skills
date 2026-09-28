# Review candidate; original preserved.
"""Three nested semicircular rainbow bands bridge the gap between two clouds at the lower corners. The clouds face inward with rounded lobes and level lower edges.

Two rainbow bands meet clouds with separate crowns, side lobes, and flat bases; third rainbow band omitted.
Construction reference: Lucide cloud: clean small lobes; concentric rainbow arcs with shared center.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '41049662-f336-4650-9604-e8d4818347cc'
SOURCE_PATH = 'pictographic-primitives/weather/weather clouds rainbow_41049662-f336-4650-9604-e8d4818347cc.svg'
AUTHOR = 'gpt-6'

class RainbowBetweenClouds(Solo48):
    icon_id = 'rainbow-between-clouds'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    categories = ('weather', 'primitives')
    aliases = ()
    keywords = ('rainbow', 'cloud', 'sky', 'weather', 'arc', 'sunlight')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_bezier('rainbow-outer',(4, 34),*(((4, 19.6405965), (14.0588745, 8.0), (24.0, 8)), ((33.9411255, 8), (44, 19.6405965), (44, 34))))
        self.add_arc('rainbow-inner',(16, 34),(32, 34),radius_x=8,radius_y=16,large_arc=False,sweep=True)
        self.add_bezier('left-crown-left',(4, 34),*(((4, 31.33247694), (5.84935233, 28.88631641), (9, 28)),))
        self.add_bezier('left-crown-right',(9, 28),*(((13.14213562, 28.0), (16.0, 30.6862915), (16, 34)),))
        self.add_arc('left-lobe',(16, 34),(16, 40),radius_x=3,radius_y=3,large_arc=False,sweep=True)
        self.add_line('left-base',(16, 40),(5, 40))
        self.add_bezier('left-corner',(5, 40),*(((4.15486929, 39.27111995), (4, 38.10876678), (4, 37)),))
        self.add_line('left-side',(4, 37),(4, 34))
        self.add_bezier('right-crown-left',(44, 34),*(((44, 31.33247694), (42.15064767, 28.88631641), (39, 28)),))
        self.add_bezier('right-crown-right',(39, 28),*(((34.85786438, 28.0), (32.0, 30.6862915), (32, 34)),))
        self.add_arc('right-lobe',(32, 34),(32, 40),radius_x=3,radius_y=3,large_arc=False,sweep=False)
        self.add_line('right-base',(32, 40),(43, 40))
        self.add_bezier('right-corner',(43, 40),*(((43.84513071, 39.27111995), (44, 38.10876678), (44, 37)),))
        self.add_line('right-side',(44, 37),(44, 34))
        self.add_contour('left',*('left-crown-left', 'left-crown-right', 'left-lobe', 'left-base', 'left-corner', 'left-side'),closed=True)
        self.add_contour('right',*('right-crown-left', 'right-crown-right', 'right-lobe', 'right-base', 'right-corner', 'right-side'),closed=True)
        self.relate('connect',*('left', 'rainbow-outer'))
        self.relate('connect',*('left', 'rainbow-inner'))
        self.relate('connect',*('right', 'rainbow-outer'))
        self.relate('connect',*('right', 'rainbow-inner'))
