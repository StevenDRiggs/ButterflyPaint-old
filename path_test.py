import os


print(f'__file__: {__file__}')
print(f'os.cwd(): {os.getcwd()}')
print(f'os.curdir: {os.curdir}')
print(f'os.path.abspath(__file__): {os.path.abspath(__file__)}')
print(f'os.path.dirname(__file__): {os.path.dirname(__file__)}')
print(f'os.path.expanduser(__file__): {os.path.expanduser(__file__)}')
print(f'os.path.expanduser("~"): {os.path.expanduser("~")}')
print(f'os.path.normpath(__file__): {os.path.normpath(__file__)}')
print(f'os.path.realpath(__file__): {os.path.realpath(__file__)}')
print(f'os.path.relpath(__file__): {os.path.relpath(__file__)}')
print(f'os.path.relpath(__file__, "~"): {os.path.relpath(__file__, "~")}')
print(f'os.path.relpath(__file__, os.path.expanduser("~")): {os.path.relpath(__file__, os.path.expanduser("~"))}')
