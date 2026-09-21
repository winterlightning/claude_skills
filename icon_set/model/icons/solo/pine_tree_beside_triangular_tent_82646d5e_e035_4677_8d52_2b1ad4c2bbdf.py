'Pine Tree beside Triangular Tent\nPlan: Pine tree beside tent on shared ground; narrow entrance retained as open seam.\nReference: Lucide tent-tree: tent and tree form a natural campsite scene.\nReduction: One triangular pine crown and one entrance seam replace nested small triangles.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82646d5e-e035-4677-8d52-2b1ad4c2bbdf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/campground_82646d5e-e035-4677-8d52-2b1ad4c2bbdf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pine-tree-beside-triangular-tent'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('pine', 'tree', 'beside', 'triangular', 'tent')

    def build(self):

        def path(name, start, steps, closed=False):
            members, point = [], start
            for index, step in enumerate(steps):
                member = f"{name}-{index}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[((x+rx,y),rx,ry,True),((x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r):
            ellipse(name,x,y,r,r)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)

        self.add_polyline('tree',(6,26),(14,6),(22,26),(14,26),(6,26))
        self.add_line('trunk',(14,26),(14,42));self.relate('connect','tree','trunk')
        self.add_polyline('tent',(22,42),(32,22),(42,42))
        
        self.add_line('ground',(6,42),(42,42));self.relate('connect','ground','trunk');self.relate('connect','ground','tent')
