from pathlib import Path
import os
import re

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = Path(os.environ.get('TRACEABILITY_ROOT', str(DEFAULT_ROOT)))
RESULTS_DIR = DATA_ROOT / 'docs/results'
RESULT_MATRIX = Path(os.environ.get('RESULT_MATRIX', str(DATA_ROOT / 'docs/results/result-matrix.md')))
ID_PATTERNS = {
    'BUILD': re.compile(r'BUILD-\d{3}'),
    'RUN': re.compile(r'RUN-\d{3}'),
    'RES': re.compile(r'RES-\d{3}'),
    'EVID': re.compile(r'EVID-\d{3}'),
}
RESULT_TARGET_RELATIONS = {
    'BUILD': ['executed_on_build', 'measured_on_build', 'collected_from_build'],
    'RUN': ['executed_in_run'],
    'RES': ['produced_result'],
    'EVID': ['produces_evidence'],
}
RESULT_PREFIXES = ['BUILD', 'RUN', 'RES', 'EVID']


def parse_markdown_table(text: str) -> list[dict[str, str]]:
    lines = [line.strip() for line in text.splitlines() if line.strip().startswith('|')]
    if len(lines) < 3:
        return []

    headers = [cell.strip() for cell in lines[0].strip('|').split('|')]
    rows = []
    for line in lines[2:]:
        cells = [cell.strip() for cell in line.strip('|').split('|')]
        if len(cells) != len(headers):
            continue
        rows.append(dict(zip(headers, cells)))
    return rows


def collect_ids(directory: Path, prefix: str) -> list[str]:
    if not directory.exists():
        return []
    pattern = ID_PATTERNS[prefix]
    ids = []
    for path in sorted(directory.glob(f'{prefix}-*.md')):
        match = pattern.search(path.read_text(encoding='utf-8'))
        if match:
            ids.append(match.group(0))
    return ids


def collect_result_ids(directory: Path) -> dict[str, list[str]]:
    return {prefix: collect_ids(directory, prefix) for prefix in RESULT_PREFIXES}


def build_result_report(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    report = {
        'BUILD missing matrix link': [],
        'RUN missing matrix link': [],
        'RES missing matrix link': [],
        'EVID missing matrix link': [],
        'Result unreferenced files': [],
    }
    result_ids = collect_result_ids(RESULTS_DIR)
    referenced_targets = {row.get('target_id') for row in rows}

    for prefix, ids in result_ids.items():
        expected_relations = RESULT_TARGET_RELATIONS[prefix]
        missing_key = f'{prefix} missing matrix link'
        for item_id in ids:
            has_link = any(
                row.get('target_id') == item_id and row.get('relation') in expected_relations
                for row in rows
            )
            if not has_link:
                report[missing_key].append(item_id)
            if item_id not in referenced_targets and not any(row.get('source_id') == item_id for row in rows):
                report['Result unreferenced files'].append(item_id)

    return report


def format_report(report: dict[str, list[str]]) -> str:
    lines = []
    for title, items in report.items():
        lines.append(f'[{title}]')
        if items:
            lines.extend(items)
        else:
            lines.append('none')
    return '\n'.join(lines)


def main() -> int:
    if not (RESULTS_DIR.exists() and RESULT_MATRIX.exists()):
        print('missing required files or directories')
        return 1

    rows = parse_markdown_table(RESULT_MATRIX.read_text(encoding='utf-8'))
    report = build_result_report(rows)
    has_failures = any(report.values())
    result_ids = collect_result_ids(RESULTS_DIR)
    result_count = sum(len(ids) for ids in result_ids.values())

    if not has_failures:
        print(f'result layer check passed ({result_count} result nodes)')
        print(format_report(report))
        return 0

    print('result layer check failed')
    print(format_report(report))
    return 2


if __name__ == '__main__':
    raise SystemExit(main())
