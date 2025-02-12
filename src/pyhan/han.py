import os


class Han:
    _dataset = {}
    _dataset2 = {}

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Han, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._initialized = True
            base_dir = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(base_dir, 'files/st.csv')
            with open(file_path) as f:
                for i in f:
                    arr = i.strip().split(',', 1)
                    self._dataset[arr[0]] = arr[1].split(',')

            file_path2 = os.path.join(base_dir, 'files/st2.csv')
            with open(file_path2) as f:
                for i in f:
                    arr = i.strip().split(',', 1)
                    if arr[0] not in self._dataset2:
                        self._dataset2[arr[0]] = []
                    self._dataset2[arr[0]].append(arr[1].split(','))

    def __predict(self, idx, original):
        character = original[idx]
        if character in self._dataset2:
            current = self._dataset2[character]
            for i in current:
                if len(i) > 1:
                    for ii in i[1:]:
                        arr = ii.split('|')
                        if original[idx + int(arr[0]):idx + int(arr[1])] == arr[2]:
                            return i[0]
                else:
                    return i[0]

    def __match(self, idx, original):
        character = original[idx]
        if character not in self._dataset:
            return character
        else:
            arr = self._dataset[character]
            if len(arr) == 1:
                return arr[0]
            else:
                character_predict = self.__predict(idx, original)
                return character_predict if character_predict else character

    def to_traditional(self, original):
        return ''.join([self.__match(i, original) for i in range(len(original))])


if __name__ == '__main__':
    print(Han().to_traditional('萝卜去哪了，可以在茶几卜上几卦'))
