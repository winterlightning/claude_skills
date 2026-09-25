"""Descending data levels and a database over a waterline. Two solid level strokes replace three outlined bars; the smallest bar and cylinder band are omitted. Lucide database informs the cylinder. Intentional asymmetry retains descending levels and upper-right storage.
SOLO48 HRECT_L; authored directly against the live contract, never scaled.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='efbcacb7-495b-4dce-b085-552411365b22'
SOURCE_PATH='pictographic-primitives/programing/data lake level_efbcacb7-495b-4dce-b085-552411365b22.svg'
AUTHOR='gpt-6'

class DataLakeLevelChart(Solo48):
    icon_id='data-lake-level-chart'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    aliases=()
    keywords=('data', 'lake', 'chart', 'bars', 'database', 'water', 'level', 'analytics')

    def build(self) -> None:
        def oval(name,x,y,rx,ry):
            self.add_arc(name+'-top',(x-rx,y),(x+rx,y),radius_x=rx,radius_y=ry)
            self.add_arc(name+'-bottom',(x+rx,y),(x-rx,y),radius_x=rx,radius_y=ry)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        def wave(name,baseline):
            members=[]
            for i in range(2):
                member=f'{name}-{i}'
                self.add_arc(member,(4+i*20,baseline),(24+i*20,baseline),radius_x=26,sweep=bool(i%2))
                members.append(member)
            self.add_contour(name,*members)

        self.add_line('level-tall',(8,8),(8,28))
        self.add_line('level-short',(22,18),(22,28))
        oval('database-rim',38,11,6,3)
        self.add_line('database-right',(44,11),(44,19))
        self.add_arc('database-bottom',(44,19),(32,19),radius_x=6,radius_y=3)
        self.add_line('database-left',(32,19),(32,11))
        self.add_contour('database-body','database-right','database-bottom','database-left')
        self.relate('connect','database-rim','database-body')
        wave('water',38)
