pythons = {'chapman': 'graham', 'cleese': 'john', 'idle': 'eric', 'jones': 'terry', 'palin': 'michael'}
# pythons['gilliam'] = 'gerry'
# pythons['gilliam'] = 'terry'
others = {'marx': 'groucho', 'howard': 'moe'}
pythons.update(others)  # 딕셔너리 결합
print(pythons)
del pythons['marx']
print(pythons)
# pythons.clear()
# print(pythons)
print('idle' in pythons)  # 해당 딕셔너리 안에 idle 키값이 있는지 확인

# .get()내장 함수 사용해서 있으면, value 값을 뱉어 내고, 없으면, nothing을 뿜어냄!
print(pythons.get('idle', 'nothing'))

signals = {"green": "gp", "yellow": "go faster", "red": "smile for the camera"}
print(signals.keys())
print(list(signals.keys()))
