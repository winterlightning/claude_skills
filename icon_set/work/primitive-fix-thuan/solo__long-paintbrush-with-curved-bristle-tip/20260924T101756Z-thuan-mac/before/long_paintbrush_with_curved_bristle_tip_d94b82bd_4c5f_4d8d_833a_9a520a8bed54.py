"""Paint Brush Creative Tool.
Plan: Diagonal rounded handle joins a broad curved bristle head at a shared slanted seam. Centerline extremes (6,6)-(42,42).
Construction: Lucide paintbrush: diagonal handle and working-head seam.
Reduction: Extraction irregularities removed; identifying parts retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd94b82bd-4c5f-4d8d-833a-9a520a8bed54'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/brush_d94b82bd-4c5f-4d8d-833a-9a520a8bed54.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/brush_d94b82bd-4c5f-4d8d-833a-9a520a8bed54.svg'

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
    icon_id = 'long-paintbrush-with-curved-bristle-tip'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('paint', 'brush', 'creative', 'tool')

    def build(self):
        self.add_line('handle-a',(18,26),(34,6))
        self.add_arc('end',(34,6),(42,14),radius_x=8)
        self.add_line('handle-b',(42,14),(26,34))
        self.add_line('joint',(26,34),(18,26))
        self.add_contour('handle','handle-a','end','handle-b','joint',closed=True)
        self.add_arc('bristles-a',(18,26),(10,34),radius_x=8,sweep=False)
        self.add_arc('bristles-b',(10,34),(6,42),radius_x=10)
        self.add_arc('bristles-c',(6,42),(26,34),radius_x=29,sweep=False)
        self.add_contour('bristles','bristles-a','bristles-b','bristles-c');self.relate('connect','bristles','handle')
