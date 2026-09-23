"""A camp flame above a six-cell brick base.
Symbol plan: One flame contour sits over a three-column, two-row base. Ink extremes (6,2)-(42,46).
Construction: flame: coherent outer flame with one inward lick, rather than nested flames.
Human construction: Not applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5a6bc318-1415-407d-8cee-66dc95d8d15f'
SOURCE_PATH = 'icon_set/work/todo-references/outdoors fire camp_5a6bc318-1415-407d-8cee-66dc95d8d15f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'outdoors-fire-camp'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('outdoors', 'fire', 'camp')

    def build(self):
        self.add_bezier('flame',(24,4),((30,8),(34,20),(24,20)),((15,20),(16,15),(18,11)),((21,17),(26,15),(24,4)))
        self.add_contour('flame-outline','flame',closed=True)
        self.add_polyline('brick-frame',(8,28),(18,28),(30,28),(40,28),(40,36),(40,44),(30,44),(18,44),(8,44),(8,36),closed=True)
        for i,x in enumerate((18,30)):
            self.add_line(f'vertical-{i}-top',(x,28),(x,36))
            self.add_line(f'vertical-{i}-bottom',(x,36),(x,44))
            self.relate('connect',f'vertical-{i}-top',f'vertical-{i}-bottom')
            for n in ('top','bottom'):self.relate('connect',f'vertical-{i}-{n}','brick-frame')
        for i,(a,b) in enumerate(zip((8,18,30),(18,30,40))):
            self.add_line(f'row-{i}',(a,36),(b,36))
            if i in (0,2):self.relate('connect',f'row-{i}','brick-frame')
            for j,x in enumerate((18,30)):
                if x in (a,b):
                    for n in ('top','bottom'):self.relate('connect',f'row-{i}',f'vertical-{j}-{n}')
            if i:self.relate('connect',f'row-{i}',f'row-{i-1}')

    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-upper',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-lower',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-upper',name+'-lower',closed=True)

    def box(self, name, x, y, right, bottom, r=4):
        pts=[(x+r,y),(right-r,y),(right,y+r),(right,bottom-r),(right-r,bottom),(x+r,bottom),(x,bottom-r),(x,y+r)]
        members=[]
        for i in range(8):
            a,b=pts[i],pts[(i+1)%8]
            if a==b: continue
            n=f'{name}-{i}'
            if i%2: self.add_arc(n,a,b,radius_x=r)
            else: self.add_line(n,a,b)
            members.append(n)
        self.add_contour(name,*members,closed=True)

    def parking_letter(self,name,x,top,bottom,width=10,bowl_height=14):
        # Vertical stem split at the bowl attachment; one smooth half-ellipse owns its loop.
        mid=top+bowl_height; shoulder=x+3
        self.add_line(name+'-stem-upper',(x,mid),(x,top))
        self.add_line(name+'-top',(x,top),(shoulder,top))
        self.add_arc(name+'-bowl',(shoulder,top),(shoulder,mid),radius_x=width-3,radius_y=bowl_height//2)
        self.add_line(name+'-return',(shoulder,mid),(x,mid))
        self.add_contour(name+'-loop',name+'-stem-upper',name+'-top',name+'-bowl',name+'-return',closed=True)
        self.add_line(name+'-stem-lower',(x,mid),(x,bottom))
        self.relate('connect',name+'-loop',name+'-stem-lower')

    def plus(self,x,y,r=2):
        names=[]
        for i,p in enumerate(((x-r,y),(x+r,y),(x,y-4),(x,y+4))):
            n=f'plus-{i}';self.add_line(n,p,(x,y))
            for prev in names:self.relate('connect',n,prev)
            names.append(n)

