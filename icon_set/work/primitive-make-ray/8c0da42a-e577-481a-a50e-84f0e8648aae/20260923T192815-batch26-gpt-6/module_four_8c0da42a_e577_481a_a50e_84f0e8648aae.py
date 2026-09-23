"""A perspective toy brick has four top studs and two visible side faces.
Construction reference: toy-brick.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8c0da42a-e577-481a-a50e-84f0e8648aae'
SOURCE_PATH = 'icon_set/work/todo-references/module four_8c0da42a-e577-481a-a50e-84f0e8648aae.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'module-four'
    keyshape = Keyshape.HRECT_L
    # Visible ink extrema: (2, 6, 46, 42).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('module', 'four')

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

        # Plan: diamond top and two faces, with four repeated oval studs.
        self.add_polyline('body',(4,22),(24,12),(44,22),(44,32),(24,40),(4,32),closed=True)
        self.add_polyline('front-edge',(4,22),(24,30),(44,22))
        self.add_line('corner',(24,30),(24,40))
        self.relate('connect','body','front-edge')
        self.relate('connect','front-edge','corner')
        self.relate('connect','body','corner')
        for i,(x,y) in enumerate([(24,11),(13,18),(35,18),(24,24)]):
            self.add_arc(f'stud-{i}-a',(x-4,y),(x+4,y),radius_x=4,radius_y=3)
            self.add_arc(f'stud-{i}-b',(x+4,y),(x-4,y),radius_x=4,radius_y=3)
            self.add_contour('stud-'+str(i),f'stud-{i}-a',f'stud-{i}-b',closed=True)
