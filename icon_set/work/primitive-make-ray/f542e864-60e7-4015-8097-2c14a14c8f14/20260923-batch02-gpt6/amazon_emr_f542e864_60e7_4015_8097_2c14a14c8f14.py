"""A plus-marked circular hub fans out to four connected square nodes.
Plan: retain complete reference arrangement using typed contours and shared repeat parameters.
Keyshape SQUARE chosen for the reference's overall proportions; authored to its exact centerline extremes.
Construction reference: workflow: repeated box nodes with explicit connecting runs.
Omissions: Rounded corners simplified to square corners to preserve node openings.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f542e864-60e7-4015-8097-2c14a14c8f14'
SOURCE_PATH = 'icon_set/work/todo-references/amazon emr_f542e864-60e7-4015-8097-2c14a14c8f14.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'amazon-emr'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface'
    aliases = ()
    keywords = ('amazon', 'emr')
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

        circle('hub',12,24,6)
        line('plus-horizontal',(9,24),(15,24))
        line('plus-top',(12,21),(12,24));line('plus-bottom',(12,24),(12,27))
        join('plus-horizontal','plus-top');join('plus-horizontal','plus-bottom');join('plus-top','plus-bottom')
        for n,x,y in [('top',24,6),('right-upper',34,18),('right-lower',34,30),('bottom',24,34)]:
            self.add_polyline(n,(x,y),(x+8,y),(x+8,y+8),(x,y+8),closed=True)
        for n,a,b in [('fan-top',(18,24),(24,14)),('fan-upper',(18,24),(34,18)),('fan-lower',(18,24),(34,38)),('fan-bottom',(18,24),(24,34)),('rim-top',(32,14),(34,18)),('rim-right',(42,26),(42,30)),('rim-bottom',(34,38),(32,42))]:line(n,a,b)
        for n,node in [('fan-top','top'),('fan-upper','right-upper'),('fan-lower','right-lower'),('fan-bottom','bottom')]:
            join(n,'hub');join(n,node)
        for a in ['fan-top','fan-upper','fan-lower','fan-bottom']:
            for b in ['fan-top','fan-upper','fan-lower','fan-bottom']:
                if a<b:join(a,b)
        for n,a,b in [('rim-top','top','right-upper'),('rim-right','right-upper','right-lower'),('rim-bottom','right-lower','bottom')]:join(n,a);join(n,b)
