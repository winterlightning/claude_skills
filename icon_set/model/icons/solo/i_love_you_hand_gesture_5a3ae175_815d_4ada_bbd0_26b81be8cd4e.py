'I Love You Hand Gesture. Plan and review: Extended little/index fingers and diagonal thumb retain the I-love-you hand gesture. Two folded fingers are reduced to one open knuckle crease; rounded fingertips follow the human and Lucide hand references. Keyshape VRECT_L centerline envelope (8,4)-(40,44). Chosen to fit the complete subject silhouette. Reference: human_ref/full_body_ref.png minimal anatomy; Lucide hand original and atomic-debug round fingertips and coherent palm.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5a3ae175-815d-4ada-bbd0-26b81be8cd4e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/wayfinding/sign language love_5a3ae175-815d-4ada-bbd0-26b81be8cd4e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'i-love-you-hand-gesture'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('i', 'love', 'you', 'hand', 'gesture')

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

        path('hand',(8,28),[(8,16),((16,16),4,4,True),(16,24),(24,24),(24,8),((32,8),4,4,True),(32,28),(40,22),(40,30),((26,44),14,14,True),(22,44),((8,30),14,14,True),(8,28)],True)
        self.add_line('knuckle',(16,24),(16,32));self.relate('connect','hand','knuckle')
