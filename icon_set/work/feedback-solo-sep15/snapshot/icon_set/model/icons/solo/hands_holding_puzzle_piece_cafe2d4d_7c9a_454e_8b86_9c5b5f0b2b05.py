"""Two cupped hands support a jigsaw piece. The piece is upright, with one top knob and one side socket instead of four dense interfaces; finger divisions are omitted. Lucide puzzle and the previously inspected hand inform the piece and palms. Hands mirror about x=24.
SOLO48 SQUARE, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='cafe2d4d-7c9a-454e-8b86-9c5b5f0b2b05'
SOURCE_PATH='pictographic-primitives/programing/module hands puzzle_cafe2d4d-7c9a-454e-8b86-9c5b5f0b2b05.svg'
AUTHOR='gpt-6'

class HandsHoldingPuzzlePiece(Solo48):
    icon_id='hands-holding-puzzle-piece'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/programming"
    aliases=()
    keywords=('puzzle', 'hands', 'module', 'piece', 'solution', 'integration', 'support', 'teamwork')

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

        self.add_line('piece-top-left',(18,10),(20,10))
        self.add_arc('piece-knob',(20,10),(28,10),radius_x=4)
        self.add_line('piece-top-right',(28,10),(30,10))
        self.add_line('piece-shoulder',(30,10),(30,12))
        self.add_arc('piece-socket',(30,12),(30,18),radius_x=3,sweep=False)
        self.add_line('piece-bottom',(30,18),(18,18))
        self.add_line('piece-left',(18,18),(18,10))
        self.add_contour('puzzle','piece-top-left','piece-knob','piece-top-right','piece-shoulder','piece-socket','piece-bottom','piece-left',closed=True)
        for side,mirror in (('left',False),('right',True)):
            def p(x,y): return (48-x if mirror else x,y)
            self.add_line(side+'-outer-wrist',p(11,42),p(6,34))
            self.add_line(side+'-outer-palm',p(6,34),p(6,28))
            self.add_arc(side+'-finger',p(6,28),p(14,28),radius_x=4,sweep=not mirror)
            self.add_line(side+'-inner-palm',p(14,28),p(14,32))
            self.add_line(side+'-thumb',p(14,32),p(19,37))
            self.add_line(side+'-inner-wrist',p(19,37),p(19,42))
            self.add_contour(side+'-hand',side+'-outer-wrist',side+'-outer-palm',side+'-finger',side+'-inner-palm',side+'-thumb',side+'-inner-wrist')
