"""Pen Pencil and Paintbrush.
Plan: Three upright tools share equal-width shafts and spacing; pen points down, pencil and brush up. Centerline extremes (4,8)-(44,40).
Construction: Lucide pencil and paintbrush: distinct ends and common upright axes.
Reduction: Pen clip and both tip seams omitted to avoid tiny enclosed holes; all three tool silhouettes retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fe91aa88-5585-4c3c-939c-ba0b27ea7e60'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/pens_fe91aa88-5585-4c3c-939c-ba0b27ea7e60.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/pens_fe91aa88-5585-4c3c-939c-ba0b27ea7e60.svg'

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
    icon_id = 'upright-pen-pencil-and-brush-set'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('pen', 'pencil', 'and', 'paintbrush')

    def build(self):
        self.add_polyline('pen',(4,8),(12,8),(12,30),(8,40),(4,30),closed=True)
        
        self.add_polyline('pencil',(20,18),(24,8),(28,18),(28,36))
        self.add_arc('eraser',(28,36),(20,36),radius_x=4)
        self.add_line('pencil-left',(20,36),(20,18))
        self.relate('connect','eraser','pencil');self.relate('connect','eraser','pencil-left');self.relate('connect','pencil-left','pencil')
        
        self.add_polyline('brush-head',(36,20),(36,16),(40,8),(44,16),(44,20),closed=True)
        self.add_line('brush-shaft',(40,20),(40,40));self.relate('connect','brush-shaft','brush-head')
