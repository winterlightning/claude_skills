from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='72680b72-4559-4142-b1cf-d15da88d0fa2'
SOURCE_PATH='icon_set/work/todo-references/picture_72680b72-4559-4142-b1cf-d15da88d0fa2.svg'
AUTHOR='gpt-6'
PLAN='Landscape picture with sun upper right and overlapping angular mountain ridges. Preserve diagonal asymmetry.'
CONSTRUCTION_REFERENCES='Lucide image: geometric peaks and framed sun.'
OMISSIONS='Sun hole reduces to a tiny native-size disc; frame uses rounded joins.'
KEYSHAPE_INK_BOUNDS=(4, 4, 44, 44)

class Drawing(Solo48):
    icon_id='picture'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('picture',)

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self,name,x,y,w,h,r=3):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8];part=f'{name}-{i}';members.append(part)
            if i%2:self.add_arc(part,a,b,radius_x=r)
            else:self.add_line(part,a,b)
        self.add_contour(name,*members,closed=True)

    def cross(self,name,cx,cy,rx,ry,diagonal=True):
        if diagonal:
            self.add_polyline(name+'-a',(cx-rx,cy-ry),(cx,cy),(cx+rx,cy+ry))
            self.add_polyline(name+'-b',(cx+rx,cy-ry),(cx,cy),(cx-rx,cy+ry))
        else:
            self.add_polyline(name+'-a',(cx-rx,cy),(cx,cy),(cx+rx,cy))
            self.add_polyline(name+'-b',(cx,cy-ry),(cx,cy),(cx,cy+ry))
        self.relate('connect',name+'-a',name+'-b')

    def pin(self,name,cx,top,r,tip,style='broad'):
        cy=top+r
        self.add_arc(name+'-dome',(cx-r,cy),(cx+r,cy),radius_x=r)
        if style=='narrow':
            self.add_bezier(name+'-right',(cx+r,cy),((cx+r,cy+8),(cx+r-4,cy+11),(cx+7,tip-9)),((cx+3,tip-6),(cx+2,tip-4),(cx,tip)))
            self.add_bezier(name+'-left',(cx,tip),((cx-2,tip-4),(cx-3,tip-6),(cx-7,tip-9)),((cx-r+4,cy+11),(cx-r,cy+8),(cx-r,cy)))
        else:
            self.add_bezier(name+'-right',(cx+r,cy),((cx+r,cy+7),(cx+7,tip-6),(cx,tip)))
            self.add_bezier(name+'-left',(cx,tip),((cx-7,tip-6),(cx-r,cy+7),(cx-r,cy)))
        self.add_contour(name,name+'-dome',name+'-right',name+'-left',closed=True)

    def aircraft(self):
        # Intentionally oblique silhouette: shared wing roots and tapered tail.
        self.add_polyline('plane',(8,12),(12,11),(17,13),(23,11),(16,6),(20,4),(29,8),(35,6))
        self.add_arc('nose',(35,6),(39,10),radius_x=3)
        self.add_polyline('plane-bottom',(39,10),(31,13),(27,20),(23,20),(25,15),(13,18),(8,12))
        self.add_contour('aircraft','plane-1','plane-2','plane-3','plane-4','plane-5','plane-6','plane-7','nose','plane-bottom-1','plane-bottom-2','plane-bottom-3','plane-bottom-4','plane-bottom-5','plane-bottom-6',closed=True)

    def build(self):
        self.add_polyline('frame',(6,6),(42,6),(42,36),(42,42),(6,42),(6,29),closed=True)
        self.add_polyline('back-mountain',(6,29),(18,17),(28,27));self.relate('connect','frame','back-mountain')
        self.add_polyline('front-mountain',(22,33),(28,27),(31,24),(42,36));self.relate('connect','front-mountain','back-mountain');self.relate('connect','front-mountain','frame')
        self.circle('sun',32,16,2)
