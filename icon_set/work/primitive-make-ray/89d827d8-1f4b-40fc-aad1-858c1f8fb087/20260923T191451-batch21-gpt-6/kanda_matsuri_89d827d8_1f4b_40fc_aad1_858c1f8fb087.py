"""A circular Kanda Matsuri emblem contains three inward-pointing heart forms and hanging strokes.
Construction reference: heart.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '89d827d8-1f4b-40fc-aad1-858c1f8fb087'
SOURCE_PATH = 'icon_set/work/todo-references/kanda matsuri_89d827d8-1f4b-40fc-aad1-858c1f8fb087.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'kanda-matsuri'
    keyshape = Keyshape.VRECT_L
    # Visible ink extremes: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('kanda', 'matsuri')

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

        # Plan: round medallion and three oriented heart shapes; paired lower strokes.
        self.circle('medallion',24,20,16)
        self.add_line('top-stem',(24,4),(24,11))
        self.add_bezier('heart-top',(24,11),((14,5),(14,15),(24,19)),((34,15),(34,5),(24,11)))
        self.add_bezier('heart-left',(20,23),((8,13),(10,24),(15,25)),((10,33),(21,34),(20,23)))
        self.add_bezier('heart-right',(28,23),((40,13),(38,24),(33,25)),((38,33),(27,34),(28,23)))
        self.add_line('stem-left',(10,28),(15,25))
        self.add_line('stem-right',(38,28),(33,25))
        self.relate('connect','top-stem','medallion')
        self.relate('connect','top-stem','heart-top')
        self.relate('connect','stem-left','heart-left')
        self.relate('connect','stem-right','heart-right')
        self.add_line('tassel-left',(8,38),(12,44))
        self.add_line('tassel-right',(40,38),(36,44))
        self.add_dot('tassel-center',(24,44))
