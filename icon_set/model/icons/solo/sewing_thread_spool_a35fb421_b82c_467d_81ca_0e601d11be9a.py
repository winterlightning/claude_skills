'Sewing Thread Spool.\nPlan and review: Retained broad spool flanges, narrow core, diagonal wrap and loose thread extending right. Reduced fine wraps to one and lowered loose end for flange clearance.\nKeyshape: VRECT_L, exact SOLO48 envelope.\nConstruction reference: Lucide spool: broad end flanges, narrow core and diagonal thread wrap.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a35fb421-b82c-467d-81ca-0e601d11be9a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/thread_a35fb421-b82c-467d-81ca-0e601d11be9a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sewing-thread-spool'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('sewing', 'thread', 'spool')

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

        box('top',8,4,40,12,4);box('bottom',8,36,40,44,4)
        self.add_polyline('core-left',(16,12),(16,24),(16,36));self.add_polyline('core-right',(32,12),(32,24),(32,36))
        for a in ('top','bottom'):
         for b in ('core-left','core-right'):self.relate('connect',a,b)
        self.add_line('wrap',(16,28),(32,24));self.relate('connect','wrap','core-left');self.relate('connect','wrap','core-right')
        self.add_line('loose-thread',(32,24),(40,22));self.relate('connect','loose-thread','wrap');self.relate('connect','loose-thread','core-right')
