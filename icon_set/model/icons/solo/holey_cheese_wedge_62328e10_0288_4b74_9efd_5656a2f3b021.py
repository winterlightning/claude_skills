"""Cheese wedge with triangular top and broad perforated side. HRECT_L allows two separated circular holes. Reference supplies curved rind and wedge; no Lucide cheese match. Reduce three holes and partial edge bite to two differently sized holes; level lower face for clearance."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '62328e10-0288-4b74-9efd-5656a2f3b021'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/cheddar_62328e10-0288-4b74-9efd-5656a2f3b021.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'holey-cheese-wedge'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ['Holey Cheese Wedge']
    keywords = ['cheese', 'wedge', 'holes', 'dairy', 'food', 'slice', 'ingredient']
    def build(self):
        self.add_line("slope",(4,22),(24,8))
        self.add_bezier("rind",(24,8),((32,8),(44,8),(44,12)))
        self.add_line("side-1",(44,12),(44,40))
        self.add_line("side-2",(44,40),(4,40))
        self.add_line("side-3",(4,40),(4,22))
        self.add_contour("outline","slope","rind","side-1","side-2","side-3",closed=True)
        self.add_line("top-seam",(4,22),(44,12))
        self.relate("connect","outline","top-seam")
        for i,(x,y,r) in enumerate(((18,30,2),(32,27,3))):
            name=f"hole{i}"
            self.add_arc(name+"a",(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+"b",(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+"a",name+"b",closed=True)
