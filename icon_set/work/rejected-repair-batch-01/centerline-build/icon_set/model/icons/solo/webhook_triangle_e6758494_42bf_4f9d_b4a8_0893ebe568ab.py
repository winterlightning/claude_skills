"""Three open hooks occupy the corners of a triangular webhook. Lucide webhook informs the three independently curled paths. Stems are rebalanced to tangent vertical and horizontal approaches; all three hooks remain. Deliberate rotational direction.
SOLO48 SQUARE, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='e6758494-42bf-4f9d-b4a8-0893ebe568ab'
SOURCE_PATH='pictographic-primitives/programing/web hook_e6758494-42bf-4f9d-b4a8-0893ebe568ab.svg'
AUTHOR='gpt-6'

class WebhookTriangle(Solo48):
    icon_id='webhook-triangle'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/programming"
    aliases=()
    keywords=('webhook', 'hook', 'api', 'integration', 'callback', 'triangle', 'link', 'event')

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

        self.add_arc('top-right',(33,15),(24,6),radius_x=9,sweep=False)
        self.add_arc('top-left',(24,6),(15,15),radius_x=9,sweep=False)
        self.add_line('left-stem',(15,15),(15,27))
        self.add_contour('top-hook','top-right','top-left','left-stem')
        self.add_arc('bottom-left',(6,33),(15,42),radius_x=9,sweep=False)
        self.add_arc('bottom-rise',(15,42),(19,38),radius_x=4,sweep=False)
        self.add_arc('bottom-turn',(19,38),(24,33),radius_x=5)
        self.add_line('bottom-stem',(24,33),(33,33))
        self.add_contour('left-hook','bottom-left','bottom-rise','bottom-turn','bottom-stem')
        self.add_line('upper-stem',(24,15),(24,18))
        self.add_arc('shoulder',(24,18),(30,24),radius_x=6,sweep=False)
        self.add_line('right-neck',(30,24),(33,24))
        self.add_arc('right-upper',(33,24),(42,33),radius_x=9)
        self.add_arc('right-lower',(42,33),(33,42),radius_x=9)
        self.add_contour('right-hook','upper-stem','shoulder','right-neck','right-upper','right-lower')
