"""An upright oval rocket has a pointed nose with a horizontal seam and a round central window. Two long curved fins sweep down beside its tapered lower body, surrounding a small flared nozzle.

VRECT_XL visible bounds (6,2)-(42,46); pointed body, round window, long curved fins and flared nozzle. Nose seam and fin seams omitted. Lucide rocket informed hierarchy; fins use mirrored arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1bcabfaa-e335-53ce-b141-b4d0ee612688'
SOURCE_PATH = 'pictographic-primitives/science/spaceship_1bcabfaa-e335-53ce-b141-b4d0ee612688.svg'
AUTHOR = 'gpt-6'

class RocketCurvedFins(Solo48):
    icon_id = 'rocket-curved-fins'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
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
        self.add_line('shoulder-right',(36,20),(36,22))
        self.add_arc('fin-right-outer',(36,22),(40,32),radius_x=4,radius_y=10)
        self.add_line('fin-right-tip',(40,32),(40,40))
        self.add_arc('fin-right-inner',(40,40),(32,34),radius_x=8,radius_y=6,sweep=False)
        self.segments('tail',(32,34),(28,36),(20,36),(16,34))
        self.add_arc('fin-left-inner',(16,34),(8,40),radius_x=8,radius_y=6,sweep=False)
        self.add_line('fin-left-tip',(8,40),(8,32))
        self.add_arc('fin-left-outer',(8,32),(12,22),radius_x=4,radius_y=10)
        self.add_line('shoulder-left',(12,22),(12,20))
        self.add_arc('nose-left',(12,20),(24,4),radius_x=20)
        self.add_contour('hull','nose-right','shoulder-right','fin-right-outer','fin-right-tip','fin-right-inner','tail-1','tail-2','tail-3','fin-left-inner','fin-left-tip','fin-left-outer','shoulder-left','nose-left',closed=True)
        self.circle('window',24,23,3)
        self.add_polyline('nozzle',(20,36),(16,44),(32,44),(28,36));self.relate('connect','nozzle','hull')
