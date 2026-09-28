"""Pencil Writing on Document.
Plan: Diagonal pencil with shared tip seam over an open rounded panel; clear gaps surround the writing point. Centerline extremes (6,6)-(42,42).
Construction: Lucide pencil: diagonal point and barrel.
Reduction: Panel edges interrupted around the pencil; extra cap band removed.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f1e687be-de9c-5ecd-9000-251c3e077b32'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/pen_f1e687be-de9c-5ecd-9000-251c3e077b32.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/pen_f1e687be-de9c-5ecd-9000-251c3e077b32.svg'

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
    icon_id = 'pencil-over-rounded-square-panel'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('pencil', 'writing', 'on', 'document')

    def build(self):
        self.add_polyline('pencil',(20,20),(34,6),(42,14),(28,28),(16,32),closed=True)
        self.add_line('point-seam',(20,20),(28,28));self.relate('connect','point-seam','pencil')
        self.add_line('panel-top',(12,18),(6,18))
        self.add_line('panel-left',(6,18),(6,38))
        self.add_arc('panel-corner',(6,38),(10,42),radius_x=4,sweep=False)
        self.add_line('panel-bottom',(10,42),(34,42))
        self.add_arc('panel-br',(34,42),(38,38),radius_x=4,sweep=False)
        self.add_line('panel-right',(38,38),(38,34))
        self.add_contour('panel','panel-top','panel-left','panel-corner','panel-bottom','panel-br','panel-right')
