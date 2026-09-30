'Smiling Boy with Cap. Plan and review: Domed cap, brim and broad smiling lower face remain recognizable. Tiny eyes and ears were omitted because the band between brim and smile cannot hold them with required clearance. Keyshape HRECT_L centerline envelope (4,8)-(44,40). Chosen to fit the complete subject silhouette. Reference: human_ref/user.svg rounded head and source domed cap.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f3212e0-4927-44c5-94cd-5399ae17ccee'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-07/mario_2f3212e0-4927-44c5-94cd-5399ae17ccee.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smiling-boy-in-cap'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('smiling', 'boy', 'in', 'cap')

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

        curve('cap',(4,20),((4,13),(13,8),(24,8)),((35,8),(44,13),(44,20)))
        self.add_line('brim',(4,20),(44,20));self.relate('connect','cap','brim')
        self.add_arc('face',(40,20),(8,20),radius_x=16,radius_y=20,sweep=True)
        self.relate('connect','face','brim')
        
        curve('smile',(19,28),((21,32),(27,32),(29,28)))
