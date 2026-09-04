# Jot
Jot is a dead-simple command-line app for taking timestamped notes. Specify a file,
start the app, and write them as they come. Every note is appended to the file
with the current local date and time prepended as soon as you press <kbd>Enter</kbd>.
This is pretty much all it does.

## How to install it?
```shell
uv tool install git+ssh://git@github.com/r73m/jot.git
```

## How to run it?
```shell
jot notes.txt
```
If the specified file doesn't exist, it will be created; if it does, appended to

## How to quit it?
Press <kbd>Control</kbd>-<kbd>C</kbd> or <kbd>Control</kbd>-<kbd>D</kbd>

## How does it process input?
The app ignores empty and whitespace-only inputs, otherwise, it strips leading
and trailing whitespaces

## Does it support non-ASCII characters?
Авжеж (_of course_) ❤️

## What date format does it use?
ISO 8601 with space delimiter (_instead of `T`_) and seconds precision, e.g.,
`2022-06-05 04:20:13`

### Why seconds precision?
I don't think a human could legitimately create multiple notes in a second

## Why did I make it?
I wanted a simple way to take timestamped notes during interviews

## Why Python 3.9?
This is the version coming with [macOS command-line tools](https://developer.apple.com/documentation/xcode/command-line-tools),
and this app doesn't need any functionality from later versions

## What's next?
So far I think this is pretty much it. "Dead-simple" is a feature.
