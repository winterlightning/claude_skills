"""Frontal Anubis head with pointed ears and long headdress sides. Extremes (5,2)-(43,46). No useful Lucide match; bilateral contour, tiny face detail omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0cddcbc2-f8fa-4b8b-8f41-459829b3d716'
SOURCE_PATH = 'pictographic-primitives/culture/batch-04/sphinx_0cddcbc2-f8fa-4b8b-8f41-459829b3d716.svg'

class JackalHeadAnubis(Solo48):
    icon_id = 'jackal-head-anubis'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('anubis', 'jackal', 'egyptian', 'god', 'mask', 'mythology', 'pharaoh', 'ancient')

    def build(self) -> None:
        self.add_line('ears-left-1', (9, 25), (9, 2))
        self.add_line('ears-left-2', (9, 2), (18, 17))
        self.add_arc('brow',(18,17),(30,17),radius_x=12)
        self.add_line('ears-right-1', (30, 17), (39, 2))
        self.add_line('ears-right-2', (39, 2), (39, 25))
        self.add_arc('cheek-right',(39,25),(29,36),radius_x=11)
        self.add_line('muzzle-right',(29,36),(29,39))
        self.add_arc('chin',(29,39),(19,39),radius_x=5)
        self.add_line('muzzle-left',(19,39),(19,36))
        self.add_arc('cheek-left',(19,36),(9,25),radius_x=11)
        self.add_contour('head','ears-left-1','ears-left-2','brow','ears-right-1','ears-right-2','cheek-right','muzzle-right','chin','muzzle-left','cheek-left',closed=True)
        self.add_polyline('left-lappet',(9,25),(5,46),(12,46))
        self.add_polyline('right-lappet',(39,25),(43,46),(36,46))
        self.relate('connect','head','left-lappet')
        self.relate('connect','head','right-lappet')
