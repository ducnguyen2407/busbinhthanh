import psycopg2, os, json

datapath ='C:/Users/DUCNGUYEN/Desktop/busbinhthanh/'

# print(os.listdir(datapath))
# for i in os.listdir(datapath):
#     f = open(datapath+i,'r',encoding='utf8')
#     data = json.loads(f.read())
#     print(data)
#     input()
    



connection = psycopg2.connect(user="postgres",
                                password="KhoaLuan1@3$",
                                host="34.126.69.133",
                                port="5432",
                                database="duc")
cursor = connection.cursor()
for i in os.listdir(datapath):
    f = open(datapath+i,'r',encoding='utf8')
    data = json.loads(f.read())
    print(data)
    if data['studentTicket'] == '':
        data['studentTicket'] = '0'
    if data['monthlyTicket'] == '':
        data['monthlyTicket'] = '0'
    postgres_insert_query = """ INSERT INTO databus (id, so_tuyen, ten_tuyen, loai_tuyen, khoang_cach, thoi_gian_hoat_dong, lo_trinh_luot_di, lo_trinh_luot_ve, gia_ve_thuong, gia_ve_hoc_sinh, gia_ve_thang, gian_cach_tuyen, don_vi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    record_to_insert = (
        data['id'],
        data['routeNo'],
        data['routeName'],
        data['type'],
        data['distance'],
        data['operationTime'],
        data['outBoundDescription'],
        data['inBoundDescription'],
        data['normalTicket'],
        int(data['studentTicket'].replace(',','').replace(' VNĐ','')),
        int(data['monthlyTicket'].replace(',','').replace(' VNĐ','')),
        data['headway'],
        data['orgs']
        )
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into mobile table")
    # input()