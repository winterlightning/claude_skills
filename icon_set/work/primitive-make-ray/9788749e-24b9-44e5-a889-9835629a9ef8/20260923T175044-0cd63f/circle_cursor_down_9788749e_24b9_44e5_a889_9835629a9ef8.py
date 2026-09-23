"""A concave down-pointing cursor within a circle.
Construction: All defining parts retained; intentional directional asymmetry.
Lucide construction reference: circle-play; coherent arcs and independent enclosed content.
Keyshape CIRCLE: radial ink radius 22, centre (24,24).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9788749e-24b9-44e5-a889-9835629a9ef8'
SOURCE_PATH = 'icon_set/work/todo-references/circle cursor down_9788749e-24b9-44e5-a889-9835629a9ef8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circle-cursor-down'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('circle', 'cursor', 'down')

    def build(self):
        # Circle symbol owns its centre and radius; independent inner content.
        cx, cy, r = 24, 24, 20
        self.add_arc('ring-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc('ring-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour('ring', 'ring-top', 'ring-bottom', closed=True)
        # One concave arrowhead; rotations preserve the paired shoulders.
        direction = 'down'
        points = [(-8,-7),(0,-2),(8,-7),(0,10)]
        def orient(x,y):
            if direction == 'up': return (-x,-y)
            if direction == 'right': return (y,-x)
            if direction == 'west': return (-y,x)
            return (x,y)
        self.add_polyline('cursor', *((24+a,24+b) for a,b in (orient(x,y) for x,y in points)), closed=True)

