from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='bc216d11-8cf2-4ba4-93cc-9f69078fdc84'
SOURCE_PATH = 'pictographic-primitives/other/play button_bc216d11-8cf2-4ba4-93cc-9f69078fdc84.svg'
AUTHOR='gpt-6'
PLAN='Television play button: antenna pair, rectangular screen, two feet and central play triangle. Symmetry axis x=24.'
CONSTRUCTION_REFERENCES='Lucide tv: paired antenna and screen; circle-play: simple triangular play glyph.'
OMISSIONS='Rounded screen corners reduced to round stroke joins; triangle compressed vertically for the screen.'
KEYSHAPE_INK_BOUNDS=(4, 4, 44, 44)

class Drawing(Solo48):
    icon_id='play-button'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('play', 'button')

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
        self.add_polyline('screen',(8,12),(24,12),(40,12),(40,42),(32,42),(16,42),(8,42),closed=True)
        self.add_polyline('antenna',(15,4),(24,12),(33,4));self.relate('connect','screen','antenna')
        for i,x in enumerate((16,32)):
         self.add_line(f'foot-{i}',(x,42),(x,44));self.relate('connect','screen',f'foot-{i}')
        self.add_polyline('play',(17,20),(31,27),(17,34),closed=True)

KEYSHAPE_REASON='The whole composition is approximately square; the centerline extremes are (6,6)–(42,42).'
