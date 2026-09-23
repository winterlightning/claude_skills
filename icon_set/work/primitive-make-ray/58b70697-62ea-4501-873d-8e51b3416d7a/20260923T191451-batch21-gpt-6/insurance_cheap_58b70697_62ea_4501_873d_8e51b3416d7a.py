"""A coin sits below a medical cross on a rising balance beam, indicating cheap insurance.
Construction reference: scale.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '58b70697-62ea-4501-873d-8e51b3416d7a'
SOURCE_PATH = 'icon_set/work/todo-references/insurance cheap_58b70697-62ea-4501-873d-8e51b3416d7a.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'insurance-cheap'
    keyshape = Keyshape.SQUARE
    # Visible ink extremes: (4, 4, 44, 44).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('insurance', 'cheap')

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

        # Plan: tilted beam and triangular fulcrum; left coin lower than right cross.
        self.circle('coin',14,18,8)
        self.add_bezier('dollar',(17,14),((10,12),(10,18),(14,18)),((19,18),(18,23),(11,22)))
        self.add_line('dollar-stem',(14,11),(14,25))
        self.relate('connect','dollar','dollar-stem')
        self.add_polyline('medical-cross',(30,6),(38,6),(38,10),(42,10),(42,18),(38,18),(38,22),(30,22),(30,18),(26,18),(26,10),(30,10),closed=True)
        self.add_polyline('beam',(6,38),(24,33),(42,28))
        self.add_polyline('fulcrum',(24,33),(16,42),(32,42),closed=True)
        self.relate('connect','beam','fulcrum')
