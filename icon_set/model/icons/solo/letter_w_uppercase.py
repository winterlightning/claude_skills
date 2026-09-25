"""Uppercase W for SOLO48; centerline envelope (6, 6)–(42, 42).
Plan: Broad mirrored diagonals share matching lower vertices and an inset middle apex.
Lucide type informs monoline strokes and explicit shared junctions.
No source drawing supplied; constructed from the uppercase character brief.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'


class LetterWUppercase(Solo48):
    icon_id = 'letter-w-uppercase'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    categories = ('typeface',)
    typeface = {'character': 'W', 'kind': 'uppercase'}
    aliases = ()
    keywords = ('W', 'uppercase', 'capital', 'typeface')

    def build(self):
        rotation = 0
        mirror = False
        axis,left,right,top,bottom=24,6,42,6,42
        runs=[((left,top),[('L',15,bottom),('L',axis,18),('L',33,bottom),('L',right,top)],False)]
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
