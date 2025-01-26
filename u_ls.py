#!/usr/bin/env python

import os
import argparse
import stat
import pwd
import grp
from datetime import datetime

def get_file_type(file):
    mode = file.stat().st_mode
    if stat.S_ISREG(mode):
        return "f"
    elif stat.S_ISDIR(mode):
        return "d"
    elif stat.S_ISLNK(mode):
        return "l"
    elif stat.S_ISCHR(mode):
        return "c"
    elif stat.S_ISBLK(mode):
        return "b"
    elif stat.S_ISSOCK(mode):
        return "s"
    elif stat.S_ISFIFO(mode):
        return "p"
    else:
        return "?"

def list_files(path = os.getcwd()):
    
    try:        
        with os.scandir(path) as it:
            for file in it:
                owner = pwd.getpwuid(file.stat().st_uid).pw_name
                group = grp.getgrgid(file.stat().st_gid).gr_name
                size = file.stat().st_size
                permissions = oct(file.stat().st_mode)[-4:]
                create_time = file.stat().st_ctime
                human_readable_time = datetime.fromtimestamp(create_time).strftime('%d-%m-%Y %H:%M:%S')
                print(f"{get_file_type(file)} - {permissions} - {owner}:{group} - {human_readable_time} - {size} bytes - {file.name}")

    except (FileNotFoundError, PermissionError) as e:
        print(f"{e}")
        exit(1)

def main():
    parser = argparse.ArgumentParser(description='List the content of a directory')
    parser.add_argument('path', metavar='path', type=str, nargs='?', help='Dir to be listed')
    args = parser.parse_args()
    list_files(args.path)

if __name__ == '__main__':
    main()