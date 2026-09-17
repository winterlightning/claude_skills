"""Female User Profile.
Plan: Circular jaw and center-parted hair above symmetric shoulder arch; detached gap 4 ink units. Ink (6,2)-(42,46).
Construction reference: human_ref/user.svg.
Reduction: Omit outward hair wisps; preserve center part, circular face and broad shoulders.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b7558322-6681-447e-8b8a-0f4a588a3f0e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/images/woman_b7558322-6681-447e-8b8a-0f4a588a3f0e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'female-user-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/images'
    aliases = ()
    keywords = ('female', 'user', 'profile')
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

        self.add_arc('hair-top',(14,14),(34,14),radius_x=10)
        self.add_arc('jaw',(34,14),(14,14),radius_x=10)
        self.add_contour('head','hair-top','jaw',closed=True)
        self.add_bezier('part-left',(14,14),((18,14),(22,12),(24,10)))
        self.add_bezier('part-right',(24,10),((26,12),(30,14),(34,14)))
        self.add_contour('hair-part','part-left','part-right')
        self.relate('connect','hair-part','head')
        self.add_arc('shoulders',(8,44),(24,32),radius_x=16,radius_y=12)
        self.add_arc('shoulders-right',(24,32),(40,44),radius_x=16,radius_y=12)
        self.add_contour('body','shoulders','shoulders-right')
