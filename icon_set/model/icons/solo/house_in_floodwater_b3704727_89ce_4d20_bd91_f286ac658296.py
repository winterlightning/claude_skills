"""The upper portion of a house rises above two horizontal rows of waves. Its broad pitched roof and single square window remain visible while the lower walls disappear at the waterline.

Omitted the small square window to retain open space under the pitched roof; retained two waterlines.
Construction reference: Lucide house: continuous roof and walls; repeated scalloped water.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b3704727-89ce-4d20-bd91-f286ac658296'
SOURCE_PATH = 'pictographic-primitives/weather/flood house_b3704727-89ce-4d20-bd91-f286ac658296.svg'
AUTHOR = 'gpt-6'

class HouseInFloodwater(Solo48):
    icon_id = 'house-in-floodwater'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    aliases = ()
    keywords = ('flood', 'house', 'water', 'wave', 'disaster', 'inundation')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_line('house-1',(9, 30),(9, 19))
        self.add_line('house-2',(9, 19),(24, 8))
        self.add_line('house-3',(24, 8),(39, 19))
        self.add_line('house-4',(39, 19),(39, 30))
        self.add_line('water-left',(4, 30),(9, 30))
        self.add_bezier('water-a',(9, 30),*(((9.0, 30.55228475), (12.91750844, 31.0), (17.0, 31.0)), ((20.86599325, 31.0), (24.0, 30.55228475), (24, 30))))
        self.add_bezier('water-b',(24, 30),*(((24.0, 30.55228475), (27.13400675, 31.0), (31.0, 31.0)), ((35.08249156, 31.0), (39.0, 30.55228475), (39, 30))))
        self.add_line('water-right',(39, 30),(44, 30))
        self.add_arc('lower-a',(4, 39),(24, 39),radius_x=10,radius_y=1,sweep=False)
        self.add_arc('lower-b',(24, 39),(44, 39),radius_x=10,radius_y=1,sweep=False)
        self.add_contour('house',*('house-1', 'house-2', 'house-3', 'house-4'),closed=False)
        self.add_contour('surface',*('water-left', 'water-a', 'water-b', 'water-right'),closed=False)
        self.add_contour('lower',*('lower-a', 'lower-b'),closed=False)
        self.relate('connect',*('house', 'surface'))
