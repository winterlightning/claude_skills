"""The digit 6, re-authored from the supplied reference for SOLO48.

Centerline extremes: left 10, top 4, right 38, bottom 44.
Plan: A circular bowl and tangent upright with a rounded terminal; nine rotates the six construction.
Reference: Lucide type — coherent monoline runs and explicit stroke junctions.
Source extraction fragments are omitted; the recognizable character is retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/Letters/6.svg'
AUTHOR = 'gpt-6'


class Digit6(Solo48):
    icon_id = 'digit-6'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "typeface"
    categories = ("typeface",)
    # Semantic body region for text composition; source geometry stays unchanged.
    typeface = {'character': '6', 'kind': 'digit'}
    aliases = ()
    keywords = ('6', "typeface", "typography", 'number')

    def build(self):
        rotation = 0
        mirror = False
        rotation = 0
        cx, cy, radius = 24, 30, 14
        runs = [((cx-radius,cy), [('A',cx,cy-radius,radius,radius,True),('A',cx+radius,cy,radius,radius,True),('A',cx,cy+radius,radius,radius,True),('A',cx-radius,cy,radius,radius,True)],True), ((10,30), [('L',10,18),('A',24,4,14,14,True),('L',34,4)],False)]

        # Emit coherent strokes. Only true shared endpoints declare contacts.
        def point(x, y):
            if mirror:
                x = 48-x
            for _ in range(rotation):
                x,y = 48-y,x
            return x,y
        contacts=[]
        for ri,(start,steps,closed) in enumerate(runs):
            previous=point(*start)
            nodes={previous}
            members=[]
            for si,step in enumerate(steps):
                end=point(step[1],step[2])
                part=f'stroke-{ri}-{si}'
                if step[0]=='L':
                    self.add_line(part,previous,end)
                else:
                    self.add_arc(part,previous,end,radius_x=step[3],radius_y=step[4],sweep=not step[5] if mirror else step[5])
                members.append(part)
                nodes.add(end)
                previous=end
            contour=f'stroke-{ri}'
            self.add_contour(contour,*members,closed=closed)
            contacts.append((contour,nodes))
        for i,(a,anodes) in enumerate(contacts):
            for b,bnodes in contacts[i+1:]:
                if anodes & bnodes:
                    self.relate('connect',a,b)
