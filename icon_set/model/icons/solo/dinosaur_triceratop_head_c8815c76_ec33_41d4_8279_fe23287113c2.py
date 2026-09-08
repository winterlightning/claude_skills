"""Mirrored triceratops head with three-point frill and tapered snout. Centerlines (5,2)-(43,46). Mirrored dot eyes; frill spikes are deliberate corners."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8815c76-ec33-41d4-8279-fe23287113c2'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur triceratop head_c8815c76-ec33-41d4-8279-fe23287113c2.svg'
AUTHOR = 'gpt-6'


class TriceratopsFrillHead(Solo48):
    icon_id = 'triceratops-frill-head'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals/prehistoric'
    aliases = ()
    keywords = ('triceratops', 'dinosaur', 'head', 'frill', 'spikes', 'prehistoric', 'reptile', 'silhouette')

    def build(self) -> None:
        self.add_arc('frill-left',(5,2),(24,2),radius_x=13,sweep=False)
        self.add_arc('frill-right',(24,2),(43,2),radius_x=13,sweep=False)
        self.add_arc('side-right',(43,2),(39,18),radius_x=4,radius_y=16)
        self.add_line('horn-right',(39,18),(37,23))
        self.add_arc('cheek-right',(42,27),(43,32),radius_x=1,radius_y=5)
        self.add_arc('jowl-right',(43,32),(37,36),radius_x=6,radius_y=4)
        self.add_arc('chin-right',(37,36),(24,46),radius_x=13,radius_y=10)
        self.add_arc('chin-left',(24,46),(11,36),radius_x=13,radius_y=10)
        self.add_arc('jowl-left',(11,36),(5,32),radius_x=6,radius_y=4)
        self.add_arc('cheek-left',(5,32),(6,27),radius_x=1,radius_y=5)
        self.add_line('horn-left',(11,23),(9,18))
        self.add_arc('side-left',(9,18),(5,2),radius_x=4,radius_y=16)
        self.add_line('join-right', (37,23), (42,27))
        self.add_line('join-left', (6,27), (11,23))
        self.add_contour('outline','horn-left','side-left','frill-left','frill-right','side-right','horn-right','join-right','cheek-right','jowl-right','chin-right','chin-left','jowl-left','cheek-left','join-left',closed=True)
        self.add_dot('eye-left', (17,27))
        self.add_dot('eye-right', (31,27))
