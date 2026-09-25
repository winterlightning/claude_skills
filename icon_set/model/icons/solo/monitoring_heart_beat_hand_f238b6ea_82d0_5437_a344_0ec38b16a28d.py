from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f238b6ea-82d0-5437-a344-0ec38b16a28d'
SOURCE_PATH = 'icon_set/work/todo-references/monitoring heart beat hand_f238b6ea-82d0-5437-a344-0ec38b16a28d.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'A hand holding a heart containing a heartbeat trace.'
CONSTRUCTION_PLAN = 'Two heart lobes and a pulse retain the medical symbol; hand contour occludes the lower-right heart through shared endpoints. Human-reference guide consulted for coherent rounded anatomy.'
KEYSHAPE_CENTERLINE_BOUNDS = [6, 6, 42, 42]

def circle(icon,name,cx,cy,r):
    icon.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
    icon.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)

def rounded_rect(icon,name,left,top,right,bottom,r=4,bottom_split=None):
    points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom)]
    if bottom_split is not None:points.append((bottom_split,bottom))
    points += [(left+r,bottom),(left,bottom-r),(left,top+r)]
    members=[]
    for i,start in enumerate(points):
        end=points[(i+1)%len(points)];n=f'{name}-{i}';members.append(n)
        if start[0]!=end[0] and start[1]!=end[1]:icon.add_arc(n,start,end,radius_x=r)
        else:icon.add_line(n,start,end)
    icon.add_contour(name,*members,closed=True)

def monitor(icon):
    # Shared screen, central attachment and two base halves, drawn on SOLO48.
    rounded_rect(icon,'screen',6,6,42,34,bottom_split=24)
    icon.add_line('stand',(24,34),(24,42))
    icon.add_line('base-left',(16,42),(24,42))
    icon.add_line('base-right',(24,42),(32,42))
    icon.relate('connect','screen','stand')
    icon.relate('connect','stand','base-left','base-right')

class Drawing(Solo48):
    icon_id = 'monitoring-heart-beat-hand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ()
    keywords = ('monitoring', 'heart', 'beat', 'hand')

    def build(self):
        self.add_line('heart-lower-1',(31, 27),(22, 34))
        self.add_line('heart-lower-2',(22, 34),(8, 20))
        self.add_bezier('heart-left',(8,20),((6,18),(6,16),(6,14)),((6,10),(10,6),(14,6)),((18,6),(20,9),(22,11)))
        self.add_bezier('heart-right',(22,11),((26,7),(26,6),(30,6)),((35,6),(38,10),(38,14)),((38,18),(35,21),(32,24)))
        self.add_contour('heart','heart-lower-1','heart-lower-2','heart-left','heart-right')
        self.add_polyline('pulse',(7,18),(13,18),(16,13),(22,24),(27,16),(30,20),(36,20))
        self.add_line('wrist-inner-1',(33, 42),(29, 37))
        self.add_line('wrist-inner-2',(29, 37),(29, 32))
        self.add_line('wrist-inner-3',(29, 32),(25, 28))
        self.add_bezier('thumb',(25,28),((21,24),(25,21),(28,24)))
        self.add_line('finger-1',(28, 24),(31, 27))
        self.add_line('finger-2',(31, 27),(35, 31))
        self.add_contour('hand-inner','wrist-inner-1','wrist-inner-2','wrist-inner-3','thumb','finger-1','finger-2')
        self.add_bezier('hand-outer',(32,24),((38,28),(39,28),(39,34)),((39,38),(40,39),(42,42)))
        self.relate('connect','heart','hand-inner')
        self.relate('connect','heart','hand-outer')
