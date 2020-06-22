def transpile(parser, path, target='bash'):
    if target == 'bash':
        transpile2bash(parser, path)
    else:
        print('not possible to choose this target: {}'.format(target))

def transpile2bash(parser, path):
    # trnsplant
    with open(path, 'w') as f:
        f.writelines('#!/bin/bash\n')
        f.writelines("echo 'this is test'")

        # f.writelines('#!/bin/bash\n')
    # args, argv = parser.parse_known_args()
    # print(args.accumulate(args.[1,2,3]))
    # for k, v in args.items():
    #     print(k, v)
    # for k, v in args:
    #     print(k, v)
    # print(args)
    # print(argv)
