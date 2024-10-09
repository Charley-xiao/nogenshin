# nogenshin

[![PyPI package](https://img.shields.io/pypi/v/nogenshin)](https://pypi.org/project/nogenshin/)
[![Last Commit](https://img.shields.io/github/last-commit/Charley-xiao/nogenshin)](https://github.com/Charley-xiao/nogenshin/commits/master)

Are you a developer who's tired of seeing the same boring errors in your code? Want to turn debugging into an adventure? Look no further—**nogenshin** is here to save the day (and your sanity)!

---

[Repository](https://github.com/Charley-xiao/nogenshin) | [中文 README](https://github.com/Charley-xiao/nogenshin/blob/main/README_zh.md)

---

## What is nogenshin?

`nogenshin` is the Python library that transforms your coding errors into epic, open-world fun. Say goodbye to stack traces and hello to Teyvat! When your code blows up, any function wrapped with `@nogenshin.start` will **launch Genshin Impact** and whisk you away from debugging woes.

And that's not all! With the new `@nogenshin.stop` in `v0.2.0`, you can finally *stop* Genshin when your bugs are getting serious. Yes, you can bring yourself back from your virtual world (but let’s be real, why would you want to?).

## Installation

Get ready to face your coding challenges head-on (or ignore them while playing Genshin):

```bash
pip install nogenshin

# Or, if you're feeling extra adventurous (or have Paimon-like energy):
pip install git+https://github.com/Charley-xiao/nogenshin.git
```

**Note**: Genshin Impact must be installed on your system. If it’s not, we can't help you there. Go download it first—priorities, people!

## Usage

### The @nogenshin.start Experience™️

```python
import nogenshin

@nogenshin.start
def buggy_function():
    print("Hold on, this will break...")
    raise ValueError("Oops!")

buggy_function()  # Time to journey into Teyvat!
```

When an error occurs, instead of frantically debugging, **nogenshin** will take you on a nice relaxing trip to the world of Genshin. Perfect timing to roll for a new 5-star character or just go vent your frustration on some slimes.

### The @nogenshin.stop Superpower

For when you actually need to, you know, *stop* playing Genshin (tragic, I know):

```python 
@nogenshin.stop
def stop_playing():
    print("This code has issues... stopping Genshin Impact.")
    raise RuntimeError("Time to get serious!")

stop_playing()  # Back to reality (but why?)
```

When your code crashes again and you realize maybe you should actually fix something, `@nogenshin.stop` will gasp close Genshin Impact. Yes, I know. It’s painful. But debugging is hard work, and eventually, someone’s got to do it.

## Why?

Because life is short, and debugging is long. Why face your errors alone when you could have Paimon by your side?

## How It Works

1. Write code (preferably the kind that works).
2. Wrap your error-prone functions with `@nogenshin.start` or `@nogenshin.stop` (because who needs normal debugging?).
3. When an exception happens, Genshin Impact either starts or stops.
4. Embrace the chaos.
5. Profit (or suffer in silence).

## FAQ

### Q: Will this help me fix my code?

A: Absolutely not. But you’ll feel better about your life choices.

### Q: Why Genshin Impact?

A: Why not? Coding errors deserve to be met with an epic game, don’t they?

### Q: What if I actually want to fix my bugs?

A: That’s between you and your error logs. Best of luck.

### Q: Can I choose a different game?

A: Technically, yes. Set the `GENSHIN_PATH` environment variable to the path of any executable game. But honestly, why would you want to play something else?

### Q: How can I prevent Genshin from starting/stopping?

A: Why would you even ask that?

## Disclaimer

This library is not guaranteed to improve your coding skills. It may reduce productivity by introducing distractions, but will likely enhance your overall mood (especially after you finally get that 5-star pull). Use at your own risk, and don't blame us if you lose track of time and end up adventuring instead of debugging.

**nogenshin**: Turning your code errors into an adventure, one bug at a time. Now go out there and either code… or lose yourself in Genshin Impact. Your call.

## License

MIT © [Charley Xiao](https://github.com/Charley-xiao)

## Contributing
Issues and pull requests are welcome! Feel free to contribute and join the madness! 😊