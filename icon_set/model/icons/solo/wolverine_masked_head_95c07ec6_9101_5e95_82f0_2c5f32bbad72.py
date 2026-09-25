'Wolverine Superhero Mask. Plan and review: Tall mirrored mask points converge over an angular exposed lower face. Tiny slanted eyes and mouth omitted; mask and jaw separation remain readable. Keyshape VRECT_L centerline envelope (8,4)-(40,44). Chosen to fit the complete subject silhouette. Reference: No useful Lucide character match; original silhouette and identifying features guide construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95c07ec6-9101-5e95-82f0-2c5f32bbad72'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-13/wolverine_95c07ec6-9101-5e95-82f0-2c5f32bbad72.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wolverine-masked-head'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('wolverine', 'masked', 'head')

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

        path('mask',(8,4),[(20,18),(24,28),(28,18),(40,4),(40,24),(36,36),(24,44),(12,36),(8,24),(8,4)],True)
        path('jaw-top',(8,24),[(24,32),(40,24)]);self.relate('connect','jaw-top','mask')
