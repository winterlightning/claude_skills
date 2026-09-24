'Soap bar with foam. Plan and review: Perspective soap bar and broad rounded suds retained. Fine lower cube edges are hidden by the foam; joined boundaries avoid narrow trapped pockets. Keyshape SQUARE centerline envelope (6,6)-(42,42). Chosen to fit the complete subject silhouette. Reference: Lucide cloud original and atomic-debug informs round overlapping foam lobes.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a98c4793-33e4-4b74-83d2-353f5158652b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/wayfinding/sponge soap_a98c4793-33e4-4b74-83d2-353f5158652b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'soap-bar-with-foam'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('soap', 'bar', 'with', 'foam')

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

        path('bar',(6,28),[(6,14),(22,6),(42,6),(42,28),(34,34)])
        path('top',(6,14),[(30,14),(42,6)]);self.relate('connect','bar','top')
        self.add_line('side',(30,14),(30,30));self.relate('connect','side','top')
        curve('foam',(6,28),((9,24),(13,24),(16,28)),((20,22),(28,24),(30,30)),((38,28),(42,34),(38,38)),((34,42),(30,42),(24,42)),((14,42),(6,42),(6,36)),((6,32),(6,30),(6,28)))
        self.relate('connect','bar','foam');self.relate('connect','side','foam')
