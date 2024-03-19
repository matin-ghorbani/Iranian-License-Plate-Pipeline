from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--a', type=int, required=True)
opt = parser.parse_args()

print(opt)
print(type(opt))
