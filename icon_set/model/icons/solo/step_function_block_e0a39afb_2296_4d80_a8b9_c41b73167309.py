"""A workflow block has top and bottom round knobs, two left contacts and one right rectangular port. Lucide puzzle informs intrinsic knobs; CPU informs attached contacts. The left capsules reduce to two solid bars and the knob holes are omitted. Deliberate unequal left and right ports.
SOLO48 SQUARE, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='e0a39afb-2296-4d80-a8b9-c41b73167309'
SOURCE_PATH='pictographic-primitives/programing/step functions_e0a39afb-2296-4d80-a8b9-c41b73167309.svg'
AUTHOR='gpt-6'

class StepFunctionBlock(Solo48):
    icon_id='step-function-block'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    categories = ("programing", "primitives")
    aliases=()
    keywords=('step', 'functions', 'workflow', 'blocks', 'puzzle', 'state-machine', 'process', 'orchestration')

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

        self.add_line('top-left',(14,10),(19,10))
        self.add_arc('top-knob',(19,10),(27,10),radius_x=4)
        self.add_line('top-right',(27,10),(32,10))
        self.add_line('upper-right',(32,10),(32,18))
        self.add_contour('upper','top-left','top-knob','top-right','upper-right')
        self.add_line('lower-right',(32,30),(32,38))
        self.add_line('bottom-right',(32,38),(27,38))
        self.add_arc('bottom-knob',(27,38),(19,38),radius_x=4)
        self.add_line('bottom-left',(19,38),(14,38))
        self.add_polyline('left-wall',(14,38),(14,30),(14,18),(14,10))
        self.add_contour('lower','lower-right','bottom-right','bottom-knob','bottom-left')
        join('upper','left-wall')
        join('lower','left-wall')
        self.add_polyline('right-port',(26,18),(32,18),(42,18),(42,30),(32,30),(26,30),closed=True)
        join('right-port','upper')
        join('right-port','lower')
        for name,y in (('upper-contact',18),('lower-contact',30)):
            self.add_polyline(name,(6,y),(14,y),(18,y))
            join(name,'left-wall')
