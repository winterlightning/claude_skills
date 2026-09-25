'Smiling Doraemon Character Face. Plan and review: Circular robot-cat face retains eyes, a central nose, nose-to-mouth stroke and cheek whisker dots. Eye surrounds, inner face boundary and extra whiskers are omitted. Keyshape CIRCLE centerline envelope radius20 about(24,24). Chosen to fit the complete subject silhouette. Reference: No useful Lucide character match; original silhouette and identifying features guide construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6ecc644a-3a00-4527-b255-62f6624f6734'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-09/robot cat blue doraemon_6ecc644a-3a00-4527-b255-62f6624f6734.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smiling-doraemon-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('smiling', 'doraemon', 'face')

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

        circle('head',24,24,20)
        self.add_dot('eye-l',(18,14));self.add_dot('eye-r',(30,14))
        circle('nose',24,23,2)
        self.add_line('philtrum',(24,25),(24,35));self.relate('connect','nose','philtrum')
        curve('smile',(16,31),((18,35),(21,35),(24,35)),((27,35),(30,35),(32,31)))
        self.relate('connect','philtrum','smile')
        self.add_dot('whisker-l',(13,23));self.add_dot('whisker-r',(35,23))
