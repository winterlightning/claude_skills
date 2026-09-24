"""Shared human_ref/full_body_ref.png: round head and coherent seated limbs. Head center (34,10), radius4; neck (34,22) gives exactly4 ink gap. Bin and person remain separate.
Fresh bad-stroke revision; fixed SOLO48 stroke4, integer grid. Keyshape SQUARE."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9c6217f6-4ce5-4d83-b2e6-1f3f8e4d6fce'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-sitting-by-trash-can/20260924T092330Z-thuan-mac/reference/user homeless poverty_9c6217f6-4ce5-4d83-b2e6-1f3f8e4d6fce.svg'
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
    category = "objects"
    aliases = ()
    keywords = ('user', 'homeless', 'poverty')
    def build(self):
        s = self
        circle(s,'head',34,10,4)
        s.add_line('torso',(34,22),(34,30));s.add_polyline('seated-legs',(34,30),(42,34),(42,42),(34,42))
        s.relate('connect','torso','seated-legs')
        s.add_polyline('arm',(34,22),(26,28),(34,30));s.relate('connect','torso','arm');s.relate('connect','seated-legs','arm')
        s.add_polyline('folded-leg',(34,42),(28,34),(24,42));s.relate('connect','seated-legs','folded-leg')
        s.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        s.add_polyline('bin',(6,24),(8,42),(16,42),(18,24),closed=True)
        s.add_line('lid',(6,24),(18,24));s.relate('connect','bin','lid')
        s.add_line('lid-handle',(12,18),(12,24));s.relate('connect','lid','lid-handle')
