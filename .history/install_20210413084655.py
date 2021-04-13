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
        if type(value) == type(""):
            parent_dir = l.join("/")

        else:
            get_children(value)
        l.append(key)

    return l


l = get_children(tools)

print(l)
# if __name__ == '__main__':
