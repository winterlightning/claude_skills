'Disguise Glasses and Mustache.\nPlan and review: Retained paired round glasses, false nose and sweeping moustache. Omitted eyebrows for clearance.\nKeyshape: HRECT_L, exact SOLO48 envelope selected for this subject.\nConstruction reference: No useful Lucide subject match; source render guides construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f7d8ff6b-331d-4056-8f6d-2059de5c8750'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face disguise_f7d8ff6b-331d-4056-8f6d-2059de5c8750.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'disguise-glasses-and-mustache'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('disguise', 'glasses', 'and', 'mustache')

    def build(self):

        def path(name, start, steps, closed=False):
            members=[]; point=start
            for index, step in enumerate(steps):
                member=f"{name}-{index}"
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep); point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def curve(name,start,*segments):
            self.add_bezier(name,start,*segments)

        circle('lens-left',12,16,8);circle('lens-right',36,16,8)
        self.add_line('bridge',(20,16),(28,16));self.relate('connect','bridge','lens-left');self.relate('connect','bridge','lens-right')
        path('nose',(20,16),[(20,27),(28,27),(28,16)]);self.relate('connect','nose','bridge');self.relate('connect','nose','lens-left');self.relate('connect','nose','lens-right')
        curve('moustache',(4,34),((6,38),(10,40),(14,40)),((18,40),(20,38),(24,36)),((28,38),(30,40),(34,40)),((38,40),(42,38),(44,34)))
