'Standard Pokeball Capture Tool. Plan and review: Circular capture ball, split equator and large central button ring retained. The smaller nested button ring is omitted. Keyshape CIRCLE centerline envelope radius20 about(24,24). Chosen to fit the complete subject silhouette. Reference: No useful Lucide character match; original silhouette and identifying features guide construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2bbe9f66-2aba-50f6-aae0-403eb84bf49a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-08/pokemon_2bbe9f66-2aba-50f6-aae0-403eb84bf49a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pokeball'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('pokeball',)

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

        path('ball',(4,24),[((44,24),20,20,True),((4,24),20,20,True)],True)
        circle('button',24,24,7)
        for name,a,b in [('left',(4,24),(17,24)),('right',(31,24),(44,24))]:
         self.add_line(name,a,b);self.relate('connect',name,'ball');self.relate('connect',name,'button')
