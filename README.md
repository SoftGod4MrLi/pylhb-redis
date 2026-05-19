# pylhb-redis

[![PyPI version](https://img.shields.io/pypi/v/pylhb-redis.svg)](https://pypi.org/project/pylhb-redis/)
[![GitHub stars](https://img.shields.io/github/stars/SoftGod4MrLi/pylhb-redis?style=flat&logo=github)](https://github.com/SoftGod4MrLi/pylhb-redis)
[![GitHub license](https://img.shields.io/github/license/SoftGod4MrLi/pylhb-redis?style=flat)](https://github.com/SoftGod4MrLi/pylhb-redis/blob/main/LICENSE)
![GitHub repo size](https://img.shields.io/github/repo-size/SoftGod4MrLi/pylhb-redis?style=flat)
[![GitHub forks](https://img.shields.io/github/forks/SoftGod4MrLi/pylhb-redis?style=flat&logo=github)](https://github.com/SoftGod4MrLi/pylhb-redis)

pylhb-redis 是我在工作过程中陆续整理的一个 Python Redis 工具包，里面就放在一个关于Redis操作的类及相关函数。与其说是一个正式的开源项目，不如说是我自己的“代码杂物间”——只不过把它打包了一下，方便在不同项目之间复用。
> 由于是个人使用为主，很多设计可能带着比较强的个人习惯，也未必是最优解。如果您发现了问题或有更好的建议，非常欢迎指正。

## 安装
```
pip install pylhb-redis
```

## 🌺mypymssql模块

Redis操作

使用示例：

```
from pylhb-redis.myredis import MyRedis

if __name__=="__main__":
    r=MyRedis()
    # 键值对测试
    print("--键值对测试--")
    r.set("Name","Mr.Lee")
    name=r.get("Name")
    print(name)

    # 哈希表
    print("--哈希表测试--")
    hdata={
        "Name":"Mr.Lee",
        "Age":19
    }
    r.hset("Man",hdata)
    name=r.hget("Man","Name")
    age=r.hget("Man","Age")
    print(name,age)
    
    # 列表处理
    print("--列表处理--")
    names=["小红","小明"]
    r.lpush("Studends",names)
    students=r.lrangle("Studends")
    print(students)

    # 集合处理
    print("--集合处理--")
    names=["李生","孔姐","李生"]
    r.sadd("Peoples",names)
    mans=r.smemebers("Peoples")
    print(mans)

    # 遍历所有键
    print("--遍历所有键--")
    r.fetchAll()

    # 清除所有键
    print("--清除所有键--")
    r.flushall()
```
