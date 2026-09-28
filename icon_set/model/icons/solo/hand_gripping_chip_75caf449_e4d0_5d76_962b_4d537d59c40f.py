"""A hand pinches a small square microchip at its upper left. Lucide hand informs a continuous cupped hand; CPU informs the square and pins. Hidden right and bottom pins and finger divisions are omitted. Intentional asymmetric grip.
SOLO48 SQUARE, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='75caf449-e4d0-5d76-962b-4d537d59c40f'
SOURCE_PATH='pictographic-primitives/programing/technology chip hold_75caf449-e4d0-5d76-962b-4d537d59c40f.svg'
AUTHOR='gpt-6'

class HandGrippingChip(Solo48):
    icon_id='hand-gripping-chip'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    categories = ("programing", "primitives")
    aliases=()
    keywords=('hand', 'chip', 'microchip', 'grip', 'hardware', 'technology', 'processor', 'electronics')

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

        self.add_polyline('chip',(10,10),(14,10),(22,10),(22,15),(22,22),(14,22),(10,22),(10,16),closed=True)
        self.add_line('top-pin',(14,6),(14,10))
        self.add_line('left-pin',(6,16),(10,16))
        join('chip','top-pin')
        join('chip','left-pin')
        self.add_line('finger-tip',(22,10),(22,8))
        self.add_arc('finger-cap',(22,8),(24,6),radius_x=2)
        self.add_arc('outer-finger',(24,6),(42,24),radius_x=18)
        self.add_line('right-wrist',(42,24),(42,42))
        self.add_contour('outer-hand','finger-tip','finger-cap','outer-finger','right-wrist')
        join('chip','outer-hand')
        self.add_line('inner-tip',(22,15),(24,15))
        self.add_arc('inner-upper',(24,15),(33,24),radius_x=9)
        self.add_arc('inner-lower',(33,24),(24,33),radius_x=9)
        self.add_line('thumb-inner',(24,33),(14,22))
        self.add_contour('inner-hand','inner-tip','inner-upper','inner-lower','thumb-inner')
        join('chip','inner-hand')
        self.add_arc('thumb-outer',(14,22),(6,30),radius_x=8,sweep=False)
        self.add_line('left-wrist',(6,30),(18,42))
        self.add_contour('lower-hand','thumb-outer','left-wrist')
        join('chip','lower-hand')
        join('inner-hand','lower-hand')
