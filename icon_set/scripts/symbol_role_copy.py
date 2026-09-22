"""Copy one existing SUB32 icon's drawing into an independent SYMBOL32 icon.

Container pairing needs a real symbol-family model, not a solo/sub icon
reused in place. This produces the exact same drawing as a standalone,
independently-editable SYMBOL32 model in icon_set/model/icons/symbol/,
matching the "independent container symbol" role-copy shape already used
across the repo (see e.g. single-tail-award-badge-sub32 and its
-symbol counterpart) -- but one icon at a time, on demand, rather than the
one-time batch migration in sub_usage_categories.py.

Scoped to the common case: a module with exactly one class, subclassing
Sub32 directly via `from ._base import Sub32`, with its own build() method.
Sub icons on a specialized base (see sub/_tall_base.py, sub/_text_base.py)
have no direct symbol-family equivalent and are refused.
"""
from __future__ import annotations

import ast
import inspect
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def copy_sub_to_symbol(sub_icon_id: str, root: Path = REPO_ROOT) -> dict:
    from icon_set.model.icons.registry import factories

    models = factories()
    cls = models.get(sub_icon_id)
    if cls is None:
        raise ValueError(f'Unknown icon: {sub_icon_id}')
    if cls.family != 'sub':
        raise ValueError(f'{sub_icon_id} is a {cls.family} icon, not a sub icon.')

    source = Path(inspect.getsourcefile(cls))
    tree = ast.parse(source.read_text())

    base_import = next((n for n in tree.body if isinstance(n, ast.ImportFrom) and n.module == '_base'
                         and n.level == 1 and any(a.name == 'Sub32' and not a.asname for a in n.names)), None)
    if base_import is None:
        raise ValueError(f'{sub_icon_id} uses a specialized base with no direct symbol-family equivalent; copy it by hand.')

    classes = [n for n in tree.body if isinstance(n, ast.ClassDef)]
    if len(classes) != 1:
        raise ValueError(f'{sub_icon_id} has more than one class in its module; copy it by hand.')
    target = classes[0]
    if not (len(target.bases) == 1 and isinstance(target.bases[0], ast.Name) and target.bases[0].id == 'Sub32'):
        raise ValueError(f'{sub_icon_id} does not subclass Sub32 directly; copy it by hand.')
    if not any(isinstance(n, ast.FunctionDef) and n.name == 'build' for n in target.body):
        raise ValueError(f'{sub_icon_id} has no explicit build() method (an inherited drawing); copy it by hand.')

    new_id = sub_icon_id + '-symbol'
    if new_id in models:
        raise ValueError(f'{new_id} already exists.')
    module = inspect.getmodule(cls)
    source_id = getattr(module, 'SOURCE_ICON_ID', None)
    suffix = '_' + str(source_id).replace('-', '_') if source_id else ''
    filename = new_id.replace('-', '_') + suffix + '.py'
    target_path = root / 'icon_set/model/icons/symbol' / filename
    if target_path.exists():
        raise ValueError(f'{target_path.relative_to(root)} already exists.')

    # Every reference to Sub32 in the body stays untouched; only the import
    # source changes, so the new file needs no other edits to its drawing.
    base_import.names = [ast.alias(name='Symbol32', asname='Sub32')]

    old_name = target.name
    target.name = old_name + 'ContainerSymbol'
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id == old_name:
            node.id = target.name

    attrs = {'icon_id': new_id, 'related_origin_icon_id': sub_icon_id,
             'variant_label': 'Independent container symbol', 'usage_category': 'symbol',
             'related_group': 'sub-origin/' + sub_icon_id, 'counterpart_icon_id': sub_icon_id}
    target.body = [n for n in target.body
                   if not (isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id in attrs for t in n.targets))]
    target.body[0:0] = [ast.Assign(targets=[ast.Name(id=key, ctx=ast.Store())], value=ast.Constant(value))
                         for key, value in attrs.items()]

    ast.fix_missing_locations(tree)
    text = ast.unparse(tree) + '\n'
    compile(text, str(target_path), 'exec')
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(text)
    return {'icon_id': new_id, 'path': str(target_path.relative_to(root)), 'source_icon_id': sub_icon_id}
