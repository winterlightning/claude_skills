"""User Profile with V Neckline.
Plan: Circular head radius8 with y20 lower edge; shared shoulder top y28 gives exactly4 ink gap. Open body and an interior neckline. Ink (6,2)-(42,46).
Construction reference: human_ref/user.svg.
Reduction: Use the reference open shoulder silhouette and move the neckline into the shirt.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c1a77ca3-a293-51b0-9aea-f66e746d0e15'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/images/man_c1a77ca3-a293-51b0-9aea-f66e746d0e15.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'user-profile-with-v-neckline'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/images'
    aliases = ()
    keywords = ('user', 'profile', 'with', 'v', 'neckline')
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

        circle('head',24,12,8)
        self.add_line('left-side',(8,44),(8,40))
        self.add_arc('shoulder-left',(8,40),(20,28),radius_x=12)
        self.add_line('shoulder-top',(20,28),(28,28))
        self.add_arc('shoulder-right',(28,28),(40,40),radius_x=12)
        self.add_line('right-side',(40,40),(40,44))
        self.add_contour('body','left-side','shoulder-left','shoulder-top','shoulder-right','right-side')

        self.add_polyline('neckline',(20,37),(24,41),(28,37))
