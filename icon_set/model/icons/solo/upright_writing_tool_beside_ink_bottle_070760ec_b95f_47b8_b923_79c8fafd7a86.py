"""Pen and Ink Bottle.
Plan: Open-ended left writing shaft and separate capped ink bottle; all seams have shared nodes. Centerline extremes (6,6)-(42,42).
Construction: Lucide pencil: structural point; stamp: centered neck construction.
Reduction: Tiny break under the writing point closed for clarity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '070760ec-b95f-47b8-b923-79c8fafd7a86'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/pen types_070760ec-b95f-47b8-b923-79c8fafd7a86.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/pen types_070760ec-b95f-47b8-b923-79c8fafd7a86.svg'

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
    icon_id = 'upright-writing-tool-beside-ink-bottle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pen', 'and', 'ink', 'bottle')

    def build(self):
        self.add_polyline('shaft',(6,42),(6,18),(18,18),(18,42))
        self.add_polyline('point',(6,18),(12,6),(18,18));self.relate('connect','point','shaft')
        self.add_polyline('bottle',(26,42),(26,30),(30,22),(38,22),(42,30),(42,42),closed=True)
        self.add_polyline('cap',(30,22),(30,14),(38,14),(38,22));self.relate('connect','cap','bottle')
        self.add_line('shoulder',(26,30),(42,30));self.relate('connect','shoulder','bottle')
