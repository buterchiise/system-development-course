
Issue: --name为空白字符时仍输出问候语

环境：Windows系统出现该问题，linux待确认

复现命令：sdt-greet --name " "

期望结果：以非零退出码结束，没有输出

实际结果：输出Hello， ！，并以零退出

提交意见
标题：修复姓名为空时仍输出问候语问题
问题：当--name仅包含空白字符时，程序仍输出问候语并以0退出。解决：增加空白检查，若空白则systemexit（2）。

评审意见
Blocking：--name为空白时未做校验，会输出无意义问候语。建议在main函数中用str.isspace()判断，若空白则sys.exit（2）。
Suggestion：可补充对应测试。
Nit：可考虑增加姓名校验独立函数。
