"""Lucide message-square-reply: corner radii and coherent return arrow. Restore rectangular speech body and distinct lower-left tail; integrated upper reply arrow stays directional.
Fresh bad-stroke revision; fixed SOLO48 stroke4, integer grid. Keyshape HRECT_L."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4bea84d2-e574-5f4d-ab3c-3cd97efde30d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__reply-message-bubble-solo/20260924T092330Z-thuan-mac/reference/reply to message_4bea84d2-e574-5f4d-ab3c-3cd97efde30d.svg'
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
    icon_id = 'reply-message-bubble-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('reply', 'to', 'message')
    def build(self):
        s = self
        path(s,'bubble',(12,16),('L',(8,16)),('A',(4,20),4,4,False),('L',(4,28)),('A',(8,32),4,4,False),('L',(12,32)),('L',(12,40)),('L',(22,32)),('L',(40,32)),('A',(44,28),4,4,False),('L',(44,20)),('A',(40,16),4,4,False),('L',(24,16)))
        s.add_polyline('arrow',(32,8),(24,16),(32,24));s.relate('connect','bubble','arrow')
