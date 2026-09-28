"""Rebuilt rounded handle cap, equal-width diagonal ferrule and smooth curved tuft; retained all three main brush regions.
Construction: Lucide paintbrush: distinct ferrule, rounded handle cap and curved tuft. Shared diagonal band edges preserve width; curved cap replaces chamfered polygon.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0ceae122-4d52-44c0-84da-c9168dce14c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/brush_0ceae122-4d52-44c0-84da-c9168dce14c9.svg'
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
    icon_id = 'rounded-artist-paintbrush-batch-019-04'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('brush',)
    def build(self):
        s = self
        path(s,'handle',(22,16),('L',(34,7)),('A',(40,15),5,5,True),('L',(28,24)))
        s.add_polyline('ferrule',(22,16),(28,24),(20,30),(14,22),closed=True)
        path(s,'bristles',(14,22),('A',(6,30),8,8,False),('L',(6,42)),('L',(10,42)),('A',(20,32),10,10,False),('L',(20,30)))
        s.relate('connect','handle','ferrule');s.relate('connect','ferrule','bristles')
