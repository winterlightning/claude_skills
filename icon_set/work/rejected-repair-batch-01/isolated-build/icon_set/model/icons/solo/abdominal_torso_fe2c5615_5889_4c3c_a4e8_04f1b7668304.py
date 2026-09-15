"""Abdominal Torso, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='fe2c5615-5889-4c3c-a4e8-04f1b7668304'
SOURCE_PATH='pictographic-primitives/sports/six pack_fe2c5615-5889-4c3c-a4e8-04f1b7668304.svg'
AUTHOR='gpt-6'

class AbdominalTorso(Solo48):
    icon_id='abdominal-torso'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('abdomen', 'torso', 'muscle', 'core', 'fitness', 'strength')
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
        arc('pec-left',(6,6),(24,6),9,7,sweep=False)
        arc('pec-right',(24,6),(42,6),9,7,sweep=False)
        self.add_contour('chest','pec-left','pec-right')
        for n,p in [('left',(6,20)),('right',mirror((6,20)))]:
            end=(8,42) if n=='left' else mirror((8,42))
            self.add_line('side-'+n,p,end)
        for i,y in enumerate((23,34)):
            arc(f'abs-{i}-left',(16,y),(24,y),4,2,sweep=False)
            arc(f'abs-{i}-right',(24,y),(32,y),4,2,sweep=False)
            self.add_contour(f'abs-{i}',f'abs-{i}-left',f'abs-{i}-right')
