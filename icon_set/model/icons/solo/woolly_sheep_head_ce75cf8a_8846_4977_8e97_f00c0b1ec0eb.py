'Sheep Head with Fluffy Wool.\nPlan and review: Retained scalloped wool, long blank face and both lateral ears; mirrored about24. No facial features invented.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: No useful exact Lucide match; source silhouette and geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ce75cf8a-8846-4977-8e97-f00c0b1ec0eb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/fleece_ce75cf8a-8846-4977-8e97-f00c0b1ec0eb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'woolly-sheep-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('woolly', 'sheep', 'head')

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

        curve('wool',(6,26),((6,18),(8,16),(12,16)),((12,8),(18,6),(24,6)),((30,6),(36,8),(36,16)),((40,16),(42,18),(42,26)))
        curve('face',(16,24),((16,36),(18,42),(24,42)),((30,42),(32,36),(32,24)),((28,18),(20,18),(16,24)))
        curve('ear-left',(6,26),((8,22),(12,22),(16,24)),((16,32),(8,32),(6,26)))
        curve('ear-right',(42,26),((40,22),(36,22),(32,24)),((32,32),(40,32),(42,26)))
        for s in ('ear-left','ear-right'):self.relate('connect',s,'wool');self.relate('connect',s,'face')
