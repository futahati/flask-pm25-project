# VScode快捷鍵

- https://vscode.com.tw/docs/reference/default-keybindings

## 註解

|   快捷鍵組合    | 說明     |
| :-------------: | :------- |
|    Ctrl + /     | 單行註解 |
| Shift + Alt + A | 區塊註解 |

## 其他

|    快捷鍵組合    | 說明                 |
| :--------------: | :------------------- |
|     Ctrl + F     | 搜尋                 |
|     Ctrl + H     | 取代                 |
|     Ctrl + D     | 選取相同字串         |
|     Ctrl + ,     | 開啟Settings設定     |
| Alt + Shift + F  | 格式化程式碼         |
| Ctrl + Shift + F | 顯示搜尋(側邊欄)     |
| Ctrl + Shift + H | 在檔案中取代(側邊欄) |

## 行的處理

|          快捷鍵組合          | 說明                                     |
| :--------------------------: | :--------------------------------------- |
|           Ctrl + L           | 選取整行                                 |
|          Alt + ↑ ↓           | 目前游標所在行，整行向上或向下移動       |
|      Alt + Shift + ↑ ↓       | 目前游標所在行，複製整行並向上或向下移動 |
| Ctrl + G ⇨⇨ 輸入`行號(數字)` | 跳到該檔案的某行號                       |
|           Alt + Z            | 自動換行                                 |
|         Ctrl + Home          | 移至程式碼開頭                           |
|          Ctrl + End          | 移至程式碼結尾                           |

## 摺疊／展開程式碼

|      快捷鍵組合      | 說明                 |
| :------------------: | :------------------- |
| Ctrl + K ⇨⇨ Ctrl + 0 | 摺疊所有程式碼       |
| Ctrl + K ⇨⇨ Ctrl + J | 展開所有程式碼       |
|   Ctrl+K ⇨⇨ Ctrl+[   | 摺疊所有子區域程式碼 |
|   Ctrl+K ⇨⇨ Ctrl+]   | 展開所有子區域程式碼 |
|   Ctrl + Shift + [   | 摺疊區域程式碼       |
|   Ctrl + Shift + ]   | 展開區域程式碼       |

## 可視視窗處理(側邊欄、下方面板等)

|            快捷鍵組合             | 說明                                       |
| :-------------------------------: | :----------------------------------------- |
|             Ctrl + =              | app視窗放大                                |
|             Ctrl + -              | app視窗縮小                                |
|             Ctrl + `              | 開啟／關閉終端機面板                       |
|         Ctrl + Shift + `          | 開啟並聚焦於新終端機分頁                   |
|             Ctrl + J              | 顯示／隱藏下方面板（Panel）                |
|         Ctrl + Shift + E          | 開啟並聚焦於「檔案總管」（Explorer）側邊欄 |
|             Ctrl + B              | 顯示／隱藏側邊欄                           |
| Ctrl + Shift + P ⇨⇨ 輸入`minimap` | 使用指令面板，顯示／隱藏縮圖               |

- 完全關閉縮圖功能 _minimap_

1. `Ctrl + ,`
1. 搜尋列 輸入 `minimap`
1. 找 Editor → Minimap:Emabled
1. 取消勾選(或設定為False)

## 問題

|    快捷鍵組合    | 說明                 |
| :--------------: | :------------------- |
| Ctrl + Shift + M | 顯示問題             |
|        F8        | 前往下一個錯誤或警告 |
|    Shift + F8    | 前往上一個錯誤或警告 |
|                  |                      |
|                  |                      |

## 使用 requirements.txt 建立，並設定虛擬環境

- 條件：資料夾裡有 `requirements.txt`
  1. Ctrl + Shift + P --- 開啟命令面板
  2. 輸入→選擇 `Python: Create Environment`
  3. 選擇環境類型
     - 首選 Venv Creates a `.venv` virtual environment in the current workspace
     - 次選 Conda Creates a `.conda` Conda environment in the current workspace
  4. 選擇基礎 Python 解譯器版本
     - 例：Python 3.11.9 ~\AppData\Local\programs\Python|python311\python.exe
  5. 勾選或選擇你的 requirements.txt 檔案
     - 打勾勾 ⬜ requirements.txt
  6. 按 `OK`

- 確認虛擬環境是否安裝成功
  1. 打開一個.py檔案
  2. 右下角點擊狀態列的 Python 版本號(出現2個)
     - 3.11.9 (.venv)：代表目前專案資料夾裡的 .venv 虛擬環境。
       - 建議點擊 3.11.9 (.venv) 這個選項。
       - 確保你在 VS Code 終端機 (Terminal) 中執行程式，以及按下右上角的「執行」按鈕時，都是使用此專案專屬的虛擬環境，避免套件版本衝突。
     - .venv (3.11.9)：代表環境的「名稱」或「類別」，後面括號標註其底層使用的 Python 版本。
  3. 打開 VS Code 終端機``Ctrl + Shift + ` `` 輸入 `python --version` 來驗證目前使用的 Python 版本號。
