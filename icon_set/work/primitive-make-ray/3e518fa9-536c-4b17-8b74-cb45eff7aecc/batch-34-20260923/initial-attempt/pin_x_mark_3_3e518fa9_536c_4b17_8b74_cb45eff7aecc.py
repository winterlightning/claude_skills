from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3e518fa9-536c-4b17-8b74-cb45eff7aecc'
SOURCE_PATH='icon_set/work/todo-references/pin x mark 3_3e518fa9-536c-4b17-8b74-cb45eff7aecc.svg'
AUTHOR='gpt-6'
PLAN='Broad rounded pin with a larger circular hole over a wide ground X. Softer base distinguishes it from pin x mark 2.'
CONSTRUCTION_REFERENCES='Lucide map-pin: domed head and hole.'
OMISSIONS='None; broad X retained.'
KEYSHAPE_INK_BOUNDS=(8, 2, 40, 46)

class Drawing(Solo48):
    icon_id='pin-x-mark-3'
    keyshape=Keyshape.VRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('pin', 'x', 'mark', '3')

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
        self.add_arc('dome',(10,18),(38,18),radius_x=14)
        self.add_bezier('right',(38,18),((38,25),(29,31),(25,33)),((24,34),(24,34),(23,33)))
        self.add_bezier('left',(23,33),((19,31),(10,25),(10,18)))
        self.add_contour('pin','dome','right','left',closed=True)
        self.circle('hole',24,18,5)
        self.cross('ground-x',24,40,9,4)
