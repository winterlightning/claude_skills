'Liquid Detergent Bottle. Plan and review: Sloping detergent neck, rounded bottle and central drop retained. Tiny nozzle and cap seam omitted; drop opening enlarged by raising its lower curve. Keyshape VRECT_L centerline envelope (8,4)-(40,44). Chosen to fit the complete subject silhouette. Reference: No useful Lucide character match; original silhouette and identifying features guide construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c232443-1304-41d8-b531-e6b54e649616'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/wayfinding/liquid detergent_9c232443-1304-41d8-b531-e6b54e649616.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'liquid-detergent-bottle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('liquid', 'detergent', 'bottle')

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

        path('bottle',(12,44),[((8,40),4,4,True),(8,24),(18,14),(22,4),(34,8),(30,18),(40,28),(40,40),((36,44),4,4,True),(12,44)],True)
        curve('drop',(24,24),((21,28),(19,30),(19,33)),((19,36),(29,36),(29,33)),((29,30),(27,28),(24,24)))
