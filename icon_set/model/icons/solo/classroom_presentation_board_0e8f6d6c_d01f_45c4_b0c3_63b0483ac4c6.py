"""Classroom Presentation Board. Empty standalone subject, per explicit user correction.
Lucide presentation: rounded board outline and shared support junctions. Symmetry about x=24; tray and legs split at real joints. Tray thickness simplified to one projecting rail.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '0e8f6d6c-d01f-45c4-b0c3-63b0483ac4c6'
SOURCE_PATH = 'pictographic-primitives/container/board_0e8f6d6c-d01f-45c4-b0c3-63b0483ac4c6.svg'
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = 'classroom-presentation-board'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'container'
    aliases = ()
    keywords = ('classroom', 'presentation', 'board')
    def build(self):
        self.add_line("board-left",(8,26),(8,10))
        self.add_arc("board-nw",(8,10),(12,6),radius_x=4)
        self.add_line("board-top",(12,6),(36,6))
        self.add_arc("board-ne",(36,6),(40,10),radius_x=4)
        self.add_line("board-right",(40,10),(40,26))
        self.add_contour("board","board-left","board-nw","board-top","board-ne","board-right")
        xs=(6,8,12,36,40,42)
        for i,(a,b) in enumerate(zip(xs,xs[1:])):
            self.add_line(f"tray-{i}",(a,26),(b,26))
        self.add_contour("tray",*(f"tray-{i}" for i in range(5)))
        self.relate("connect","board","tray")
        for side,x in (("left",12),("right",36)):
            self.add_line(side+"-upper",(x,26),(x,34))
            self.add_line(side+"-lower",(x,34),(x,42))
            self.add_contour(side+"-leg",side+"-upper",side+"-lower")
            self.relate("connect","tray",side+"-leg")
        self.add_line("crossbar",(12,34),(36,34))
        self.relate("connect","crossbar","left-leg","right-leg")
