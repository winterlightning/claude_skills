"""A tall upright rocket has a sharply pointed nose divided by a horizontal seam, a narrow oval window, and triangular side fins. A small pointed exhaust flame hangs directly below the body.

VRECT_XL visible bounds (6,2)-(42,46); tall pointed rocket, vertical oval window, triangular fins and pointed exhaust. Nose seam omitted for window clearance. Lucide rocket informed silhouette; mirrored geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '333e59a6-020c-5ee8-88db-84be7c39ea0f'
SOURCE_PATH = 'pictographic-primitives/science/rocket_333e59a6-020c-5ee8-88db-84be7c39ea0f.svg'
AUTHOR = 'gpt-6'

class LaunchingRocketOvalWindow(Solo48):
    icon_id = 'launching-rocket-oval-window'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('rocket', 'launch', 'window', 'flame', 'fin', 'space')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('nose-right',(24,4),(37,18),radius_x=22)
        self.segments('body',(37,18),(37,26),(40,36),(31,36),(17,36),(8,36),(11,26),(11,18))
        self.add_arc('nose-left',(11,18),(24,4),radius_x=22)
        self.add_contour('hull','nose-right',*(f'body-{i}' for i in range(1,8)),'nose-left',closed=True)
        self.add_arc('window-right',(24,17),(24,27),radius_x=3,radius_y=5)
        self.add_arc('window-left',(24,27),(24,17),radius_x=3,radius_y=5)
        self.add_contour('window','window-right','window-left',closed=True)
        self.add_polyline('flame',(17,36),(24,44),(31,36));self.relate('connect','flame','hull')
