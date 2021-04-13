import json
import os

tools_file = open("tools.json")
tools = json.load(tools_file)
print(tools)

# tool_name = ""
# for key, value in tools.items():
#     tool_name += key
#     if operation !=
#     operation = value
#     if


def get_children(d, parent=None, l=[]):
    for key, value in d.items():
        l.append(key)
        if type(value) != type(""):
            get_children(value)
    return l


l = get_children(tools)

print(l)
# if __name__ == '__main__':
