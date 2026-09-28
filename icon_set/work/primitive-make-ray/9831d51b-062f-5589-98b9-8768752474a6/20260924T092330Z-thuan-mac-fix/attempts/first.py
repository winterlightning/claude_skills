"""Lucide pencil-line: diagonal barrel, rounded cap, joined nib and detached writing line. Barrel facet omitted to preserve clearance.
Fresh bad-stroke revision; fixed SOLO48 stroke4, integer grid. Keyshape SQUARE."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9831d51b-062f-5589-98b9-8768752474a6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pencil-above-writing-line/20260924T092330Z-thuan-mac/reference/pencil edit_9831d51b-062f-5589-98b9-8768752474a6.svg'
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
    category = "objects"
    aliases = ()
    keywords = ('pencil', 'edit')
    def build(self):
        s = self
        path(s,'pencil',(6,34),('L',(10,22)),('L',(24,8)),('L',(26,6)),('L',(34,6)),('A',(42,14),8,8,True),('L',(36,20)),('L',(26,30)),('L',(18,30)),('L',(6,34)),closed=True)
        s.add_line('cap-seam',(24,8),(36,20));s.relate('connect','pencil','cap-seam')
        s.add_line('nib-seam',(10,22),(18,30));s.relate('connect','pencil','nib-seam')
        s.add_line('writing-line',(18,42),(42,42))
