'A left-facing whale emits two curved water spouts above its rounded back; lobed tail rises at right and flipper below. HRECT_L spans4,8..44,40. Source supplies the whale, lobed tail and paired spouts. No local Lucide whale match; use coherent contour construction. Omit mouth seam to retain eye clearance. Spouts are mirrored semicircles joined to one stem.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '231dc062-282f-4d6f-ad1c-b148bd0de9d8'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_07/blowhole_231dc062-282f-4d6f-ad1c-b148bd0de9d8.svg'
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = 'whale-with-two-arcing-spouts'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ['Whale with Two Arcing Spouts']
    keywords = ['whale', 'spout', 'water', 'marine', 'tail', 'flipper', 'animal']
    def build(self):
        def path(name,start,steps,closed=False):
            point=start; members=[]
            for i,step in enumerate(steps):
                pid=f'{name}-{i}'
                if len(step)==2:
                    self.add_line(pid,point,step);point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(pid,point,end,radius_x=rx,radius_y=ry,sweep=sweep);point=end
                members.append(pid)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[((x+r,y),r,r,True),((x,y+r),r,r,True),((x-r,y),r,r,True),((x,y-r),r,r,True)],True)
        self.add_bezier('back',(4,28),((4,20),(12,20),(20,20)),((26,20),(28,24),(32,28)))
        self.add_bezier('upper-tail',(32,28),((35,22),(39,22),(44,22)))
        self.add_bezier('tail-notch',(44,22),((44,27),(42,29),(39,30)))
        self.add_bezier('lower-tail',(39,30),((42,31),(44,34),(44,38)),((38,38),(35,36),(32,32)))
        self.add_bezier('belly',(32,32),((30,37),(26,38),(22,38)))
        self.add_line('flipper-top',(22,38),(22,40))
        self.add_line('flipper-bottom',(22,40),(18,40))
        self.add_line('flipper-front',(18,40),(14,36))
        self.add_bezier('head-bottom',(14,36),((6,36),(4,33),(4,28)))
        self.add_contour('body','back','upper-tail','tail-notch','lower-tail','belly','flipper-top','flipper-bottom','flipper-front','head-bottom',closed=True)
        self.add_dot('eye',(19,29))
        path('spout-left',(8,14),[((20,14),6,6,True)])
        path('spout-right',(20,14),[((32,14),6,6,True)])
        self.add_line('spout-stem',(20,14),(20,20))
        self.relate('connect','spout-left','spout-right')
        self.relate('connect','spout-left','spout-stem')
        self.relate('connect','spout-right','spout-stem')
        self.relate('connect','spout-stem','body')
