"""Pen Scribble Drawing.
Plan: Short diagonal pen with a broad upper-left scribbled curve. Centerline extremes (6,6)-(42,42).
Construction: Lucide pencil: diagonal pointed tool.
Reduction: Scribble reduced to broad bends; no tiny hatch detail.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4b1e8875-4559-40ca-942d-32ed1ca8d489'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/pen draw 1_4b1e8875-4559-40ca-942d-32ed1ca8d489.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/pen draw 1_4b1e8875-4559-40ca-942d-32ed1ca8d489.svg'

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
    icon_id = 'short-pen-beside-curved-scribble'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('pen', 'scribble', 'drawing')

    def build(self):
        self.add_line('pen-left',(24,32),(34,16))
        self.add_arc('pen-end',(34,16),(42,24),radius_x=8)
        self.add_polyline('pen-lower',(42,24),(32,38),(22,42),(24,32))
        self.relate('connect','pen-left','pen-end');self.relate('connect','pen-end','pen-lower');self.relate('connect','pen-lower','pen-left')
        self.add_arc('scribble-a',(22,6),(6,22),radius_x=16,sweep=False)
        self.add_arc('scribble-b',(6,22),(14,22),radius_x=4,sweep=False)
        self.add_arc('scribble-c',(14,22),(18,26),radius_x=4)
        self.add_contour('scribble','scribble-a','scribble-b','scribble-c')
