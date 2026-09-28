"""Revision of nintendo-switch. The rejected console was too tall and its seams dominated. Rebuilt the three panels with balanced controller widths and smooth outside corners.
Symbol plan: redraw the original subject with one coherent SOLO48 construction.
"""
"""Nintendo switch (video-games), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '447b2d50-1abc-5da9-852c-420f8701c4d4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__nintendo-switch/20260927T074149Z-thuan-mac-1/reference/nintendo switch_447b2d50-1abc-5da9-852c-420f8701c4d4.svg'
AUTHOR = 'gpt-6'

class NintendoSwitch(Solo48):
    icon_id = 'nintendo-switch'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('nintendo', 'switch', 'video-games')

    def build(self):
        points=[(12,10),(36,10),(44,18),(44,30),(36,38),(12,38),(4,30),(4,18),(12,10)]
        names=[]
        for i,(a,b) in enumerate(zip(points,points[1:])):
            n=f'edge-{i}'
            if i%2: self.add_arc(n,a,b,radius_x=8)
            else: self.add_line(n,a,b)
            names.append(n)
        self.add_contour('outer',*names,closed=True)
        for name,x in [('left-seam',14),('right-seam',34)]:
            self.add_line(name,(x,10),(x,38))
            self.relate('connect',name,'outer')
