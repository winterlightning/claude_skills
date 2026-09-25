'Winged Pegasus Head. Plan and review: Left-facing horse muzzle, pointed ear and swept wing retained. Eye, mane and fine feather tiers omitted. Wing junction shares a real contour endpoint. Keyshape HRECT_L centerline envelope (4,8)-(44,40). Chosen to fit the complete subject silhouette. Reference: No useful Lucide character match; original silhouette and identifying features guide construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cda51915-716e-48bb-b297-9522c520ad53'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-04/fantasy pegasus_cda51915-716e-48bb-b297-9522c520ad53.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pegasus-head-with-wing'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('pegasus', 'head', 'with', 'wing')

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

        path('head',(4,22),[(14,14),(14,8),(22,12)])
        curve('crown',(22,12),((29,12),(32,16),(30,25)));self.relate('connect','head','crown')
        curve('muzzle',(4,22),((4,30),(10,30),(16,27)));self.relate('connect','head','muzzle')
        curve('neck',(16,27),((12,33),(14,36),(14,40)));self.relate('connect','muzzle','neck')
        curve('wing',(22,40),((27,34),(18,29),(30,25)),((36,23),(40,21),(44,18)),((44,33),(36,40),(22,40)))
        self.relate('connect','crown','wing')
