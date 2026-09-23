"""A play triangle is surrounded by three hexagons and three outward arrows.
Plan: retain complete reference arrangement using typed contours and shared repeat parameters.
Keyshape SQUARE chosen for the reference's overall proportions; authored to its exact centerline extremes.
Construction reference: arrow-up: shaft and chevrons meet at a shared point.
Omissions: No parts omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c4945396-13ec-470f-9338-45638fe16eb2'
SOURCE_PATH = 'icon_set/work/todo-references/amazon web service elemental medialive_c4945396-13ec-470f-9338-45638fe16eb2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'amazon-web-service-elemental-medialive'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface'
    aliases = ()
    keywords = ('amazon', 'web', 'service', 'elemental', 'medialive')
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

        # Three repeated hexagon definitions retain the triangular arrangement.
        for n,x,y in [('top',24,12),('left',12,34),('right',36,34)]:
            self.add_polyline(n,(x,y-6),(x+6,y-3),(x+6,y+3),(x,y+6),(x-6,y+3),(x-6,y-3),closed=True)
        self.add_polyline('play',(20,22),(29,27),(20,32),closed=True)
        for n,tip,end,a,b in [('left',(6,18),(13,22),(12,14),(6,25)),('right',(42,18),(35,22),(36,14),(42,25)),('down',(24,42),(24,36),(19,38),(29,38))]:
            poly(n+'-head',a,tip,b);line(n+'-shaft',end,tip);join(n+'-head',n+'-shaft')
