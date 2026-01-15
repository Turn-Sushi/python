import json

def getData() :
    f = open("./data/wordList.json", "r", encoding="utf-8")
    return json.load(f)

# 단어 리스트
def wordList() :
    print("list 호출")
    data = getData()
    arr = data["list"]
    for v in arr : print(f"id: {v['id']}, word: {v['word']}")


# 단어 추가
def add(word) :
    data = getData()
    arr = data["list"]
    if len(arr) == 0 :
        newId = 1
    else :
        newId = arr[-1]["id"] + 1
    arr.append({"id":newId, "word": word})
    f = open("./data/wordList.json", "w", encoding="utf-8")
    json.dump(data, f, ensure_ascii=False)
    print(f"등록완료 : {word} (id:{newId})")


# 단어 삭제
def delete(id) :
    data = getData()
    arr = data["list"]

    def checkId(row) :
        return row["id"] != id
    data["list"] = list(filter(checkId, arr))

    # data["list"] = list(filter(lambda row : row["id"] != id, arr))

    f = open("./data/wordList.json", "w", encoding="utf-8")
    json.dump(data, f, ensure_ascii=False)

    print(data)


# 단어 수정
def ammend(id, word) :
    data = getData()
    arr = data["list"]
    # print(arr[0]["id"])
    
    for i in range(len(arr)):
        if arr[i]["id"] == id:
            arr[i]["word"] = word
    
    print(arr)

    f = open("./data/wordList.json", "w", encoding="utf-8")
    json.dump(arr, f, ensure_ascii=False)

    # print(id, word, data)
    