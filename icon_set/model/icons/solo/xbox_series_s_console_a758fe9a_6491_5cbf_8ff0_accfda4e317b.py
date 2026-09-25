'Xbox Series S Gaming Console. Plan and review: Three-quarter upright console with circular front vent retained. Narrow side controls omitted; vent reduced to a complete circular mark using the existing small-circle allowance. Keyshape VRECT_L centerline envelope (8,4)-(40,44). Chosen to fit the complete subject silhouette. Reference: Lucide hard-drive original and atomic-debug: joined perspective shell; circular vent from source.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a758fe9a-6491-5cbf-8ff0-accfda4e317b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-13/xbox series s_a758fe9a-6491-5cbf-8ff0-accfda4e317b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'xbox-series-s-console'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('xbox', 'series', 's', 'console')

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

        path('case',(8,10),[(20,4),(40,12),(40,38),(28,44),(8,36),(8,10)],True)
        path('seams',(8,10),[(28,18),(40,12)]);self.relate('connect','case','seams')
        self.add_line('side',(28,18),(28,44));self.relate('connect','case','side');self.relate('connect','side','seams')
        circle('vent',18,27,2)
