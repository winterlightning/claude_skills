"""Five curved data streams narrow beside a three-column analytics chart.
Plan: retain complete reference arrangement using typed contours and shared repeat parameters.
Keyshape SQUARE chosen for the reference's overall proportions; authored to its exact centerline extremes.
Construction reference: No useful Lucide match for this asymmetric stream construction.
Omissions: No streams or chart bars omitted; tiny terminal dash retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8a60c977-db4f-4a2b-852f-9198df1fc339'
SOURCE_PATH = 'icon_set/work/todo-references/amazon kinesis data analytics_8a60c977-db4f-4a2b-852f-9198df1fc339.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'amazon-kinesis-data-analytics'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface'
    aliases = ()
    keywords = ('amazon', 'kinesis', 'data', 'analytics')
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

        # Related stream series: each is an elliptical quadrant with a horizontal exit.
        for n,start,end,rx,ry in [('upper-a',(6,10),(32,22),26,12),('upper-b',(15,6),(42,14),27,8),('upper-c',(25,6),(42,8),17,2),('lower-a',(6,36),(24,25),18,11),('lower-b',(15,42),(27,32),12,10)]:
            self.add_arc(n,start,end,radius_x=rx,radius_y=ry,sweep=n.startswith('lower'))
        line('terminal',(40,22),(42,22))
        # Split the baseline at actual bar attachments.
        for j,(a,b) in enumerate([(26,29),(29,35),(35,41),(41,42)]):line(f'base-{j}',(a,42),(b,42))
        for j,x,y in [(0,29,36),(1,35,28),(2,41,33)]:
            line(f'bar-{j}',(x,42),(x,y))
            join(f'bar-{j}',f'base-{j}');join(f'bar-{j}',f'base-{j+1}')
        for j in range(3):join(f'base-{j}',f'base-{j+1}')
