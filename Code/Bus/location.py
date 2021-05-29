import psycopg2, os, json
datapath ='C:/Users/Admin/Downloads/Compressed/test/test/busbinhthanh/'

connection = psycopg2.connect(user="postgres",
                                password="postgres",
                                host="localhost",
                                port="5432",
                                database="duc")
cursor = connection.cursor()
for i in os.listdir(datapath):
    f = open(datapath+i,'r',encoding='utf8')
    data = json.loads(f.read())

    postgres_insert_query = """ INSERT INTO bus_station (thu_tu_tram, huong_tram, id_tuyen, ten_tram, diem_duong_di, dia_chi_tram, vi_do, kinh_do) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

    for j in range(len(data['stations'])):
        c = str(data['stations'][j]['lat']) + ',' + str(data['stations'][j]['lng']) if (data['stations'][j]['pathPoints'] == '' or data['stations'][j]['pathPoints'] == ' ') else data['stations'][j]['pathPoints'].replace(" ", ",")
        print(c)
        # record_to_insert = (
        #     (data['stations'][j]['stationOrder']),
        #     (data['stations'][j]['stationDirection']),
        #     (data['routeId']),
        #     (data['stations'][j]['stationName']),
        #     (c),
        #     (data['stations'][j]['stationAddress']),
        #     (data['stations'][j]['lat']),
        #     (data['stations'][j]['lng'])
        # )
        # cursor.execute(postgres_insert_query, record_to_insert)
        # connection.commit()
        # count = cursor.rowcount
        # print(count, "Record inserted successfully into mobile table")
    