"""Database root distributing to square child nodes. Three children reduce to two and intermediate cylinder bands are removed so the square openings remain legal. Lucide database and network inform the cylinder and equal branch construction; bilateral symmetry.
SOLO48 VRECT_L; authored directly against the live contract, never scaled.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='0fa8599a-e471-5ab4-977f-c512cb403729'
SOURCE_PATH='pictographic-primitives/programing/database hierarchy_0fa8599a-e471-5ab4-977f-c512cb403729.svg'
AUTHOR='gpt-6'

class DatabaseHierarchy(Solo48):
    icon_id='database-hierarchy'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    aliases=()
    keywords=('database', 'hierarchy', 'tree', 'structure', 'data', 'schema', 'nodes', 'storage')

    def build(self) -> None:
        def oval(name,x,y,rx,ry):
            self.add_arc(name+'-top',(x-rx,y),(x+rx,y),radius_x=rx,radius_y=ry)
            self.add_arc(name+'-bottom',(x+rx,y),(x-rx,y),radius_x=rx,radius_y=ry)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        oval('rim',24,8,12,4)
        self.add_line('database-right',(36,8),(36,14))
        self.add_arc('base-right',(36,14),(24,18),radius_x=12,radius_y=4)
        self.add_arc('base-left',(24,18),(12,14),radius_x=12,radius_y=4)
        self.add_line('database-left',(12,14),(12,8))
        self.add_contour('database','database-right','base-right','base-left','database-left')
        self.relate('connect','rim','database')
        self.add_line('root-stem',(24,18),(24,27))
        self.relate('connect','database','root-stem')
        for side,x in (('left',12),('right',36)):
            self.add_polyline(side+'-branch',(24,27),(x,27),(x,36))
            self.add_polyline(side+'-node',(x-4,36),(x,36),(x+4,36),(x+4,44),(x-4,44),closed=True)
            self.relate('connect',side+'-branch',side+'-node')
            self.relate('connect',side+'-branch','root-stem')
        self.relate('connect','left-branch','right-branch')
