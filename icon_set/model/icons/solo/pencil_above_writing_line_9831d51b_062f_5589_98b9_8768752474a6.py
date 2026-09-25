"""Rebuilt pencil with parallel barrel edges, a tangent circular cap, a distinct nib seam and a separated writing line; omitted the fine barrel facet.
Construction: Lucide pencil-line: diagonal barrel, rounded cap, joined nib and detached writing line. Barrel facet omitted to preserve clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9831d51b-062f-5589-98b9-8768752474a6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/pencil edit_9831d51b-062f-5589-98b9-8768752474a6.svg'
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
    icon_id = 'pencil-above-writing-line'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('pencil', 'edit')
    def build(self):
        s = self
        path(s,'pencil',(6,38),('L',(10,25)),('L',(26,13)),('L',(34,7)),('A',(40,15),5,5,True),('L',(32,21)),('L',(16,33)),('L',(6,38)),closed=True)
        s.add_line('cap-seam',(26,13),(32,21));s.relate('connect','pencil','cap-seam')
        s.add_line('nib-seam',(10,25),(16,33));s.relate('connect','pencil','nib-seam')
        s.add_line('writing-line',(24,42),(42,42))
