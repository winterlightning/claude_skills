"""Hourglass with Sand Level; standalone reconstruction of the supplied reference.
Construction: Lucide hourglass informed coherent contours and structural joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1873be1c-2600-5197-83a2-680121a9a499'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hourglass_1873be1c-2600-5197-83a2-680121a9a499.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hourglass-with-sand-level'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/interface-essential"
    aliases = ()
    keywords = ('hourglass', 'sand', 'timer', 'time', 'glass', 'chambers')

    def build(self):
        # Plan: taller upper chamber accommodates its sand bar; crossing waist.
        # VRECT_L extremes (8,4)-(40,44); each curve has continuous tangents.
        axis=24
        for side,sign in (("left",-1),("right",1)):
            x=axis+sign*14
            opposite=axis-sign*14
            self.add_line(side+"-upper",(x,4),(x,12))
            self.add_bezier(side+"-glass",(x,12),
                ((x,20),(axis+sign*6,22),(axis,28)),
                ((axis-sign*6,34),(opposite,32),(opposite,40)))
            self.add_line(side+"-lower",(opposite,40),(opposite,44))
            self.add_contour(side,side+"-upper",side+"-glass",side+"-lower")
        self.relate("connect","left","right")
        for end,y in (("top",4),("bottom",44)):
            self.add_polyline(end,(8,y),(10,y),(38,y),(40,y))
            for side in ("left","right"):
                self.relate("connect",end,side)
        self.add_line("sand-level",(21,12),(27,12))
