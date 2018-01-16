![pineapple-lang](pineapple-lang.png)

# pineapple-lang

`pineapple-lang` is an abstract, English-looking programming language for controlling real-time audio. Its purpose is to be suitable for both newcomers to the programmatic and/or musical world, as well as experienced musicians.

## Installation
* Requires [Sublime Text 3](https://www.sublimetext.com/3)
* Run `python setup.py` to install
* Add the following to your user key map:
```
[
  { "keys": ["shift+enter"], "command": "pa_execute_line" },
]
```
* Receive OSC commands on port 3001

## Examples

```
let the key be Am
let the feel be sweeping or intense
alter feel every 18 to 32 bars
play in 5/4 at 132bpm
   but faster when the feel is intense

add 🍍 to *bass
```
