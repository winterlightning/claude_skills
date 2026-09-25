"""Pencil and Measuring Ruler.
Plan: Upright pencil and taller ruler, with three regularly spaced attached ticks. Centerline extremes (6,6)-(42,42).
Construction: Lucide ruler: repeated graduation spacing; pencil: triangular point.
Reduction: Eraser band omitted to preserve clear pencil interior.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '363ae461-a706-4a47-8694-4d6ea0bed9fd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/pencil ruler_363ae461-a706-4a47-8694-4d6ea0bed9fd.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/pencil ruler_363ae461-a706-4a47-8694-4d6ea0bed9fd.svg'

def _run(icon, name, *points):
    for i,(a,b) in enumerate(zip(points,points[1:]),1):
        icon.add_line(f'{name}-{i}',a,b)

def _circle(icon,name,cx,cy,r):
    a,b=(cx-r,cy),(cx+r,cy)
    icon.add_arc(name+'-a',a,b,radius_x=r)
    icon.add_arc(name+'-b',b,a,radius_x=r)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)

def _box(icon,name,l,t,r,b,rad,top_nodes=()):
    xs=[l+rad]+sorted(x for x in top_nodes if l+rad<x<r-rad)+[r-rad]
    _run(icon,name+'-top',*[(x,t) for x in xs])
    icon.add_arc(name+'-tr',(r-rad,t),(r,t+rad),radius_x=rad)
    icon.add_line(name+'-right',(r,t+rad),(r,b-rad))
    icon.add_arc(name+'-br',(r,b-rad),(r-rad,b),radius_x=rad)
    icon.add_line(name+'-bottom',(r-rad,b),(l+rad,b))
    icon.add_arc(name+'-bl',(l+rad,b),(l,b-rad),radius_x=rad)
    icon.add_line(name+'-left',(l,b-rad),(l,t+rad))
    icon.add_arc(name+'-tl',(l,t+rad),(l+rad,t),radius_x=rad)
    icon.add_contour(name,*[name+f'-top-{i}' for i in range(1,len(xs))],*[name+'-'+s for s in ('tr','right','br','bottom','bl','left','tl')],closed=True)

class Drawing(Solo48):
    icon_id = 'upright-pencil-beside-three-tick-ruler'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('pencil', 'and', 'measuring', 'ruler')

    def build(self):
        self.add_polyline('pencil',(6,18),(12,6),(18,18),(18,36))
        self.add_arc('eraser',(18,36),(6,36),radius_x=6)
        self.add_line('left',(6,36),(6,18))
        self.relate('connect','pencil','eraser');self.relate('connect','left','eraser');self.relate('connect','left','pencil')
        self.add_line('seam',(6,18),(18,18));self.relate('connect','seam','pencil');self.relate('connect','seam','left')
        self.add_polyline('ruler',(30,6),(42,6),(42,42),(26,42),(26,34),(26,26),(26,18),(26,10))
        self.add_arc('ruler-tl',(26,10),(30,6),radius_x=4);self.relate('connect','ruler','ruler-tl')
        for i in range(3):
         y=18+8*i;self.add_line(f'tick-{i}',(26,y),(32,y));self.relate('connect',f'tick-{i}','ruler')
