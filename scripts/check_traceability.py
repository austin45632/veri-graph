from pathlib import Path
import os
import re

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = Path(os.environ.get('TRACEABILITY_ROOT', str(DEFAULT_ROOT)))
MATRIX = Path(os.environ.get('TRACEABILITY_MATRIX', str(DATA_ROOT / 'docs/traceability/trace-matrix.md')))
REQ_DIR = DATA_ROOT / 'docs/requirements'
TR_DIR = DATA_ROOT / 'docs/test-requirements'
TC_DIR = DATA_ROOT / 'docs/testcases'
TS_DIR = DATA_ROOT / 'docs/test-scripts'
ID_PATTERNS = {
    'REQ': re.compile(r'REQ-\d{3}'),
    'TR': re.compile(r'TR-\d{3}'),
    'TC': re.compile(r'TC-\d{3}'),
    'TS': re.compile(r'TS-\d{3}'),
}


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


def build_traceability_report(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    report = {
        'REQ missing TR': [],
        'TR missing TC': [],
        'TC missing TS': [],
        'Unreferenced files': [],
    }
    req_ids = collect_ids(REQ_DIR, 'REQ')
    tr_ids = collect_ids(TR_DIR, 'TR')
    tc_ids = collect_ids(TC_DIR, 'TC')
    ts_ids = collect_ids(TS_DIR, 'TS')

    for req_id in req_ids:
        if not any(row.get('source_id') == req_id and row.get('relation') == 'validated_by' for row in rows):
            report['REQ missing TR'].append(req_id)

    for tr_id in tr_ids:
        if not any(row.get('source_id') == tr_id and row.get('relation') == 'verified_by' for row in rows):
            report['TR missing TC'].append(tr_id)

    for tc_id in tc_ids:
        if not any(row.get('source_id') == tc_id and row.get('relation') == 'implemented_by' for row in rows):
            report['TC missing TS'].append(tc_id)

    referenced_targets = {row.get('target_id') for row in rows}
    for tr_id in tr_ids:
        if tr_id not in referenced_targets and not any(row.get('source_id') == tr_id for row in rows):
            report['Unreferenced files'].append(tr_id)
    for tc_id in tc_ids:
        if tc_id not in referenced_targets and not any(row.get('source_id') == tc_id for row in rows):
            report['Unreferenced files'].append(tc_id)
    for ts_id in ts_ids:
        if ts_id not in referenced_targets and not any(row.get('source_id') == ts_id for row in rows):
            report['Unreferenced files'].append(ts_id)

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
    required_paths = [MATRIX, REQ_DIR, TR_DIR]
    if not all(path.exists() for path in required_paths):
        print('missing required files or directories')
        return 1

    traceability_rows = parse_markdown_table(MATRIX.read_text(encoding='utf-8'))
    traceability_report = build_traceability_report(traceability_rows)
    has_failures = any(traceability_report.values())

    req_ids = collect_ids(REQ_DIR, 'REQ')
    tr_ids = collect_ids(TR_DIR, 'TR')
    tc_ids = collect_ids(TC_DIR, 'TC')
    ts_ids = collect_ids(TS_DIR, 'TS')

    if not has_failures:
        print(
            'traceability check passed '
            f'({len(req_ids)} REQ, {len(tr_ids)} TR, {len(tc_ids)} TC, {len(ts_ids)} TS)'
        )
        print(format_report(traceability_report))
        return 0

    print('traceability check failed')
    print(format_report(traceability_report))
    return 2


if __name__ == '__main__':
    raise SystemExit(main())
