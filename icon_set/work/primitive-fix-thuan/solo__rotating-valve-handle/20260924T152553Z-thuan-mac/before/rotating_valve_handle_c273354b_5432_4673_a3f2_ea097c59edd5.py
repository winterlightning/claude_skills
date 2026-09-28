"""Rotating Valve Handle. Reference preserves whole subject. No useful local Lucide valve match was found.
The centered capsule owns its tangent arcs; arrows rotate as one definition.
Simplification omits the collar and reduces the mounting base to its horizontal foot.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'c273354b-5432-4673-a3f2-ea097c59edd5'
SOURCE_PATH = 'pictographic-primitives/construction/valve_c273354b-5432-4673-a3f2-ea097c59edd5.svg'
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = 'rotating-valve-handle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    aliases = ()
    keywords = ('rotating', 'valve', 'handle')
    def build(self):
        self.add_line("handle-top",(20,12),(28,12))
        self.add_arc("handle-right",(28,12),(28,20),radius_x=4)
        self.add_line("handle-bottom-right",(28,20),(24,20))
        self.add_line("handle-bottom-left",(24,20),(20,20))
        self.add_arc("handle-left",(20,20),(20,12),radius_x=4)
        self.add_contour("handle","handle-top","handle-right","handle-bottom-right","handle-bottom-left","handle-left",closed=True)
        self.add_line("stem",(24,20),(24,40))
        self.add_line("base-left",(16,40),(24,40))
        self.add_line("base-right",(24,40),(32,40))
        self.relate("connect","handle","stem")
        self.relate("connect","base-left","base-right","stem")
        for side in (0,1):
            def p(x,y): return (x,y) if side==0 else (48-x,40-y)
            n=f"rotation-{side}"
            self.add_bezier(n,p(10,8),(p(6,10),p(4,14),p(4,20)),(p(4,24),p(4,28),p(4,32)))
            self.add_polyline(n+"-head",p(4,26),p(4,32),p(10,32))
            self.relate("connect",n,n+"-head")
