from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='5ba1d1e1-9400-4baf-a55c-e0c11aabf158'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_31/plane trip person_5ba1d1e1-9400-4baf-a55c-e0c11aabf158.svg'
AUTHOR='gpt-6'
PLAN='Walking traveler carrying a rectangular bag, with a small aircraft upper right. Head follows upper torso axis.'
CONSTRUCTION_REFERENCES='Shared human-reference.md/full_body_ref.png: circular head and coherent limbs; Lucide plane: directional wing branches.'
OMISSIONS='Outlined limbs reduced to the shared stick-figure vocabulary. Bag and aircraft retained.'
KEYSHAPE_INK_BOUNDS=(6, 2, 42, 46)

class Drawing(Solo48):
    icon_id='plane-trip-person'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('plane', 'trip', 'person')

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
        # Shared human reference: upright torso and outlined circular head, exact 4-unit ink gap.
        self.circle('head',22,9,3)
        self.add_line('torso',(22,20),(22,32))
        self.add_line('arm-right',(22,20),(28,26));self.relate('connect','torso','arm-right')
        self.add_line('arm-left',(22,20),(14,28));self.relate('connect','torso','arm-left');self.relate('connect','arm-left','arm-right')
        self.box('bag',6,26,8,10,2);self.relate('connect','bag','arm-left')
        self.add_polyline('legs',(22,42),(22,32),(34,42));self.relate('connect','torso','legs')
        self.mark_human_figure('traveler',head='head',torso='torso',torso_junction='start')
        self.add_polyline('plane-spine',(38,6),(38,8),(38,18))
        self.add_polyline('wings',(34,10),(38,8),(42,10));self.relate('connect','plane-spine','wings')
        self.add_polyline('tail',(36,20),(38,18),(40,20));self.relate('connect','plane-spine','tail')
