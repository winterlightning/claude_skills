'Video Game Console and Controller. Plan and review: Console and foreground controller retained as a natural hardware pair. Tiny controller buttons and console control arch omitted to keep grip openings clear. Keyshape SQUARE centerline envelope (6,6)-(42,42). Chosen to fit the complete subject silhouette. Reference: Lucide gamepad-2 and hard-drive originals and atomic-debug: controller grips and hardware outline.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '28ff4455-b8a9-4b98-8095-3709c8f6d9ba'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-08/playstation four controller_28ff4455-b8a9-4b98-8095-3709c8f6d9ba.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'gaming-console-with-foreground-controller'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('gaming', 'console', 'with', 'foreground', 'controller')

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

        path('console',(6,26),[(6,6),(22,6),(34,10),(34,18)])
        self.add_line('spine',(14,6),(14,17));self.relate('connect','console','spine')
        curve('gamepad',(16,42),((11,42),(10,39),(12,34)),((13,29),(14,27),(18,27)),((24,27),(30,27),(34,27)),((38,27),(40,29),(41,34)),((43,39),(42,42),(38,42)),((35,42),(33,36),(30,36)),((27,36),(25,36),(23,36)),((20,36),(19,42),(16,42)))
        
