#data format
import csv
import more_itertools as mit



'''
environmental data

#Tempature(*C), Barometric Pressure (in/Mg), Humidity(%), Gas/VOC(KOhms), Altitude(m)

Geo data

$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A

Where:
     RMC          Recommended Minimum sentence C
     123519       Fix taken at 12:35:19 UTC
     A            Status A=active or V=Void.
     4807.038,N   Latitude 48 deg 07.038' N
     01131.000,E  Longitude 11 deg 31.000' E
     022.4        Speed over the ground in knots
     084.4        Track angle in degrees True
     230394       Date - 23rd of March 1994
     003.1,W      Magnetic Variation
     *6A          The checksum data, always begins with *
'''



def cleandata(gps,environment):
    #1. read the data from text file
    #2. put the data into list
    #3. clear the data so that the data only contains date,time,latitude,longtitude
    #4. find location that we stayed for more than 30 mins
    #5. group the data that stayed more than 30 mins
    #6.

    f  = open(gps, "r")
    gpsdatalist = []
    envdatalist = []
    envcleanlist = []
    gpscleanlist = []
    cleangpscleanlist = []
    cleanlist = []



    for line in f:
        '''
        $GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A
              0      1 2        3 4         5 6     7     8      9     10
        '''
        if len(line)>69:
            # print line
        # print type(line)
        # print line[3]
            locater_index = list(mit.locate(line, lambda x: x == ","))
            time = line[locater_index[0]+1:locater_index[1]-4]

            latitude = line[locater_index[2]+1:locater_index[3]]
            # print latitude
            degree = float(latitude[0:2])
            second = float(latitude[2:4]+"."+latitude[5:9])/60
            latitude = str(degree+second)
            # print latitude


            longtitude = line[locater_index[4]+1:locater_index[5]]
            # print longtitude
            degree = float(longtitude[0:3])
            # print degree
            second = float(longtitude[3:5]+"."+longtitude[6:10])/60
            # print second
            longtitude = '-'+str(degree+second)
            # print longtitude

            speed = line[locater_index[6]+1:locater_index[7]]
            date = line[locater_index[8]+1:locater_index[9]]
            gpscleanlist.append([date,time,latitude,longtitude,speed])
    print len(gpscleanlist)



        # print gpscleanlist
        # try:
        #     degree = float(items[20:22])
        #     # print items[22:24]
        #     # print items[25:29]
        #     second = float(items[22:24]+"."+items[25:29])/60
        #     latitude = str(degree+second)
        #     # print latitude
        #     # latitude = str(float(items[20:22])+float(items[22:24]+"."+items[26:29])/60)
        #     # latitude = latitude[0:6]
        # except:
        #     pass
        # latitude = items[20:22]+"."+str(float(items[22:24]+items[26:29])/60)
        # latitude = items[20:31]
        # for i in range(len(line)):
        #
        #     if line[i] == "$":
        #         #look for the dollar sign and append the next 63 letters into it
        #         #put the data into list
        #         # print line[i]
        #         # for i in range()
        #
        #         onedata =
        #         onedata = line[i:(i+63)]
        #         gpsdatalist.append(onedata)
        #     # print gpsdatalist
        #     # break
        # break




    # print gpsdatalist
    # print "blablabla"
    # # $GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A
    # # print gpsdatalist[0][7:13]
    # # print gpsdatalist[0][20:31]
    # # print gpsdatalist[0][32:44]
    # # print gpsdatalist[0][57:63]
    # print len(gpsdatalist)
    # print "CLEAN"
    # print gpsdatalist[0]
    # for items in gpsdatalist:
    #     gpseachlist = []
    #     #put each line of data into a list with format
    #     # [date,time,latitude,longtitude]
    #
    #     #date
    #     date = items[57:63]
    #     gpseachlist.append(date)
    #     #time
    #     time = items[7:13]
    #     gpseachlist.append(time)
    #     #latitude
    #     #reformat the latitude
    #     try:
    #         degree = float(items[20:22])
    #         # print items[22:24]
    #         # print items[25:29]
    #         second = float(items[22:24]+"."+items[25:29])/60
    #         latitude = str(degree+second)
    #         # print latitude
    #         # latitude = str(float(items[20:22])+float(items[22:24]+"."+items[26:29])/60)
    #         # latitude = latitude[0:6]
    #     except:
    #         pass
    #     # latitude = items[20:22]+"."+str(float(items[22:24]+items[26:29])/60)
    #     # latitude = items[20:31]
    #     gpseachlist.append(latitude)
    #     #longtitude
    #     #reformat the longtitude
    #     try:
    #         longtitude = "-"+str(float(items[32:35])+float(items[35:37]+"."+items[38:42])/60)
    #         # longtitude = longtitude[0:9]
    #     except:
    #         pass
    #     # longtitude = "-"+items[32:35]+"."+str(float(items[35:37]+items[38:42])/60)
    #     # longtitude = items[32:44]
    #     gpseachlist.append(longtitude)
    #     gpscleanlist.append(gpseachlist)
    #     # break



    # for items in gpscleanlist:
    #     # print items
    #     # discard any date that don't have the date or wrong date information
    #     if len(items[0])== 6:
    #         try:
    #             int(items[0])
    #             cleangpscleanlist.append(items)
    #         except:
    #             pass
    #
    #
    #
    # print len(cleangpscleanlist)
    # for item in cleangpscleanlist:
    #     print item
    # print cleangpscleanlist
    #
    #
    # print gpscleanlist

    '''
    dealing with environmental data

    environmental data

    #Tempature(*C), Barometric Pressure (in/Mg), Humidity(%), Gas/VOC(KOhms), Altitude(m)
    23:13:6, 26.32, 29.82, 43.10, 74.59, 149.85
    01234567
           0      1      2      3      4

    '''

    f  = open(environment, "r")

    for line in f:
        time = []
        locater_index = list(mit.locate(line, lambda x: x == ","))
        # print locater_index

        #time
        time = line[:locater_index[0]]
        # print len(time)
        time_locater_index = list(mit.locate(line, lambda x: x == ":"))
        # print time_locater_index == [2, 5]
        # print len(time) == 8
        # print time
        n=0
        if time_locater_index == [2, 5]:
            '''
            00:00:00
            00:00:0
            '''
            if len(time) == 8:
                time = time[0:2]+time[3:5]+time[6:]
                n=n+1
            if len(time) == 7 and n == 0:
                time = time[0:2]+time[3:5]+'0'+time[6:]
                n=n+1
        if time_locater_index == [2, 4] and n ==0:
            '''
            00:0:00
            00:0:0
            '''
            if len(time) == 7:
                time = time[0:2]+'0'+time[3:4]+time[5:]
                n=n+1
            if len(time) == 6 and n == 0:
                time = time[0:2]+'0'+time[3:4]+'0'+time[5:]
                n=n+1
        if time_locater_index == [1, 4] and n == 0:
            '''
            0:00:00
            0:00:0
            '''
            if len(time) == 7:
                # print time
                time = '0'+time[0:1]+time[2:4]+time[5:]
                n=n+1
                # print time
                # break
            if len(time) == 6 and n == 0:
                time = '0'+time[0:1]+time[2:4]+'0'+time[5:]
                n=n+1
            # print len(time)

        if time_locater_index == [1, 3] and n == 0:
            '''
            0:0:00
            0:0:0

            '''
            if len(time) == 6:
                time = '0'+time[0:1]+'0'+time[2:3]+time[4:]
            if len(time) == 5:
                time = '0'+time[0:1]+'0'+time[2:3]+'0'+time[4:]
        # print time










        # break
    #Tempature
        Tempature = line[locater_index[0]+1:locater_index[1]]
        #Barometric Pressure
        Barometric_Pressure = line[locater_index[1]+2:locater_index[2]]
        #Humidity
        Humidity = line[locater_index[2]+2:locater_index[3]]
        #Gas/VOC
        Gas = line[locater_index[3]+2:locater_index[4]]
        #Altitude
        Altitude = line[(locater_index[4]+2):(locater_index[4]+8)]
        #append each line of data to the environmental data environment data list
        envdatalist.append([time,Tempature,Barometric_Pressure,Humidity,Gas,Altitude])



    # for item in envdatalist:
    #     print item


    # print len(envdatalist)
    for i in range(len(gpscleanlist)):
        for j in range(len(envdatalist)):
            if gpscleanlist[i][1] == envdatalist[j][0]:
                eachlist = gpscleanlist[i]+envdatalist[j][1:]
                cleanlist.append(eachlist)
                eachlist = []

    # for items in cleanlist:
    #     print items
    print len(cleanlist)

    #     envdatalist.append(line)
    #
    # print len(envdatalist)
    # print envdatalist[0]
    # for items in envdatalist:
    #     enveachlist = []
    #     #put each line into the clean environmental data list
    #     #time
    #     enveachlist.append(items[0:2]+items[3:5]+items[6:8])
    #     #Tempature
    #     enveachlist.append(items[10:15])
    #     #Barometric Pressure
    #     enveachlist.append(items[17:22])
    #     #Humidity
    #     enveachlist.append(items[24:29])
    #     #Gas/VOC
    #     enveachlist.append(items[31:35])
    #     #Altitude
    #     enveachlist.append(items[37:43])
    #
    #
    #     envcleanlist.append(enveachlist)
    #     # break
    #
    # for items in envcleanlist:
    #     print items
    #
    gpsdataformat = ["Date","Time","Latitude","Longtitude","Speed"]
    with open('gpsdata313.csv', 'wb') as g:
        writer = csv.writer(g)
        writer.writerow(gpsdataformat)
        writer.writerows(gpscleanlist)

    envdataformat = ["time","Tempature","Barometric_Pressure","Humidity","Gas","Altitude"]
    with open('envdata313.csv', 'wb') as g:
        writer = csv.writer(g)
        writer.writerow(envdataformat)
        writer.writerows(envdatalist)
        writer.writerows(cleangpscleanlist)
    dataformat = gpsdataformat+["Tempature","Barometric_Pressure","Humidity","Gas","Altitude"]
    with open('data313.csv', 'wb') as g:
        writer = csv.writer(g)
        writer.writerow(dataformat)
        writer.writerows(cleanlist)

cleandata("gpsdata313.txt","envdata313.txt")
