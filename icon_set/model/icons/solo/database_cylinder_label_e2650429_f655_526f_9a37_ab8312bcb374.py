"""Tall database cylinder with two label lines. Lucide database supplies elliptical-rim and parallel-wall construction. Extra source bands are omitted to preserve clear space around the label; shared axis and ellipse radii.
SOLO48 VRECT_L; authored directly against the live contract, never scaled.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='e2650429-f655-526f-9a37-ab8312bcb374'
SOURCE_PATH='pictographic-primitives/programing/database 1_e2650429-f655-526f-9a37-ab8312bcb374.svg'
AUTHOR='gpt-6'

class DatabaseCylinderLabel(Solo48):
    icon_id='database-cylinder-label'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    categories = ("programing", "primitives")
    aliases=()
    keywords=('database', 'cylinder', 'storage', 'data', 'server', 'table', 'record', 'sql')

    def build(self) -> None:
        def oval(name,x,y,rx,ry):
            self.add_arc(name+'-top',(x-rx,y),(x+rx,y),radius_x=rx,radius_y=ry)
            self.add_arc(name+'-bottom',(x+rx,y),(x-rx,y),radius_x=rx,radius_y=ry)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        oval('rim',24,9,16,5)
        self.add_line('wall-right',(40,9),(40,39))
        self.add_arc('bottom',(40,39),(8,39),radius_x=16,radius_y=5)
        self.add_line('wall-left',(8,39),(8,9))
        self.add_contour('body','wall-right','bottom','wall-left')
        self.relate('connect','rim','body')
        self.add_line('label-upper',(18,26),(30,26))
        self.add_line('label-lower',(20,35),(28,35))
