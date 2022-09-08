import json

a = json.dumps([1, 'simple', 'list'])
# print(a, type(a), sep='\n')
path = './json/jslearn.json'
dic = {"MineCraft": {
            "type": "sandbox game", 
            "price": "100dollor"
            },
        "Hollow Knight": {
            "type": "2d fight", 
            "price": "30RMB", 
            "score": 4.9
            }
    }
# print(dic["MineCraft"]["type"])

def file():
    file = open(path, 'w')
    json.dump(dic, file)
    file.close()

    dfile = open(path, 'r')
    da = json.load(dfile)
    print(da)
    dfile.close()
# file()

def json_string():
    js = json.dumps(dic)
    jsf = json.dumps(dic, indent=4)
    print(js)
    print(jsf)
    print(type(js))
# json_string()

def sort():
    js = json.dumps(dic, indent=4)
    jsf = json.dumps(dic, indent=4, sort_keys=True)    # sort keys alphabetically
    print(js, end='\n\n')
    print(jsf)
# sort()

def delete_dictionary():
    d = {"MineCraft": {
            "type": "sandbox game", 
            "price": "100dollor"
            },
        "Hollow Knight": {
            "type": "2d fight", 
            "price": "30RMB", 
            "score": 4.9
            }
    }
    # del d['MineCraft']
    # del d
    d.clear()
    print(d)
# delete_dictionary()

def loads():
    js = json.dumps(dic)
    dics = json.loads(js)
    print(type(js))
    print(type(js.encode('ascii')))
    print(type(dics))
# loads()

def enter_Chinese_into_json():
    # https://blog.csdn.net/weixin_43834228/article/details/105768998?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-4&spm=1001.2101.3001.4242
    chinese_dic = {
        "哈哈哈": "我是中国人",
        "我": "喜欢说中文"
    }
    print(json.dumps(chinese_dic, indent=4))
    print(json.dumps(chinese_dic, indent=4, ensure_ascii=False))
    # json.dump 也是一样，加上 ensure_ascii=False 就好啦！
# enter_Chinese_into_json()


