"""Angular Gear.
Plan: Seven angular teeth derived as a symmetric polygon about x24; preserve flat tips and open center. Ink (4,4)-(44,44).
Construction reference: settings.
Reduction: Omit tiny central mark; preserve seven angular teeth instead of adding an unrequested hub.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8ce3c661-d221-45e9-90b3-0342f52ed76e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_8ce3c661-d221-45e9-90b3-0342f52ed76e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'angular-gear'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('angular', 'gear')
    def build(self):

        def circle(name, cx, cy, r):
            self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
            self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        def rect(name,x,y,w,h,r=2):
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r),(x+r,y)]
            for i,(a,b) in enumerate(zip(pts,pts[1:])):
                if i%2: self.add_arc(f'{name}-{i}',a,b,radius_x=r)
                else: self.add_line(f'{name}-{i}',a,b)
            self.add_contour(name,*(f'{name}-{i}' for i in range(8)),closed=True)

        left=[(21,6),(19,12),(15,14),(10,12),(6,18),(10,23),(9,24),(6,26),(8,34),(12,34),(12,42),(20,42),(20,34),(24,34)]
        points=left+[(48-x,y) for x,y in reversed(left[:-1])]
        self.add_polyline('gear',*points,closed=True)
