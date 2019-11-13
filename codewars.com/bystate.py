# https://www.codewars.com/kata/bystate/train/python


def by_state(s: str):
    acronym2name = {
        'AZ': 'Arizona',
        'CA': 'California',
        'ID': 'Idaho',
        'IN': 'Indiana',
        'MA': 'Massachusetts',
        'OK': 'Oklahoma',
        'PA': 'Pennsylvania',
        'VA': 'Virginia',
    }
    result = {k: [] for k in acronym2name.keys()}
    for line in s.splitlines():
        for current_acronym in acronym2name:
            if line.endswith(current_acronym):
                acronym = current_acronym
                break
        else:
            raise Exception(line)
        line = line[::-1].replace(  # rreplace xD
            acronym[::-1], acronym2name[acronym][::-1], 1
        )[::-1]
        result[acronym].append(line.replace(',', ''))
    result = {acronym2name[a]: sorted(result[a]) for a in result}
    result = {n: ''.join(f'..... {x}\r\n' for x in result[n]) for n in result}
    result = ''.join(f' {n}\r\n{result[n]}' for n in result if result[n])
    return result[1:-2]
