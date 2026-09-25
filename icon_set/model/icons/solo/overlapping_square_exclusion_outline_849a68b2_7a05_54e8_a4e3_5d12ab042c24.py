"""Overlapping Squares Exclude Intersection.
Plan: Two offset squares form a stepped outside contour; separated inner corners mark excluded overlap. Centerline extremes (6,6)-(42,42).
Construction: Lucide shapes: orthogonal outlines.
Reduction: Broken inner edges shortened to preserve their deliberate gaps.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '849a68b2-7a05-54e8-a4e3-5d12ab042c24'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/pathfinder exclude_849a68b2-7a05-54e8-a4e3-5d12ab042c24.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/pathfinder exclude_849a68b2-7a05-54e8-a4e3-5d12ab042c24.svg'

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
    icon_id = 'overlapping-square-exclusion-outline'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('overlapping', 'squares', 'exclude', 'intersection')

    def build(self):
        self.add_polyline('outside',(6,6),(30,6),(30,18),(42,18),(42,42),(18,42),(18,30),(6,30),closed=True)
        self.add_polyline('inside-upper',(18,22),(18,18),(22,18))
        self.add_polyline('inside-lower',(30,26),(30,30),(26,30))
