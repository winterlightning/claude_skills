"""A wide gemstone has a flat top, angled shoulders, and a sharp lower point. A horizontal division and two inward-sloping facet lines divide its face into a broad central section and narrow side facets.

HRECT_XL visible bounds (2,6)-(46,42); flat top, angled shoulders, pointed base and two lower facets. Upper minor facets omitted. Lucide gem informed silhouette and facet hierarchy. Bilateral symmetry retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '86994634-b2ec-4d84-9b8a-9809a8c207a9'
SOURCE_PATH = 'pictographic-primitives/science/platinum_86994634-b2ec-4d84-9b8a-9809a8c207a9.svg'
AUTHOR = 'gpt-6'

class FacetedDiamond(Solo48):
    icon_id = 'faceted-diamond'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('diamond', 'gem', 'facet', 'crystal', 'jewel', 'mineral')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_polyline('outline',(14,8),(34,8),(44,20),(24,40),(4,20),closed=True)
        self.add_polyline('table',(4,20),(16,20),(32,20),(44,20))
        self.add_polyline('facets',(16,20),(24,40),(32,20))
        self.relate('connect','outline','table');self.relate('connect','outline','facets');self.relate('connect','table','facets')
