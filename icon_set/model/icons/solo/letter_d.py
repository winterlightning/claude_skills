"""The lowercase letter d, re-authored from the supplied reference for SOLO48.

Centerline extremes: left 10, top 4, right 38, bottom 44.
Plan: A round counter and tangent stem; shared bowl radius, reflected for right stems and shifted for descenders.
Reference: Lucide type — coherent monoline runs and explicit stroke junctions.
Source extraction fragments are omitted; the recognizable character is retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/Letters/D.svg'
AUTHOR = 'gpt-6'


class LetterD(Solo48):
    icon_id = 'letter-d'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "typeface"
    # Semantic body region for text composition; source geometry stays unchanged.
    typeface = {'character': 'd', 'kind': 'lowercase'}
    aliases = ()
    keywords = ('d', "typeface", "typography", 'lowercase')

    def build(self):
        rotation = 0
        mirror = False
        mirror = True
        cx, cy, r = 24, 30, 14
        runs = [((cx-r,cy), [('A',cx,cy-r,r,r,True),('A',cx+r,cy,r,r,True),('A',cx,cy+r,r,r,True),('A',cx-r,cy,r,r,True)],True), ((cx-r,cy), [('L',cx-r,4)],False)]

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
