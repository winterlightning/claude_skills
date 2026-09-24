from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='373ac967-90cc-46ee-9b78-f2b3cc4a75c9'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_31/plane trip food service_373ac967-90cc-46ee-9b78-f2b3cc4a75c9.svg'
AUTHOR='gpt-6'
PLAN='Oblique airplane above a divider with fork and knife below. Fork owns shared tine spacing; knife keeps its curved blade.'
CONSTRUCTION_REFERENCES='Lucide plane: continuous wing silhouette; source determines utensil shapes.'
OMISSIONS='None; aircraft, separator, fork and knife retained.'
KEYSHAPE_INK_BOUNDS=(6, 2, 42, 46)

class Drawing(Solo48):
    icon_id='plane-trip-food-service'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('plane', 'trip', 'food', 'service')

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

    def build(self):
        # Aircraft shares the cocktail-service construction; fork tines have an eight-unit gap.
        self.add_polyline('aircraft',(8,16),(14,14),(20,12),(26,10),(32,8),(40,8))
        self.add_polyline('wings',(16,4),(26,10),(22,18));self.relate('connect','aircraft','wings')
        self.add_polyline('tail',(10,8),(14,14),(10,18));self.relate('connect','aircraft','tail')
        self.add_line('fork-left',(12,26),(12,30))
        self.add_arc('fork-bl',(12,30),(16,34),radius_x=4,sweep=False)
        self.add_arc('fork-br',(16,34),(20,30),radius_x=4,sweep=False)
        self.add_line('fork-right',(20,30),(20,26))
        self.add_contour('fork','fork-left','fork-bl','fork-br','fork-right')
        self.add_line('fork-stem',(16,34),(16,44));self.relate('connect','fork','fork-stem')
        self.add_polyline('knife-back',(32,44),(32,34),(32,26))
        self.add_arc('blade',(32,26),(40,34),radius_x=8)
        self.add_line('blade-bottom',(40,34),(32,34));self.relate('connect','knife-back','blade');self.relate('connect','blade','blade-bottom');self.relate('connect','knife-back','blade-bottom')
