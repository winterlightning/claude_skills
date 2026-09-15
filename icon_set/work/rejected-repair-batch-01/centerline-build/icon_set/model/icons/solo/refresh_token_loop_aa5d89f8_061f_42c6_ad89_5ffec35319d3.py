"""Two open concentric loops terminate beside an attached token ring. Lucide rotate-cw informs coherent circular arcs; the source establishes the double loop without an arrow. The inner loop is shortened at its lower end for token clearance. Intentional open lower-right sector.
SOLO48 SQUARE, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='aa5d89f8-061f-42c6-ad89-5ffec35319d3'
SOURCE_PATH='pictographic-primitives/programing/refresh token authentication coin loading_aa5d89f8-061f-42c6-ad89-5ffec35319d3.svg'
AUTHOR='gpt-6'

class RefreshTokenLoop(Solo48):
    icon_id='refresh-token-loop'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/programming"
    aliases=()
    keywords=('refresh', 'token', 'loading', 'coin', 'authentication', 'cycle', 'progress', 'renew')

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

        self.add_arc('outer-lower',(15,40),(6,24),radius_x=9,radius_y=16)
        self.add_arc('outer-left',(6,24),(24,6),radius_x=18)
        self.add_arc('outer-upper',(24,6),(42,24),radius_x=18)
        self.add_contour('outer','outer-lower','outer-left','outer-upper')
        self.add_arc('inner-left',(24,33),(24,15),radius_x=9)
        self.add_arc('inner-upper',(24,15),(33,24),radius_x=9)
        self.add_contour('inner','inner-left','inner-upper')
        self.add_line('token-stem',(33,24),(33,30))
        ring('token',33,36,6)
        join('inner','token-stem')
        join('token','token-stem')
