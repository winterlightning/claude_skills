"""Crossed Swords, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='267b73de-82b1-4ce3-8f55-d126ce956c5c'
SOURCE_PATH='pictographic-primitives/sports/swords_267b73de-82b1-4ce3-8f55-d126ce956c5c.svg'
AUTHOR='gpt-6'

class CrossedSwords(Solo48):
    icon_id='crossed-swords'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    aliases=()
    keywords=('sword', 'crossed', 'blade', 'fencing', 'combat', 'equipment')
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
        def wave(n,y):
            for i,x in enumerate((6,18,30)):
                arc(f'{n}-{i}',(x,y),(x+12,y),6,2,sweep=i%2==0)
            self.add_contour(n,*[f'{n}-{i}' for i in range(3)])
        axis=24
        def mirror(p):return (2*axis-p[0],p[1])
        points=[(6,6),(12,6),(24,18),(30,24),(36,30),(33,33),(30,36),(24,30),(18,24),(6,12)]
        for n,flip in [('front',False),('back',True)]:
            transform=mirror if flip else lambda p:p
            self.add_polyline('blade-'+n,*[transform(p) for p in points],closed=True)
            self.add_polyline('guard-'+n,*[transform(p) for p in [(29,37),(30,36),(33,33),(36,30),(37,29)]])
            self.add_line('grip-'+n,transform((33,33)),transform((42,42)))
            self.relate('connect','blade-'+n,'guard-'+n)
            self.relate('connect','blade-'+n,'grip-'+n)
            self.relate('connect','guard-'+n,'grip-'+n)
        self.relate('connect','blade-front','blade-back')
