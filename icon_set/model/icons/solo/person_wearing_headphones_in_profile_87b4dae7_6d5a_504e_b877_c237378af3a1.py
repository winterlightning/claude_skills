"""Rebuilt smooth circular skull, continuous anatomical neck, circular earcup and vertical headband. Omitted duplicate band edge and earcup center dot.
Construction: Human reference user.svg informs smooth head; continuous anatomical neck follows source profile. Lucide headphones informs circular cup and vertical band; duplicate band omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '87b4dae7-6d5a-504e-b877-c237378af3a1'
SOURCE_PATH = 'pictographic-primitives/audio/headphones human_87b4dae7-6d5a-504e-b877-c237378af3a1.svg'
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
    icon_id = 'person-wearing-headphones-in-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "audio"
    aliases = ()
    keywords = ('headphones', 'human')
    def build(self):
        s = self
        path(s,'head',(16,44),('L',(16,36)),('A',(8,28),8,8,True),('L',(8,18)),('A',(22,4),14,14,True),('A',(36,18),14,14,True),('L',(40,28)),('L',(34,28)),('L',(34,34)),('A',(28,40),6,6,True),('L',(28,44)))
        circle(s,'earcup',22,20,5)
        s.add_line('band',(22,4),(22,15));s.relate('connect','band','head');s.relate('connect','band','earcup')
