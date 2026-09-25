"""A conical flask has a short narrow neck, flared rim, and rounded lower corners. A small pointed flame rises directly above the mouth, while a short horizontal line marks liquid inside.

VRECT_XL visible bounds (6,2)-(42,46); conical flask and pointed flame above its mouth. Nested flame and liquid line omitted to leave clear interiors. Lucide flask-conical informed neck and bowl; symmetric vessel.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '03227ed1-073e-5f3d-b9bc-fadb0e3ac918'
SOURCE_PATH = 'pictographic-primitives/science/lab flame bottle_03227ed1-073e-5f3d-b9bc-fadb0e3ac918.svg'
AUTHOR = 'gpt-6'

class FlamingLaboratoryFlask(Solo48):
    icon_id = 'flaming-laboratory-flask'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('flask', 'flame', 'laboratory', 'chemistry', 'liquid', 'experiment')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.segments('neck-left',(18,28),(18,32),(8,40))
        self.add_arc('bottom-left',(8,40),(12,44),radius_x=4,sweep=False)
        self.add_line('bottom',(12,44),(36,44))
        self.add_arc('bottom-right',(36,44),(40,40),radius_x=4,sweep=False)
        self.segments('neck-right',(40,40),(30,32),(30,28),(18,28))
        self.add_contour('flask','neck-left-1','neck-left-2','bottom-left','bottom','bottom-right','neck-right-1','neck-right-2','neck-right-3',closed=True)
        self.add_arc('flame-rise-right',(24,4),(30,12),radius_x=10)
        self.add_arc('flame-base-right',(30,12),(24,18),radius_x=6)
        self.add_arc('flame-base-left',(24,18),(18,12),radius_x=6)
        self.add_arc('flame-rise-left',(18,12),(24,4),radius_x=10)
        self.add_contour('flame','flame-rise-right','flame-base-right','flame-base-left','flame-rise-left',closed=True)
