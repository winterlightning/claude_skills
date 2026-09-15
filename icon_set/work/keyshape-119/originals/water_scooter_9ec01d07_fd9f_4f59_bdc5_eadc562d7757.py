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
    category = 'objects/vehicle'
    aliases = ()
    keywords = ('jet-ski', 'water-scooter', 'watercraft', 'waves', 'sea', 'sport', 'vehicle', 'summer')

    def build(self) -> None:
        self.add_polyline('upper-body', (6, 27), (10, 23), (22, 23), (30, 15), (42, 25))
        self.add_arc('bow', (42, 25), (42, 27), radius_x=2, radius_y=2, sweep=True)
        self.relate("connect", 'upper-body', 'bow')
        self.add_polyline('handlebar', (30, 15), (26, 8), (20, 8))
        self.relate("connect", 'upper-body', 'handlebar')
        self.add_arc('wave-left', (6, 36), (24, 36), radius_x=10, radius_y=4, sweep=False)
        self.add_arc('wave-right', (24, 36), (42, 36), radius_x=10, radius_y=4, sweep=False)
        self.add_contour('water', 'wave-left', 'wave-right')
