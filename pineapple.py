import sublime
import sublime_plugin
import random

try:
    from .pythonosc import udp_client
except ImportError:
    from pythonosc import udp_client

# Adapted from
# https://github.com/wch/SendText/blob/master/SendText.py

class PaExecuteLineCommand(sublime_plugin.TextCommand):
  @staticmethod
  def escapeString(s):
    s = s.replace('\\', '\\\\')
    s = s.replace('"', '\\"')
    return s

  @staticmethod
  def send(selection):
    # Remove trailing newline
    selection = selection.rstrip('\n')
    # Remove trailing space
    selection = selection.rstrip(' ')
    # Split selection into lines
    selection = PaExecuteLineCommand.escapeString(selection)
    
    array = selection.split(' ')
    print(array)

    client = udp_client.SimpleUDPClient("127.0.0.1", 3001)
    client.send_message("/frompineapple", array)
    # self.view.insert(edit, 0, "Hello, World!")


  def run(self, edit):
    global settings
    settings = sublime.load_settings('SendText.sublime-settings')

    # get selection
    selection = ""
    for region in self.view.sel():
      if region.empty():
        selection += self.view.substr(self.view.line(region)) + "\n"
        # self.advanceCursor(region)
      else:
        selection += self.view.substr(region) + "\n"

    # only proceed if selection is not empty
    if (selection == "" or selection == "\n"):
        return

    self.send(selection)

  def advanceCursor(self, region):
    (row, col) = self.view.rowcol(region.begin())

    # Make sure not to go past end of next line
    nextline = self.view.line(self.view.text_point(row + 1, 0))
    if nextline.size() < col:
      loc = self.view.text_point(row + 1, nextline.size())
    else:
      loc = self.view.text_point(row + 1, col)

    # Remove the old region and add the new one
    self.view.sel().subtract(region)
    self.view.sel().add(sublime.Region(loc, loc))
