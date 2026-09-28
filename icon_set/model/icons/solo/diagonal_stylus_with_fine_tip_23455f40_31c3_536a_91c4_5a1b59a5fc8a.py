"""Graphic Tablet Stylus Pen.
Plan: Long stylus with rounded cap and pointed conical lower end. Centerline extremes (6,6)-(42,42).
Construction: Lucide pipette; geometric diagonal body.
Reduction: Tiny projecting tip absorbed into the point; lower conical band omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '23455f40-31c3-536a-91c4-5a1b59a5fc8a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/graphic tablet drawing pen_23455f40-31c3-536a-91c4-5a1b59a5fc8a.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/graphic tablet drawing pen_23455f40-31c3-536a-91c4-5a1b59a5fc8a.svg'

def _run(icon, name, *points):
    for i,(a,b) in enumerate(zip(points,points[1:]),1):
        icon.add_line(f'{name}-{i}',a,b)

def _circle(icon, name, cx, cy, radius):
    a,b=(cx-radius,cy),(cx+radius,cy)
    icon.add_arc(name+'-a',a,b,radius_x=radius)
    icon.add_arc(name+'-b',b,a,radius_x=radius)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)


class Drawing(Solo48):
    icon_id = 'diagonal-stylus-with-fine-tip'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('graphic', 'tablet', 'stylus', 'pen')

    def build(self):
        self.add_arc('cap',(32,6),(42,16),radius_x=10)
        _run(self,'outline',(42,16),(36,22),(18,40),(6,42),(8,30),(26,12),(32,6))
        self.add_contour('body','cap',*[f'outline-{i}' for i in range(1,7)],closed=True)
        self.add_line('band',(26,12),(36,22))
        self.relate('connect','band','body')
