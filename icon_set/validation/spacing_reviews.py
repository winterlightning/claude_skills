"""Explicit visual decisions for exact sampled opposing-edge findings.

These records never waive model validation, certified MIC, or hole checks.
Changing the SVG, rules, or flagged pair invalidates the recorded decision.
"""
from pathlib import Path
import json


REVIEW_PATH = Path(__file__).resolve().parents[1] / 'model' / 'contracts' / 'spacing-reviews.v1.json'


def apply_spacing_reviews(icon, result, svg_sha256, rules_sha256, *, records=None):
    if records is None:
        records = json.loads(REVIEW_PATH.read_text()) if REVIEW_PATH.exists() else {}
    if records.get('version') != 1:
        return result
    record = records.get('icons', {}).get(f'{icon.family}/{icon.icon_id}', {})
    if (record.get('svg_sha256') != svg_sha256
            or record.get('rules_sha256') != rules_sha256
            or not record.get('reviewer') or not record.get('reason')):
        return result
    accepted = {tuple(sorted(pair)) for pair in record.get('elements', [])}
    findings = []
    for finding in result['findings']:
        item = dict(finding)
        if tuple(sorted(item['elements'])) in accepted:
            item['visual_review'] = {
                'decision': 'retain', 'reviewer': record['reviewer'],
                'reason': record['reason'], 'evidence': record.get('evidence'),
            }
        findings.append(item)
    reviewed = sum('visual_review' in item for item in findings)
    fully_reviewed = bool(findings) and reviewed == len(findings)
    return {**result, 'findings': findings,
            'measured_status': result['status'], 'reviewed_finding_count': reviewed,
            'status': 'reviewed' if fully_reviewed else result['status'],
            'notice': ('Sampled findings retained after explicit visual review of this exact drawing. '
                       'Model spacing and hole checks still apply.' if fully_reviewed
                       else result.get('notice', 'Unresolved sampled findings require review.'))}
