检测protobuf 是否有重复项，是否使用未定义项
=================

```bash
python check_protobuf.py test/test.proto
#result
#Repeat item:
#['PkgUserRegisterRsp']
#Total:7
#Total after remove repeat items:6
#Used but not defined:[]
```