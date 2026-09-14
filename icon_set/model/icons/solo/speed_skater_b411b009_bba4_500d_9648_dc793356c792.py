"""Speed Skater, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='b411b009-bba4-500d-9648-dc793356c792'
SOURCE_PATH='pictographic-primitives/sports/speed skating_b411b009-bba4-500d-9648-dc793356c792.svg'
AUTHOR='gpt-6'

class SpeedSkater(Solo48):
    icon_id='speed-skater'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('speed', 'skater', 'ice', 'winter', 'athlete', 'racing')
    def build(self) -> None:
        # SQUARE centerline extremes (6, 6, 42, 42) from current SOLO48 contract.
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
        circle('head',39,9,3)
        self.add_polyline('arms',(29,14),(20,6),(18,13))
        self.add_polyline('body',(29,14),(19,24),(27,33),(25,42))
        self.add_polyline('rear-leg',(19,24),(13,31),(6,33))
        self.add_polyline('skate',(20,42),(25,42),(37,42),(42,38))
        self.relate('connect','arms','body')
        self.relate('connect','body','rear-leg')
        self.relate('connect','body','skate')
        self.add_line('motion-a',(6,14),(9,14))
        self.add_line('motion-b',(6,23),(9,23))
