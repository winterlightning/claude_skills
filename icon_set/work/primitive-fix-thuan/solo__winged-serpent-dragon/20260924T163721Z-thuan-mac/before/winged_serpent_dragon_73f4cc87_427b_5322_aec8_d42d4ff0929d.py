'Winged Serpent Dragon. Plan and review: Long-snouted serpent, tall swept wing and broad curling tail retained. Small fins and fine wing divisions omitted; the open lower contour follows the source. Keyshape SQUARE centerline envelope (6,6)-(42,42). Chosen to fit the complete subject silhouette. Reference: No useful Lucide character match; original silhouette and identifying features guide construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '73f4cc87-427b-5322-aec8-d42d4ff0929d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-03/fantasy amphiptere dragon_73f4cc87-427b-5322-aec8-d42d4ff0929d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'winged-serpent-dragon'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('winged', 'serpent', 'dragon')

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

        path('snout',(6,26),[(6,20),(16,12),(14,22)])
        curve('neck',(14,22),((22,20),(22,30),(32,32)))
        self.relate('connect','snout','neck')
        curve('back',(32,32),((37,28),(34,21),(34,17)))
        self.relate('connect','neck','back')
        path('wing',(34,17),[(42,14),(24,6),(26,20)])
        self.relate('connect','back','wing')
        curve('belly',(6,26),((10,30),(12,36),(22,40)),((26,42),(30,42),(34,42)),((38,42),(40,39),(42,36)))
        self.relate('connect','snout','belly')
