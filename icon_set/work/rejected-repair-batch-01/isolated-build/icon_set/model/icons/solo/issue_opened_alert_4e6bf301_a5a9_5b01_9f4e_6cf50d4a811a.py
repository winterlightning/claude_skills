"""An exclamation mark rises through the opening of a rounded bowl outline. The tapered hollow mark and ring dot become a clear stroke and solid dot. Lucide circle-alert informs the exclamation proportions; quarter-ellipse shoulders join the circular bowl smoothly. Bilateral symmetry.
SOLO48 SQUARE, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='4e6bf301-a5a9-5b01-9f4e-6cf50d4a811a'
SOURCE_PATH='pictographic-primitives/programing/issue opened_4e6bf301-a5a9-5b01-9f4e-6cf50d4a811a.svg'
AUTHOR='gpt-6'

class IssueOpenedAlert(Solo48):
    icon_id='issue-opened-alert'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/programming"
    aliases=()
    keywords=('issue', 'alert', 'exclamation', 'warning', 'open', 'bug', 'report', 'attention')

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

        self.add_line('exclamation',(24,6),(24,22))
        self.add_dot('dot',(24,32))
        self.add_arc('shoulder-left',(14,18),(6,30),radius_x=8,radius_y=12,sweep=False)
        self.add_arc('base-left',(6,30),(18,42),radius_x=12,sweep=False)
        self.add_line('base',(18,42),(30,42))
        self.add_arc('base-right',(30,42),(42,30),radius_x=12,sweep=False)
        self.add_arc('shoulder-right',(42,30),(34,18),radius_x=8,radius_y=12,sweep=False)
        self.add_contour('bowl','shoulder-left','base-left','base','base-right','shoulder-right')
