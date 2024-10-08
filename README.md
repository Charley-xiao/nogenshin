# nogenshin 不要原神！

Are you a developer who's tired of seeing the same boring errors in your code? Want to turn debugging into an adventure? Look no further—**nogenshin** is here to save the day (and your sanity)!

你是那个已经厌倦了自己代码里那些千篇一律的报错的开发者吗？想把调试代码变成一次冒险之旅吗？别再找了——**nogenshin** 出场拯救你（和你的理智）了！

## What is nogenshin? 什么是不要原神？

`nogenshin` is the Python library you never knew you needed. It's simple: whenever your code throws an error inside a function decorated with `@nogenshin.start`, it will launch **Genshin Impact** instead of leaving you staring at an ugly stack trace. Because if you're going to suffer, you might as well enjoy it!

`nogenshin` 是一个你从未意识到自己需要的 Python 库。它的原理很简单：每当你代码中某个被 `@nogenshin.start` 装饰器装饰的函数抛出错误时，它不会给你显示丑陋的堆栈信息，而是直接启动《原神》。因为，如果注定要受苦，那为什么不选择开心点呢？

## Installation 安装

First, make sure you're ready for chaos:

首先，确保你已经做好迎接混乱的准备：

```bash
pip install nogenshin

# Or, if you're feeling adventurous:
pip install git+https://github.com/Charley-xiao/nogenshin.git
```

And, of course, Genshin Impact must already be installed on your system. If it's not, what are you even doing here?

当然，你的电脑上必须已经安装了《原神》。如果还没有安装，你为什么不装？《原神》怎么你了？

## Usage 用法

Here's how you can embrace your inner Traveler (and bug-hunter):

以下是如何激发你内心旅行者（兼 bug 猎手）灵魂的操作：

```python
import os 
# This is optional. If your game follows this path, you don't need to set it.
os.environ['GENSHIN_IMPACT_PATH'] = 'C:/Program Files/Genshin Impact/GenshinImpact.exe'

import nogenshin

@nogenshin.start
def buggy_function():
    print("This will probably break...")
    raise ValueError("Oops!")

buggy_function()  # Prepare for adventure if it fails!
```

When an exception happens, instead of fixing the error, nogenshin will fire up Genshin Impact and let you chill in Teyvat while you contemplate your life choices.

当你的代码发生异常时，nogenshin 会自动启动《原神》，让你在提瓦特的美景中反思人生选择，而不是盯着报错发呆。

## Why? 为什么？

Why not? Debugging is stressful. Go fight some hilichurls instead. Or go get that 5-star character you’ve been dreaming of while your bugs roam free.

为什么不呢？调试代码太压力山大了。去打打丘丘人，放松一下吧！或者去抽你梦寐以求的五星角色，让 bug 自由飞翔。

## How It Works 它怎么工作的

Step 1: Write code.

Step 2: Wrap your error-prone functions with `@nogenshin.start`.

Step 3: When your code blows up, nogenshin launches Genshin Impact.

Step 4: ????

Step 5: Profit (or cry about not getting Zhongli again).

第一步： 写代码。

第二步： 用 `@nogenshin.start` 包裹那些容易出问题的函数。

第三步： 当代码崩溃时，nogenshin 启动《原神》。

第四步： ????

第五步： 水到渠成（或者继续哭着抱怨抽不到钟离）。

## FAQ 常见问题

Q: Will this help me debug my code?

A: Not even a little.

Q: Why Genshin Impact?

A: Why not?

Q: What if I actually want to fix my bugs?

A: That’s a 'you' problem.

Q: Is there a way to choose different games?

A: No. You either launch Genshin, or you face your errors alone. Just joking, you can set the `GENSHIN_IMPACT_PATH` environment variable to the path of your game.

问： 这个库能帮我调试代码吗？

答： 完全不能。

问： 为什么是《原神》？

答： 为什么不是呢？

问： 如果我真的想修复 bug 怎么办？

答： 那是你的问题，不是我的。

问： 能选择其他游戏吗？

答： 不行。要么启动原神，要么面对自己那满屏的错误。（开玩笑的，你可以设置 `GENSHIN_IMPACT_PATH` 环境变量为你游戏的路径）

## Disclaimer 免责声明

Use at your own risk. This library will absolutely not fix your code. But hey, at least you’ll have fun, right? And yes, this might reduce your productivity. But isn't that what coding is all about?

使用本库请自担风险。nogenshin 绝对不会帮你修复代码。但嘿，至少你可以玩得开心嘛！对，没错，这可能会大大降低你的工作效率。但编程不就是为了快乐吗？

**nogenshin**: Turning every error into an adventure. Now go out there and debug... or pull for characters. Your call.

**nogenshin**：让每一次报错都变成一场冒险。现在去吧，调试代码...还是抽卡，全看你了。