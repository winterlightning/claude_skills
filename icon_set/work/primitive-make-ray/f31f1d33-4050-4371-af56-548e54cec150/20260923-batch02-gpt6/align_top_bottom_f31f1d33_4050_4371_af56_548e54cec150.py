"""Two horizontal blocks with a vertical double arrow.
Plan: retain complete reference arrangement using typed contours and shared repeat parameters.
Keyshape VRECT_L chosen for the reference's overall proportions; authored to its exact centerline extremes.
Construction reference: arrow-up: shared shaft and chevron endpoint.
Omissions: No parts omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f31f1d33-4050-4371-af56-548e54cec150'
SOURCE_PATH = 'icon_set/work/todo-references/align top bottom_f31f1d33-4050-4371-af56-548e54cec150.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'align-top-bottom'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface'
    aliases = ()
    keywords = ('align', 'top', 'bottom')
    # Upright stacked composition; visible extremes (6,2)-(42,46), centerline (8,4)-(40,44).
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

        box('upper',8,4,40,12,2)
        box('lower',8,36,40,44,2)
        line('shaft',(24,20),(24,28))
        poly('up',(19,25),(24,20),(29,25))
        poly('down',(19,23),(24,28),(29,23))
        join('shaft','up');join('shaft','down')
