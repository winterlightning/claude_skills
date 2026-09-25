"""Uppercase S for SOLO48; centerline envelope (10, 4)–(38, 44).
Plan: Two opposed elliptical lobes share a tangent waist and rotational symmetry.
Lucide type informs monoline strokes and explicit shared junctions.
No source drawing supplied; constructed from the uppercase character brief.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'


class LetterSUppercase(Solo48):
    icon_id = 'letter-s-uppercase'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    categories = ('typeface',)
    typeface = {'character': 'S', 'kind': 'uppercase'}
    aliases = ()
    keywords = ('S', 'uppercase', 'capital', 'typeface')

    def build(self):
        rotation = 0
        mirror = False
        runs=[((38,14),[('A',24,4,14,10,False),('A',10,14,14,10,False),('A',24,24,14,10,False),('A',38,34,14,10,True),('A',24,44,14,10,True),('A',10,34,14,10,True)],False)]
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
