import  pymysql
from config import host , user , password , db_name
import datetime
admins = [854686840, 1212477490]

all_groups = {1: {1: {1: 'Группа ГМУ-111', 2: 'Группа ЭБ-111', 3: 'Группа ЭБ-112', 4: 'Группа МЕН-111', 5: 'Группа МЕН-112', 6: 'Группа МЕН-113', 7: 'Группа МЕН-114'},
                  2: {1: 'Группа МЕН-121', 2: 'Группа МЕН-124', 3: 'Группа МЕН-125', 4: 'Группа ГМУ-121', 5: 'Группа ЭБ-121', 6: 'Группа ЭБ-122', 7: 'Группа СЕР-121', 8: 'Группа ТУР-121'},
                  3: {1: 'Группа МЕН-132', 2: 'Группа МЕН-133', 3: 'Группа МЕН-134', 4: 'Группа УП-131', 5: 'Группа ГМУ-131', 6: 'Группа ЭБ-131', 7: 'Группа ЭБ-132', 8: 'Группа ЭБ-133'},
                  4: {1: 'Группа МЕН-141', 2: 'Группа МЕН-142', 3: 'Группа МЕН-143', 4: 'Группа МЕН-144', 5: 'Группа УП-141', 6: 'Группа СЕР-141', 7: 'Группа ЭБ-141', 8: 'Группа ЭБ-142', 9: 'Группа ЭБ-143', 10: 'Группа ГМУ-141'},
                  5: {1: 'Группа ЭБ-151', 2: 'Группа ЭБ-152', 3: 'Группа ЭБ-153'}},
              2: {1: {1: 'Группа ТОР-211', 2: 'Группа ТОР-212', 3: 'Группа ТОР-214', 4: 'Группа РСО-211', 5: 'Группа РСО-212', 6: 'Группа ТД-211'},
                  2: {1: 'Группа ТОР-221', 2: 'Группа ТОР-222', 3: 'Группа ТОР-224', 4: 'Группа ОРМ-221', 5: 'Группа РСО-221', 6: 'Группа РСО-222', 7: 'Группа ТД-221', 8: 'Группа ТД-222', 9: 'Группа ТОВ-221'},
                  3: {1: 'Группа ТОР-231', 2: 'Группа ТОР-232', 3: 'Группа ТОР-234', 4: 'Группа ОРМ-231', 5: 'Группа РСО-231', 6: 'Группа ТД-231', 7: 'Группа ТД-232'},
                  4: {1: 'Группа ТОР-241', 2: 'Группа ТОР-242', 3: 'Группа ТОР-243', 4: 'Группа ТОР-244', 5: 'Группа ОРМ-241', 6: 'Группа РСО-241', 7: 'Группа ТД-241', 8: 'Группа ТД-242', 9: 'Группа ТД-243', 10: 'Группа ТОВ-241'},
                  5: {1: 'Группа ТД-251', 2: 'Группа ТД-252'}},
              3: {1: {1: 'Группа ИБ-311', 2: 'Группа ИБ-312', 3: 'Группа ИСТ-311', 4: 'Группа ИСТ-312', 5: 'Группа ПИ-311', 6: 'Группа ПРИ-311', 7: 'Группа ПРИ-312', 8: 'Группа БИН-311', 9: 'Группа ПМИ-311'},
                  2: {1: 'Группа ИСТ-321', 2: 'Группа ИСТ-322', 3: 'Группа ПИ-321', 4: 'Группа ПИ-322', 5: 'Группа ПРИ-321', 6: 'Группа ПРИ-322', 7: 'Группа ИБ-321', 8: 'Группа ИБ-322', 9: 'Группа БИН-321', 10: 'Группа ПМИ-321'},
                  3: {1: 'Группа ИСТ-331', 2: 'Группа ИСТ-332', 3: 'Группа ПИ-331', 4: 'Группа ПИ-332', 5: 'Группа ПРИ-331', 6: 'Группа ПРИ-332', 7: 'Группа ИБ-331', 8: 'Группа БИН-331'},
                  4: {1: 'Группа ПМИ-341', 2: 'Группа ИСТ-341', 3: 'Группа ПИ-341', 4: 'Группа ПРИ-341', 5: 'Группа ИБ-341', 6: 'Группа ИБ-342'}},
              4: {1: {1: 'Группа МО-411', 2: 'Группа ЭК-411', 3: 'Группа ЭК-4110', 4: 'Группа ЭК-4111', 5: 'Группа ЭК-412', 6: 'Группа ЭК-414', 7: 'Группа ЭК-415', 8: 'Группа ЭК-417', 9: 'Группа ЭК-418', 10: 'Группа СТ-411'},
                  2: {1: 'Группа ЭК-421', 2: 'Группа ЭК-4210', 3: 'Группа ЭК-4211', 4: 'Группа ЭК-422', 5: 'Группа ЭК-424', 6: 'Группа ЭК-425', 7: 'Группа ЭК-427', 8: 'Группа ЭК-428', 9: 'Группа ЭК-429', 10: 'Группа МО-421'},
                  3: {1: 'Группа ЭК-431', 2: 'Группа ЭК-4310', 3: 'Группа ЭК-4311', 4: 'Группа ЭК-4312', 5: 'Группа ЭК-432', 6: 'Группа ЭК-433', 7: 'Группа ЭК-434', 8: 'Группа ЭК-435', 9: 'Группа ЭК-437', 10: 'Группа ЭК-439'},
                  4: {1: 'Группа ЭК-441', 2: 'Группа ЭК-442', 3: 'Группа ЭК-443', 4: 'Группа ЭК-444', 5: 'Группа ЭК-445', 6: 'Группа ЭК-446', 7: 'Группа ЭК-447', 8: 'Группа ЭК-448', 9: 'Группа ЭК-4410', 10: 'Группа ЭК-4411'}},
              5: {1: {1: 'Группа ЭК-511', 2: 'Группа ЭК-512', 3: 'Группа ЭК-513', 4: 'Группа ЭК-514', 5: 'Группа ЭК-517', 6: 'Группа ЭК-518'},
                  2: {1: 'Группа ЭК-521', 2: 'Группа ЭК-523', 3: 'Группа ЭК-524', 4: 'Группа ЭК-526', 5: 'Группа ЭК-527'},
                  3: {1: 'Группа ЭК-531', 2: 'Группа ЭК-532', 3: 'Группа ЭК-535', 4: 'Группа ЭК-536', 5: 'Группа ЭК-537', 6: 'Группа ЭК-538', 7: 'Группа ЭК-5311'},
                  4: {1: 'Группа ЭК-541', 2: 'Группа ЭК-5411', 3: 'Группа ЭК-542', 4: 'Группа ЭК-545', 5: 'Группа ЭК-546', 6: 'Группа ЭК-547', 7: 'Группа ЭК-548'}},
              6: {1: {1: 'Группа СЭ-611', 2: 'Группа СЭ-612', 3: 'Группа ЮР-611', 4: 'Группа ЮР-612', 5: 'Группа ЮР-613', 6: 'Группа ЮР-614', 7: 'Группа ЮР-615', 8: 'Группа ЮР-616', 9: 'Группа ЮР-617', 10: 'Группа ЮР-618'},
                  2: {1: 'Группа ЮР-621', 2: 'Группа ЮР-622', 3: 'Группа ЮР-623', 4: 'Группа ЮР-624', 5: 'Группа ЮР-625', 6: 'Группа ЮР-626', 7: 'Группа ЮР-627', 8: 'Группа СЭ-621', 9: 'Группа СЭ-622'},
                  3: {1: 'Группа ЮР-631', 2: 'Группа ЮР-632', 3: 'Группа ЮР-633', 4: 'Группа ЮР-634', 5: 'Группа ЮР-635', 6: 'Группа СЭ-631', 7: 'Группа СЭ-632'},
                  4: {1: 'Группа ЮР-641', 2: 'Группа ЮР-642', 3: 'Группа ЮР-643', 4: 'Группа ЮР-644', 5: 'Группа ЮР-645', 6: 'Группа ЮР-646', 7: 'Группа ЮР-647', 8: 'Группа ЮР-648', 9: 'Группа СЭ-641', 10: 'Группа СЭ-642'}, 5: {1: 'Группа СЭ-651', 2: 'Группа СЭ-652'}},
              7: {1: {1: 'Группа ЖУР-711', 2: 'Группа ЖУР-712', 3: 'Группа ПЕР-711', 4: 'Группа ПЕР-712', 5: 'Группа ПЕР-713', 6: 'Группа РЕГ-711', 7: 'Группа РЕГ-712'},
                  2: {1: 'Группа ПЕР-721', 2: 'Группа ПЕР-722', 3: 'Группа РЕГ-721', 4: 'Группа РЕГ-722', 5: 'Группа ЖУР-721', 6: 'Группа ЖУР-722', 7: 'Группа ПЕР-723'},
                  3: {1: 'Группа ПЕР-731', 2: 'Группа ПЕР-732', 3: 'Группа РЕГ-731', 4: 'Группа РЕГ-732', 5: 'Группа ЖУР-731', 6: 'Группа ЖУР-732'},
                  4: {1: 'Группа ПЕР-741', 2: 'Группа ПЕР-742', 3: 'Группа РЕГ-741', 4: 'Группа РЕГ-742', 5: 'Группа ЖУР-741', 6: 'Группа ЖУР-742'}}}
all_groups_list =['ГМУ-111', 'ЭБ-111', 'ЭБ-112', 'МЕН-111', 'МЕН-112', 'МЕН-113', 'МЕН-114', 'МЕН-121', 'МЕН-124', 'МЕН-125', 'ГМУ-121', 'ЭБ-121', 'ЭБ-122', 'СЕР-121', 'ТУР-121', 'МЕН-132', 'МЕН-133', 'МЕН-134', 'УП-131', 'ГМУ-131', 'ЭБ-131', 'ЭБ-132', 'ЭБ-133', 'МЕН-141', 'МЕН-142', 'МЕН-143', 'МЕН-144', 'УП-141', 'СЕР-141', 'ЭБ-141', 'ЭБ-142', 'ЭБ-143', 'ГМУ-141', 'ЭБ-151', 'ЭБ-152', 'ТОР-211', 'ТОР-212', 'ТОР-214', 'РСО-211', 'РСО-212', 'ТД-211', 'ТОР-221', 'ТОР-222', 'ТОР-224', 'ОРМ-221', 'РСО-221', 'РСО-222', 'ТД-221', 'ТД-222', 'ТОВ-221', 'ТОР-231', 'ТОР-232', 'ТОР-234', 'ОРМ-231', 'РСО-231', 'ТД-231', 'ТД-232', 'ТОР-241', 'ТОР-242', 'ТОР-243', 'ТОР-244', 'ОРМ-241', 'РСО-241', 'ТД-241', 'ТД-242', 'ТД-243', 'ТОВ-241', 'ТД-251', 'ИБ-311', 'ИБ-312', 'ИСТ-311', 'ИСТ-312', 'ПИ-311', 'ПРИ-311', 'ПРИ-312', 'БИН-311', 'ПМИ-311', 'ИСТ-321', 'ИСТ-322', 'ПИ-321', 'ПИ-322', 'ПРИ-321', 'ПРИ-322', 'ИБ-321', 'ИБ-322', 'БИН-321', 'ПМИ-321', 'ИСТ-331', 'ИСТ-332', 'ПИ-331', 'ПИ-332', 'ПРИ-331', 'ПРИ-332', 'ИБ-331', 'БИН-331', 'ПМИ-341', 'ИСТ-341', 'ПИ-341', 'ПРИ-341', 'ИБ-341', 'МО-411', 'ЭК-411', 'ЭК-4110', 'ЭК-4111', 'ЭК-412', 'ЭК-414', 'ЭК-415', 'ЭК-417', 'ЭК-418', 'СТ-411', 'ЭК-421', 'ЭК-4210', 'ЭК-4211', 'ЭК-422', 'ЭК-424', 'ЭК-425', 'ЭК-427', 'ЭК-428', 'ЭК-429', 'МО-421', 'ЭК-431', 'ЭК-4310', 'ЭК-4311', 'ЭК-4312', 'ЭК-432', 'ЭК-433', 'ЭК-434', 'ЭК-435', 'ЭК-437', 'ЭК-439', 'ЭК-441', 'ЭК-442', 'ЭК-443', 'ЭК-444', 'ЭК-445', 'ЭК-446', 'ЭК-447', 'ЭК-448', 'ЭК-4410', 'ЭК-511', 'ЭК-512', 'ЭК-513', 'ЭК-514', 'ЭК-517', 'ЭК-518', 'ЭК-521', 'ЭК-523', 'ЭК-524', 'ЭК-526', 'ЭК-527', 'ЭК-531', 'ЭК-532', 'ЭК-535', 'ЭК-536', 'ЭК-537', 'ЭК-538', 'ЭК-5311', 'ЭК-541', 'ЭК-5411', 'ЭК-542', 'ЭК-545', 'ЭК-546', 'ЭК-547', 'СЭ-611', 'СЭ-612', 'ЮР-611', 'ЮР-612', 'ЮР-613', 'ЮР-614', 'ЮР-615', 'ЮР-616', 'ЮР-617', 'ЮР-618', 'ЮР-621', 'ЮР-622', 'ЮР-623', 'ЮР-624', 'ЮР-625', 'ЮР-626', 'ЮР-627', 'СЭ-621', 'СЭ-622', 'ЮР-631', 'ЮР-632', 'ЮР-633', 'ЮР-634', 'ЮР-635', 'СЭ-631', 'СЭ-632', 'ЮР-641', 'ЮР-642', 'ЮР-643', 'ЮР-644', 'ЮР-645', 'ЮР-646', 'ЮР-647', 'ЮР-648', 'СЭ-641', 'СЭ-642', 'СЭ-651', 'ЖУР-711', 'ЖУР-712', 'ПЕР-711', 'ПЕР-712', 'ПЕР-713', 'РЕГ-711', 'РЕГ-712', 'ПЕР-721', 'ПЕР-722', 'РЕГ-721', 'РЕГ-722', 'ЖУР-721', 'ЖУР-722', 'ПЕР-723', 'ПЕР-731', 'ПЕР-732', 'РЕГ-731', 'РЕГ-732', 'ЖУР-731', 'ЖУР-732', 'ПЕР-741', 'ПЕР-742', 'РЕГ-741', 'РЕГ-742', 'ЖУР-741']
def all_user(user_id):
        if user_id in admins:
                try:
                        connection = pymysql.connect(
                                host=host,
                                port=3306,
                                user=user,
                                password=password,
                                database=db_name,
                                cursorclass=pymysql.cursors.DictCursor)
                        try:
                                with connection.cursor() as cursor:
                                        query = f"SELECT  * FROM `user`"
                                        cursor.execute(query)
                                        rows = cursor.fetchall()
                                        return(len(rows))
                                        # return [rows[0]['faculty'],rows[0]['course'],rows[0]['academic_group']]
                                        # return rows
                        finally:
                                connection.close()
                except Exception as ex:
                        print(f"Ошибка {ex}")
        else:
                return 'No'
def find_number_group(group):
        if group in all_groups_list:
                for f in all_groups:
                        for k in all_groups[f]:
                                for g in all_groups[f][k]:
                                        name = all_groups[f][k][g].split(' ')
                                        if group ==name[1]:
                                                if f == 1:
                                                        facylty = 'МИП'
                                                if f == 2:
                                                        facylty = 'ТД'
                                                if f == 3:
                                                        facylty = 'КТИИБ'
                                                if f == 4:
                                                        facylty = 'УЭФ'
                                                if f == 5:
                                                        facylty = 'ЭИФ'
                                                if f == 6:
                                                        facylty = 'ЮР'
                                                if f == 7:
                                                        facylty = 'ЛИЖ'
                                                #####
                                                kind = k
                                                return [facylty,kind,group]
        else:
                return 'No'

def find_number_group_for_parsing(group):
        if group in all_groups_list:
                for f in all_groups:
                        for k in all_groups[f]:
                                for g in all_groups[f][k]:
                                        name = all_groups[f][k][g].split(' ')
                                        if group ==name[1]:

                                                return [f,k,g]

def find_group(name_group):
        faculty = find_number_group(group)[0]
        kind = find_number_group(group)[1]
        group = find_number_group(group)[2]
        try:
                connection = pymysql.connect(
                        host=host,
                        port=3306,
                        user=user,
                        password=password,
                        database=db_name,
                        cursorclass=pymysql.cursors.DictCursor)
                try :
                        with connection.cursor() as cursor:
                                query = f""
                                cursor.execute(query)
                                connection.commit()
                finally:
                        connection.close()
        except Exception as ex:
                print (f"Ошибка {ex}")

def NewUser(user_id, username, first_name, last_name):
        try:
                connection = pymysql.connect(
                        host=host,
                        port=3306,
                        user=user,
                        password=password,
                        database=db_name,
                        cursorclass=pymysql.cursors.DictCursor)
                try :
                        with connection.cursor() as cursor:
                                query = f"INSERT INTO `user` (`user_id` , `username` , `first_name` , `last_name` ,`faculty` , `course` , `academic_group`) VALUES ({user_id} , '{username}' , '{first_name}', '{last_name}' , 'None' , 'None' , 'None')"
                                cursor.execute(query)
                                connection.commit()
                finally:
                        connection.close()
        except Exception as ex:
                print (f"Ошибка {ex}")

def CheckUser (user_id):
        try:
                connection = pymysql.connect(
                        host=host,
                        port=3306,
                        user=user,
                        password=password,
                        database=db_name,
                        cursorclass=pymysql.cursors.DictCursor)
                try :
                        with connection.cursor() as cursor:
                                query = f"SELECT  `user_id` FROM `user`"
                                cursor.execute(query)
                                rows = cursor.fetchall()
                        all_user = []
                        for i in rows :
                                all_user.append(i['user_id'])
                        if str(user_id) in all_user:
                                return 'Yes'
                        else :
                                return 'No'
                finally:
                        connection.close()
        except Exception as ex:
                print (f"Ошибка {ex}")

def UpdateFak(user_id , faculty):
        try:
                connection = pymysql.connect(
                        host=host,
                        port=3306,
                        user=user,
                        password=password,
                        database=db_name,
                        cursorclass=pymysql.cursors.DictCursor)
                try :
                        with connection.cursor() as cursor:
                                query = f"UPDATE `user` SET `faculty` = '{faculty}' WHERE `user_id` = '{user_id}'"
                                cursor.execute(query)
                                connection.commit()
                finally:
                        connection.close()
        except Exception as ex:
                print (f"Ошибка {ex}")

def UpdateKind(user_id , kind):
        try:
                connection = pymysql.connect(
                        host=host,
                        port=3306,
                        user=user,
                        password=password,
                        database=db_name,
                        cursorclass=pymysql.cursors.DictCursor)
                try :
                        with connection.cursor() as cursor:
                                query = f"UPDATE `user` SET `course` = '{kind}' WHERE `user_id` = '{user_id}'"
                                cursor.execute(query)
                                connection.commit()
                finally:
                        connection.close()
        except Exception as ex:
                print (f"Ошибка {ex}")

def NewGroup(group):
        try:
                connection = pymysql.connect(
                        host=host,
                        port=3306,
                        user=user,
                        password=password,
                        database=db_name,
                        cursorclass=pymysql.cursors.DictCursor)
                try :
                        with connection.cursor() as cursor:
                                query = f"CREATE TABLE {group} (day varchar(32) , item varchar(32) , cabinet varchar(32) , teacher varchar(32) , type varchar(32) , time varchar(32))"
                                cursor.execute(query)
                                connection.commit()
                finally:
                        connection.close()
        except Exception as ex:
                print (f"Ошибка {ex}")

def UserFak(id):
        try:
                connection = pymysql.connect(
                        host=host,
                        port=3306,
                        user=user,
                        password=password,
                        database=db_name,
                        cursorclass=pymysql.cursors.DictCursor)
                try :
                        with connection.cursor() as cursor:
                                query = f"SELECT  `faculty` FROM `user` WHERE `user_id` = {id}"
                                cursor.execute(query)

                                rows = cursor.fetchall()
                        if rows[0]['faculty'] == 'КТиИБ':
                                return 'KTiIB'
                        if rows[0]['faculty'] == 'МИП':
                                return 'MIP'
                        if rows[0]['faculty'] == 'ТД':
                                return "TD"
                        if rows[0]['faculty'] == 'ЮР':
                                return "YR"
                        if rows[0]['faculty'] == 'УЭФ':
                                return 'YEF'
                        if rows[0]['faculty'] == 'ЭИФ':
                                return 'EIF'
                        if rows[0]['faculty'] == 'ЛИЖ':
                                return 'LIJ'
                finally:
                        connection.close()
        except Exception as ex:
                print (f"Ошибка {ex}")
# XUY
def InfoUser(user_id):
        try:
                connection = pymysql.connect(
                        host=host,
                        port=3306,
                        user=user,
                        password=password,
                        database=db_name,
                        cursorclass=pymysql.cursors.DictCursor)
                try :
                        with connection.cursor() as cursor:
                                query = f"SELECT  * FROM `user`"
                                cursor.execute(query)
                                rows = cursor.fetchall()
                                for i in rows:
                                        if i['user_id'] == str(user_id):
                                                return [i['faculty'],i['course'],i['academic_group']]
                                # return [rows[0]['faculty'],rows[0]['course'],rows[0]['academic_group']]
                                # return rows
                finally:
                        connection.close()
        except Exception as ex:
                print (f"Ошибка {ex}")
def UpdateInfoUser(user_id,name_group):
        faculty = find_number_group(name_group)[0]
        kind = find_number_group(name_group)[1]
        group = find_number_group(name_group)[2]
        try:
                connection = pymysql.connect(
                        host=host,
                        port=3306,
                        user=user,
                        password=password,
                        database=db_name,
                        cursorclass=pymysql.cursors.DictCursor)
                try :
                        with connection.cursor() as cursor:
                                query = f"UPDATE `user` SET `faculty` = '{faculty}' WHERE `user_id` = '{user_id}'"
                                cursor.execute(query)
                                query = f"UPDATE `user` SET `course` = '{kind}' WHERE `user_id` = '{user_id}'"
                                cursor.execute(query)
                                query = f"UPDATE `user` SET `academic_group` = '{group}' WHERE `user_id` = '{user_id}'"
                                cursor.execute(query)
                                connection.commit()
                finally:
                        connection.close()
        except Exception as ex:
                print (f"Ошибка {ex}")

def New_Offer(user_id,message):
        now = datetime.datetime.now()
        try:
                connection = pymysql.connect(
                        host=host,
                        port=3306,
                        user=user,
                        password=password,
                        database=db_name,
                        cursorclass=pymysql.cursors.DictCursor)
                try :
                        with connection.cursor() as cursor:
                                query = f"INSERT INTO `offers` (`user_id`, `message`, `time`) VALUES ('{user_id}', '{message}','{now}');"
                                cursor.execute(query)
                                connection.commit()
                finally:
                        connection.close()
        except Exception as ex:
                print (f"Ошибка {ex}")
def New_Mistake(user_id,message):
        now = datetime.datetime.now()
        try:
                connection = pymysql.connect(
                        host=host,
                        port=3306,
                        user=user,
                        password=password,
                        database=db_name,
                        cursorclass=pymysql.cursors.DictCursor)
                try :
                        with connection.cursor() as cursor:
                                query = f"INSERT INTO `mistakes` (`user_id`, `message`, `time`) VALUES ('{user_id}', '{message}','{now}');"
                                cursor.execute(query)
                                connection.commit()
                finally:
                        connection.close()
        except Exception as ex:
                print (f"Ошибка {ex}")
if __name__ == '__main__':
        None


