# 漢字

漢字處理工具，python實現。
目前支持簡體字轉漢字。

## Install

```
pip install pyhan
```

## Example

```
from pyhan import to_traditional

if __name__ == '__main__':
    res = to_traditional('萝卜去哪了，可以在茶几卜上几卦')
    # output: 蘿蔔去哪了，可以在茶几卜上幾卦
    print(res)
```