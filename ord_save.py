import os
import re
from functools import reduce

def addToClipBoard(text):
    command = 'echo | set /p =' + text.strip() + '| clip'
    os.system(command)

dirName = "C:/Users/{}/Documents/Warcraft III/CustomMapData/ORD9".format(os.getlogin())

file = open(
            next(
                map(
                    lambda x:
                        os.path.join(dirName,x),
                    filter(
                        lambda x:
                            re.search("_{}.txt".format(
                                reduce(
                                    lambda acc, x:
                                        max(acc,x),
                                    map(
                                        int,
                                        map(
                                            lambda x:
                                                re.sub(
                                                    "[a-zA-Z0-9]*_|.txt",
                                                    "",
                                                    x
                                                )
                                            ,
                                            os.listdir(dirName)
                                        )
                                    )
                                )
                            ),x),
                        os.listdir(dirName)
                    )
                )
            ),
            'r',
            encoding="UTF8"
        )

addToClipBoard(
    '-load {}'.format(
        list(
            map(
                lambda x:
                    x.replace('"',"")
                        .split(),
                file
            )
        )[5][3]
    )
)

file.close()
