'Spotted Power Up Mushroom. Plan and review: Broad spotted cap and eyed stem retained. One central spot replaces the three source spots; short eye strokes meet the cap rim to fit the stem without crowding. Keyshape HRECT_L centerline envelope (4,8)-(44,40). Chosen to fit the complete subject silhouette. Reference: No useful Lucide character match; original silhouette and identifying features guide construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a7841b5e-c25b-5e19-933a-963ef3039f49'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-07/mario mushroom_a7841b5e-c25b-5e19-933a-963ef3039f49.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'spotted-power-up-mushroom'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('spotted', 'power', 'up', 'mushroom')

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

        curve('cap',(4,26),((4,16),(13,8),(24,8)),((35,8),(44,16),(44,26)))
        self.add_line('rim',(4,26),(44,26));self.relate('connect','cap','rim')
        path('stem',(10,26),[(10,34),((16,40),6,6,False),(32,40),((38,34),6,6,False),(38,26)]);self.relate('connect','stem','rim')
        self.add_dot('spot',(24,17))
        for x in (20,28):
         self.add_line('eye-'+str(x),(x,26),(x,30));self.relate('connect','rim','eye-'+str(x))
