"""Rounded enclosure construction from Lucide message-square-reply. A true arc question hook and distinct dot replace the folded stroke; side alert rays restored. Center ray reduced to dot for spacing.
Fresh bad-stroke revision; fixed SOLO48 stroke4, integer grid. Keyshape VRECT_L."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1f2d1b12-2c74-4b57-91be-a4a84e1da748'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pop-up-alert/20260924T092330Z-thuan-mac/reference/pop up alert_1f2d1b12-2c74-4b57-91be-a4a84e1da748.svg'
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
    icon_id = 'pop-up-alert'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('pop', 'up', 'alert')
    def build(self):
        s = self
        box(s,'panel',8,12,40,44,4)
        path(s,'question',(20,24),('A',(28,24),4,4,True),('A',(24,28),4,4,True))
        s.add_dot('question-dot',(24,36))
        s.add_line('ray-left',(8,4),(10,6));s.add_dot('ray-top',(24,4));s.add_line('ray-right',(38,6),(40,4))
