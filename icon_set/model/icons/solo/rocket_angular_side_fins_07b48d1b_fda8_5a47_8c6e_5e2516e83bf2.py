"""A short upright rocket has a pointed rounded body and one circular window. Two broad angular fins spread outward near the bottom, above a small flared nozzle centered beneath the flat tail.

VRECT_XL visible bounds (6,2)-(42,46); curved pointed body, round window, angular wing-like fins and flared nozzle. Fin interior seams omitted. Lucide rocket informed part hierarchy; mirrored fins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '07b48d1b-fda8-5a47-8c6e-5e2516e83bf2'
SOURCE_PATH = 'pictographic-primitives/science/rocket_07b48d1b-fda8-5a47-8c6e-5e2516e83bf2.svg'
AUTHOR = 'gpt-6'

class RocketAngularSideFins(Solo48):
    icon_id = 'rocket-angular-side-fins'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('rocket', 'fin', 'window', 'nozzle', 'space', 'spacecraft')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('nose-right',(24,4),(36,20),radius_x=20)
        self.segments('fins',(36,20),(36,22),(40,28),(40,38),(32,34),(28,36),(20,36),(16,34),(8,38),(8,28),(12,22),(12,20))
        self.add_arc('nose-left',(12,20),(24,4),radius_x=20)
        self.add_contour('hull','nose-right',*(f'fins-{i}' for i in range(1,12)),'nose-left',closed=True)
        self.circle('window',24,23,3)
        self.add_polyline('nozzle',(20,36),(16,44),(32,44),(28,36))
        self.relate('connect','nozzle','hull')
