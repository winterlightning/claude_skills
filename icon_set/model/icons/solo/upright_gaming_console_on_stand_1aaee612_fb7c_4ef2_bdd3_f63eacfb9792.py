'Vertical Video Game Console. Plan and review: Upright sloped console, left spine and wide stand retained. Stand supports share the case bottom and do not duplicate it. Keyshape VRECT_L centerline envelope (8,4)-(40,44). Chosen to fit the complete subject silhouette. Reference: Lucide hard-drive original and atomic-debug: sparse hardware silhouette and joined case edges.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1aaee612-fb7c-4ef2-bdd3-f63eacfb9792'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-08/playstation four_1aaee612-fb7c-4ef2-bdd3-f63eacfb9792.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upright-gaming-console-on-stand'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('upright', 'gaming', 'console', 'on', 'stand')

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

        path('case',(12,4),[(24,4),(36,10),(36,34),(12,34),(12,4)],True)
        self.add_line('spine',(20,4),(20,34));self.relate('connect','case','spine')
        path('stand',(8,44),[(16,34)]);self.relate('connect','case','stand');path('stand-right',(32,34),[(40,44),(8,44)]);self.relate('connect','case','stand-right');self.relate('connect','stand','stand-right')
