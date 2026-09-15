"""A paper scroll with opposite curled ends and two text lines. Lucide scroll-text informs tangent curl transitions; the source sets the top-right and bottom-left curls. Both text lines remain, with intentional asymmetric rolls.
SOLO48 SQUARE, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='e0b6bba5-0e9a-4d10-b2c8-8f4ade021780'
SOURCE_PATH='pictographic-primitives/programing/programming language code_e0b6bba5-0e9a-4d10-b2c8-8f4ade021780.svg'
AUTHOR='gpt-6'

class ScrollWithTextLines(Solo48):
    icon_id='scroll-with-text-lines'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/programming"
    aliases=()
    keywords=('scroll', 'script', 'code', 'document', 'paper', 'language', 'text', 'programming')

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

        self.add_line('page-top',(12,6),(38,6))
        self.add_arc('top-curl',(38,6),(42,10),radius_x=4)
        self.add_line('tab-right',(42,10),(42,16))
        self.add_line('tab-base',(42,16),(34,16))
        self.add_line('page-right',(34,16),(34,36))
        self.add_arc('page-foot',(34,36),(28,42),radius_x=6)
        self.add_line('roll-base',(28,42),(11,42))
        self.add_arc('roll-left',(11,42),(11,32),radius_x=5)
        self.add_line('roll-top',(11,32),(22,32))
        self.add_contour('scroll','page-top','top-curl','tab-right','tab-base','page-right','page-foot','roll-base','roll-left','roll-top')
        self.add_arc('upper-inner',(38,6),(34,10),radius_x=4,sweep=False)
        self.add_line('upper-inner-wall',(34,10),(34,16))
        self.add_contour('upper-fold','upper-inner','upper-inner-wall')
        join('scroll','upper-fold')
        self.add_arc('lower-inner',(22,32),(22,42),radius_x=5,sweep=False)
        join('scroll','lower-inner')
        self.add_line('page-left',(12,6),(12,32))
        join('scroll','page-left')
        self.add_line('text-1',(21,15),(25,15))
        self.add_line('text-2',(21,23),(25,23))
