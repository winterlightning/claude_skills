from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='d6c565a3-4a7c-5c14-8898-e8d4416031e0'
SOURCE_PATH='icon_set/work/todo-references/photo sound wave_d6c565a3-4a7c-5c14-8898-e8d4416031e0.svg'
AUTHOR='gpt-6'
PLAN='A photo window contains two smooth sound waves below a header.'
OMISSIONS='Tiny header dot omitted; two complete waves retained.'
LUCIDE_REFERENCE='audio-lines'
HUMAN_REFERENCE=None
class Drawing(Solo48):
    icon_id='photo-sound-wave'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/media'
    aliases=()
    keywords=('photo', 'sound', 'wave')

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for j,a in enumerate(pts):
            b=pts[(j+1)%8];name=f'{n}-{j}';names.append(name)
            if j%2:self.add_arc(name,a,b,radius_x=r)
            else:self.add_line(name,a,b)
        self.add_contour(n,*names,closed=True)

    def handset(self):
        # One coherent side-profile receiver: round outer sweep and two ear pads.
        self.add_bezier('receiver',(9,6),((6,6),(6,12),(6,15)),((6,26),(22,42),(33,42)),((37,42),(42,40),(42,37)),((42,35),(36,30),(34,30)),((32,30),(30,34),(28,32)),((22,28),(19,25),(16,20)),((14,17),(19,15),(19,12)),((19,10),(12,6),(9,6)))

    def build(self):
        # A photo window contains two smooth sound waves below a header.

        self.box('frame',6,6,36,36,3)
        self.add_line('header',(6,15),(42,15));self.relate('connect','header','frame')
        for n,y in [('upper',25),('lower',35)]:
            self.add_bezier(n,(6,y),((12,y),(12,y-2),(18,y-2)),((24,y-2),(24,y+1),(30,y+1)),((36,y+1),(36,y-2),(42,y)))
            self.relate('connect',n,'frame')

