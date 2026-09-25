"""Rebuilt seated figure with a round head, bent legs and arm resting at the knee; squared the separate bin. Head center (38,10), radius4 and neck (38,22) give exact 8 centerline / 4 ink gap on the vertical torso axis. Omitted bin taper and clothing details.
Construction: Shared human_ref/full_body_ref.png: round head and coherent seated limbs. Head center (38,10), radius4; neck (38,22) gives exactly4 ink gap. Bin and person remain separate.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9c6217f6-4ce5-4d83-b2e6-1f3f8e4d6fce'
SOURCE_PATH = 'pictographic-primitives/users/user homeless poverty_9c6217f6-4ce5-4d83-b2e6-1f3f8e4d6fce.svg'
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
    icon_id = 'person-sitting-by-trash-can'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "users"
    categories = ("users", "primitives")
    aliases = ()
    keywords = ('user', 'homeless', 'poverty')
    def build(self):
        s = self
        circle(s,'head',38,10,4)
        s.add_line('torso',(38,22),(38,24))
        path(s,'back',(38,24),('L',(38,34)),('A',(30,42),8,8,True))
        s.relate('connect','torso','back')
        s.add_polyline('legs',(30,42),(28,32),(24,42));s.relate('connect','back','legs')
        s.add_line('arm',(38,24),(28,32));s.relate('connect','arm','torso');s.relate('connect','arm','back');s.relate('connect','arm','legs')
        s.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        s.add_polyline('bin',(6,24),(6,42),(16,42),(16,24),(11,24),closed=True)
        s.add_line('lid-handle',(11,17),(11,24));s.relate('connect','lid-handle','bin')
