"""Three stacked log rolls, with opposite curved end faces on the lower two. The plain top roll reduces to one solid stroke; both lower roll outlines and end faces remain. Lucide logs informs the stacked rhythm, not the capsule shape. Source establishes the roll construction and deliberate offsets.
SOLO48 VRECT_L, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='f256a628-0e30-4674-a772-b5c809a93a94'
SOURCE_PATH='pictographic-primitives/programing/logs authentication stack_f256a628-0e30-4674-a772-b5c809a93a94.svg'
AUTHOR='gpt-6'

class StackedLogRolls(Solo48):
    icon_id='stacked-log-rolls'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/programming"
    aliases=()
    keywords=('logs', 'stack', 'rolls', 'records', 'storage', 'authentication', 'layers', 'data')

    def build(self) -> None:
        def ring(name,x,y,r):
            points=((x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r))
            members=[]
            for i,(a,b) in enumerate(zip(points,points[1:])):
                member=f'{name}-{i}'
                self.add_arc(member,a,b,radius_x=r)
                members.append(member)
            self.add_contour(name,*members,closed=True)

        def join(*names):
            from itertools import combinations
            for a,b in combinations(names,2): self.relate('connect',a,b)

        self.add_line('top-roll',(12,4),(32,4))
        for name,x,y in (('middle',8,16),('lower',12,36)):
            self.add_line(name+'-top',(x+4,y),(x+24,y))
            self.add_arc(name+'-right',(x+24,y),(x+24,y+8),radius_x=4)
            self.add_line(name+'-bottom',(x+24,y+8),(x+4,y+8))
            self.add_arc(name+'-left',(x+4,y+8),(x+4,y),radius_x=4)
            self.add_contour(name+'-roll',name+'-top',name+'-right',name+'-bottom',name+'-left',closed=True)
        self.add_arc('middle-end-face',(12,16),(12,24),radius_x=4)
        self.add_arc('lower-end-face',(36,44),(36,36),radius_x=4)
        join('middle-end-face','middle-roll')
        join('lower-end-face','lower-roll')
