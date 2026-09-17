"""The lowercase letter c, re-authored from the supplied reference for SOLO48.

Centerline extremes: left 6, top 6, right 42, bottom 42.
Plan: A circular open bowl; paired terminals mirror across the horizontal axis.
Reference: Lucide type — coherent monoline runs and explicit stroke junctions.
Source extraction fragments are omitted; the recognizable character is retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/Letters/C.svg'
AUTHOR = 'gpt-6'


class LetterC(Solo48):
    icon_id = 'letter-c'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "typeface"
    # Semantic body region for text composition; source geometry stays unchanged.
    typeface = {'character': 'c', 'kind': 'lowercase'}
    aliases = ()
    keywords = ('c', "typeface", "typography", 'lowercase')

    def build(self):
        rotation = 0
        mirror = False
        runs = [((42,12), [('A',24,6,18,6,False),('A',6,24,18,18,False),('A',24,42,18,18,False),('A',42,36,18,6,False)],False)]

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
