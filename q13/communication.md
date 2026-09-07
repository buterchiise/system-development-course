Issue: --name为空白字符时仍输出问候语

环境：Windows系统出现该问题，linux待确认

复现命令：sdt-greet --name " "

期望结果：以非零退出码结束，没有输出

实际结果：输出Hello， ！，并以零退出
