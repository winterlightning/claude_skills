"""Sumo Wrestler, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='9ed19462-8339-482a-a209-2c66f9e595f9'
SOURCE_PATH='pictographic-primitives/sports/sumo_9ed19462-8339-482a-a209-2c66f9e595f9.svg'
AUTHOR='gpt-6'

class SumoWrestler(Solo48):
    icon_id='sumo-wrestler'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('sumo', 'wrestler', 'wrestling', 'athlete', 'combat', 'sport')
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
        circle('head',24,14,4)
        self.add_line('topknot',(24,6),(24,10))
        self.relate('connect','head','topknot')
        self.add_polyline('body',(16,24),(14,32),(20,32),(28,32),(34,32),(32,24))
        self.add_polyline('arm-left',(16,24),(6,28))
        self.add_polyline('arm-right',mirror((16,24)),mirror((6,28)))
        for n in ['arm-left','arm-right']:self.relate('connect',n,'body')
        self.add_polyline('leg-left',(14,32),(10,37),(10,42))
        self.add_polyline('leg-right',mirror((14,32)),mirror((10,37)),mirror((10,42)))
        self.add_polyline('belt-panel',(20,32),(20,40),(28,40),(28,32))
        for n in ['leg-left','leg-right','belt-panel']:self.relate('connect',n,'body')
