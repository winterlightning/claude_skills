"""Demeter in a draped garment holding a branching harvest stalk. Preserve female figure and held plant; reduce hair and folds to one sweep."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b451532-820c-4276-ab4a-3f9c1c9b785d'
SOURCE_PATH = 'pictographic-primitives/religion/demeter_1b451532-820c-4276-ab4a-3f9c1c9b785d.svg'
AUTHOR = 'gpt-6'


class DemeterHoldingStalk(Solo48):
    icon_id = 'demeter-holding-stalk'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "religion"
    aliases = ()
    keywords = ('demeter', 'stalk', 'harvest', 'goddess', 'greek', 'mythology', 'figure')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-bottom', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # VRECT box (8,4)-(40,44); held stalk at right.
        self.oval('head',16,11,7)
        self.add_line('hair',(9,11),(8,20))
        self.relate('connect','head','hair')
        self.add_polyline('gown',(13,27),(8,44),(27,44),(25,34),(23,27),(13,27))
        self.add_line('arm',(25,34),(35,34))
        self.relate('connect','arm','gown')
        self.add_polyline('stalk',(35,44),(35,34),(35,23),(35,12))
        self.add_polyline('leaves',(30,17),(35,23),(40,17))
        self.relate('connect','stalk','leaves');self.relate('connect','stalk','arm')
