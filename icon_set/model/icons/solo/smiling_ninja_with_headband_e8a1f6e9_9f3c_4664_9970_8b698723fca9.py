'Smiling Ninja Anime Character Face. Plan and review: Spiky hair, broad forehead band, paired eyes and smile retained. Tiny headband emblem and ears are omitted; broad hair spikes replace crowded narrow triangles. Keyshape SQUARE centerline envelope (6,6)-(42,42). Chosen to fit the complete subject silhouette. Reference: No useful Lucide character match; original silhouette and identifying features guide construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8a1f6e9-9f3c-4664-9970-8b698723fca9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-07/ninja naruto shippuden_e8a1f6e9-9f3c-4664-9970-8b698723fca9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smiling-ninja-with-headband'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('smiling', 'ninja', 'with', 'headband')

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

        path('hair',(6,18),[(6,6),(15,9),(24,6),(33,9),(42,6),(42,18),(6,18)],True)
        path('jaw',(6,18),[(6,28),((20,42),14,14,False),(28,42),((42,28),14,14,False),(42,18)])
        self.relate('connect','hair','jaw')
        for x in (16,32):self.add_dot('eye-'+str(x),(x,26))
        curve('smile',(22,33),((23,34),(25,34),(26,33)))
