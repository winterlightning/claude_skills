"""Lucide rocket: repeated body and fins; descending rockets above curved horizon. Shared dimensions retain equality; right rocket intentionally higher; one exhaust stroke each.
Fresh bad-stroke revision; fixed SOLO48 stroke4, integer grid. Keyshape HRECT_L."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cfa6fcad-81e5-4bf3-ad9e-2a0d1f969fa6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rockets-over-horizon/20260924T092330Z-thuan-mac/reference/network firewall rocket_cfa6fcad-81e5-4bf3-ad9e-2a0d1f969fa6.svg'
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
    icon_id = 'rockets-over-horizon'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('network', 'firewall', 'rocket')
    def build(self):
        s = self
        for name,x,y in (('left',12,20),('right',36,16)):
            s.add_polyline(name+'-body',(x-4,y),(x+4,y),(x+4,y+6),(x,y+12),(x-4,y+6),closed=True)
            path(s,name+'-fin-left',(x-8,y-4),('L',(x-8,y+2)),('A',(x-4,y+6),4,4,False))
            path(s,name+'-fin-right',(x+8,y-4),('L',(x+8,y+2)),('A',(x+4,y+6),4,4,True))
            for side in ('left','right'):s.relate('connect',name+'-body',name+'-fin-'+side)
            s.add_line(name+'-exhaust',(x,8),(x,y-8))
        s.add_arc('horizon',(4,40),(44,40),radius_x=101)
