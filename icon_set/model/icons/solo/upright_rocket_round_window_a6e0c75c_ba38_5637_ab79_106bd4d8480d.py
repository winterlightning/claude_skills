"""A slender upright rocket has a pointed nose separated by a horizontal seam and one circular window on its body. Matching side fins meet the flat lower edge, above a small flared engine nozzle.

VRECT_XL visible bounds (6,2)-(42,46) preserve an upright rocket. Paired fins are integrated into the outline; nose seam omitted to give the round window clearance. Lucide rocket informed nose, fin and body hierarchy; symmetric about x=24.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6e0c75c-ba38-5637-ab79-106bd4d8480d'
SOURCE_PATH = 'pictographic-primitives/science/exploration apollo saturn v_a6e0c75c-ba38-5637-ab79-106bd4d8480d.svg'
AUTHOR = 'gpt-6'

class UprightRocketRoundWindow(Solo48):
    icon_id = 'upright-rocket-round-window'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('rocket', 'space', 'window', 'fin', 'nozzle', 'launch')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_polyline('hull',(24,4),(36,16),(36,24),(40,36),(28,36),(20,36),(8,36),(12,24),(12,16),closed=True)
        self.circle('window',24,24,3)
        self.add_polyline('nozzle',(20,36),(16,44),(32,44),(28,36))
        self.relate('connect','hull','nozzle')
