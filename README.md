# 漢字

漢字處理工具，python實現。
目前支持簡體字轉漢字。

## all language

## install

```
pip install pyhan
```

## example

```
from pyhan import to_traditional

if __name__ == '__main__':
    res = to_traditional('萝卜去哪了，可以在茶几卜上几卦')
    print(res)
```