import json
import requests

print("OMG A CHANGE 2")

thekahootid = ('1f76d2dd-4353-4d9a-ab57-71ea9607d050')

url = 'https://create.kahoot.it/details/' + thekahootid

kahoot_id = url.split('/')[-1]
answers_url = 'https://create.kahoot.it/rest/kahoots/{kahoot_id}/card/?includeKahoot=true'.format(kahoot_id=kahoot_id)
data = requests.get(answers_url).json()

j = json.dumps(data, indent=4)

print(j)
a = 0
for q in data['kahoot']['questions']:
    a = 0
    try:
        for choice in q['choices']:
            a += 1
            if choice['correct']:
                break
        num = a; a=0
        print('Q: {}\n A: {:<50} Place: {}\n  '.format(q['question'].replace('&nbsp;', ' ').replace("<b>", '').replace("</b>", '').replace("<i>", '').replace("</i>", ''), choice['answer'].replace('&nbsp;', ' '), num))

    except:
        print("\n")
