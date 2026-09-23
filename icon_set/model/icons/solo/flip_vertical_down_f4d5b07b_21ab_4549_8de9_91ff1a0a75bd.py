"""A central curved down arrow separates two horizontal balance marks. Its direction creates deliberate vertical asymmetry; envelope bounds (4,8)-(44,40).
Construction references: No useful local Lucide match. One smooth bent stem and connected three-point arrowhead preserve the source direction."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f4d5b07b-21ab-4549-8de9-91ff1a0a75bd'
SOURCE_PATH = 'icon_set/work/todo-references/flip vertical down_f4d5b07b-21ab-4549-8de9-91ff1a0a75bd.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'flip-vertical-down'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'arrows'
    aliases = ()
    keywords = ('flip', 'vertical', 'down')

    def page(self):
        self.add_line("page-top",(12,4),(28,4)); self.add_line("page-fold-edge",(28,4),(40,16)); self.add_line("page-right",(40,16),(40,40))
        self.add_arc("page-br",(40,40),(36,44),radius_x=4); self.add_line("page-bottom",(36,44),(12,44)); self.add_arc("page-bl",(12,44),(8,40),radius_x=4)
        self.add_line("page-left",(8,40),(8,8)); self.add_arc("page-tl",(8,8),(12,4),radius_x=4)
        self.add_contour("page","page-top","page-fold-edge","page-right","page-br","page-bottom","page-bl","page-left","page-tl",closed=True)
        self.add_polyline("fold-crease",(28,4),(28,16),(40,16)); self.relate("connect","page","fold-crease")

    def circle(self,name,x,y,r):
        self.add_arc(name+"-upper",(x-r,y),(x+r,y),radius_x=r,sweep=False); self.add_arc(name+"-lower",(x+r,y),(x-r,y),radius_x=r,sweep=False)
        self.add_contour(name,name+"-upper",name+"-lower",closed=True)

    def build(self):
        self.add_line("left-mark",(4,24),(8,24))
        self.add_line("right-mark",(40,24),(44,24))
        self.add_bezier("arrow-stem",(25,8),((20,15),(17,29),(20,40)))
        self.add_polyline("arrow-head",(14,34),(20,40),(26,34))
        self.relate("connect","arrow-stem","arrow-head")
