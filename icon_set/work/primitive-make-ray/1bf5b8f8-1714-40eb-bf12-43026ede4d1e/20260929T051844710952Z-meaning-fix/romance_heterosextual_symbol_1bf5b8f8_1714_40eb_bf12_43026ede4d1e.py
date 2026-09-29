"""Restore circular gender-symbol ring around an independent heart, with a northeast arrow and lower cross.
Reference comparison: The rejected symbol used a heart as the whole outline and omitted the enclosing circle. The reference has a heart inside a circle with male arrow and female cross.
Construction references: Lucide heart: paired lobes and tapered point; supplied reference owns combined symbol structure.
Omissions: No defining features omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1bf5b8f8-1714-40eb-bf12-43026ede4d1e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__romance-heterosextual-symbol/20260929T051531Z-thuan-mac/reference/romance heterosextual symbol_1bf5b8f8-1714-40eb-bf12-43026ede4d1e.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'romance-heterosextual-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def path(self, name, start, *steps, closed=False):
        ids=[]; p=start
        for n,step in enumerate(steps):
            key=f"{name}-{n}"; end=step[1]
            if step[0]=='L': self.add_line(key,p,end)
            elif step[0]=='C': self.add_bezier(key,p,(step[2],step[3],end))
            else: self.add_arc(key,p,end,radius_x=step[2],radius_y=step[3],sweep=step[4],large_arc=step[5] if len(step)>5 else False)
            ids.append(key);p=end
        if closed and p!=start:
            key=f"{name}-close";self.add_line(key,p,start);ids.append(key)
        self.add_contour(name,*ids,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

    def build(self):
        self.circle('symbol-ring',21,23,15)
        self.add_line('male-stem',(32,12),(43,3));self.add_polyline('male-arrow',(35,3),(43,3),(43,11))
        self.add_line('female-stem',(21,38),(21,45));self.add_line('female-cross',(15,42),(27,42))
        self.path('heart',(21,19),('A',(13,20),4,4,False),('C',(21,30),(13,24),(17,27)),('C',(29,20),(25,27),(29,24)),('A',(21,19),4,4,False),closed=True)
        self.relate('connect','symbol-ring','female-stem');self.relate('connect','male-stem','male-arrow');self.relate('connect','female-stem','female-cross')

Drawing.exception = {'reason': 'Nested heart and gender ring require compact internal spacing and extended directional marks. All defining parts remain clear under the user-authorized visual exception.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'fd7946e68c2e60aef762e67705d022293bc6363986717b8deb3fe27aff848c6c'}
