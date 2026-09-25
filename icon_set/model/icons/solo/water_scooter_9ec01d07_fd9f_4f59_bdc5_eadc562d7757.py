"""Water Scooter. Retains the rising bow, long seat, bent handlebar and waterline; omits tiny hull accents. Deliberate right-facing asymmetry.

HRECT_L visible extremes (2, 6, 46, 42), centerlines (4, 8, 44, 40).
Lucide sailboat: sparse side silhouette and coherent hull contour. The supplied reference sets the scooter seat, handlebar and waterline.
Geometry authored directly on SOLO48. Letter order and directional numerals
retain intentional asymmetry; repeated letters share construction parameters.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9ec01d07-fd9f-4f59-bdc5-eadc562d7757'
SOURCE_PATH = 'pictographic-primitives/symbol/Water Scooter_9ec01d07-fd9f-4f59-bdc5-eadc562d7757.svg'
AUTHOR = 'gpt-6'


class WaterScooter(Solo48):
    icon_id = 'water-scooter'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbol'
    aliases = ()
    keywords = ('jet-ski', 'water-scooter', 'watercraft', 'waves', 'sea', 'sport', 'vehicle', 'summer')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_line('upper-body-1',(4, 27),(9, 23))
        self.add_line('upper-body-2',(9, 23),(22, 23))
        self.add_line('upper-body-3',(22, 23),(30, 15))
        self.add_line('upper-body-4',(30, 15),(44, 25))
        self.add_bezier('bow',(44, 25),*(((44, 25.61880215), (44, 26.38119785), (44, 27)),))
        self.add_line('handlebar-1',(30, 15),(26, 8))
        self.add_line('handlebar-2',(26, 8),(20, 8))
        self.add_bezier('wave-left',(4, 38),*(((6.08858053, 39.22495165), (10.45846765, 40), (15.0, 40)), ((18.83322588, 40), (22.32913558, 39.22495165), (24, 38))))
        self.add_bezier('wave-right',(24, 38),*(((25.67086442, 39.22495165), (29.16677412, 40), (33.0, 40)), ((37.54153235, 40), (41.91141947, 39.22495165), (44, 38))))
        self.add_contour('upper-body',*('upper-body-1', 'upper-body-2', 'upper-body-3', 'upper-body-4'),closed=False)
        self.add_contour('handlebar',*('handlebar-1', 'handlebar-2'),closed=False)
        self.add_contour('water',*('wave-left', 'wave-right'),closed=False)
        self.relate('connect',*('upper-body', 'bow'))
        self.relate('connect',*('upper-body', 'handlebar'))
