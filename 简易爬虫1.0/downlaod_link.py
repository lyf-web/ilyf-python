#!/usr/bin/python3
# -*- coding:utf-8 -*-
#Author:lyf
#Datetime:2020-8-16
#Filename:download_link.py

def is_download(group1,group2,group3):
    if group1 == 'magnet:?xt=urn:btih':
        if group3 == 'mp4':
            movie_download = 'magnet:?xt=urn:btih:' + group2 + '.mp4'
        elif group3 == 'mkv':
            movie_download = 'magnet:?xt=urn:btih:' + group2 + '.mkv'
        elif group3 == 'rm':
            movie_download = 'magnet:?xt=urn:btih:' + group2 + '.rm'
        elif group3 == 'rmvb':
            movie_download = 'magnet:?xt=urn:btih:' + group2 + '.rmvb'
        elif group3 == 'avi':
            movie_download = 'magnet:?xt=urn:btih:' + group2 + '.avi'
        elif group3 == 'wmv':
            movie_download = 'magnet:?xt=urn:btih:' + group2 + '.wmv'
        else:
            print(group3)
    elif group1 == 'ftp://d':
        if group3 == 'mp4':
            movie_download = 'ftp://d:' + group2 + '.mp4'
        elif group3 == 'mkv':
            movie_download = 'ftp://d:' + group2 + '.mkv'
        elif group3 == 'rm':
            movie_download = 'ftp://d:' + group2 + '.rm'
        elif group3 == 'rmvb':
            movie_download = 'ftp://d:' + group2 + '.rmvb'
        elif group3 == 'avi':
            movie_download = 'ftp://d:' + group2 + '.avi'
        elif group3 == 'wmv':
            movie_download = 'ftp://d:' + group2 + '.wmv'
        else:
            print(group3)
    elif group1 == 'ftp://j':
        if group3 == 'mp4':
            movie_download = 'ftp://j:' + group2 + '.mp4'
        elif group3 == 'mkv':
            movie_download = 'ftp://j:' + group2 + '.mkv'
        elif group3 == 'rm':
            movie_download = 'ftp://j:' + group2 + '.rm'
        elif group3 == 'rmvb':
            movie_download = 'ftp://j:' + group2 + '.rmvb'
        elif group3 == 'avi':
            movie_download = 'ftp://j:' + group2 + '.avi'
        elif group3 == 'wmv':
            movie_download = 'ftp://j:' + group2 + '.wmv'
        else:
            print(group3)
    elif group1 == 'ftp://z':
        if group3 == 'mp4':
            movie_download = 'ftp://z:' + group2 + '.mp4'
        elif group3 == 'mkv':
            movie_download = 'ftp://z:' + group2 + '.mkv'
        elif group3 == 'rm':
            movie_download = 'ftp://z:' + group2 + '.rm'
        elif group3 == 'rmvb':
            movie_download = 'ftp://z:' + group2 + '.rmvb'
        elif group3 == 'avi':
            movie_download = 'ftp://z:' + group2 + '.avi'
        elif group3 == 'wmv':
            movie_download = 'ftp://z:' + group2 + '.wmv'
        else:
            print(group3)
    elif group1 == 'ftp://2':
        if group3 == 'mp4':
            movie_download = 'ftp://2:' + group2 + '.mp4'
        elif group3 == 'mkv':
            movie_download = 'ftp://2:' + group2 + '.mkv'
        elif group3 == 'rm':
            movie_download = 'ftp://2:' + group2 + '.rm'
        elif group3 == 'rmvb':
            movie_download = 'ftp://2:' + group2 + '.rmvb'
        elif group3 == 'avi':
            movie_download = 'ftp://2:' + group2 + '.avi'
        elif group3 == 'wmv':
            movie_download = 'ftp://2:' + group2 + '.wmv'
        else:
            print(group3)
    elif group1 == 'ftp://y':
        if group3 == 'mp4':
            movie_download = 'ftp://y:' + group2 + '.mp4'
        elif group3 == 'mkv':
            movie_download = 'ftp://y:' + group2 + '.mkv'
        elif group3 == 'rm':
            movie_download = 'ftp://y:' + group2 + '.rm'
        elif group3 == 'rmvb':
            movie_download = 'ftp://y:' + group2 + '.rmvb'
        elif group3 == 'avi':
            movie_download = 'ftp://y:' + group2 + '.avi'
        elif group3 == 'wmv':
            movie_download = 'ftp://y:' + group2 + '.wmv'
        else:
            print(group3)
    return movie_download
