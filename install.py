import json
import os

tools_file = open("tools.json")
tools = json.load(tools_file)
print(tools)


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


tools_dir = []
tools_parse(tools)

print(tools_dir)
dirs = []
for i in tools_dir:
    if i[0] not in dirs:
        dirs.append(i[0])
        os.system("mkdir -p " + i[0])
    else:
        os.system("git clone " + i[1] + " " + i[0])

# if __name__ == '__main__':
