"""Inward Scale Down Arrow.
Plan: Quarter-circle boundary with a dashed outer corner and a down-left inward arrow. Centerline extremes (6,6)-(42,42).
Construction: Lucide shrink: inward diagonal arrow.
Reduction: Dashed boundary reduced to two well-separated strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7e004778-d88c-4db0-9a9c-c9364d42ee86'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/transform inside_7e004778-d88c-4db0-9a9c-c9364d42ee86.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/transform inside_7e004778-d88c-4db0-9a9c-c9364d42ee86.svg'

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
    icon_id = 'inward-arrow-with-curved-and-dashed-bounds'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('inward', 'scale', 'down', 'arrow')

    def build(self):
        self.add_arc('boundary',(6,6),(42,42),radius_x=36)
        self.add_line('dash-top',(32,6),(34,6))
        self.add_line('dash-right',(42,6),(42,14))
        self.add_line('shaft',(24,24),(12,36))
        self.add_polyline('head',(12,24),(12,36),(24,36))
        self.relate('connect','head','shaft')
