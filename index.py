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

def generate_HTML_string(groups):
    start = '<!DOCTYPE NETSCAPE-Bookmark-file-1>\n' + '<!-- This is an automatically generated file.\n' +'It will be read and overwritten.\n' + 'DO NOT EDIT! -->\n' + '<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n' + '<TITLE>Bookmarks</TITLE>\n' + '<H1>Bookmarks</H1>\n'
    middle = "<DL><p>\n"
    for k, g in groups.items():
        group_line = "\t<DT><H3>" + g['title'] + "</H3>\n"
        site_lines = ""
        sites = g['sites']
        for s in sites:
            site_line = '\t\t<DT><A HREF="'+ s['url'] + '" ADD_DATE="'+ str(s['ts_created']) + '">' + s['title'] + '</A>\n'
            site_lines = site_lines + site_line
        site_lines  = "\t<DL><p>\n" + site_lines + "</DL><p>\n"
        all_lines = group_line + site_lines
        middle = middle + all_lines
    middle = middle + "</DL><p>\n"

    return start + middle



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
        with open(OUTPUT_FILE, 'w') as out_file:
            out_file.write(generate_HTML_string(groups))

if __name__ == '__main__':
    main()
