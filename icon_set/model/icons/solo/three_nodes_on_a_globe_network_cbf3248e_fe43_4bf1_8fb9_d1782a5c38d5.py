"""Three circular nodes form a smooth triangular network inside a circular globe.
Omissions: Meridian extension to outer circle omitted to preserve node spacing.
Construction references: ['globe', 'network'].
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cbf3248e-fe43-4bf1-8fb9-d1782a5c38d5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/amazon cloud front_cbf3248e-fe43-4bf1-8fb9-d1782a5c38d5.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='three-nodes-on-a-globe-network'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('amazon', 'cloud', 'front')

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
        self.circle('globe',24,24,20)
        for n,x,y in [('a',24,16),('b',16,28),('c',32,28)]:self.circle(n,x,y,3)
        for n,flip in [('ab',False),('ac',True)]:
            def p(x,y):return (48-x,y) if flip else (x,y)
            self.path(n,p(21,16),[('C',p(16,25),p(18,17),p(16,21))]);self.relate('connect',n,'a');self.relate('connect',n,'c' if flip else 'b')
        self.add_line('bc',(19,28),(29,28));self.relate('connect','bc','b');self.relate('connect','bc','c')
