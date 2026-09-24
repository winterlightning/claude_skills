"""Rounded scan frame joins skull; left-facing profile has curved forehead, nose and chin with continuous neck.
Keyshape SQUARE. Shared human user.svg smooth human construction; supplied profile and scan frame.
Omissions: Ear omitted to preserve face interior."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b97885e6-dbf9-5160-931c-e559629ea220'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/artificial-intelligence/deepfake side_b97885e6-dbf9-5160-931c-e559629ea220.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'human-head-side-profile-scan-solo-b001-14'
    keyshape = Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('human', 'head', 'side', 'profile', 'scan', 'solo', 'b001', '14')

    def build(self):

        def path(n, start, steps, closed=False):
            members=[]; here=start
            for i,(kind,end,*a) in enumerate(steps):
                if here==end: continue
                tag=f'{n}-{i}'
                if kind=='L': self.add_line(tag,here,end)
                elif kind=='A': self.add_arc(tag,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C': self.add_bezier(tag,here,(a[0],a[1],end))
                members.append(tag); here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,q=4):
            path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('frame',(30,6),[('L',(10,6)),('A',(6,10),4,4,False),('L',(6,38)),('A',(10,42),4,4,False),('L',(25,42))])
        path('skull',(30,6),[('A',(42,18),12,12,True),('C',(36,34),(42,25),(36,28)),('L',(36,42))]);join('frame','skull')
        path('face',(25,15),[('C',(19,21),(21,15),(19,17)),('L',(15,26)),('L',(23,27)),('L',(23,30)),('A',(27,34),4,4,False)])

