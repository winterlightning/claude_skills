'A domed empty birdcage with top knob, center bar and perch on a rectangular base. VRECT_L gives the tall cage room. Mirror dome around24; shared center bar nodes and base attachment endpoints. Lucide bell contributes arched shoulders; source contributes cage base and intrinsic perch. Knob simplified to small round loop.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '68164997-d185-4b80-87f8-d9463fb372a8'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/bird cage empty_68164997-d185-4b80-87f8-d9463fb372a8.svg'
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = 'domed-birdcage-with-a-central-perch'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ['Domed Birdcage with a Central Perch']
    keywords = ['birdcage', 'cage', 'dome', 'perch', 'knob', 'base', 'pet']
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
        circle('knob',24,6,2)
        self.add_line('knob-stem',(24,8),(24,14))
        path('dome',(10,36),[(10,28),((24,14),14,14,True),((38,28),14,14,True),(38,36)])
        self.add_polyline('base',(8,36),(10,36),(24,36),(38,36),(40,36),(40,44),(8,44),closed=True)
        self.add_polyline('bar',(24,14),(24,26),(24,36))
        self.add_polyline('perch',(18,26),(24,26),(30,26))
        for a,b in [('knob','knob-stem'),('knob-stem','dome'),('knob-stem','bar'),('dome','bar'),('dome','base'),('bar','base'),('bar','perch')]:
            self.relate('connect',a,b)
