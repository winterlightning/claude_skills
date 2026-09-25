"""A three-lobed cotton boll above pointed bracts and a curved stem. SQUARE extremes (6,6)-(42,42).
Reduction: Reduced three bract leaf interiors to two open bract strokes.
Lucide construction: cloud, leaf
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f4344a39-4867-5bbb-8d94-61f624e6ed6b'
SOURCE_PATH = 'pictographic-primitives/nature/cotton flower bloom_f4344a39-4867-5bbb-8d94-61f624e6ed6b.svg'
AUTHOR = 'gpt-6'


class CottonBoll(Solo48):
    icon_id = 'cotton-boll'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    categories = ("nature", "primitives")
    aliases = ()
    keywords = ('cotton', 'boll', 'plant', 'flower', 'fibre', 'crop', 'natural', 'soft')

    def build(self) -> None:
        self.add_arc("top",(14,16),(34,16),radius_x=10)
        self.add_arc("right",(34,16),(34,32),radius_x=8)
        self.add_line("base-right",(34,32),(24,36))
        self.add_line("base-left",(24,36),(14,32))
        self.add_arc("left",(14,32),(14,16),radius_x=8)
        self.add_contour("boll","top","right","base-right","base-left","left",closed=True)
        self.add_polyline("bracts",(18,24),(24,36),(30,24))
        self.add_line("stem",(24,36),(24,38))
        self.add_arc("stem-tip",(24,38),(20,42),radius_x=4)
        self.add_contour("stalk","stem","stem-tip")
        for member in ("base-right","base-left","bracts-1","bracts-2"):
            self.relate("connect",member,"stem")
        for a in ("base-right","base-left"):
            for b in ("bracts-1","bracts-2"):self.relate("connect",a,b)
