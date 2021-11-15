import csv
from pypinyin import pinyin, Style
from zh_wiki import zh2Hans

nasal = {}

def has_nasal(py:str):
    if py.endswith('en') or py.endswith('eng') or py.endswith('in') or py.endswith('ing') or py.startswith('l') or py.startswith('n'):
        return True
    return False

cnt = 0
for i in range(0x4e00, 0x9fa5+1):
    ch = chr(i)
    # 去除繁体字
    if ch in zh2Hans and ch != zh2Hans[ch]:
        continue
    pys = pinyin(ch, heteronym=True, style=Style.NORMAL)[0]
    for py in pys:
        if has_nasal(py):
            if py not in nasal:
                nasal[py] = []
            nasal[py].append(ch)
            cnt += 1

print(nasal)
print(0x9fa5-0x4e00+1)
print(cnt)
nasal_keys = list(nasal.keys())
nasal_keys.sort()
print(nasal_keys)
rows = []
for nasal_key in nasal_keys:
    rows.append([nasal_key, *nasal[nasal_key]])
print(rows)
# 这样筛选出来的字还是太多太多了，好多古字现在都不用了
# 我也没找到很好的办法筛选一级字和二级字
# 因此我附带了我手工整理出来的nasal_example.csv
with open('nasal.csv', 'w', newline='', encoding='utf-8-sig') as fp:
    csv_w = csv.writer(fp)
    csv_w.writerows(rows)