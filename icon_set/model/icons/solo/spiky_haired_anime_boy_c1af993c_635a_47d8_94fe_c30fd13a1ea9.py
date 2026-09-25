'Spiky Hair Anime Boy Face. Plan and review: Broad spiky hair silhouette and jagged fringe surround a smiling lower face. Narrow secondary spikes, brows and eyes are omitted; wider hair bands preserve clear openings. Keyshape SQUARE centerline envelope (6,6)-(42,42). Chosen to fit the complete subject silhouette. Reference: No useful Lucide character match; original silhouette and identifying features guide construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c1af993c-635a-47d8-94fe-c30fd13a1ea9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-02/dragonball son goku_c1af993c-635a-47d8-94fe-c30fd13a1ea9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'spiky-haired-anime-boy'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('spiky', 'haired', 'anime', 'boy')

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

        path('hair',(6,22),[(6,6),(16,10),(24,6),(32,10),(42,6),(42,22)])
        path('jaw',(6,22),[(10,22),(10,28),((24,42),14,14,False),((38,28),14,14,False),(38,22),(42,22)])
        self.relate('connect','hair','jaw')
        path('fringe',(6,22),[(16,18),(24,22),(32,18),(42,22)])
        self.relate('connect','jaw','fringe');self.relate('connect','hair','fringe')
        curve('smile',(21,31),((23,34),(25,34),(27,31)))
