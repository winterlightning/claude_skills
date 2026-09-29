from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '746eedc8-eb0c-4e03-8d4c-d25625ee4a35'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__square-phone/20260929T091947Z-thuan-mac/reference/square phone_746eedc8-eb0c-4e03-8d4c-d25625ee4a35.svg'
AUTHOR = "gpt-6"
# Plan: Restore a complete curved receiver with two rounded earpieces inside the square.
# Keyshape: SQUARE; preserve reference arrangement.
# Construction reference: phone.

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
    icon_id = 'square-phone'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve a complete receiver with rounded earpieces rather than a crescent; the compact handset opening and frame gap remain legible at 48px.', 'approved_by': 'user-authorized visual judgment by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'c62c8923e5a3a6e0048850a165a0abb004a739f1db56414923dd76015f7cfa61'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'frame', 'M 10 6 L 38 6 A 4 4 1 42 10 L 42 38 A 4 4 1 38 42 L 10 42 A 4 4 1 6 38 L 6 10 A 4 4 1 10 6 Z')
        _draw(self, 'receiver', 'M 16 13 C 17 12 18 13 20 15 L 22 18 C 23 19 21 21 19 22 C 21 26 23 28 27 29 L 30 26 C 31 25 33 27 35 29 C 38 32 34 36 31 36 C 24 36 12 24 12 18 C 12 16 14 14 16 13 Z')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
