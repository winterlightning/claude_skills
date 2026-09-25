"""A semicircular guard covers a toothed lower blade and small hub; concentric hub reduced to one ring."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0fbcf6e4-e1c9-4228-8437-36dabfe32073'
SOURCE_PATH = 'pictographic-primitives/tools/power tools circular saw_0fbcf6e4-e1c9-4228-8437-36dabfe32073.svg'
AUTHOR = 'gpt-6'

class GuardedCircularSawBlade(Solo48):
    icon_id = 'guarded-circular-saw-blade'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    aliases = ()
    keywords = ('circular saw', 'saw', 'blade', 'guard', 'power tool', 'cutting', 'woodworking', 'teeth')

    def build(self) -> None:

        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)

        self.add_arc('guard-arc',(6,24),(42,24),radius_x=20)
        self.add_line('guard-right',(42,24),(27,24))
        self.add_line('guard-left',(21,24),(6,24))
        circle('hub',24,24,3)
        self.relate('connect','hub','guard-right')
        self.relate('connect','hub','guard-left')
        self.add_contour('guard','guard-left','guard-arc','guard-right')
        self.add_polyline('blade',(6,24),(6,32),(12,32),(12,38),(18,38),(24,42),(30,38),(36,38),(36,32),(42,32),(42,24))
        self.relate('connect','blade','guard')
