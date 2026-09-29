from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '7acafe9e-8c82-4fc5-aa6b-a6d51b2fb48b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__twin-peaks-inside-a-rounded-hill-emblem-7acafe9e/20260929T090755Z-thuan-mac/reference/basecamp logo_7acafe9e-8c82-4fc5-aa6b-a6d51b2fb48b.svg'
AUTHOR = "gpt-6"
# Plan: Restore the domed emblem, bowl-shaped base and two gently rounded unequal peaks.
# Keyshape: HRECT_L; preserve reference arrangement.
# Construction reference: none.

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
    icon_id = 'twin-peaks-inside-a-rounded-hill-emblem-7acafe9e'
    keyshape = Keyshape.HRECT_L
    exception = {'reason': 'Preserve the twin mountains joining a curved dome/base; the intended junction is visually continuous.', 'approved_by': 'user-authorized visual judgment by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'df412483cd21215e4ab84f17c989529d0bd7c72c65bb353bc04cf1caefb06711'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'outline', 'M 4 31 C 4 24 13 8 24 8 C 35 8 44 24 44 31 C 44 43 4 43 4 31 Z')
        _draw(self, 'peaks', 'M 6 35 L 14 23 C 16 20 18 23 20 25 C 22 28 23 27 25 24 L 29 19 C 31 17 33 20 35 22 L 42 34')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
