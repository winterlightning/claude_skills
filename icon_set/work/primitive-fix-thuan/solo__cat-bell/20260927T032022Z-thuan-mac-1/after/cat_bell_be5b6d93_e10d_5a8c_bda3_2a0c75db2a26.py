"""Cat Bell.

Plan: Symmetric arched bell shoulders flow into flared skirt; top suspension loop attaches at crown.
Keyshape centerline extremes: (6,6)-(42,42)
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'be5b6d93-e10d-5a8c-bda3-2a0c75db2a26'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cat-bell/20260927T032022Z-thuan-mac-1/reference/cat bell_be5b6d93-e10d-5a8c-bda3-2a0c75db2a26.svg'
AUTHOR = 'gpt-6'

class CatBell(Solo48):
    icon_id = 'cat-bell'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('bell', 'cat', 'collar', 'jingle', 'pet', 'accessory', 'sound')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(point): return (2 * axis - point[0], point[1])
        # The loop meets two explicit crown nodes; a flat crown keeps the opening broad.
        arc('loop',(20,10),mirror((20,10)),4)
        line('loop-left',(20,10),(20,18))
        line('loop-right',mirror((20,10)),mirror((20,18)))
        contour('hanger','loop-left')
        line('crown',(20,18),mirror((20,18)))
        arc('shoulder-left',(20,18),(12,26),8,sweep=False)
        arc('skirt-left',(12,26),(6,42),18,sweep=True)
        line('lip',(6,42),mirror((6,42)))
        arc('skirt-right',mirror((6,42)),mirror((12,26)),18,sweep=True)
        arc('shoulder-right',mirror((12,26)),mirror((20,18)),8,sweep=False)
        contour('bell','shoulder-left','skirt-left','lip','skirt-right','shoulder-right')
        self.relate('connect','loop','hanger')
        self.relate('connect','loop','loop-right')
        self.relate('connect','hanger','bell')
        self.relate('connect','loop-right','bell')
        self.relate('connect','crown','bell')
        self.relate('connect','crown','hanger')
        self.relate('connect','crown','loop-right')
