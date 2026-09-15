"""Cache identity for QA overlays and the circle/hole rules they depend on."""
from pathlib import Path
import hashlib
ROOT = Path(__file__).resolve().parents[2]
def checker_fingerprint():
    paths = ['qa_overlays.py', 'icon_set/scripts/qa_fingerprint.py',
             'icon_set/validation/library_qa.py', 'icon_set/validation/hole_geometry.py',
             'icon_set/validation/circle_exceptions.py',
             'icon_set/model/contracts/negative-space.v1.json',
             'icon_set/model/contracts/icon-profile.v1.json']
    digest = hashlib.sha256()
    for name in paths:
        digest.update(name.encode()); digest.update((ROOT/name).read_bytes())
    return digest.hexdigest()
