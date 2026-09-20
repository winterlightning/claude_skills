'Smiling Boy Face. Plan and review: Rounded smiling head with a broad swept fringe. The fringe is balanced about the face axis; ears and eyebrows are omitted to preserve facial spacing. Keyshape SQUARE centerline envelope (6,6)-(42,42). Chosen to fit the complete subject silhouette. Reference: human_ref/user.svg head vocabulary; source fringe; no specific Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '41efa512-77c6-49b9-9e5d-7406a2d96367'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-02/cute male boy charactor_41efa512-77c6-49b9-9e5d-7406a2d96367.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smiling-boy-face-reference-41efa512'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('smiling', 'boy', 'face', 'reference', '41efa512')

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

        box('head',6,6,42,42,12)
        curve('fringe',(6,17),((14,17),(18,16),(24,14)),((30,16),(34,17),(42,17)))
        self.relate('connect','head','fringe')
        for x in (18,30):self.add_dot('eye-'+str(x),(x,25))
        curve('smile',(22,33),((23,34),(25,34),(26,33)))
