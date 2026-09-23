"""Unequal columns move upward toward a horizontal alignment rule.
Plan: retain complete reference arrangement using typed contours and shared repeat parameters.
Keyshape HRECT_L chosen for the reference's overall proportions; authored to its exact centerline extremes.
Construction reference: arrow-up: chevrons share their tips with shafts.
Omissions: No parts omitted; narrow arrow lanes retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c7665d4b-d589-4003-8834-958ea7cbf3a9'
SOURCE_PATH = 'icon_set/work/todo-references/align top move_c7665d4b-d589-4003-8834-958ea7cbf3a9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'align-top-move'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface'
    aliases = ()
    keywords = ('align', 'top', 'move')
    # Wide rule/rail composition; visible extremes (2,6)-(46,42), centerline (4,8)-(44,40).
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

        line('rule',(4,8),(44,8))
        box('tall',16,18,24,40,2)
        box('short',32,28,40,40,2)
        for n,x in [('left',6),('right',42)]:
            poly(n+'-head',(x-2,21),(x,18),(x+2,21))
            line(n+'-shaft',(x,18),(x,27));join(n+'-head',n+'-shaft')
