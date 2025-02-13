# 漢字

漢字處理工具。當前支持簡化字轉漢字。

附：[《通用規範漢字表》](./files/)

## 安裝

```
pip install pyhan
```

## 示例

```
from pyhan import to_traditional

if __name__ == '__main__':
    res = to_traditional('萝卜去哪了，可以在茶几卜上几卦')
    # output: 蘿蔔去哪了，可以在茶几卜上幾卦
    print(res)
```

## 完善

如果你需要增加规则，可以编辑 [st2.csv](./src/pyhan/files/st2.csv) 文件, 例如：

```csv
卜,蔔,-1|0|萝
卜,卜
```

會匹配第三列及以後，這裡是`-1|0|萝`，`-1`代表索引開始，`0`代表索引結束，`萝`代表匹配的目標詞，如果匹配成功，返回第二列

如果沒有第三列，返回第二列

### 測試

```
make test
```

## 貢獻

你可以按照以下步驟貢獻代碼：

1. Fork 本倉庫。
2. 提交 pull request。