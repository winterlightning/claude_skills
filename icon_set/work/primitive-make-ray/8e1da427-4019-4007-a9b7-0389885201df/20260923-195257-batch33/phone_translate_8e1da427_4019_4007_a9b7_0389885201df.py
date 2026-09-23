from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='8e1da427-4019-4007-a9b7-0389885201df'
SOURCE_PATH='icon_set/work/todo-references/phone translate_8e1da427-4019-4007-a9b7-0389885201df.svg'
AUTHOR='gpt-6'
PLAN='A phone with Latin A and Chinese translation strokes across its screen.'
OMISSIONS='Glyphs reduced to their essential strokes, preserving the bilingual layout.'
LUCIDE_REFERENCE=None
HUMAN_REFERENCE=None
class Drawing(Solo48):
    icon_id='phone-translate'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/media'
    aliases=()
    keywords=('phone', 'translate')

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
        # A phone with Latin A and Chinese translation strokes across its screen.

        self.add_polyline('phone-top',(12,8),(12,4),(36,4),(36,8))
        self.add_polyline('phone-bottom',(12,40),(12,44),(36,44),(36,40))
        self.add_polyline('a',(8,33),(13,18),(18,33));self.add_line('a-bar',(10,27),(16,27));self.relate('connect','a','a-bar')
        self.add_line('wen-top',(26,20),(40,20));self.add_line('wen-stem',(33,16),(33,20));self.relate('connect','wen-top','wen-stem')
        self.add_polyline('wen-left',(28,20),(30,25),(32,27),(34,29),(40,32))
        self.add_polyline('wen-right',(38,20),(34,25),(32,27),(30,29),(26,32));self.relate('connect','wen-left','wen-right')
        self.relate('connect','wen-left','wen-top');self.relate('connect','wen-right','wen-top')

