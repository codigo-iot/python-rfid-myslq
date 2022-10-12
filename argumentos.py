# Bibliotecas
import argparse

# Parser
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()

# Cuerpo del programa
print(args.echo)