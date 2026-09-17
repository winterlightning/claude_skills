"""Marker Pen and Scribble.
Plan: Angled banded painting tool with curved pointed working end and a separate physical wavy stroke. Centerline extremes (6,6)-(42,42).
Construction: Lucide paintbrush: banded handle and broad working end.
Reduction: Tool identity remains unspecified; wave reduced to three broad bends.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b06e64f7-64ba-40ee-b75d-72b9fb3f5a30'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/tube painting_b06e64f7-64ba-40ee-b75d-72b9fb3f5a30.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/tube painting_b06e64f7-64ba-40ee-b75d-72b9fb3f5a30.svg'

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
    icon_id = 'paint-applicator-with-wavy-stroke'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('marker', 'pen', 'and', 'scribble')

    def build(self):
        self.add_polyline('tool',(30,6),(42,10),(38,20),(34,30),(22,26),(26,16),closed=True)
        self.add_line('band',(26,16),(38,20));self.relate('connect','band','tool')
        self.add_arc('tip-left',(22,26),(18,42),radius_x=16,sweep=False)
        self.add_arc('tip-right',(18,42),(34,30),radius_x=20,sweep=False)
        self.add_contour('tip','tip-left','tip-right');self.relate('connect','tip','tool')
        self.add_arc('wave-a',(10,12),(6,20),radius_x=4,radius_y=8,sweep=False)
        self.add_arc('wave-b',(6,20),(10,28),radius_x=4,radius_y=8,sweep=False)
        self.add_arc('wave-c',(10,28),(6,36),radius_x=4,radius_y=8)
        self.add_contour('paint','wave-a','wave-b','wave-c')
