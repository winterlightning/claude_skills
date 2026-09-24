from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='102607c1-25ef-426c-be86-bf3e263e4a81'
SOURCE_PATH='icon_set/work/todo-references/plane trip cocktail service_102607c1-25ef-426c-be86-bf3e263e4a81.svg'
AUTHOR='gpt-6'
PLAN='Oblique airplane above a divider, cocktail bowl, stem and citrus garnish below. All service elements remain together.'
CONSTRUCTION_REFERENCES='Lucide plane: coherent wing contour; martini: stem and foot construction, while preserving source’s round bowl.'
OMISSIONS='Minor aircraft edge rounding simplified; garnish retained.'
KEYSHAPE_INK_BOUNDS=(6, 2, 42, 46)

class Drawing(Solo48):
    icon_id='plane-trip-cocktail-service'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('plane', 'trip', 'cocktail', 'service')

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
        # Aircraft is a single outline using explicit continuous segments.
        self.add_polyline('aircraft',(8,12),(12,11),(17,13),(23,11),(16,6),(20,4),(29,8),(36,6),(40,8),(39,11),(31,13),(27,20),(23,20),(25,15),(13,18),closed=True)
        self.add_line('divider',(8,26),(40,26))
        self.add_arc('bowl',(15,32),(29,32),radius_x=7,radius_y=6,sweep=False)
        self.add_line('rim',(15,32),(29,32));self.relate('connect','bowl','rim')
        self.add_line('stem',(22,38),(22,44));self.relate('connect','bowl','stem')
        self.add_polyline('foot',(18,44),(22,44),(26,44));self.relate('connect','stem','foot')
        self.add_arc('citrus',(29,28),(29,34),radius_x=3)

KEYSHAPE_REASON='The upright complete composition uses centerline extremes (8,4)–(40,44).'
