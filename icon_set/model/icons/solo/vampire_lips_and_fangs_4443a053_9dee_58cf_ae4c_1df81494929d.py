'Vampire Fangs and Lips. Plan and review: Parted curved lips and two descending fangs retained. The inner lip duplication is removed; fangs shortened to open the space above the lower lip. Keyshape HRECT_M centerline envelope (4,10)-(44,38). Chosen to fit the complete subject silhouette. Reference: No useful Lucide character match; original silhouette and identifying features guide construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4443a053-9dee-58cf-ae4c-1df81494929d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-04/fantasy vampire lips mouth_4443a053-9dee-58cf-ae4c-1df81494929d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'vampire-lips-and-fangs'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('vampire', 'lips', 'and', 'fangs')

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

        curve('upper',(4,22),((12,16),(14,10),(20,10)),((22,10),(24,14),(24,14)),((24,14),(26,10),(28,10)),((34,10),(36,16),(44,22)))
        curve('lower',(4,22),((10,32),(16,38),(24,38)),((32,38),(38,32),(44,22)))
        self.relate('connect','upper','lower')
        path('mouth',(4,22),[(14,22),(18,27),(20,22),(28,22),(30,27),(34,22),(44,22)])
        self.relate('connect','mouth','upper');self.relate('connect','mouth','lower')
