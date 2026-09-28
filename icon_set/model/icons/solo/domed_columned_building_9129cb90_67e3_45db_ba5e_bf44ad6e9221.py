"""Domed government building, front view.
SQUARE (6,6)-(42,42). A semicircular dome owns its cornice, a shared
12-unit series owns three columns. Mirror about x=24. Lucide landmark
contributes detached column rhythm; source provides dome. Omit thick
cornice/base outlines and reduce columns to three weight-matched strokes.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = "9129cb90-67e3-45db-ba5e-bf44ad6e9221"
SOURCE_PATH = "pictographic-primitives/_uncategorized_29/official building 2_9129cb90-67e3-45db-ba5e-bf44ad6e9221.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "domed-columned-building"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("Domed Government Building",)
    keywords = ("building", "dome", "columns", "classical", "government", "architecture")
    def build(self):
        self.add_arc('dome',(8,22),(40,22),radius_x=16,sweep=True)
        xs=(6,8,40,42)
        for i,(a,b) in enumerate(zip(xs,xs[1:])):
            self.add_line(f'cornice-{i}',(a,22),(b,22))
        self.add_contour('cornice','cornice-0','cornice-1','cornice-2')
        self.relate('connect','dome','cornice-0','cornice-1','cornice-2')
        xs=(6,12,24,36,42)
        for i,(a,b) in enumerate(zip(xs,xs[1:])):
            self.add_line(f'base-{i}',(a,42),(b,42))
        self.add_contour('base',*[f'base-{i}' for i in range(4)])
        for i,x in enumerate((12,24,36)):
            self.add_line(f'column-{i}',(x,31),(x,42))
            self.relate('connect',f'column-{i}',f'base-{i}',f'base-{i+1}')
