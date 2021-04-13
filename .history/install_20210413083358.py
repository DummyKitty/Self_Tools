import json
import os

tools_file = open("tools.json")
tools = json.load(tools_file)
print(tools)
for tools_name,operation in tools.items():
    

# if __name__ == '__main__':
