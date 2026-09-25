"""Restored a pitched house roof and a rounded pencil cap; retained drafting line, omitted tiny doorway, second dash and cap band.
Construction: Lucide house and pencil-line: pitched roof and rounded pencil cap. House stays below-left of diagonal pencil; omit door and cap seam.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c74c88d8-5693-44d0-8cc1-01e35bd5345e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/construction/project plan pen_c74c88d8-5693-44d0-8cc1-01e35bd5345e.svg'
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
    icon_id = 'pencil-drawing-house-plan-solo-b003-07'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "construction"
    categories = ("construction", "primitives")
    aliases = ()
    keywords = ('project', 'plan', 'pen')
    def build(self):
        s = self
        s.add_polyline('house',(6,32),(14,24),(24,32),(24,42),(6,42),closed=True)
        path(s,'pencil',(26,20),('L',(28,10)),('L',(32,6)),('L',(36,6)),('A',(42,12),6,6,True),('L',(36,18)),('L',(26,20)),closed=True)
        s.add_line('drafting-line',(6,14),(16,14))
