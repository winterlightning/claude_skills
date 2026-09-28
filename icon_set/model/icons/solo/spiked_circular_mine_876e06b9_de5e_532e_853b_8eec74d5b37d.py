'Spiked Circular Mine. Plan and review: Eight-pointed mine rim and central round plate retained. Center plate is reduced to the existing complete-circle small-hole allowance. Keyshape SQUARE centerline envelope (6,6)-(42,42). Chosen to fit the complete subject silhouette. Reference: No useful Lucide character match; original silhouette and identifying features guide construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '876e06b9-de5e-532e-853b-8eec74d5b37d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-09/roleplay game ability mine_876e06b9-de5e-532e-853b-8eec74d5b37d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'spiked-circular-mine'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('spiked', 'circular', 'mine')

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

        path('rim',(24,6),[(28,14),(36,12),(34,20),(42,24),(34,28),(36,36),(28,34),(24,42),(20,34),(12,36),(14,28),(6,24),(14,20),(12,12),(20,14),(24,6)],True)
        circle('plate',24,24,2)
