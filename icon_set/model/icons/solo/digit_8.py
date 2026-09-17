"""The digit 8, re-authored from the supplied reference for SOLO48.

Centerline extremes: left 10, top 4, right 38, bottom 44.
Plan: Two equal elliptical counters meet at a shared waist; mirrored about both axes.
Reference: Lucide type — coherent monoline runs and explicit stroke junctions.
Source extraction fragments are omitted; the recognizable character is retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/Letters/8.svg'
AUTHOR = 'gpt-6'


class Digit8(Solo48):
    icon_id = 'digit-8'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "typeface"
    # Semantic body region for text composition; source geometry stays unchanged.
    typeface = {'character': '8', 'kind': 'digit'}
    aliases = ()
    keywords = ('8', "typeface", "typography", 'number')

    def build(self):
        rotation = 0
        mirror = False
        cx, waist, rx, ry = 24, 24, 14, 10
        steps=[]
        for sign,sweep in ((-1,True),(1,False)):
            cy=waist+sign*ry
            steps.extend([('A',cx-rx,cy,rx,ry,sweep),('A',cx,cy+sign*ry,rx,ry,sweep),('A',cx+rx,cy,rx,ry,sweep),('A',cx,waist,rx,ry,sweep)])
        runs=[((cx,waist),steps,True)]

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
