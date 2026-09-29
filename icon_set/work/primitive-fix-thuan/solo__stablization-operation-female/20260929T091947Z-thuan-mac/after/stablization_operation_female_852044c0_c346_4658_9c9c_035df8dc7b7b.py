from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '852044c0-c346-4658-9c9c-035df8dc7b7b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__stablization-operation-female/20260929T091947Z-thuan-mac/reference/stablization operation female_852044c0-c346-4658-9c9c-035df8dc7b7b.svg'
AUTHOR = "gpt-6"
# Plan: Restore upright closed surgical scissors with two finger loops and the separate curved crossed marker.
# Keyshape: SQUARE; preserve reference arrangement.
# Construction reference: scissors.

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
    icon_id = 'stablization-operation-female'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve the closed surgical scissors and separate curved crossed marker; compact contacts and natural combined envelope are intentional.', 'approved_by': 'user-authorized visual judgment by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '4815ae836a482042d1ab25c8602ff75b2e0fb1ebd2368f758e3db74fddd78eed'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'blade', 'M 14 30 L 14 20 L 18 6 L 22 20 L 22 30')
        _draw(self, 'blade-seam', 'M 14 26 L 22 20')
        _draw(self, 'left-loop', 'M 4 36 A 6 6 1 16 36 A 6 6 1 4 36 Z')
        _draw(self, 'right-loop', 'M 20 36 A 6 6 1 32 36 A 6 6 1 20 36 Z')
        _draw(self, 'curve', 'M 30 12 C 42 12 43 25 35 30')
        _draw(self, 'marker-stem', 'M 37 15 L 42 8')
        _draw(self, 'cross-a', 'M 37 4 L 44 11')
        _draw(self, 'cross-b', 'M 44 4 L 37 11')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
