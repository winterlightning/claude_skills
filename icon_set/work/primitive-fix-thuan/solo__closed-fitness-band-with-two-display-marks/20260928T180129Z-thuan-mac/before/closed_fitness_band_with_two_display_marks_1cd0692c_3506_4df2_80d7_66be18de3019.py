"""Smart Fitness Band.

Symbol plan: Closed fitness band in oblique view: broad left display and narrow right wrist opening. Two marks share length and 8-unit pitch. No close Lucide shape match. Remove transverse panel seams to give the two marks sufficient clearance.
Keyshape HRECT_L; exact visible bounds (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1cd0692c-3506-4df2-80d7-66be18de3019'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/devices/wearable smart watch_1cd0692c-3506-4df2-80d7-66be18de3019.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'closed-fitness-band-with-two-display-marks'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    categories = ('primitives', 'devices')
    aliases = ()
    keywords = ('smart', 'fitness', 'band')

    def build(self):
        self.rect('outer',4,8,40,32,16)
        self.add_arc('opening',(28,8),(28,40),radius_x=4,radius_y=16,sweep=False)
        self.relate('connect','opening','outer')
        for i,y in enumerate((20,28)):self.add_line(f'mark-{i}',(14,y),(16,y))

    def rect(self,name,x,y,w,h,r=2):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for i,start in enumerate(points):
            end=points[(i+1)%8];part=f'{name}-{i}'
            if start==end: continue
            if i%2:self.add_arc(part,start,end,radius_x=r)
            else:self.add_line(part,start,end)
            names.append(part)
        self.add_contour(name,*names,closed=True)
