import pymysql
import pymysql.cursors
import json

class Webmanager(object):
    def __init__(self):
        self.sqlpassword = None
        self.logindb = None
        self.actressdb = None

    def get(self, username):
        
        try:
            conn = pymysql.connect(host= 'localhost',
                                    user= 'root',
                                    password= self.sqlpassword,
                                    database= self.logindb,
                                    cursorclass= pymysql.cursors.DictCursor,
                                    charset= 'utf8')
        except:
            print('connect fail')

        cursor = conn.cursor()

        user = self.check(conn, cursor)
        if user:
            return None

        sql = "select password from register where username = '{0}'".format(username)

        cursor.execute(sql)

        password = cursor.fetchone()

        conn.close()

        return password


    def push(self, email, username, password):

        try:
            conn = pymysql.connect(host= 'localhost',
                                    user= 'root',
                                    password= self.sqlpassword,
                                    database= self.logindb,
                                    cursorclass= pymysql.cursors.DictCursor,
                                    charset= 'utf8')
        except:
            print('connect fail')

        user = self.check(conn, username)
        if user:
            return False

        cursor = conn.cursor()

        sql = "insert into register (email, username, password) values ('{0}', '{1}', '{2}')".format(email, username, password)

        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()

        conn.close()

        return True


    def check(self, conn, username):

        cursor = conn.cursor()

        sql = "select * from register where username = '{0}'".format(username)

        try:
            cursor.execute(sql)
        except:
            conn.rollback()

        user = cursor.fetchall()

        return user
        

    def make_actressdict(self):

        try:
            conn = pymysql.connect(host= 'localhost',
                                    user= 'root',
                                    password= self.sqlpassword,
                                    database= self.actressdb,
                                    cursorclass= pymysql.cursors.DictCursor,
                                    charset= 'utf8')
        except:
            print('connect fail')

        cursor = conn.cursor()

        sql = "select * from actresslist"

        cursor.execute(sql)

        actresses = cursor.fetchall()

        girls_dict = []

        for actress in actresses:

            node = {}

            node['headshot'] = actress['headshot']
            node['jp'] = actress['jp']
            node['en'] = actress['en']
            node['ch'] = actress['ch']
            node['birth'] = actress['birth']
            node['company'] = actress['company']
            node['body'] = actress['body']

            girls_dict.append(node)
    
        cursor = conn.cursor()

        for girl in girls_dict:
        
            try:
                sql = "select day, number, title, cover from {0} where name = '{1}' order by day desc".format(girl['company'], girl['jp'])

                cursor.execute(sql)

                videos = cursor.fetchall()
            except:
                videos = []

            girl['video'] = {}

            for video in videos:

                date = video['day'].split('-')
            
                year = date[0]

                if year not in girl['video']:

                    girl['video'][year] = []

                girl['video'][year].append({'day': video['day'], 'number': video['number'], 'title': video['title'], 'video': video['cover']})

        
        with open("./girls_data.json", 'w') as f:
            json.dump(girl_dict, f)
        

        return girls_dict


