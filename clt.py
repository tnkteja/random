#!/usr/bin/python

from argparse import Action, ArgumentParser

class CustomAction(argparse.Action):
    def __init__(self,option_strings,dest,nargs=None,const=None,default=None,type=None,choices=None,required=False,help=None,metavar=None):
        argparse.Action.__init__(self, option_strings=option_strings,dest=dest,nargs=nargs,const=const,default=default,type=type,choices=choices,required=required,help=help,metavar=metavar)
        print 'Initializing CustomAction'
        for name,value in sorted(locals().items()):
            if name == 'self' or value is None:
                continue
            print '  %s = %r' % (name, value)
        return

    def __call__(self, parser, namespace, values, option_string=None):
        print
        print 'Processing CustomAction for "%s"' % self.dest
        print '  parser = %s' % id(parser)
        print '  values = %r' % values
        print '  option_string = %r' % option_string
        
        # Do some arbitrary processing of the input values
        if isinstance(values, list):
            values = [ v.upper() for v in values ]
        else:
            values = values.upper()
        # Save the results in the namespace using the destination
        # variable given to our constructor.
        setattr(namespace, self.dest, values)

parser = ArgumentParser(description="")

subparsers == parser.add_subparsers(help="Some")

someparser=subparser.add_parser("someName", help="")
group = someparser.add_argument_group("someGroupName)
group.add_argument("-b","--someBooleanVariable",action="store_true", default=False, help="")
group.add_argument("-v","--someVariable", type=int, nargs=3,action="store", dest="someVariable", help="")
group.add_argument("%v","--someVariableWithDifferentPrefix", type=str, nargs='?',choices=["one","zero"],action="store", dest="someVariable", help="")
group.add_argument("&v","--someVariableWithDifferentPrefix2", type=float, nargs='*',action="store", dest="someVariable", help="")
group.add_argument("$v","--someVariableWithDifferentPrefix3", type=file, nargs='+',action="store", dest="someVariable", help="")

group.add_argument("/V","--someInitialisedVariable",type=int, action="store_const", const=23, dest="someInitialisedVariable", help="")
group.add_argument("+a","--someArrayVariable",action="append",default=[],dest="someArrayVariable",help="")
group.add_argument("*A","--someInitialisedArrayVariable", action="append_const", default=[], dest="someInitialisedArrayVariable", help="")
group.add_argument("--version", action="version", version="1.0.0.0.0.1")

megroup = parser.add_mutually_exclusive_group()

args = parser.parse_args()



## References
# 1. https://pymotw.com/2/argparse/
# 2. https://docs.python.org/2/howto/argparse.html
