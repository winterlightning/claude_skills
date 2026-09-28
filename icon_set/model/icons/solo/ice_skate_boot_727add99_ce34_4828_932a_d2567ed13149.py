"""Right-facing skate boot with two blade supports and a curled runner. No exact local Lucide match; coherent quarter arcs join the ankle and toe. Laces omitted.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '727add99-ce34-4828-932a-d2567ed13149'
SOURCE_PATH = 'pictographic-primitives/symbol/skate ice_727add99-ce34-4828-932a-d2567ed13149.svg'
AUTHOR = 'gpt-6'


class IceSkateBoot(Solo48):
    icon_id = 'ice-skate-boot'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('ice-skate', 'skating', 'winter', 'sport', 'blade', 'rink', 'boot', 'figure-skating')

    def build(self) -> None:

        pts=[(10,10),(24,6),(24,18)]
        for j,(a,b) in enumerate(zip(pts,pts[1:]),1):self.add_line('ankle-'+str(j),a,b)
        self.add_arc('ankle-turn',(24,18),(30,24),radius_x=6,sweep=False)
        self.add_arc('toe',(30,24),(36,30),radius_x=6)
        pts=[(36,30),(32,30),(18,30),(10,30),(10,10)]
        for j,(a,b) in enumerate(zip(pts,pts[1:]),1):self.add_line('sole-'+str(j),a,b)
        self.add_contour('boot','ankle-1','ankle-2','ankle-turn','toe',*['sole-'+str(j) for j in range(1,5)],closed=True)
        self.add_polyline('blade-flat',(6,42),(18,42),(32,42),(36,42))
        self.add_arc('blade-curl',(36,42),(42,36),radius_x=6,sweep=False)
        self.relate('connect','blade-flat','blade-curl')
        for x in (18,32):
            self.add_line('post-'+str(x),(x,30),(x,42))
            self.relate('connect','post-'+str(x),'boot')
            self.relate('connect','post-'+str(x),'blade-flat')
