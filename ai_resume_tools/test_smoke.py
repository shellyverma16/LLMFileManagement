import json
from pathlib import Path

import fs_tools
import llm_file_assistant


def main():
    base = Path(__file__).parent / 'sample_resumes'
    print('Base resumes folder:', str(base))

    files = fs_tools.list_files(str(base))
    print('\n--- LIST FILES ---')
    print(json.dumps(files, indent=2))

    print('\n--- SEARCH FOR "Python" ---')
    results = {}
    for f in files:
        r = fs_tools.search_in_file(f['path'], 'Python')
        results[f['name']] = {'count': r.get('count'), 'matches': r.get('matches')}
    print(json.dumps(results, indent=2))

    if files:
        first = files[0]
        print('\n--- READ FIRST FILE ---')
        r = fs_tools.read_file(first['path'])
        print(json.dumps({'file': first['name'], 'success': r.get('success'), 'snippet': (r.get('content') or '')[:200]}, indent=2))

    summary_result = llm_file_assistant.simple_router('Create a summary file for resume_john_doe.txt')
    print('\n--- SUMMARY FILE FLOW ---')
    print(json.dumps(summary_result, indent=2, ensure_ascii=False))
    assert summary_result.get('success') is True, 'Summary flow should create a summary file'
    assert Path(summary_result['path']).exists(), 'Summary file should exist'


if __name__ == '__main__':
    main()
