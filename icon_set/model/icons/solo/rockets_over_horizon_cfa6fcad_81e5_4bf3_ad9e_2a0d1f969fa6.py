"""Rebuilt equal descending rocket bodies with higher right placement, diagonal fins and a shared curved horizon. Enclosed fin panels reduced to strokes and exhaust pairs to one mark each for clearance.
Construction: Lucide rocket: repeated body and fins; descending rockets above curved horizon. Shared dimensions retain equality; right rocket intentionally higher; one exhaust stroke each.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='cfa6fcad-81e5-4bf3-ad9e-2a0d1f969fa6'
SOURCE_PATH='pictographic-primitives/programing/network firewall rocket_cfa6fcad-81e5-4bf3-ad9e-2a0d1f969fa6.svg'
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
    category = "programing"
    categories = ("programing", "primitives")
    aliases = ()
    keywords = ('network', 'firewall', 'rocket')
    def build(self):
        s = self
        for name,x,y in (('left',12,18),('right',36,16)):
            s.add_polyline(name+'-body',(x-5,y),(x+5,y),(x+5,y+4),(x+5,y+6),(x,y+12),(x-5,y+6),(x-5,y+4),closed=True)
            s.add_line(name+'-fin-left',(x-8,y-2),(x-5,y+4))
            s.add_line(name+'-fin-right',(x+8,y-2),(x+5,y+4))
            for side in ('left','right'):s.relate('connect',name+'-body',name+'-fin-'+side)
            s.add_line(name+'-exhaust',(x,8),(x,y-8))
        s.add_arc('horizon',(4,40),(44,40),radius_x=101)
