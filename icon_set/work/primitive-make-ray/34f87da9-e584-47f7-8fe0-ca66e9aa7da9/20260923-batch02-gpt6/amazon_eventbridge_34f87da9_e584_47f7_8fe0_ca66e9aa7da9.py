"""Four circular event nodes surround a central hexagon on an angular ring.
Plan: retain complete reference arrangement using typed contours and shared repeat parameters.
Keyshape SQUARE chosen for the reference's overall proportions; authored to its exact centerline extremes.
Construction reference: workflow: explicit links between repeated nodes; circles replace square nodes as required.
Omissions: No parts omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '34f87da9-e584-47f7-8fe0-ca66e9aa7da9'
SOURCE_PATH = 'icon_set/work/todo-references/amazon eventbridge_34f87da9-e584-47f7-8fe0-ca66e9aa7da9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'amazon-eventbridge'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface'
    aliases = ()
    keywords = ('amazon', 'eventbridge')
    # Square overall composition; visible extremes (4,4)-(44,44), centerline (6,6)-(42,42).
    def build(self):

        def path(name,start,steps,closed=False):
            members=[]; point=start
            for j,step in enumerate(steps):
                member=f'{name}-{j}'
                if len(step)==2:
                    self.add_line(member,point,step);point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep);point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*points):self.add_polyline(name,*points)
        def join(a,b):self.relate('connect',a,b)

        for n,x,y in [('nw',14,10),('ne',38,18),('se',34,38),('sw',10,32)]:circle(n,x,y,4)
        poly('north',(18,10),(32,10),(38,14));join('north','nw');join('north','ne')
        poly('east',(38,22),(42,26),(38,38));join('east','ne');join('east','se')
        poly('south',(30,38),(16,38),(10,36));join('south','se');join('south','sw')
        poly('west',(10,28),(6,24),(10,10));join('west','sw');join('west','nw')
        self.add_polyline('hexagon',(21,18),(27,18),(31,24),(27,30),(21,30),(17,24),closed=True)
