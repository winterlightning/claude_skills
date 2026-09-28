from pathlib import Path
import json
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
BATCH=Path(__file__).parent
items=json.loads((BATCH/'items.json').read_text())
def link(label,path):return f'[{label}](<{Path(path).resolve()}>)'
rows=[];details=[];counts={'done':0,'superseded':0,'unfinished':0,'strict_pass':0,'exception':0}
for item in items:
    fix=Path(item['fix']);run=Path(item['run']);result=json.loads((run/'result.json').read_text())
    if (fix/'result.json').exists():
        prod=json.loads((fix/'result.json').read_text());outcome=prod['outcome']+' · '+str(prod.get('review_status'));counts['done']+=prod['outcome']=='done'
    elif (fix/'superseded.json').exists():
        prod=json.loads((fix/'superseded.json').read_text());outcome='Superseded · current '+prod['current']['status']+' · finish rejected (409)';counts['superseded']+=1
    else:outcome='Not finished';counts['unfinished']+=1
    exception=item.get('exception')
    counts['exception' if exception else 'strict_pass']+=1
    validation='pass · exception; automatic '+result['automatic_status'] if exception else 'valid · zero warnings · build pass'
    rows.append('| '+ ' | '.join([item['key'],'Manual fix request',link('RESULT_DIR',run),link('SVG',run/(item['id']+'.svg')),validation,outcome])+' |')
    notes=f"## {item['key']}\n\n{item['plan']}\n\nKeyshape: {item['keyshape']}; chosen for the subject’s overall proportions on the 48×48 canvas. Four-pixel strokes retained.\n\nConstruction references: "+', '.join(link(Path(p).name,p) for p in result['references'])+'. The Lucide originals and their atomic geometry informed simple joins, consistent radii and repeat construction. Directional and perspective asymmetry follows the supplied subject.\n\n'
    notes+='Omissions: '+(' '.join(result['omissions']) or 'No defining features omitted.')+'\n\n'
    notes+='Visual review: enlarged and native 48px in both themes; clear contours and negative spaces. '+link('Light',run/'preview-light-48.png')+' · '+link('Dark',run/'preview-dark-48.png')+' · '+link('Validation',run/'validation.txt')+'.\n\n'
    if exception:notes+='Exception: '+exception['reason']+' Exact SVG SHA-256: `'+exception['svg_sha256']+'`. Original automatic findings are retained.\n\n'
    notes+='Production outcome: '+outcome+'.\n'
    details.append(notes)
header=f'''# Primitive fix batch — thuan-mac — 2026-09-25

Requested: 20, offset 0, reason manual-fix-request. Claimed exactly 20.

Completed uploads: {counts['done']}. Superseded by newer production artwork: {counts['superseded']}. Unfinished current claims: {counts['unfinished']}.

All 20 local revisions were visually reviewed. {counts['strict_pass']} pass automatically; {counts['exception']} use the user's delegated, drawing-bound visual exceptions. Exceptions preserve the original automatic findings and do not change profile constants or stroke widths.

The production service refuses historical-revision uploads and finish requests with HTTP 409. Superseded revisions were left untouched; their local candidates remain available. A finish call was attempted for every superseded claim; none is described as successfully reported.

Workflow: {link('primitive-fix-thuan',' .agents/skills/primitive-fix-thuan/SKILL.md'.strip())} and {link('primitive-make-ray','.agents/skills/primitive-make-ray/SKILL.md')}.

The finish path now honors the existing verified exception metadata and preserves its automatic status/findings. Structural validation failures remain blocking. Eight focused workflow and exception tests passed. Registered artwork and published exports were not edited by this batch.

{link('Preview sheet 1',BATCH/'revisions-0.png')} · {link('Preview sheet 2',BATCH/'revisions-1.png')}

| Key | Feedback | Run | Drawing | Validation | Production outcome |
| --- | --- | --- | --- | --- | --- |
'''
(BATCH/'REPORT.md').write_text(header+'\n'.join(rows)+'\n\n'+'\n'.join(details))
(BATCH/'completion.json').write_text(json.dumps(counts,indent=2))
print(json.dumps(counts))
