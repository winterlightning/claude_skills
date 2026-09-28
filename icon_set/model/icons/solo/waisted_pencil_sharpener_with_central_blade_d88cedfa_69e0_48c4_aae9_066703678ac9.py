"""Manual Pencil Sharpener.
Plan: Symmetric sharpener with shallow concave grips and a long central U-ended blade. Centerline extremes (8,4)-(40,44).
Construction: Lucide shapes: rounded frame and coherent U contour; no exact sharpener match.
Reduction: Small screw omitted because the blade cannot contain it with legal clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd88cedfa-69e0-48c4-aae9-066703678ac9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/sharpener_d88cedfa-69e0-48c4-aae9-066703678ac9.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/sharpener_d88cedfa-69e0-48c4-aae9-066703678ac9.svg'

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
    icon_id = 'waisted-pencil-sharpener-with-central-blade'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('manual', 'pencil', 'sharpener')

    def build(self):
        _run(self,'top',(12,4),(18,4),(30,4),(36,4))
        self.add_arc('tr',(36,4),(40,8),radius_x=4)
        self.add_line('ru',(40,8),(40,14))
        self.add_arc('right-grip',(40,14),(40,34),radius_x=2,radius_y=10,sweep=False)
        self.add_line('rl',(40,34),(40,40))
        self.add_arc('br',(40,40),(36,44),radius_x=4)
        self.add_line('bottom',(36,44),(12,44))
        self.add_arc('bl',(12,44),(8,40),radius_x=4)
        self.add_line('ll',(8,40),(8,34))
        self.add_arc('left-grip',(8,34),(8,14),radius_x=2,radius_y=10,sweep=False)
        self.add_line('lu',(8,14),(8,8))
        self.add_arc('tl',(8,8),(12,4),radius_x=4)
        self.add_contour('body','top-1','top-2','top-3','tr','ru','right-grip','rl','br','bottom','bl','ll','left-grip','lu','tl',closed=True)
        self.add_line('blade-left',(18,4),(18,30))
        self.add_arc('blade-end',(18,30),(30,30),radius_x=6,sweep=False)
        self.add_line('blade-right',(30,30),(30,4))
        self.add_contour('blade','blade-left','blade-end','blade-right');self.relate('connect','blade','body')
