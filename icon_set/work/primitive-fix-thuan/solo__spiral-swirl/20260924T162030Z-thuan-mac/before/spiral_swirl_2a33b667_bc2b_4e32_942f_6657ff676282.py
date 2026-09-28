'Spiral Swirl Symbol. Plan and review: Continuous rounded spiral with an open outer end. Innermost curl shortened to preserve the minimum separation between turns. Source explicitly requests a standalone SOLO48 symbol. Keyshape SQUARE centerline envelope (6,6)-(42,42). Chosen to fit the complete subject silhouette. Reference: Lucide shell original and atomic-debug: a continuous spiral with widening outer turns; explicitly standalone SOLO48 brief.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a33b667-bc2b-4e32-942f-6657ff676282'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-05/logo heartstone_2a33b667-bc2b-4e32-942f-6657ff676282.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'spiral-swirl'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('spiral', 'swirl')

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

        curve('spiral',(24,42),((34,42),(42,34),(42,24)),((42,14),(34,6),(24,6)),((14,6),(6,14),(6,24)),((6,31),(11,34),(18,34)),((26,34),(32,30),(32,24)),((32,18),(28,15),(23,15)),((17,15),(15,18),(15,24)),((15,26),(17,26),(18,25)))
