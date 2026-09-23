"""An oxygen cylinder with a valve and round timer gauge.
Symbol plan: Rounded bottle with attached neck and valve; a right-side gauge attaches by a hose. Ink extremes (4,4)-(44,44).
Construction: No exact Lucide match inspected; rounded enclosure and circular gauge use shared geometric construction.
Human construction: Not applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '12af7a01-21fd-509d-9eae-c7bfcfdaedd2'
SOURCE_PATH = 'icon_set/work/todo-references/oxygen tank timer_12af7a01-21fd-509d-9eae-c7bfcfdaedd2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'oxygen-tank-timer'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('oxygen', 'tank', 'timer')

    def build(self):
        self.box('tank',6,20,22,42,4)
        self.add_polyline('neck',(10,20),(10,12),(14,12),(18,12),(18,20))
        self.relate('connect','tank','neck')
        self.add_line('valve',(14,6),(14,12))
        self.relate('connect','valve','neck')
        self.add_polyline('valve-handle',(10,6),(14,6),(18,6))
        self.relate('connect','valve','valve-handle')
        self.add_line('hose',(18,16),(26,16))
        self.relate('connect','hose','neck')
        self.circle('gauge',34,16,8)
        self.relate('connect','hose','gauge')
        self.add_polyline('gauge-hands',(34,12),(34,16),(38,16))

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

