"""Feather Quill Pen.
Plan: Feather rises diagonally from an exposed shaft; vein and one notch retained. Centerline extremes (6,6)-(42,42).
Construction: Lucide feather; exposed shaft and diagonal vein.
Reduction: Irregular edge detail reduced to one broad notch.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '67e893bc-5345-575c-b7bf-64734a8a6322'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/design tool quill_67e893bc-5345-575c-b7bf-64734a8a6322.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/design tool quill_67e893bc-5345-575c-b7bf-64734a8a6322.svg'

def _run(icon, name, *points):
    for i,(a,b) in enumerate(zip(points,points[1:]),1):
        icon.add_line(f'{name}-{i}',a,b)

def _circle(icon, name, cx, cy, radius):
    a,b=(cx-radius,cy),(cx+radius,cy)
    icon.add_arc(name+'-a',a,b,radius_x=radius)
    icon.add_arc(name+'-b',b,a,radius_x=radius)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)


class Drawing(Solo48):
    icon_id = 'feather-quill-with-side-notch'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('feather', 'quill', 'pen')

    def build(self):
        root=(12,36); tip=(42,6)
        self.add_arc('left',root,tip,radius_x=30,sweep=True)
        self.add_arc('right-top',tip,(36,24),radius_x=30,sweep=True)
        self.add_polyline('notch',(36,24),(26,24))
        self.add_arc('right-bottom',(30,30),root,radius_x=30,sweep=True)
        self.add_line('shaft',(6,42),root)
        self.add_line('vein',root,(28,18))
        for a,c in [('left','shaft'),('left','vein'),('right-bottom','shaft'),('right-bottom','vein'),('shaft','vein'),('right-top','notch')]:self.relate('connect',a,c)
        self.relate('connect','left','right-top')
        self.relate('connect','left','right-bottom')
