'Vampire Character with Bow Tie. Plan and review: UNRESOLVED visual fidelity: the existing UUID-matched vampire draft was continued in place, replacing boxy shoulders with the current curved avatar construction. Circular face, pointed ears and fangs pass checks, but the requested bow tie is absent. Do not count as completed or reused. Head radius14 at(24,18), jaw bottom32, shoulder top36: zero visible head/body gap. A separate reviewed bow-tie design is still needed. Keyshape VRECT_L centerline envelope (8,4)-(40,44). Chosen to fit the complete subject silhouette. Reference: human_ref/user.svg circular head and curved shoulders; no useful Lucide vampire match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae244bd3-e9a8-521e-a4d6-3d68b8182792'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-04/fantasy vampire_ae244bd3-e9a8-521e-a4d6-3d68b8182792.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'vampire-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'video-games'
    aliases = ()
    keywords = ('vampire', 'bust')

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

        self.add_arc('head-top',(10,18),(38,18),radius_x=14,sweep=True)
        self.add_arc('jaw',(38,18),(10,18),radius_x=14,sweep=True)
        self.add_contour('head','head-top','jaw',closed=True)
        self.add_line('ear-left',(10,18),(8,12));self.add_line('ear-right',(38,18),(40,12))
        self.relate('connect','ear-left','head');self.relate('connect','ear-right','head')
        self.add_polyline('fangs',(20,21),(20,18),(28,18),(28,21))
        path('body',(8,44),[((24,36),16,8,True),((40,44),16,8,True)])
        self.relate('connect','head','body')
