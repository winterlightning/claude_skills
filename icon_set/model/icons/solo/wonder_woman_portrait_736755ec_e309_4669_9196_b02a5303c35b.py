'Wonder Woman Superhero Portrait. Plan and review: Long hair, pointed tiara-shaped forehead and circular lower jaw above broad curved shoulders retained. Facial dots, smile and costume neckline omitted. Circular jaw radius6 centered(24,20) ends at26; shoulder apex30 gives zero visible gap. Keyshape VRECT_L centerline envelope (8,4)-(40,44). Chosen to fit the complete subject silhouette. Reference: Human references: icon_set/references/human_ref/user.svg and full_body_ref.png. Long hair, pointed tiara-shaped forehead and circular lower jaw above broad curved shoulders retained. Facial dots, smile and costume neckline omitted. Circular jaw radius6 centered(24,20) ends at26; shoulder apex30 gives zero visible gap.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '736755ec-e309-4669-9196-b02a5303c35b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-13/wonder woman_736755ec-e309-4669-9196-b02a5303c35b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wonder-woman-portrait'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('wonder', 'woman', 'portrait')

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

        path('hair',(8,44),[(8,20),((24,4),16,16,True),((40,20),16,16,True),(40,44)])
        path('face',(18,20),[(18,13),(24,17),(30,13),(30,20),((18,20),6,6,True)],True)
        path('body',(8,44),[((24,30),16,14,True),((40,44),16,14,True)])
        self.relate('connect','face','body');self.relate('connect','hair','body')
