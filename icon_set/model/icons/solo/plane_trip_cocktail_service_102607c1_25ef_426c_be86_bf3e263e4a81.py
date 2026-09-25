"""Aircraft above a cocktail glass and citrus garnish.
Plan: VRECT_L preserves the vertical aircraft/service arrangement.
Reduction: Divider omitted; aircraft outline reduced to fuselage, wings and tail strokes; garnish reduced to an open semicircle.
Construction: plane: fuselage/wing/tail hierarchy; martini: bowl, stem and foot with actual joins. Source round bowl retained. Aircraft remains directional.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='102607c1-25ef-426c-be86-bf3e263e4a81'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_31/plane trip cocktail service_102607c1-25ef-426c-be86-bf3e263e4a81.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='plane-trip-cocktail-service'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
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
        # Rising aircraft skeleton: fuselage, long wings and a smaller tail; service below.
        self.add_polyline('aircraft',(8,16),(14,14),(20,12),(26,10),(32,8),(40,8))
        self.add_polyline('wings',(16,4),(26,10),(22,18));self.relate('connect','aircraft','wings')
        self.add_polyline('tail',(10,8),(14,14),(10,18));self.relate('connect','aircraft','tail')
        self.add_arc('bowl-left',(14,26),(23,35),radius_x=9,sweep=False)
        self.add_arc('bowl-right',(23,35),(32,26),radius_x=9,sweep=False)
        self.add_contour('bowl','bowl-left','bowl-right')
        self.add_line('rim',(14,26),(32,26));self.relate('connect','rim','bowl')
        self.add_line('stem',(23,35),(23,44));self.relate('connect','stem','bowl')
        self.add_polyline('foot',(17,44),(23,44),(29,44));self.relate('connect','stem','foot')
        self.add_arc('citrus',(32,26),(40,26),radius_x=4)
        self.relate('connect','citrus','rim');self.relate('connect','citrus','bowl')
