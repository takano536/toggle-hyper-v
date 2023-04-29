[English](https://github.com/takano536/toggle-hyper-v/blob/master/README_EN.md)  
# toggle-hyper-v
本ツールは、Windows 10 Proで[Hyper-V](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/)の切り替えを自動化するツールです。  
[こちらのリリースページ](https://github.com/takano536/toggle-hyper-v/releases)からダウンロードすることができます。

## 使い方
「ToggleHyperV.exe」は、CLIソフトです。ダブルクリックで起動します。管理者権限で実行してください。    
起動後、現在Hyper-Vが有効かどうかが表示されます。  
Hyper-Vを切り替える場合は「Yes」を、切り替えない場合は「No」を入力してください。
```
Hyper-V is deactivated
Do you want to switch to Hyper-V? [Y/n] >
```
入力後、Hyper-Vの切り替えに成功したかどうかが表示されます。  
その後、再起動するかどうか尋ねられます。同様に、「Yes」または「No」を入力してください。
```
Hyper-V is deactivated
Do you want to switch to Hyper-V? [Y/n] > Yes
Hyper-V switching finished successfully
Do you want to reboot? [Y/n] >

```
## ライセンス
本ソフトは無保証です。詳しくは[LICENSE](https://github.com/takano536/toggle-hyper-v/blob/master/LICENSE)をご覧ください。
