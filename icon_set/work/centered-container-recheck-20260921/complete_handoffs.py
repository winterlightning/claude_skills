"""Add reuse guidance without changing the five-field icon subject contract."""
import hashlib,json,re
from pathlib import Path
P=Path(__file__).resolve().parent
plans=json.loads((P/'authoring-plans.json').read_text())
for number,plan in plans.items():
    p=Path(plan['brief_path']); assert p.is_file()
    subject=plan['subject']; stem=Path(plan['source_copy']).stem
    content=p.read_text().split('\n## Reuse and source identity\n')[0]
    content=re.sub(r'^- tags:.*$', '- tags: '+', '.join(subject['tags']),content,flags=re.M)
    content=content.replace('/icon-solo','$icon-solo')
    target=plan['existing_target']
    guidance={
        'new_solo':'No suitable existing whole icon was found in the reviewed inventory. Author one solo icon for the shared concept.',
        'repair_existing':'Repair the existing source-matched solo icon under its current icon_id. Do not create a second model for the same source.',
        'adapt_to_solo':'Use the mapped existing artwork as the starting point and match the complete reference subject in the solo family. Search the live library again before authoring to avoid a concurrent duplicate.'
    }[plan['operation']]
    content+='\n## Reuse and source identity\n\n'+guidance+'\n\n'
    content+=f"- Existing artwork: `{target or 'none matched'}`\n- Operation: `{plan['operation']}`\n"
    content+=f"- Original source: `{plan['reference_path']}`\n- Source UUID: `{plan['source_uuid']}`\n"
    content+=f"- Unchanged source copy: `{plan['source_copy']}`\n- Source SHA-256: `{plan['source_sha256']}`\n"
    content+=f"- Inspected 320 px render: `{P/'solo-briefs/png'/f'{stem}.png'}`\n"
    content+=f"- Inspected native 48 px render: `{P/'solo-briefs/png'/f'{stem}@48.png'}`\n"
    content+=f"- Shared review references: {', '.join('#'+str(n) for n in plan['source_numbers'])}\n\n"
    content+='Carry the complete reference UUID and original path into SOURCE_ICON_ID and SOURCE_PATH. This handoff prepares files only; no job is queued.\n'
    p.write_text(content)
    p.with_suffix('.json').write_text(json.dumps(subject,indent=2)+'\n')
    assert hashlib.sha256(Path(plan['source_copy']).read_bytes()).hexdigest()==plan['source_sha256']
    assert all((P/'solo-briefs/png'/f'{stem}{suffix}.png').is_file() for suffix in ('','@48'))
print('Completed',len(plans),'five-field solo handoffs.')
