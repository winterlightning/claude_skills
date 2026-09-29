from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'ca2e907d-e297-46ef-946a-c08a49756d52'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__stacked-hands/20260929T091947Z-thuan-mac/reference/workflow teamwork hand gather_ca2e907d-e297-46ef-946a-c08a49756d52.svg'
AUTHOR = "gpt-6"
# Plan: Restore a top wrist, left supporting palm and diagonal foreground hand with distinct finger creases.
# Keyshape: SQUARE; preserve reference arrangement.
# Construction reference: hand.

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
    icon_id = 'stacked-hands'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve three overlapping hands and wrist directions with two clear foreground finger creases; accept intended contact and organic envelope.', 'approved_by': 'user-authorized visual judgment by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '4594d195a1251db9732ae3b38a8945065e529e5dfa7a48de82bcc769b4172f42'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'top-left', 'M 19 4 L 19 10 C 19 14 15 13 15 19')
        _draw(self, 'top-right', 'M 29 4 L 29 10 C 29 14 33 14 33 20')
        _draw(self, 'left-hand', 'M 4 35 L 8 30 C 7 27 8 24 10 20 C 11 17 15 18 14 22 L 13 25')
        _draw(self, 'left-wrist', 'M 10 44 L 16 39 C 20 39 22 37 24 35')
        _draw(self, 'front-hand', 'M 44 35 L 39 30 C 40 26 38 22 34 19 L 29 14 C 25 10 21 14 24 18 L 30 24')
        _draw(self, 'fingers', 'M 24 18 L 19 14 C 15 10 11 15 15 19 L 25 29')
        _draw(self, 'low', 'M 15 19 C 11 17 8 22 12 26 L 25 38 C 29 41 33 37 36 41 L 40 44')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
