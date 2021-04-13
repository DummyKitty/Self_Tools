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


def tools_parse(d, parent=None, l=[]):
    for key, value in d.items():
        if type(value) == type(""):
            parent_dir = "/".join(l)
            # l.pop()
            if value.startswith("http"):
                tools_dir.append((parent_dir, "git clone " + value))
            elif value.startswith("docker"):
                tools_dir.append((parent_dir, value))
        else:
            l.append(key)
            tools_parse(value)
            l.pop()

    return l


tools_dir = []
tools_parse(tools)

print(tools_dir)
# if __name__ == '__main__':
