"""Feather Writing Pen.
Plan: Feather above a written baseline; tall envelope keeps legal feather-to-line clearance. Centerline extremes (8,4)-(40,44).
Construction: Lucide feather; exposed shaft and diagonal vein.
Reduction: Small edge detail reduced to one notch; baseline moved below the feather.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a24ffe73-f135-5e6a-8d24-76f126353421'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/quill_a24ffe73-f135-5e6a-8d24-76f126353421.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/quill_a24ffe73-f135-5e6a-8d24-76f126353421.svg'

def _run(icon, name, *points):
    for i,(a,b) in enumerate(zip(points,points[1:]),1):
        icon.add_line(f'{name}-{i}',a,b)

def _circle(icon, name, cx, cy, radius):
    a,b=(cx-radius,cy),(cx+radius,cy)
    icon.add_arc(name+'-a',a,b,radius_x=radius)
    icon.add_arc(name+'-b',b,a,radius_x=radius)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)


class Drawing(Solo48):
    icon_id = 'feather-quill-touching-baseline'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('feather', 'writing', 'pen')

    def build(self):
        root=(10,34); tip=(40,4)
        self.add_arc('left',root,tip,radius_x=30,sweep=True)
        self.add_arc('right-top',tip,(34,22),radius_x=30,sweep=True)
        self.add_polyline('notch',(34,22),(24,22))
        self.add_arc('right-bottom',(28,28),root,radius_x=30,sweep=True)
        self.add_line('shaft',(8,44),root)
        self.add_line('vein',root,(26,16))
        for a,c in [('left','shaft'),('left','vein'),('right-bottom','shaft'),('right-bottom','vein'),('shaft','vein'),('right-top','notch')]:self.relate('connect',a,c)
        self.relate('connect','left','right-top')
        self.relate('connect','left','right-bottom')

        self.add_line('baseline',(8,44),(40,44))
        self.relate('connect','baseline','shaft')
