"""Lucide square-pen: outlined ballot choices and pencil. Equal boxes preserve the source hierarchy; cross is essential and must remain readable.
Fresh bad-stroke revision; fixed SOLO48 stroke4, integer grid. Keyshape VRECT_L."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8baf23d7-4390-4407-a5c3-c22b45141f27'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pencil-marking-ballot/20260924T092330Z-thuan-mac/reference/election_8baf23d7-4390-4407-a5c3-c22b45141f27.svg'
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
    icon_id = 'pencil-marking-ballot'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('election',)
    def build(self):
        s = self
        s.add_polyline('empty-box',(8,4),(24,4),(24,20),(8,20),closed=True)
        s.add_polyline('marked-box',(8,28),(24,28),(24,44),(8,44),closed=True)
        s.add_line('cross-a',(12,32),(20,40));s.add_line('cross-b',(12,40),(20,32));s.relate('connect','cross-a','cross-b')
        path(s,'pencil',(32,8),('A',(40,8),4,4,True),('L',(40,24)),('L',(36,32)),('L',(32,24)),('L',(32,8)),closed=True)
