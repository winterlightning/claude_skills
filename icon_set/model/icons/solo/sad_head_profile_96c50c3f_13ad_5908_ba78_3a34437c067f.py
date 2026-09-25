"""Rebuilt circular skull, continuous anatomical neck and smoother circular chin; increased nose-to-mouth separation while retaining inclined sad eye and downturned mouth.
Construction: Shared human user.svg informs circular head construction; source establishes continuous neck and right-facing profile. Expand nose-to-mouth spacing and use smoother circular chin; inclined sad eye retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '96c50c3f-13ad-5908-ba78-3a34437c067f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/depression disorder symptoms_96c50c3f-13ad-5908-ba78-3a34437c067f.svg'
AUTHOR = "gpt-6"

def path(s,n,start,*steps,closed=False):
    ids=[]; here=start
    for i,c in enumerate(steps):
        k,end,*args=c; ident=f'{n}-{i}'
        if k=='L': s.add_line(ident,here,end)
        else: s.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
        ids.append(ident);here=end
    s.add_contour(n,*ids,closed=closed)

def circle(s,n,x,y,r):
    path(s,n,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

def box(s,n,l,t,r,b,k=3):
    path(s,n,(l+k,t),('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True),closed=True)

class Drawing(Solo48):
    icon_id = 'sad-head-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ()
    keywords = ('depression', 'disorder', 'symptoms')
    def build(self):
        s = self
        path(s,'profile',(14,44),('L',(14,36)),('A',(8,30),6,6,True),('L',(8,18)),('A',(36,18),14,14,True),('L',(40,24)),('L',(34,24)),('L',(34,32)),('A',(26,40),8,8,True),('L',(26,44)))
        s.add_arc('mouth',(24,34),(34,32),radius_x=10,radius_y=4);s.relate('connect','mouth','profile')
        s.add_line('eye',(22,18),(26,16))
