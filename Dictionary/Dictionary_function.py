#x.keys()		��ųʸ� x�� key�� ��� dict_keys([key1, key2, ...])�������� ��ȯ
#x.valuse()	��ųʸ� x�� value�� ��� dict_values([key1, key2, ...])�������� ��ȯ
#x.items()		��ųʸ� x�� key�� value�� Ʃ��� ���� dict_items([(key1,value1), (key2,valuse2), ...])�������� ��ȯ
#x.clear()		��ųʸ��� ��� ���� ����
#x.get(key)	x[key]�� ���������� �ش� key�� value ��ȯ
#key in x		key ���� x ��ųʸ��� �����ϴ��� �Ǻ��ϴ� Ű����
#���̽� 3���� ��ü�� ��ȯ�ϵ��� ������ ����Ʈ�� �ʿ��ϸ� list(~~~~)��������
#clear �� �� ��ųʸ��� ����� del�� ��ü��ü�� �����Ѵٴ� ������ �ٸ�
#get() �Լ��� key�� �������� ������ 'None'�� ��ȯ�ϰ� x.get(key, ����ϰ������)" �������� ǥ�ð��� x[key]�� ������ ����Ŵ
#in �Լ��� True False�� ��ȯ

animals = {'cat' : 1, 'dog' : 10, 'horse': 3}

keys = list(animals.keys())
print(keys)

values = list(animals.values())
print(values)

animals.clear()

b = 'cat' in animals
print(b)