#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)  # Unikal ədədləri set-ə çevir
    return sum(unique)     # Set-dəki bütün elementləri topla
