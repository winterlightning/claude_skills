"""Code chevrons and slash sit between two pipeline rails with outward tabs.
Plan: retain complete reference arrangement using typed contours and shared repeat parameters.
Keyshape HRECT_L chosen for the reference's overall proportions; authored to its exact centerline extremes.
Construction reference: No useful Lucide match beyond elementary polylines.
Omissions: No parts omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '12be411f-98cd-4c43-b650-b16b090dc516'
SOURCE_PATH = 'icon_set/work/todo-references/amazon web service codepipeline 1_12be411f-98cd-4c43-b650-b16b090dc516.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'amazon-web-service-codepipeline-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface'
    aliases = ()
    keywords = ('amazon', 'web', 'service', 'codepipeline', '1')
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

        for side,x,outer in [('left',8,4),('right',40,44)]:
            for j,(a,b) in enumerate([(8,12),(12,36),(36,40)]):line(side+f'-rail-{j}',(x,a),(x,b))
            for j,y in enumerate([12,36]):
                line(side+f'-tab-{j}',(x,y),(outer,y))
                join(side+f'-tab-{j}',side+f'-rail-{j}');join(side+f'-tab-{j}',side+f'-rail-{j+1}')
                join(side+f'-rail-{j}',side+f'-rail-{j+1}')
        poly('code-left',(20,17),(14,24),(20,31))
        poly('code-right',(28,17),(34,24),(28,31))
        line('slash',(26,15),(22,33))
