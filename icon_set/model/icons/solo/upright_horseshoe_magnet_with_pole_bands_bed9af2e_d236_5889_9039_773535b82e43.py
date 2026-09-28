"""Horseshoe Magnet.
Plan: Mirrored inverted-U magnet; concentric arch radii, equal-width arms and two pole bands. Centerline extremes (6,6)-(42,42).
Construction: Lucide magnet: concentric return and paired pole bands.
Reduction: Extraction irregularities removed; identifying parts retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bed9af2e-d236-5889-9039-773535b82e43'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/design tool magnet_bed9af2e-d236-5889-9039-773535b82e43.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/design tool magnet_bed9af2e-d236-5889-9039-773535b82e43.svg'

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
    icon_id = 'upright-horseshoe-magnet-with-pole-bands'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('horseshoe', 'magnet')

    def build(self):
        axis=24
        self.add_arc('outer',(6,24),(42,24),radius_x=18)
        _run(self,'right-outer',(42,24),(42,34),(42,39))
        self.add_arc('right-tip-a',(42,39),(39,42),radius_x=3)
        self.add_line('right-tip-b',(39,42),(35,42))
        self.add_arc('right-tip-c',(35,42),(32,39),radius_x=3)
        _run(self,'right-inner',(32,39),(32,34),(32,24))
        self.add_arc('inner',(32,24),(16,24),radius_x=8,sweep=False)
        _run(self,'left-inner',(16,24),(16,34),(16,39))
        self.add_arc('left-tip-a',(16,39),(13,42),radius_x=3)
        self.add_line('left-tip-b',(13,42),(9,42))
        self.add_arc('left-tip-c',(9,42),(6,39),radius_x=3)
        _run(self,'left-outer',(6,39),(6,34),(6,24))
        self.add_contour('magnet','outer','right-outer-1','right-outer-2','right-tip-a','right-tip-b','right-tip-c','right-inner-1','right-inner-2','inner','left-inner-1','left-inner-2','left-tip-a','left-tip-b','left-tip-c','left-outer-1','left-outer-2',closed=True)
        for side in (-1,1):
         a,c=sorted((axis+side*8,axis+side*18))
         name=f'pole-{side}'
         self.add_line(name,(a,34),(c,34));self.relate('connect',name,'magnet')
