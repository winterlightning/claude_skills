'Tanjirou Kamado Character Head. Plan and review: Round lower face, swept/spiked upper hair, paired eyes and angular forehead scar retained. The scar uses one broad angular bend instead of the tiny double lightning turn; hairline curls and slanted brows are omitted. Keyshape SQUARE centerline envelope (6,6)-(42,42). Chosen to fit the complete subject silhouette. Reference: No useful Lucide character match; original silhouette and identifying features guide construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9ef48cbe-cc4f-4534-9267-a5b1a90c74e3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-02/demon slayer kamado tanjirou_9ef48cbe-cc4f-4534-9267-a5b1a90c74e3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tanjirou-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('tanjirou', 'head')

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

        path('head',(6,22),[(10,10),(20,6),(20,8),(30,6),(38,10),(42,22),(42,24),((24,42),18,18,True),((6,24),18,18,True),(6,22)],True)
        path('scar',(22,17),[(27,20),(22,23)])
        self.add_dot('eye-left',(17,31));self.add_dot('eye-right',(31,31))
