# -*- coding: utf-8 -*-
"""
IS211 Wk 10 Assignment

Connects databases and asks for data.
"""

import sqlite3 as lite
import sys

def DataFind():
    userinput = None
    
    try:
        while userinput != -1:
            userinput = raw_input('Input the person\'s ID number: ')
            con = lite.connect('pets.db')
            cur = con.cursor()
            cur2 = con.cursor()
            cur.execute('SELECT first_name, plast_name FROM'
                        ' person WHERE id = ?', (userinput))

            cur2.execute('SELECT name, breed, age '
                         'FROM pet '
                         'INNER JOIN person_pet '
                         'ON pet.id = person_pet.pet_id '
                         'INNER JOIN person '
                         'ON person_pet.person_id = person.id '
                         'WHERE person.id = ?', (userinput))

            row1 = cur.fetchall()
            row2 = cur2.fetchall()

            print '{} {}, {} years old.'.format(row1[0][0], row1[0][1], row1[0][2])
            print '=' * 80
            print '{} {} owned {}, a {}, that was {} years old'.format(row1[0][0], row1[0][1],
                                                                       row2[0][0], row2[0][1],
                                                                       row2[0][2], row2[0][3])


            con.commit()

    except lite.Error, error:

        if con:
            con.rollback()

            print "Error {}".format(error)
            DataFind()
        else:
            sys.exit()


if __name__ == '__main__':
    DataFind()
    