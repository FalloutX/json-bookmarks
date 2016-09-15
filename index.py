import json
from config import INPUT_FILE, OUTPUT_FILE

def group_sites(groups, sites):
    result = {}
    for k,v in groups.items():
        result_key = v['id']
        result[result_key] = v
        result[result_key]['sites'] = []

    for k,v in sites.items():
        group_id = v['idgroup']
        print(group_id, k)
        result[group_id]['sites'].append(v)

    return result


def main():
    with open(INPUT_FILE) as input_file:
        data = json.load(input_file)
        groups = data['groups']
        sites = data['dials']

        # print("len(groups) =>", len(groups))
        # print("len(sites) =>", len(sites))
        groups = group_sites(groups, sites)
        print(groups)
        for g,v in groups.items():
            print(g, v['title'], len(v['sites']))

if __name__ == '__main__':
    main()
