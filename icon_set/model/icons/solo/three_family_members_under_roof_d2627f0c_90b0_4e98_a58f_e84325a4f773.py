'Family Under a Roof.\nSymbol plan: Three stick figures under a roof: circular heads radius3 at(9,25),(24,22),(39,25). Their torso junctions are8 centerline units below each head outline, exactly4 units between ink. Torso, arms and split legs share exact nodes and explicit human flags.\nConstruction reference: human_ref/full_body_ref.png: circular detached heads and rounded limb strokes; source roof scene.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd2627f0c-90b0-4e98-a58f-e84325a4f773'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_18/family home_d2627f0c-90b0-4e98-a58f-e84325a4f773.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'three-family-members-under-roof'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('three', 'family', 'members', 'under', 'roof')

    def build(self):
        def path(name, start, steps, closed=False):
            members = []
            point = start
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

        def circle(name, x, y, radius):
            path(name, (x-radius,y), [((x+radius,y),radius,radius,True),
                 ((x-radius,y),radius,radius,True)], True)

        def box(name, left, top, right, bottom, radius):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        self.add_polyline('roof',(6,12),(24,6),(42,12))
        for j,(x,y) in enumerate(((9,25),(24,22),(39,25))):
            circle(f'head-{j}',x,y,3)
            top=y+11
            hip=38 if j==1 else 40
            width=4 if j==1 else 3
            self.add_line(f'torso-{j}',(x,top),(x,hip))
            self.add_polyline(f'arms-{j}',(x-width,top+2),(x,top),(x+width,top+2))
            self.add_polyline(f'legs-{j}',(x-width+1,42),(x,hip),(x+width-1,42))
            self.relate('connect',f'torso-{j}',f'arms-{j}')
            self.relate('connect',f'torso-{j}',f'legs-{j}')
            self.mark_human_figure(f'person-{j}',head=f'head-{j}',torso=f'torso-{j}',torso_junction='start')
