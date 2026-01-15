# JSON 형식의 데이터를 다루기 위한 도구를 가져옴
import json

# FILE_PATH : 파일이 있는 위치명, 대문자 : 상수처럼 쓰겠다는 의미
# 데이터가 저장될 파일의 경로를 변수에 저장 (상수는 대문자로 쓰는 관습이 있음)
FILE_PATH = "./data/memo.json"

# [데이터 가져오기]
# 파일을 읽어서 파이썬이 이해할 수 있는 상태로 변환
def getData():
  # 파일을 '읽기(r)' 모드로 열기
  f = open(FILE_PATH, "r", encoding="utf-8")
  # 파일 안의 JSON 내용을 파이썬 딕셔너리(객체)로 변환 
  result = json.load(f)
  # 파일 사용이 끝났으니 닫기
  f.close()
  # 변환된 데이터를 결과로 돌려줌
  return result


# [데이터 저장하기]
# 파이썬 데이터를 다시 파일에 기록
def setData(data):
  # 파일을 '쓰기(w)' 모드로 열기 → 기존 내용 덮어씀
  f = open(FILE_PATH, "w", encoding="utf-8")
  # 데이터를 파일에 저장 (ensure_ascii=False : 한글을 깨지지 않게 함)
  json.dump(data, f, ensure_ascii=False)
  # 파일 닫기
  f.close()
  # 저장 후에 목록을 자동으로 한 번 보여줌  
  list()


# [목록 출력]
# 화면에 예쁘게 표 형태로 보여줌
def list():
  # 파일에서 최신 데이터를 가져옴
  data = getData()
  # 저장된 단어가 하나라도 있다면
  if len(data["words"]) > 0:
    # 선 만들기
    line1 = "=" * 50
    line2 = "-" * 50
    print(line1)
    # 제목 출력 (\t는 탭 간격)
    print(f"번호\t내용")

    # 단어 개수만큼 반복
    for i in range(len(data["words"])):
      # 단어 사이에 구분선 출력
      if i < len(data["words"]): print(line2)
      # 해당 순서의 단어 번호(id)와 내용(word)을 출력
      print(f"{data["words"][i]["id"]}\t{data["words"][i]["word"]}")
    print(line1)

  # 단어가 하나도 없다면
  else:
    print("데이터가 없습니다.")


# [단어 추가]
def insert(word):
  # 1. 기존 데이터를 가져옴
  data = getData()

  # 2. 새로운 번호(id) 생성
  # 현재 번호들 중 가장 큰 값에 1을 더함 (없으면 0부터 시작)
  id = (max((word["id"] for word in data["words"]), default=0) + 1)

  # 3. 한 줄의 데이터로 만듦
  row = {"id": id, "word": word}

  # 4. 전체 리스트에 방금 만든 한 줄을 추가
  data["words"].append(row)

  # 4. 파일에 최종 저장
  setData(data)


# [단어 수정]
def update(id, word):
  # 1. 기존 데이터를 가져옴
  data = getData()

  # 2. 전체 단어를 하나씩 살펴봄
  for i in range(len(data["words"])):
    
    # 3. 입력한 번호와 일치하는 단어를 찾으면 (id는 숫자로 형변환해서 비교)
    if data["words"][i]["id"] == int(id):
      
      # 4. 내용을 새 단어로 바꿈
      data["words"][i]["word"] = word

      # 5. 찾았으니 반복문 종료
      break
  
  # 6. 파일에 최종 저장
  setData(data)


# [단어 삭제]
def remove(id):
  # 1. 기존 데이터를 가져옴
  data = getData()

  # 2. 전체 단어를 하나씩 살펴봄
  for i in range(len(data["words"])):

    # 3. 번호가 일치하는 것을 찾으면
    if data["words"][i]["id"] == int(id):
      
      # 4. 그 위치의 데이터를 삭제
      del data["words"][i]

      # 5. 종료
      break

  # 6. 파일에 최종 저장
  setData(data)
