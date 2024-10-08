# nogenshin

Are you a developer who's tired of seeing the same boring errors in your code? Want to turn debugging into an adventure? Look no further—**nogenshin** is here to save the day (and your sanity)!

## What is nogenshin?

`nogenshin` is the Python library you never knew you needed. It's simple: whenever your code throws an error inside a function decorated with `@nogenshin.start`, it will launch **Genshin Impact** instead of leaving you staring at an ugly stack trace. Because if you're going to suffer, you might as well enjoy it!

## Installation

First, make sure you're ready for chaos:

```bash
pip install git+https://github.com/Charley-xiao/nogenshin.git
```

And, of course, Genshin Impact must already be installed on your system. If it's not, what are you even doing here?

## Usage

Here's how you can embrace your inner Traveler (and bug-hunter):

```python
import nogenshin

@nogenshin.start
def buggy_function():
    print("This will probably break...")
    raise ValueError("Oops!")

buggy_function()  # Prepare for adventure if it fails!
```

When an exception happens, instead of fixing the error, nogenshin will fire up Genshin Impact and let you chill in Teyvat while you contemplate your life choices.

## Why?

Why not? Debugging is stressful. Go fight some hilichurls instead. Or go get that 5-star character you’ve been dreaming of while your bugs roam free.

## How It Works

Step 1: Write code.

Step 2: Wrap your error-prone functions with @nogenshin.start.

Step 3: When your code blows up, nogenshin launches Genshin Impact.

Step 4: ????

Step 5: Profit (or cry about not getting Zhongli again).

## FAQ

Q: Will this help me debug my code?

A: Not even a little.

Q: Why Genshin Impact?

A: Why not?

Q: What if I actually want to fix my bugs?

A: That’s a ‘you’ problem.

Q: Is there a way to choose different games?

A: No. You either launch Genshin, or you face your errors alone.

## Disclaimer

Use at your own risk. This library will absolutely not fix your code. But hey, at least you’ll have fun, right? And yes, this might reduce your productivity. But isn’t that what coding is all about?

**nogenshin**: Turning every error into an adventure. Now go out there and debug... or pull for characters. Your call.