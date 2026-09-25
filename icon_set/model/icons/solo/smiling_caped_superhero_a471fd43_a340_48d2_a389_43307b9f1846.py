'Smiling Superhero Man. Plan and review: Circular head and curved shoulders surround an angular chest panel identifying the superhero costume. Hair and facial smile were omitted to make the costume panel readable. Head radius8 at(24,12); shoulder apex(24,24): head/body centerline separation4 and visible gap0. Keyshape VRECT_L centerline envelope (8,4)-(40,44). Chosen to fit the complete subject silhouette. Reference: Human references: icon_set/references/human_ref/user.svg and full_body_ref.png. Circular head and curved shoulders surround an angular chest panel identifying the superhero costume. Hair and facial smile were omitted to make the costume panel readable. Head radius8 at(24,12); shoulder apex(24,24): head/body centerline separation4 and visible gap0.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a471fd43-a340-48d2-a389-43307b9f1846'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-11/superman_a471fd43-a340-48d2-a389-43307b9f1846.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smiling-caped-superhero'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('smiling', 'caped', 'superhero')

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

        circle('head',24,12,8)
        path('body',(8,44),[(8,40),((24,24),16,16,True),((40,40),16,16,True),(40,44)])
        self.relate('connect','head','body')
        path('chest',(24,33),[(31,38),(24,43),(17,38),(24,33)],True)
