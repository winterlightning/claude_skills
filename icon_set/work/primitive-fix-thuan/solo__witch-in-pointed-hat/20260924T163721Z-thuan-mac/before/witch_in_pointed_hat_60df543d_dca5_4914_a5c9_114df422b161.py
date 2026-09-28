'Witch Face with Pointed Hat. Plan and review: Left-facing projecting nose, bent pointed hat and trailing hair retained. Small eye and smile omitted; long smooth lower profile replaces small chin details. Keyshape SQUARE centerline envelope (6,6)-(42,42). Chosen to fit the complete subject silhouette. Reference: No useful Lucide character match; original silhouette and identifying features guide construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '60df543d-dca5-4914-a5c9-114df422b161'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-13/witch_60df543d-dca5-4914-a5c9-114df422b161.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'witch-in-pointed-hat'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('witch', 'in', 'pointed', 'hat')

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

        path('hat',(6,20),[(22,6),(36,6),(42,18),(32,12),(28,20),(6,20)])
        path('profile',(18,20),[(18,28),(6,32),(16,32),(16,34),((24,42),8,8,False),(28,42)])
        self.relate('connect','hat','profile')
        curve('hair',(32,20),((30,32),(40,30),(40,42)))
        self.relate('connect','hat','hair')
