"""Selection Cursor with Curved Path.
Plan: Large upper-left cursor and separate downward-turning selected path. Centerline extremes (6,6)-(42,42).
Construction: Lucide mouse-pointer-2: pointed silhouette with a deep notch.
Reduction: Curved path retains its separate placement; no modifier identity imposed.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '34495936-986d-5ad6-b06d-801712a5af57'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/transform direct select_34495936-986d-5ad6-b06d-801712a5af57.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/transform direct select_34495936-986d-5ad6-b06d-801712a5af57.svg'

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
    icon_id = 'selection-cursor-beside-curved-path'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('selection', 'cursor', 'with', 'curved', 'path')

    def build(self):
        self.add_polyline('cursor',(6,6),(34,18),(22,22),(18,34),closed=True)
        self.add_line('path-start',(30,30),(34,30))
        self.add_arc('path-turn',(34,30),(42,38),radius_x=8)
        self.add_line('path-end',(42,38),(42,42))
        self.add_contour('path','path-start','path-turn','path-end')
