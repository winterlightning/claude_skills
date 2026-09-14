"""Radial sun; shared center and paired rays; Lucide sun informs detached rays."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e141771c-b8fb-4c6b-9a3e-9b6103d1efa0'
SOURCE_PATH = 'pictographic-primitives/video/video edit brightness 1_e141771c-b8fb-4c6b-9a3e-9b6103d1efa0.svg'
AUTHOR = 'gpt-6'

class SunWithEightRays(Solo48):
    icon_id = 'sun-with-eight-rays'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('sun', 'brightness', 'light', 'rays', 'day', 'sunshine', 'weather')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def rounded(self, name, x, y, w, h, r):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8]; ident=name+'-'+str(i);ids.append(ident)
            if i%2:self.add_arc(ident,a,b,radius_x=r)
            else:self.add_line(ident,a,b)
        self.add_contour(name,*ids,closed=True)

    def build(self):
        # Radial sun; shared center and paired rays; Lucide sun informs detached rays.
        self.circle('disc',24,24,7)
        for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            self.add_line(f'axial-{dx}-{dy}',(24+dx*16,24+dy*16),(24+dx*20,24+dy*20))
        for dx,dy in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            self.add_line(f'diagonal-{dx}-{dy}',(24+dx*12,24+dy*12),(24+dx*14,24+dy*14))
