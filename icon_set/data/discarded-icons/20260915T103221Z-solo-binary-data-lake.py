"""A representative 101 binary row above two water waves. Ten digits in two rows reduce to three in one row to preserve binary and water identity. Lucide binary informs the digits; wave arcs are fresh tangent-matched circular segments, with equal phase and spacing.
SOLO48 HRECT_L; authored directly against the live contract, never scaled.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='e8929314-39ec-46c6-9cfb-5107ebede2dc'
SOURCE_PATH='pictographic-primitives/programing/data lake code_e8929314-39ec-46c6-9cfb-5107ebede2dc.svg'
AUTHOR='gpt-6'

class BinaryDataLake(Solo48):
    icon_id='binary-data-lake'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/programming"
    aliases=()
    keywords=('data', 'lake', 'binary', 'water', 'waves', 'storage', 'analytics', 'digits')

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

        self.add_line('one-left',(8,8),(8,16))
        oval('zero',24,12,4,4)
        self.add_line('one-right',(40,8),(40,16))
        wave('water-upper',26)
        wave('water-lower',38)
