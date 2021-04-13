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
            l.clear()
            tools_dir.append(parent_dir + "/" + value)
        else:
            l.append(key)
            get_children(value)

    return l


tools_dir = []
l = get_children(tools)

print(l)
# if __name__ == '__main__':
