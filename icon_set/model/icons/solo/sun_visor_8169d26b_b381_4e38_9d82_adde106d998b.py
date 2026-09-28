"""Sun visor with a mirrored domed band and smoothly scalloped brim; paired curves share horizontal and vertical tangents.
Omissions: None
Construction references: no useful direct Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8169d26b-b381-4e38-9d82-adde106d998b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/visor_8169d26b-b381-4e38-9d82-adde106d998b.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='sun-visor'
    keyshape=Keyshape.HRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('visor',)

    def path(self, name, start, commands, closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            eid=f'{name}-{i}'; ids.append(eid)
            if c[0]=='L': self.add_line(eid,here,c[1])
            elif c[0]=='A': self.add_arc(eid,here,c[1],radius_x=c[2],radius_y=c[3],sweep=c[4],large_arc=c[5] if len(c)>5 else False)
            elif c[0]=='C': self.add_bezier(eid,here,(c[2],c[3],c[1]))
            here=c[1]
        self.add_contour(name,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,x,y,w,h,r):
        self.path(n,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)

    def build(self):
        self.path('visor',(4,30),[('C',(6,20),(4,27),(5,25)),('C',(24,10),(7,15),(14,10)),('C',(42,20),(34,10),(41,15)),('C',(44,30),(43,25),(44,27)),('C',(37,38),(44,35),(41,38)),('C',(24,34),(33,38),(30,34)),('C',(11,38),(18,34),(15,38)),('C',(4,30),(7,38),(4,35))],True)
        self.path('band',(4,30),[('C',(24,22),(10,25),(17,22)),('C',(44,30),(31,22),(38,25))])
        self.relate('connect','band','visor')
