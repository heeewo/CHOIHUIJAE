#x.keys()		딕셔너리 x의 key만 모아 dict_keys([key1, key2, ...])형식으로 반환
#x.valuse()	딕셔너리 x의 value만 모아 dict_values([key1, key2, ...])형식으로 반환
#x.items()		딕셔너리 x의 key와 value를 튜블로 묶어 dict_items([(key1,value1), (key2,valuse2), ...])형식으로 반환
#x.clear()		딕셔너리의 모든 값을 삭제
#x.get(key)	x[key]와 마찬가지로 해당 key의 value 반환
#key in x		key 값이 x 딕셔너리에 존재하는지 판별하는 키워드
#파이썬 3부터 객체를 반환하도록 수정함 리스트가 필요하면 list(~~~~)형식으로
#clear 는 빈 딕셔너리를 만들고 del은 객체자체를 삭제한다는 점에서 다름
#get() 함수는 key가 존재하지 않으면 'None'을 반환하고 x.get(key, 출력하고싶은값)" 설정으로 표시가능 x[key]는 오류를 일으킴
#in 함수는 True False를 반환

animals = {'cat' : 1, 'dog' : 10, 'horse': 3}

keys = list(animals.keys())
print(keys)

values = list(animals.values())
print(values)

animals.clear()

b = 'cat' in animals
print(b)