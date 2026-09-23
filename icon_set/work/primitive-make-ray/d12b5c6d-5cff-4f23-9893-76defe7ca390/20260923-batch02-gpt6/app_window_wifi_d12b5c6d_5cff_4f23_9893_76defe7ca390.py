"""A browser window has two wireless arcs outside its upper-left corner.
Plan: retain complete reference arrangement using typed contours and shared repeat parameters.
Keyshape SQUARE chosen for the reference's overall proportions; authored to its exact centerline extremes.
Construction reference: app-window: rounded frame and header; wifi: concentric signal arcs.
Omissions: Two tiny header dashes omitted to avoid crowding the 8-unit header band.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd12b5c6d-5cff-4f23-9893-76defe7ca390'
SOURCE_PATH = 'icon_set/work/todo-references/app window wifi_d12b5c6d-5cff-4f23-9893-76defe7ca390.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'app-window-wifi'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface'
    aliases = ()
    keywords = ('app', 'window', 'wifi')
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

        # Concentric quarter circles share their conceptual centre at (18,18).
        self.add_arc('signal-outer',(6,18),(18,6),radius_x=12,sweep=True)
        self.add_arc('signal-inner',(14,18),(18,14),radius_x=4,sweep=True)
        # Separate header and lower frame share exactly their side junctions.
        path('header',(22,27),[(22,23),((26,19),4,4,True),(38,19),((42,23),4,4,True),(42,27)])
        line('divider',(22,27),(42,27))
        path('body',(42,27),[(42,38),((38,42),4,4,True),(26,42),((22,38),4,4,True),(22,27)])
        join('header','divider');join('body','divider');join('header','body')
