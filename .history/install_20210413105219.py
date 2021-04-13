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
                tools_dir.append((parent_dir+'/'+key, "git clone " + value))
            elif value.startswith("docker"):
                # tools_dir.append((parent_dir+'/'+key, value))
                pass
        else:
            l.append(key)
            tools_parse(value)
            l.pop()


tools_dir = []
tools_parse(tools)

print(tools_dir)
dirs = []
base_dir = "Self_Tools"
os.system("mkdir Self_Tools")
for i in tools_dir:
    dirs.append(i[0])
    os.system("mkdir -p Self_Tools/" + i[0])
    if i[1].startswith("git"):
        os.system(i[1] + " Self_Tools/" + i[0])
    else:
        os.system(i[1])

# if __name__ == '__main__':
