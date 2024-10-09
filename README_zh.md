# nogenshin

[![PyPI package](https://img.shields.io/pypi/v/nogenshin)](https://pypi.org/project/nogenshin/)
[![Last Commit](https://img.shields.io/github/last-commit/Charley-xiao/nogenshin)](https://github.com/Charley-xiao/nogenshin/commits/master)

你是不是已经对代码里那些千篇一律的错误弹窗感到麻木了？想让调试变得像冒险一样充满惊喜吗？不用再找了，**nogenshin** 来拯救你（和你的精神）了！

---

[GitHub 仓库](https://github.com/Charley-xiao/nogenshin) | [English README](https://github.com/Charley-xiao/nogenshin/blob/main/README.md)

---

## nogenshin 是什么？

`nogenshin` 是那个你从来不知道自己需要的 Python 库！它的工作原理非常简单：只要在你装饰了 `@nogenshin.start` 的函数里抛出异常，**原神**就会自动启动！因为如果你注定要遭遇 bug 的折磨，为什么不顺便享受一下呢？

当然，这还不够！在 `v0.2.0` 版本中，我们推出了新的 `@nogenshin.stop`，让你可以在代码崩溃时关闭**原神**。是的，现实总要回来的（但你确定真的想退出吗？）

## 安装

准备好迎接混乱了吗？来吧：

```bash
pip install nogenshin

# 或者，如果你是个喜欢冒险的人：
pip install git+https://github.com/Charley-xiao/nogenshin.git
```

**注意**：你必须已经在电脑上安装了**原神**。还没装？那还等什么呢？**原神**怎么你了？赶紧下载！

## 使用方法

### @nogenshin.start 的体验™️

```python
import nogenshin

@nogenshin.start
def buggy_function():
    print("这代码马上要崩...")
    raise ValueError("哎呀！")

buggy_function()  # 准备好去提瓦特放松一下吧！
```

当发生异常时，nogenshin 不会让你头疼地面对那些可怕的报错信息，而是直接把你送去**原神**的世界，给你一个稍事休息的机会。去抽一个五星角色，或者痛揍几个史莱姆吧！

### @nogenshin.stop 的超能力

如果你终于意识到你得回归现实、真正去解决那些代码问题时：

```python
@nogenshin.stop
def stop_playing():
    print("代码出问题了……关闭原神吧。")
    raise RuntimeError("是时候认真了！")

stop_playing()  # 回到现实生活……但你真的想回去吗？
```

当代码再次崩溃，而你发现也许真的需要修复某些 bug 时，`@nogenshin.stop` 会叹息，然后关掉**原神**。是的，痛苦的现实就在眼前。不过你得承认，编程确实很辛苦，不是吗？

## 为什么要这样？

因为生活很短，调试却很长。既然要面对 bug，为什么不带着派蒙一起呢？

## 工作原理

1. 写代码（最好是能运行的代码）。
2. 用 `@nogenshin.start` 或 `@nogenshin.stop` 包裹那些充满错误的函数（因为正常的调试不够刺激）。
3. 代码崩溃时，要么启动，要么关闭**原神**。
4. 接受混乱的命运。
5. 大赚一笔（或者继续悲伤地等着钟离池复刻）。

## 常见问题

### Q: 这个库能帮我修复代码吗？

A: 完全不能，但你会心情变好。

### Q: 为什么是原神？

A: 为什么*不是*原神呢？coding 崩溃时应该配得上史诗般的游戏世界！

### Q: 如果我真的想修复我的 bug 呢？

A: 那就是你的问题了，祝你好运。

### Q: 我可以选择其他游戏吗？

A: 技术上可以。你可以通过设置 `GENSHIN_PATH` 环境变量，将它指向任意游戏的可执行文件。但老实说，原神怎么你了？

### Q: 我怎么才能阻止原神的启动/停止？

A: 你居然想问这个？

## 声明

这个库**绝对不会**提高你的编程水平。它可能会因为引入太多分心的事物而降低你的工作效率，但极有可能改善你的心情（特别是当你终于抽到那个五星角色的时候）。请慎重使用，代码报错了别找我们。

**nogenshin**：让每一个错误都变成一场冒险。现在，继续写代码吧……或者沉迷于提瓦特。由你决定。

## 许可证

MIT © [Charley Xiao](https://github.com/Charley-xiao)

## 贡献

欢迎提出问题和 PR！快来贡献代码，一起加入这场疯狂吧！😊
