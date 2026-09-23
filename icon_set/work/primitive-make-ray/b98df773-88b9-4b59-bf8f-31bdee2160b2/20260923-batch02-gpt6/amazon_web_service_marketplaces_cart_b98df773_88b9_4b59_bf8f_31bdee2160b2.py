"""A shopping cart carries a honeycomb of three hexagonal packages.
Plan: retain complete reference arrangement using typed contours and shared repeat parameters.
Keyshape SQUARE chosen for the reference's overall proportions; authored to its exact centerline extremes.
Construction reference: shopping-cart: open basket silhouette, raised handle and two circular wheels.
Omissions: Basket corners use deliberate angled joins; no packages omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b98df773-88b9-4b59-bf8f-31bdee2160b2'
SOURCE_PATH = 'icon_set/work/todo-references/amazon web service marketplaces cart_b98df773-88b9-4b59-bf8f-31bdee2160b2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'amazon-web-service-marketplaces-cart'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface'
    aliases = ()
    keywords = ('amazon', 'web', 'service', 'marketplaces', 'cart')
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

        poly('basket',(6,14),(10,31),(34,31),(39,6),(42,6))
        for n,x in [('left',14),('right',32)]:circle('wheel-'+n,x,39,3)
        # Tiled hexagons share complete edges, emitted once as a single lattice.
        poly('packages-outline',(23,6),(28,9),(28,15),(33,18),(33,24),(28,27),(23,24),(18,27),(13,24),(13,18),(18,15),(18,9),(23,6))
        poly('package-top-divider',(18,15),(23,18),(28,15))
        line('package-lower-divider',(23,18),(23,24))
        join('packages-outline','package-top-divider');join('packages-outline','package-lower-divider');join('package-top-divider','package-lower-divider')
