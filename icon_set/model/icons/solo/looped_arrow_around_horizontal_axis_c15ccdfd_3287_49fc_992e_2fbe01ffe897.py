"""Horizontal Axis Rotation Arrow.
Plan: Elliptical rotation arrow crosses a horizontal axis, with an open rear section. Centerline extremes (6,6)-(42,42).
Construction: Lucide rotate-3d; elliptical loop and open arrowhead.
Reduction: Tiny detached continuation stroke removed.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c15ccdfd-3287-49fc-992e-2fbe01ffe897'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/rotation x axis_c15ccdfd-3287-49fc-992e-2fbe01ffe897.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/rotation x axis_c15ccdfd-3287-49fc-992e-2fbe01ffe897.svg'

def _run(icon, name, *points):
    for i,(a,b) in enumerate(zip(points,points[1:]),1):
        icon.add_line(f'{name}-{i}',a,b)

def _circle(icon, name, cx, cy, radius):
    a,b=(cx-radius,cy),(cx+radius,cy)
    icon.add_arc(name+'-a',a,b,radius_x=radius)
    icon.add_arc(name+'-b',b,a,radius_x=radius)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)


class Drawing(Solo48):
    icon_id = 'looped-arrow-around-horizontal-axis'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('horizontal', 'axis', 'rotation', 'arrow')

    def build(self):
        self.add_arc('upper-left',(12,20),(24,6),radius_x=12,radius_y=14)
        self.add_arc('upper-right',(24,6),(36,24),radius_x=12,radius_y=18)
        self.add_arc('lower-right',(36,24),(24,42),radius_x=12,radius_y=18)
        self.add_contour('loop','upper-left','upper-right','lower-right')
        self.add_polyline('arrow',(6,14),(12,20),(18,14))
        self.relate('connect','arrow','loop')
        self.add_polyline('axis',(6,24),(36,24),(42,24))
        self.relate('connect','axis','loop')
