'Fairy with Spread Wings.\nPlan: Round detached head, central torso, paired triangular wings and short skirt. Head-to-torso ink gap4; lower legs omitted to keep skirt separate from wings. Bounds6..42.\nReference: human_ref/full_body_ref.png: circular head and detached torso; narrow wings retain the source fairy identity.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd3b05c39-172a-5ed7-bf29-831a42c4e3db'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-03/fairy_d3b05c39-172a-5ed7-bf29-831a42c4e3db.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'fairy-with-narrow-wings'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'video-games'
    aliases = ()
    keywords = ('fairy', 'with', 'narrow', 'wings')

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

        circle('head',24,10,4)
        self.add_line('torso',(24,22),(24,34));self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.add_polyline('skirt',(16,42),(24,34),(32,42),closed=True);self.relate('connect','skirt','torso')
        
        self.add_polyline('wing-left',(6,18),(24,26),(6,30),closed=True);self.add_polyline('wing-right',(42,18),(24,26),(42,30),closed=True);self.relate('connect','wing-left','torso');self.relate('connect','wing-right','torso');self.relate('connect','wing-left','wing-right')
