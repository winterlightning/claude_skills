from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '4b4c4e57-da6a-4ce9-9d53-b8f095c266b7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__square-right/20260929T091947Z-thuan-mac/reference/square right_4b4c4e57-da6a-4ce9-9d53-b8f095c266b7.svg'
AUTHOR = "gpt-6"
# Plan: Restore the softly rounded right-pointing frame and a longer arrow with balanced wings.
# Keyshape: SQUARE; preserve reference arrangement.
# Construction reference: arrow-right.

def _draw(icon, name, description):
    tokens=description.split(); pos=0; part=0; count=0; members=[]; start=None; point=None
    def finish(closed=False):
        nonlocal members,part
        if members: icon.add_contour(name if part==0 else f"{name}-part{part}",*members,closed=closed)
        members=[];part+=1
    while pos<len(tokens):
        op=tokens[pos];pos+=1
        if op=='M':
            if members: finish()
            point=tuple(map(int,tokens[pos:pos+2]));pos+=2;start=point
        elif op=='Z':
            if point!=start:
                count+=1;eid=f"{name}-{count}";icon.add_line(eid,point,start);members.append(eid);point=start
            finish(True)
        else:
            count+=1;eid=f"{name}-{count}";members.append(eid)
            if op=='L':
                end=tuple(map(int,tokens[pos:pos+2]));pos+=2;icon.add_line(eid,point,end)
            elif op=='C':
                values=list(map(int,tokens[pos:pos+6]));pos+=6;c1=tuple(values[:2]);c2=tuple(values[2:4]);end=tuple(values[4:]);icon.add_bezier(eid,point,(c1,c2,end))
            elif op=='A':
                rx,ry,sweep,x,y=map(int,tokens[pos:pos+5]);pos+=5;end=(x,y);icon.add_arc(eid,point,end,radius_x=rx,radius_y=ry,sweep=bool(sweep))
            point=end
    if members: finish()

class Revision(Solo48):
    icon_id = 'square-right'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'frame', 'M 11 6 L 28 6 C 30 6 30 7 32 9 L 40 17 C 42 19 42 20 42 24 C 42 28 42 29 40 31 L 32 39 C 30 41 30 42 28 42 L 11 42 A 5 5 1 6 37 L 6 11 A 5 5 1 11 6 Z')
        _draw(self, 'arrow', 'M 15 24 L 32 24')
        _draw(self, 'head', 'M 25 17 L 32 24 L 25 31')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
