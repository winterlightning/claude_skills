"""Right Angled Triangle Ruler.
Plan: Right triangle set square with three equally spaced base graduations and one broad triangular interior. Centerline extremes (6,6)-(42,42).
Construction: Lucide ruler: consistent attached graduations.
Reduction: Five graduations reduced to three; the nested triangular outline omitted because its opening becomes undersized at the required clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fd56634a-3d62-59eb-95af-c407a5e2b93c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/ruler triangle_fd56634a-3d62-59eb-95af-c407a5e2b93c.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/ruler triangle_fd56634a-3d62-59eb-95af-c407a5e2b93c.svg'

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
    icon_id = 'triangular-set-square-with-five-ticks'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('right', 'angled', 'triangle', 'ruler')

    def build(self):
        self.add_polyline('ruler',(6,6),(42,42),(30,42),(22,42),(14,42),(6,42),closed=True)
        
        for i,x in enumerate((14,22,30)):
         self.add_line(f'tick-{i}',(x,42),(x,38));self.relate('connect',f'tick-{i}','ruler')
