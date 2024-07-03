from dateutil.parser import *
from dateutil.parser import ParserError


def setup():
    example1 = {"timedatestamp": "Wed Aug  4 06:06:31 2004"}
    example2 = {"TimeStamp": "2004:08:04 08:06:31+02:00"}
    example3 = {"link date": "4:24 AM 3/13/2012"}
    example4 = {"TimeStamp": "2012:03:13 03:24:49+01:00"}
    example5 = {"TimeStamp": "0000:00:00 00:00:00"}
    examples = []
    examples.append(example1)
    examples.append(example2)
    examples.append(example3)
    examples.append(example4)
    examples.append(example5)

    return examples


def main():
    examples = setup()
    for example in examples:
        k, v = list(example.items())[0]
        first_token = v.split(" ")[0]
        print("orginal date:", v)
        #print(first_token)
        if first_token.count(':') == 2:
            v = v.replace(':', '-', 2)  # only replace first 2 colons
        print("new date:",v)
        try:
            print("parsed date:", parse(v),"\n")
        except ValueError:
            print("date error")
        continue

main()
