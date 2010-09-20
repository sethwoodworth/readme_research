import csv
import os.path
import re
import urllib

def find_readmes(list):
    for r in list:
        proj = re.sub('/', '_', r[1])
        cat = r[0][3:-2]
        html = urllib.urlopen('http://github.com/api/v2/yaml/blob/all/' + r[1] + '/master')
        for row in html:
            if re.search("readme", row, re.I):
                readme_file = row[2:-43]
                url = 'http://github.com/' + r[1] + '/raw/master/' + readme_file
                r_me = urllib.urlopen(url).read()
                f = open('./readme/' + cat + '/' + proj + '/' + re.sub('/', '_7_', readme_file), 'w')
                f.write(r_me)
                f.close()
            

def make_folders(list):
    for row in list:
        category = row[0][3:-2]
        project = re.sub('/', '_', row[1])
        if not os.path.isdir("./readme/" + category + "/"):
            os.mkdir("./readme/" + category + "/")
        if not os.path.isdir("./readme/" + category + "/" + project + "/"):
            os.mkdir("./readme/" + category + "/" + project + "/")


def load_csv():
    c = csv.reader(open('./github_data.csv', 'r'))
    list = []
    for row in c:
        list.append(row)
    return list

if __name__ == '__main__':
    list = load_csv()
    make_folders(list)
    find_readmes(list)


#http://github.com/aslakhellesoy/cucumber/raw/master/lib/README.rdoc
#http://github.com/api/v2/yaml/blob/all/defunkt/facebox/master
