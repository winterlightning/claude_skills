'Pointed Artist Paintbrush\nPlan: Diagonal pointed brush with rounded handle, ferrule and flowing pointed bristles.\nReference: Lucide paintbrush: coherent head/handle attachment; supplied reference keeps pointed bristles.\nReduction: Retain the defining silhouette and visible parts.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f6746ee9-8a45-44c8-81ef-7d3da12c0bca'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/paintbrush_f6746ee9-8a45-44c8-81ef-7d3da12c0bca.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pointed-artist-paintbrush'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('pointed', 'artist', 'paintbrush')

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

        # Broad diagonal handle, explicit ferrule junctions, and pointed bristle tuft.
        self.add_polyline('handle-side-a',(22,22),(34,6))
        self.add_arc('handle-cap',(34,6),(42,14),radius_x=8)
        self.add_line('handle-side-b',(42,14),(30,30))
        self.add_line('handle-base',(30,30),(22,22))
        self.add_contour('handle-outline','handle-side-a','handle-cap','handle-side-b','handle-base',closed=True)
        self.add_polyline('ferrule',(22,22),(16,28),(24,36),(30,30))
        self.relate('connect','ferrule','handle-outline')
        self.add_bezier('bristles',(16,28),((6,28),(12,38),(6,42)),((17,42),(24,42),(24,36)))
        self.relate('connect','bristles','ferrule')
