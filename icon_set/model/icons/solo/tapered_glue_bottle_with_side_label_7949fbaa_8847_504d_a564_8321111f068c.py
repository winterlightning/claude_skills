"""Liquid Glue Bottle.
Plan: Bottle widens below sloping shoulders; truncated nozzle and side-attached rectangular label remain. Centerline extremes (10,4)-(38,44).
Construction: Lucide milk: bottle silhouette and structural neck.
Reduction: Collar simplified to the shoulder seam; label remains attached to the left edge.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7949fbaa-8847-504d-a564-8321111f068c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/design tool glue_7949fbaa-8847-504d-a564-8321111f068c.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/design tool glue_7949fbaa-8847-504d-a564-8321111f068c.svg'

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
    icon_id = 'tapered-glue-bottle-with-side-label'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('liquid', 'glue', 'bottle')

    def build(self):
        self.add_polyline('nozzle',(18,18),(20,4),(28,4),(30,18))
        self.add_arc('base-left',(14,44),(10,40),radius_x=4)
        _run(self,'upper',(10,40),(10,34),(10,30),(12,26),(16,18),(18,18),(30,18),(32,18),(38,40))
        self.add_arc('base-right',(38,40),(34,44),radius_x=4)
        self.add_line('base',(34,44),(14,44))
        self.add_contour('body','base-left',*[f'upper-{i}' for i in range(1,9)],'base-right','base',closed=True)
        self.relate('connect','nozzle','body')
        self.add_polyline('label',(12,26),(26,26),(26,34),(10,34))
        self.relate('connect','label','body')
