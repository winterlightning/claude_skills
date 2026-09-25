"""Rubber Stamp Tool.
Plan: Mirrored rounded knob, flared waist and two-tier stamp base. Centerline extremes (6,6)-(42,42).
Construction: Lucide stamp: symmetrical grip and horizontal base.
Reduction: Minor traced asymmetries removed; grip shape distinguishes the pair.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a182e0ea-5fb7-5370-b959-cf73071535e3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/design tool stamp_a182e0ea-5fb7-5370-b959-cf73071535e3.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/design tool stamp_a182e0ea-5fb7-5370-b959-cf73071535e3.svg'

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
    icon_id = 'rubber-stamp-with-flared-neck-grip'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('rubber', 'stamp', 'tool')

    def build(self):
        self.add_arc('knob',(16,14),(32,14),radius_x=8)
        self.add_arc('neck-r',(32,14),(28,22),radius_x=10)
        self.add_arc('neck-l',(20,22),(16,14),radius_x=10)
        self.add_arc('flare-r',(28,22),(32,26),radius_x=4,sweep=False)
        self.add_arc('flare-l',(16,26),(20,22),radius_x=4,sweep=False)
        self.add_contour('grip','flare-l','neck-l','knob','neck-r','flare-r')

        _run(self,'base-top',(10,26),(16,26),(20,26),(28,26),(32,26),(38,26))
        self.add_arc('base-tr',(38,26),(42,30),radius_x=4)
        _run(self,'base-lower',(42,30),(42,34),(34,34),(14,34),(6,34),(6,30))
        self.add_arc('base-tl',(6,30),(10,26),radius_x=4)
        self.add_contour('base',*[f'base-top-{j}' for j in range(1,6)],'base-tr',*[f'base-lower-{j}' for j in range(1,6)],'base-tl',closed=True)
        self.relate('connect','grip','base')
        self.add_line('rubber-r',(34,34),(34,38))
        self.add_arc('rubber-br',(34,38),(30,42),radius_x=4)
        self.add_line('rubber-bottom',(30,42),(18,42))
        self.add_arc('rubber-bl',(18,42),(14,38),radius_x=4)
        self.add_line('rubber-l',(14,38),(14,34))
        self.add_contour('rubber','rubber-r','rubber-br','rubber-bottom','rubber-bl','rubber-l');self.relate('connect','rubber','base')
