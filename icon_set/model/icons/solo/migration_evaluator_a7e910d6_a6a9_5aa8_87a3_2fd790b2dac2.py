"""A four-point migration star has a right chevron and four outward corner arrows.
Construction reference: none.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a7e910d6-a6a9-5aa8-87a3-2fd790b2dac2'
SOURCE_PATH = 'icon_set/work/todo-references/migration evaluator_a7e910d6-a6a9-5aa8-87a3-2fd790b2dac2.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'migration-evaluator'
    keyshape = Keyshape.SQUARE
    # Visible ink extrema: (4, 4, 44, 44).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('migration', 'evaluator')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)
    def rect(self,name,x,y,w,h,r=2):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for i,a in enumerate(pts):
            n=f'{name}-{i}';b=pts[(i+1)%8]
            if i%2:self.add_arc(n,a,b,radius_x=r)
            else:self.add_line(n,a,b)
            names.append(n)
        self.add_contour(name,*names,closed=True)

    def build(self):

        # Plan: cardinal star around (24,24), central direction and mirrored corner tips.
        self.add_polyline('star',(24,6),(29,19),(42,24),(29,29),(24,42),(19,29),(6,24),(19,19),closed=True)
        self.add_polyline('center-chevron',(23,21),(26,24),(23,27))
        for sx in (-1,1):
            for sy in (-1,1):
                self.add_polyline(f'corner-{sx}-{sy}',(24+sx*10,24+sy*12),(24+sx*15,24+sy*15),(24+sx*12,24+sy*10))
