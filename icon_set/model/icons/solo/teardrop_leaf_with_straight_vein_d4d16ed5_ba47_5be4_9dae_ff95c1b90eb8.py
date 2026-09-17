"""Simple Teardrop Leaf Symbol.
Plan: Symmetric teardrop leaf with a rounded base and a straight central vein. Centerline extremes (8,4)-(40,44).
Construction: Lucide droplet: symmetrical pointed top and broad lower bowl.
Reduction: Vein shortened to maintain clear tip and base gaps.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd4d16ed5-ba47-5be4-9dae-ff95c1b90eb8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/drop pick_d4d16ed5-ba47-5be4-9dae-ff95c1b90eb8.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/drop pick_d4d16ed5-ba47-5be4-9dae-ff95c1b90eb8.svg'

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
    icon_id = 'teardrop-leaf-with-straight-vein'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('simple', 'teardrop', 'leaf', 'symbol')

    def build(self):
        self.add_arc('right',(24,4),(40,28),radius_x=26)
        self.add_arc('base-r',(40,28),(24,44),radius_x=16)
        self.add_arc('base-l',(24,44),(8,28),radius_x=16)
        self.add_arc('left',(8,28),(24,4),radius_x=26)
        self.add_contour('leaf','right','base-r','base-l','left',closed=True)
        self.add_line('vein',(24,20),(24,35))
