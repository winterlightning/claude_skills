"""Taj Mahal onion dome, crescent and paired minarets. Centerline extremes (2,2)-(46,46). Terrace bands omitted; doorway retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd0de3f5b-4550-54a2-8cc2-24f251ef93ea'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-04/taj mahal_d0de3f5b-4550-54a2-8cc2-24f251ef93ea.svg'
AUTHOR = 'gpt-6'

class TajMahal(Solo48):
    icon_id = 'taj-mahal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/landmarks"
    aliases = ()
    keywords = ('taj mahal', 'india', 'agra', 'mausoleum', 'dome', 'minaret', 'landmark', 'heritage')

    def build(self) -> None:
        self.add_arc('crescent-left', (20, 2), (24, 6), radius_x=4, radius_y=4, sweep=False)
        self.add_arc('crescent-right', (24, 6), (28, 2), radius_x=4, radius_y=4, sweep=False)
        self.add_contour('crescent', 'crescent-left', 'crescent-right', closed=False)
        self.add_line('finial', (24, 6), (24, 13))
        self.add_arc('onion-left', (24, 13), (14, 26), radius_x=14, radius_y=11, sweep=False)
        self.add_arc('onion-base-left', (14, 26), (24, 31), radius_x=10, radius_y=5, sweep=False)
        self.add_arc('onion-base-right', (24, 31), (34, 26), radius_x=10, radius_y=5, sweep=False)
        self.add_arc('onion-right', (34, 26), (24, 13), radius_x=14, radius_y=11, sweep=False)
        self.add_contour('onion', 'onion-left', 'onion-base-left', 'onion-base-right', 'onion-right', closed=True)
        self.add_line('dome-neck', (24, 31), (24, 33))
        self.add_polyline('terrace', (2, 23), (2, 46), (20, 46), (28, 46), (46, 46), (46, 23), closed=False)
        self.add_polyline('roof', (2, 33), (24, 33), (46, 33), closed=False)
        self.add_line('door-left', (20, 46), (20, 44))
        self.add_arc('door-arch', (20, 44), (28, 44), radius_x=4, radius_y=4, sweep=True)
        self.add_line('door-right', (28, 44), (28, 46))
        self.add_contour('door', 'door-left', 'door-arch', 'door-right', closed=False)
        self.relate("connect", 'crescent', 'finial')
        self.relate("connect", 'finial', 'onion')
        self.relate("connect", 'onion', 'dome-neck')
        self.relate("connect", 'dome-neck', 'roof')
        self.relate("connect", 'terrace', 'door')
