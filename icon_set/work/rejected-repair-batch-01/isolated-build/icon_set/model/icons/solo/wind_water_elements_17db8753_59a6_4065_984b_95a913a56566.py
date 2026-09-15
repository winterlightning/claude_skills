"""Two droplet outlines sit diagonally apart, with the larger droplet at the lower right. Curled wind strokes occupy the upper-right space and a short diagonal stroke separates the drops.

Retained two full drops and a single upper curl; removed small detached stroke.
Construction reference: Lucide wind tangent curl; teardrops authored from paired outlines.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17db8753-59a6-4065-984b-95a913a56566'
SOURCE_PATH = 'pictographic-primitives/weather/elements_17db8753-59a6-4065-984b-95a913a56566.svg'
AUTHOR = 'gpt-6'

class WindWaterElements(Solo48):
    icon_id = 'wind-water-elements'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('element', 'wind', 'water', 'droplet', 'air', 'weather')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_line('small-left',(4, 16),(12, 8))
        self.add_line('small-right',(12, 8),(20, 16))
        self.add_bezier('small-bottom',(20, 16),*(((18.59104929, 17.59157911), (15.91031608, 18.57938541), (12.75, 18.57938541)), ((9.1121049, 18.57938541), (5.76118839, 17.59157911), (4, 16))))
        self.add_line('large-left',(24, 38),(34, 26))
        self.add_line('large-right',(34, 26),(42, 38))
        self.add_bezier('large-bottom',(42, 38),*(((40.32913558, 39.22495165), (36.83322588, 40), (33.0, 40)), ((29.16677412, 40), (25.67086442, 39.22495165), (24, 38))))
        self.add_line('wind-run',(30, 17),(40, 17))
        self.add_arc('wind-curl',(40, 17),(40, 9),radius_x=4,radius_y=4,large_arc=False,sweep=False)
        self.add_contour('small',*('small-left', 'small-right', 'small-bottom'),closed=True)
        self.add_contour('large',*('large-left', 'large-right', 'large-bottom'),closed=True)
        self.add_contour('wind',*('wind-run', 'wind-curl'),closed=False)
