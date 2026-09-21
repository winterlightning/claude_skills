"""Hanging Scoreboard, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='0918c48a-7ee6-4895-9035-4645fdc17ae1'
SOURCE_PATH='pictographic-primitives/sports/scoreboard_0918c48a-7ee6-4895-9035-4645fdc17ae1.svg'
AUTHOR='gpt-6'

class HangingScoreboard(Solo48):
    icon_id='hanging-scoreboard'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('scoreboard', 'score', 'game', 'match', 'sport', 'result')
    def build(self) -> None:
        # HRECT_L centerline extremes (4, 8, 44, 40) from current SOLO48 contract.
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(n+'-b',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def arc(n,a,b,r,ry=None,sweep=True):
            self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*pts):
            for i,(a,b) in enumerate(zip(pts,pts[1:]),1):self.add_line(f'{n}-{i}',a,b)
        axis=24
        def mirror(p):return (2*axis-p[0],p[1])
        top,bottom=14,40
        # One rounded frame; paired mounting points derive from x=24.
        poly('top',(8,top),(14,top),(34,top),(40,top))
        arc('tr',(40,top),(44,top+4),4)
        self.add_line('right',(44,top+4),(44,bottom-4))
        arc('br',(44,bottom-4),(40,bottom),4)
        poly('bottom',(40,bottom),(34,bottom),(14,bottom),(8,bottom))
        arc('bl',(8,bottom),(4,bottom-4),4)
        self.add_line('left',(4,bottom-4),(4,top+4))
        arc('tl',(4,top+4),(8,top),4)
        self.add_contour('frame','top-1','top-2','top-3','tr','right','br','bottom-1','bottom-2','bottom-3','bl','left','tl',closed=True)
        for x in (14,2*axis-14):
            self.add_line(f'mount-{x}',(x,14),(x,8))
            self.relate('connect',f'mount-{x}','frame')
        arc('two-top',(13,25),(21,25),4,2)
        poly('two-lower',(21,25),(13,31),(21,31))
        self.add_contour('two','two-top','two-lower-1','two-lower-2')
        circle('zero',32,27,3)
