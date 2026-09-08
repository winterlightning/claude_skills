#!/usr/bin/env python3
"""Create an independent, editable variant without changing its parent file.

python3 icon_set/scripts/create_variant.py --icon square --family sub --label "Softer corners"
The new file is a starting copy. Modify it, then run build.py for its family.
"""
from __future__ import annotations
import argparse
import ast
import inspect
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from icon_set.model.icons.registry import factories, validate_variants


def prepare_variant(icon_id: str, family: str, label: str) -> tuple[Path, str, str]:
    registered = factories()
    validate_variants(registered)
    if icon_id not in registered:
        raise ValueError(f'Unknown icon: {icon_id}')
    factory = registered[icon_id]
    if factory.family != family:
        raise ValueError(f'{icon_id} belongs to {factory.family}, not {family}')
    if not label.strip():
        raise ValueError('Provide a short label describing the requested change')
    if getattr(factory.keyshape, 'name', '') == 'FREE':
        raise ValueError('This icon uses a per-ID FREE exception; create an approved exception for a new variant ID before scaffolding it manually.')
    source = Path(inspect.getsourcefile(factory)).resolve()
    root = factory
    while getattr(root, 'variant_of', None):
        root = registered[root.variant_of]
    number = 2
    while True:
        new_id = f'{root.icon_id}--v{number}'
        destination = source.with_name(new_id.replace('-', '_') + '.py')
        if new_id not in registered and not destination.exists():
            break
        number += 1
    tree = ast.parse(source.read_text(encoding='utf-8'))
    cls = next(node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == factory.__name__)
    # Shared modules may define other registered icons. Import those siblings,
    # rather than defining them again and producing duplicate registry IDs.
    siblings = {f.__name__ for f in registered.values()
                if f.__module__ == factory.__module__ and f is not factory}
    module_name = factory.__module__.rsplit('.', 1)[-1]
    tree.body = [ast.ImportFrom(module=module_name, names=[ast.alias(name=node.name)], level=1)
                 if isinstance(node, ast.ClassDef) and node.name in siblings else node
                 for node in tree.body]
    old_name = cls.name
    cls.name = f'{root.__name__}Variant{number}'
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id == old_name:
            node.id = cls.name
    attributes = {'icon_id': new_id, 'variant_of': icon_id, 'variant_label': label.strip()}
    def replaced(node):
        targets = node.targets if isinstance(node, ast.Assign) else [node.target] if isinstance(node, ast.AnnAssign) else []
        return any(isinstance(target, ast.Name) and target.id in attributes for target in targets)
    cls.body = [node for node in cls.body if not replaced(node)]
    insert_at = 1 if cls.body and isinstance(cls.body[0], ast.Expr) and isinstance(cls.body[0].value, ast.Constant) and isinstance(cls.body[0].value.value, str) else 0
    cls.body[insert_at:insert_at] = [ast.Assign(targets=[ast.Name(id=key, ctx=ast.Store())], value=ast.Constant(value=value)) for key, value in attributes.items()]
    ast.fix_missing_locations(tree)
    text = f'# Variant of {icon_id}; parent file remains unchanged.\n' + ast.unparse(tree) + '\n'
    compile(text, str(destination), 'exec')
    return destination, new_id, text


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--icon', required=True)
    parser.add_argument('--family', required=True, choices=['solo', 'sub', 'container'])
    parser.add_argument('--label', required=True)
    args = parser.parse_args(argv)
    try:
        destination, icon_id, text = prepare_variant(args.icon, args.family, args.label)
        # Exclusive creation also protects against another agent allocating this name.
        with destination.open('x', encoding='utf-8') as file:
            file.write(text)
    except (OSError, ValueError) as error:
        parser.exit(1, f'error: {error}\n')
    print(f'New variant: {icon_id}\nPython file: {destination}\nParent preserved: {args.icon}\nEdit the new file, then run: python3 icon_set/scripts/build.py --family {args.family}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
