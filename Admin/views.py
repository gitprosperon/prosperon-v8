from django.shortcuts import render
from .forms import AddLocationForm, AddApartmentForm, OriginalJobForm, CreateNewJobForm
from Student.models import Location, Apartment, Job

# Create your views here.

def create_lcoations(request):
    list = ["New York, NY", "Los Angeles, CA", "Chicago, IL", "Dallas, TX", "Houston, TX", "Washington, DC",
            "Miami, FL", "Philadelphia, PA", "Atlanta, GA", "Phoenix, AZ", "Boston, MA", "San Francisco, CA",
            "Riverside, CA", "Detroit, MI", "Seattle, WA", "Minneapolis, MN", "San Diego, CA", "Tampa, FL",
            "Denver, CO", "St. Louis, MO", "Baltimore, MD", "Charlotte, NC", "Orlando, FL", "San Antonio, TX",
            "Portland, OR", "Sacramento, CA", "Las Vegas, NV", "Pittsburgh, PA", "Austin, TX", "Cincinnati, OH",
            "Kansas City, MO", "Columbus, OH", "Indianapolis, IN", "Cleveland, OH", "San Jose, CA", "Nashville, TN",
            "Virginia Beach, VA", "Providence, RI", "Jacksonville, FL", "Milwaukee, WI", "Oklahoma City, OK",
            "Raleigh, NC", "Memphis, TN", "Richmond, VA", "New Orleans, LA", "Louisville, KY", "Salt Lake City, UT",
            "Hartford, CT", "Buffalo, NY", "Birmingham, AL", "Grand Rapids, MI", "Rochester, NY", "Tucson, AZ",
            "Tulsa, OK", "Fresno, CA", "Urban Honolulu, HI", "Omaha, NE", "Worcester, MA", "Bridgeport, CT",
            "Greenville, SC", "Albuquerque, NM", "Bakersfield, CA", "Albany, NY", "Knoxville, TN", "McAllen, TX",
            "Baton Rouge, LA", "North Port, FL", "New Haven, CT", "Columbia, SC", "Allentown, PA", "El Paso, TX",
            "Oxnard, CA", "Charleston, SC", "Cape Coral, FL", "Greensboro, NC", "Boise City, ID", "Stockton, CA",
            "Colorado Springs, CO", "Little Rock, AR", "Lakeland, FL", "Des Moines, IA", "Akron, OH", "Springfield, MA",
            "Ogden, UT", "Deltona, FL", "Winston, NC", "Madison, WI", "Provo, UT", "Durham, NC", "Syracuse, NY",
            "Wichita, KS", "Toledo, OH", "Augusta, GA", "Palm Bay, FL", "Jackson, MS", "Harrisburg, PA", "Spokane, WA",
            "Chattanooga, TN", "Scranton, PA", "Modesto, CA", "Fayetteville, AR", "Lansing, MI", "Lancaster, PA",
            "Portland, ME", "Youngstown, OH", "Fayetteville, NC", "Lexington, KY", "Myrtle Beach, SC", "Pensacola, FL",
            "Port St. Lucie, FL", "Santa Rosa, CA", "Lafayette, LA", "Huntsville, AL", "Reno, NV", "Springfield, MO",
            "Visalia, CA", "Killeen, TX", "Asheville, NC", "York, PA", "Vallejo, CA", "Santa Maria, CA", "Salem, OR",
            "Salinas, CA", "Corpus Christi, TX", "Mobile, AL", "Brownsville, TX", "Salisbury, MD", "Reading, PA",
            "Gulfport, MS", "Manchester, NH", "Fort Wayne, IN", "Flint, MI", "Anchorage, AK", "Peoria, IL",
            "Canton, OH", "Savannah, GA", "Naples, FL", "Shreveport, LA", "Beaumont, TX", "Tallahassee, FL",
            "Eugene, OR", "Davenport, IA", "Ocala, FL", "Montgomery, AL", "Hickory, NC", "Trenton, NJ", "Ann Arbor, MI",
            "Fort Collins, CO", "Huntington, WV", "Lincoln, NE", "Rockford, IL", "Greeley, CO", "Gainesville, FL",
            "Boulder, CO", "Lubbock, TX", "Spartanburg, SC", "Green Bay, WI", "South Bend, IN", "Columbus, GA",
            "Evansville, IN", "Clarksville, TN", "Roanoke, VA", "Kingsport, TN", "Kennewick, WA", "Wilmington, NC",
            "Olympia, WA", "Hagerstown, MD", "Crestview, FL", "Duluth, MN", "Utica, NY", "Longview, TX",
            "San Luis Obispo, CA", "Merced, CA", "Waco, TX", "Cedar Rapids, IA", "Sioux Falls, SD", "Bremerton, WA",
            "Santa Cruz, CA", "Erie, PA", "College Station, TX", "Kalamazoo, MI", "Amarillo, TX", "Norwich, CT",
            "Lynchburg, VA", "Atlantic City, NJ", "Charleston, WV", "Tuscaloosa, AL", "Yakima, WA", "Fort Smith, AR",
            "Fargo, ND", "Appleton, WI", "Binghamton, NY", "Tyler, TX", "Lafayette, IN", "Bellingham, WA", "Topeka, KS",
            "Macon, GA", "Daphne, AL", "Hilton Head Island, SC", "Champaign, IL", "Rochester, MN", "Medford, OR",
            "Las Cruces, NM", "Burlington, VT", "Charlottesville, VA", "Yuma, AZ", "Lake Havasu City, AZ", "Athens, GA",
            "Barnstable Town, MA", "Chico, CA", "Lake Charles, LA", "Columbia, MO", "Houma, LA", "Gainesville, GA",
            "Elkhart, IN", "Springfield, IL", "Johnson City, TN", "Florence, SC", "Jacksonville, NC", "Hilo, HI",
            "St. Cloud, MN", "Bend, OR", "Monroe, LA", "Racine, WI", "Punta Gorda, FL", "Saginaw, MI",
            "Warner Robins, GA", "Terre Haute, IN", "St. George, UT", "Billings, MT", "Midland, TX", "Dover, DE",
            "Greenville, NC", "Bowling Green, KY", "El Centro, CA", "Joplin, MO", "Torrington, CT", "Jackson, TN",
            "Redding, CA", "Kingston, NY", "Yuba City, CA", "Iowa City, IA", "Muskegon, MI", "Abilene, TX",
            "Oshkosh, WI", "Burlington, NC", "Panama City, FL", "Bloomington, IL", "Coeur d'Alene, ID",
            "East Stroudsburg, PA", "Eau Claire, WI", "Pueblo, CO", "Hattiesburg, MS", "Bloomington, IN",
            "Waterloo, IA", "Kahului, HI", "Odessa, TX", "Blacksburg, VA", "Auburn, AL", "Tupelo, MS", "Wausau, WI",
            "Janesville, WI", "Sebastian, FL", "State College, PA", "Madera, CA", "Jackson, MI", "Chambersburg, PA",
            "Grand Junction, CO", "Idaho Falls, ID", "Elizabethtown, KY", "Niles, MI", "Homosassa Springs, FL",
            "Decatur, AL", "Hanford, CA", "Concord, NH", "Wichita Falls, TX", "Santa Fe, NM", "Bangor, ME",
            "Alexandria, LA", "Monroe, MI", "Dothan, AL", "Jefferson City, MO", "Texarkana, TX", "Florence, AL",
            "Valdosta, GA", "Rocky Mount, NC", "Albany, GA", "Sioux City, IA", "Rapid City, SD", "Logan, UT",
            "Flagstaff, AZ", "Winchester, VA", "Lebanon, PA", "Pottsville, PA", "Morgantown, WV", "Sumter, SC",
            "The Villages, FL", "Sherman, TX", "Wheeling, WV", "La Crosse, WI", "Hammond, LA", "Napa, CA",
            "Harrisonburg, VA", "Jonesboro, AR", "Carbondale, IL", "Eureka, CA", "Springfield, OH", "Battle Creek, MI",
            "Albany, OR", "Mount Vernon, WA", "Manhattan, KS", "Bismarck, ND", "Johnstown, PA", "Sierra Vista, AZ",
            "Lawton, OK", "Cleveland, TN", "Pittsfield, MA", "Ames, IA", "Staunton, VA", "Farmington, NM",
            "New Bern, NC", "Augusta, ME", "San Angelo, TX", "St. Joseph, MO", "Lawrence, KS", "Missoula, MT",
            "Wenatchee, WA", "Altoona, PA", "Mansfield, OH", "Brunswick, GA", "Holland, MI", "Bozeman, MT",
            "Wooster, OH", "Cookeville, TN", "Sheboygan, WI", "Weirton, WV", "California, MD", "Anniston, AL",
            "Muncie, IN", "Williamsport, PA", "Twin Falls, ID", "Show Low, AZ", "Longview, WA", "Roseburg, OR",
            "Michigan City, IN", "Kankakee, IL", "Lewiston, ME", "Richmond, KY", "Watertown, NY", "Sebring, FL",
            "Tullahoma, TN", "Kalispell, MT", "Bluefield, WV", "Whitewater, WI", "Pinehurst, NC", "LaGrange, GA",
            "Fond du Lac, WI", "Gettysburg, PA", "Mankato, MN", "Bay City, MI", "Lima, OH", "Ithaca, NY",
            "Cheyenne, WY", "Grand Forks, ND", "Hot Springs, AR", "Truckee, CA", "Victoria, TX", "Moses Lake, WA",
            "Shelby, NC", "Rome, GA", "Meridian, MS", "Dubuque, IA", "Cape Girardeau, MO", "Pocatello, ID",
            "Fairbanks, AK", "Corning, NY", "Corvallis, OR", "Clarksburg, WV", "Hermiston, OR", "Parkersburg, WV",
            "Grants Pass, OR", "Beaver Dam, WI", "Lufkin, TX", "Pine Bluff, AR", "Ukiah, CA", "Zanesville, OH",
            "Oak Harbor, WA", "Orangeburg, SC", "New Castle, PA", "Watertown, WI", "Columbus, IN", "Athens, TX",
            "Indiana, PA", "Midland, MI", "Hinesville, GA", "Bloomsburg, PA", "Kokomo, IN", "Centralia, WA",
            "Wilson, NC", "Stillwater, OK", "Great Falls, MT", "Statesboro, GA", "Casper, WY", "Warsaw, IN",
            "Searcy, AR", "Glenwood Springs, CO", "Heber, UT", "Minot, ND", "Keene, NH", "Jefferson, GA",
            "Aberdeen, WA", "Findlay, OH", "Danville, IL", "Frankfort, KY", "Key West, FL", "Shawnee, OK",
            "Lake City, FL", "Wisconsin Rapids, WI", "Huntsville, TX", "Stevens Point, WI", "Morehead City, NC",
            "Klamath Falls, OR", "Shelton, WA", "Alamogordo, NM", "Muskogee, OK", "Faribault, MN", "Richmond, IN",
            "Roswell, NM", "Red Bluff, CA", "Clearlake, CA", "Baraboo, WI", "Sanford, NC", "Hutchinson, KS",
            "Laconia, NH", "Walla Walla, WA", "Enid, OK", "Salina, KS", "Hudson, NY", "Starkville, MS", "Ardmore, OK",
            "Carlsbad, NM", "Fernley, NV", "Norwalk, OH", "Gaffney, SC", "Cedar City, UT", "Durango, CO", "Branson, MO",
            "Carson City, NV", "St. Marys, GA", "Oxford, MS", "Warrensburg, MO", "Elizabeth City, NC",
            "Milledgeville, GA", "Rexburg, ID", "Enterprise, AL", "Kerrville, TX", "Corsicana, TX", "Newport, OR",
            "Winona, MN", "Pullman, WA", "Ellensburg, WA", "Ozark, AL", "Clovis, NM", "Pahrump, NV", "New Castle, IN",
            "Fort Polk South, LA", "Norfolk, NE", "Sandpoint, ID", "Ruston, LA", "Vicksburg, MS", "Rolla, MO",
            "Thomasville, GA", "Stephenville, TX", "Rock Springs, WY", "Moscow, ID", "Astoria, OR", "Murray, KY",
            "Laramie, WY", "Cambridge, OH", "Pittsburg, KS", "Williston, ND", "Ada, OK", "Crawfordsville, IN",
            "Bay City, TX", "Fremont, NE", "Emporia, KS", "Brookings, SD", "North Platte, NE", "Butte, MT",
            "Susanville, CA", "Kirksville, MO", "The Dalles, OR", "Fallon, NV", "Jamestown, ND"]
    list2 = ["3062.22", "2916.55", "1838.89", "1802.25", "1654.29", "2198.16", "2770.63", "1776.65", "1953.03",
             "1881.83", "2874.26", "3100.37", "2513.50", "1420.79", "2166.16", "1613.64", "2990.96", "2093.40",
             "1970.08", "1290.66", "1763.62", "1781.49", "1995.62", "1480.59", "1874.88", "2264.30", "1799.91",
             "1327.96", "1869.35", "1516.23", "1356.28", "1408.74", "1442.52", "1331.23", "3216.48", "1855.86",
             "1628.65", "1898.67", "1757.23", "1194.47", "1306.06", "1744.11", "1481.09", "1547.93", "1525.33",
             "1281.07", "1751.30", "1667.39", "1217.58", "1293.38", "1605.09", "1362.81", "1582.43", "1278.16",
             "1893.19", "2619.85", "1233.08", "1857.63", "2687.80", "1520.05", "1537.87", "1680.08", "1364.44",
             "1717.83", "1179.35", "1343.98", "2457.48", "1803.83", "1465.97", "1710.70", "1460.57", "2942.04",
             "1897.78", "2251.39", "1413.98", "1751.62", "2329.59", "1835.28", "1143.65", "1876.67", "1179.53",
             "1122.54", "1694.92", "1730.78", "1891.45", "1586.49", "1556.00", "1681.78", "1667.00", "1467.24",
             "992.12", "1164.35", "1332.82", "2019.12", "1411.98", "1325.57", "1521.49", "1544.02", "1181.95",
             "1909.57", "1496.64", "1213.70", "1307.88", "2134.03", "867.16", "1391.52", "1356.68", "1805.87",
             "1616.04", "2332.96", "2623.06", "1184.89", "1517.97", "1913.73", "1209.84", "1736.63", "1340.73",
             "1835.17", "1285.47", "2394.52", "3550.27", "1696.16", "2458.24", "1335.30", "1098.77", "1134.38",
             "1727.85", "1282.47", "1362.31", "1901.35", "1113.38", "1051.69", "1588.51", "965.35", "988.57", "1742.90",
             "3151.50", "974.16", "1224.18", "1319.51", "1801.38", "916.61", "1591.59", "1226.29", "1438.15", "2345.52",
             "2092.86", "1820.47", "857.31", "1165.27", "1057.43", "1732.26", "1620.45", "2347.28", "1250.00",
             "1344.73", "932.30", "1212.47", "1200.43", "910.97", "1322.43", "1308.04", "1275.69", "1778.76", "1757.98",
             "2027.92", "1416.30", "1943.77", "1571.34", "1183.75", "1249.71", "2636.83", "1836.65", "1535.98",
             "960.45", "1116.48", "1978.77", "3438.20", "958.50", "1850.61", "1440.53", "1320.07", "1698.76", "1210.42",
             "1765.80", "821.41", "1537.91", "1397.66", "1043.36", "1233.56", "1162.48", "1303.36", "1497.79",
             "1349.08", "1981.04", "1023.79", "1086.30", "1604.12", "2295.86", "1096.61", "1443.95", "1824.90",
             "1355.03", "2009.76", "1705.46", "1436.25", "1612.44", "1879.44", "2514.85", "1604.34", "1123.87",
             "1184.41", "1222.47", "1771.97", "1131.50", "1097.51", "1311.62", "1206.22", "1258.00", "2574.00",
             "1309.35", "2177.14", "1081.50", "960.91", "2543.93", "863.33", "1376.19", "891.84", "1719.00", "1420.90",
             "1369.74", "1552.06", "1460.68", "1294.24", "1737.50", "1020.56", "1536.15", "1484.72", "1489.67",
             "2006.79", "2051.75", "1171.71", "1101.12", "1024.60", "963.73", "1295.88", "1739.42", "1233.14",
             "1817.98", "1800.62", "1110.72", "1318.01", "1342.19", "1744.30", "979.71", "3546.67", "1228.05",
             "1612.20", "1493.01", "1182.92", "801.94", "903.33", "2297.09", "1826.10", "1940.83", "1046.22", "1163.33",
             "1524.36", "1220.00", "1283.90", "1404.46", "1540.82", "1338.22", "1871.33", "1866.98", "1098.76",
             "1946.62", "1302.78", "991.67", "1112.48", "1466.67", "987.50", "1121.11", "1192.67", "1430.44", "1203.89",
             "1078.99", "1062.08", "1428.29", "1332.22", "2239.57", "1656.89", "1275.14", "950.00", "1338.01",
             "1176.24", "2121.39", "1462.75", "835.67", "1000.07", "1270.95", "3022.96", "1507.73", "1293.81", "852.78",
             "1385.00", "866.25", "1130.13", "1622.86", "2140.21", "1258.77", "1230.89", "883.38", "1207.08", "902.72",
             "1394.38", "1469.03", "1184.63", "1173.00", "1212.50", "1450.61", "1348.13", "1422.34", "797.08",
             "1507.75", "1747.57", "1785.52", "855.42", "950.00", "1686.77", "1436.56", "2506.01", "1089.25", "1455.25",
             "1025.00", "790.14", "1494.40", "1085.56", "1005.69", "892.50", "1572.92", "2125.00", "1629.72", "1500.00",
             "861.00", "1213.67", "1424.50", "1052.29", "1279.44", "1315.27", "1416.67", "2104.42", "633.33", "1209.86",
             "1842.42", "1454.72", "901.00", "1136.39", "1539.33", "1018.78", "1012.78", "2041.22", "1246.26", "835.54",
             "1023.19", "2263.49", "1181.50", "1486.03", "1436.25", "1282.36", "937.50", "915.65", "833.61", "1090.11",
             "1645.67", "1273.13", "1725.74", "858.61", "1279.38", "861.67", "1750.00", "777.00", "1075.00", "850.00",
             "1929.17", "864.17", "1744.16", "1450.00", "806.25", "1085.83", "1106.53", "1498.75", "1276.28", "1407.76",
             "1546.98", "1078.47", "837.86", "1225.83", "860.00", "1157.08", "1289.19", "1126.33", "1162.37", "1655.50",
             "1017.50", "20134.92", "2823.56", "865.02", "1521.67", "2003.33", "1405.83", "1019.50", "630.93", "844.33",
             "4506.11", "1053.75", "1434.75", "998.13", "1100.75", "1686.67", "1708.89", "1625.00", "1414.00",
             "1325.00", "778.67", "1397.50", "745.00", "1433.33", "1500.00", "1583.33", "987.00", "961.25", "722.50",
             "1775.00", "1679.33", "1093.88", "781.50", "2119.44", "990.00", "1103.00", "1890.83", "1748.75", "1199.50",
             "880.00", "1437.92", "1826.94", "1075.00", "1766.67", "1663.81", "2041.67", "831.63", "1360.27", "1295.83",
             "1047.08", "1187.44", "1416.67", "1133.58", "1450.00", "995.83", "1078.61", "1685.14", "1175.00",
             "1034.11", "1504.17", "916.11", "1162.50", "823.33", "1700.00", "818.06", "725.00", "850.00", "1447.50",
             "1525.00", "1153.73", "795.00", "1646.33", "963.33", "1055.17", "649.50", "900.00", "937.09", "869.00",
             "891.00", "1067.00", "1086.94", "737.50", "1192.67", "866.67", "998.61", "1322.50", "727.25", "1530.56",
             "1456.25", "681.75"]

    i = 0
    while i <= 494:
        city = list[i]
        average_rent = list2[i]

        form = AddLocationForm(request.POST)

        newLocation = form.save(commit=False)

        newLocation.city = city
        newLocation.average_rent = average_rent

        newLocation.save()




        print(list[i])
        print(list2[i])
        i += 1

    print('test264323452')
    return render(request, 'Admin/create-locations.html')


def apartmentAdd(request, title, address, sqFeet, yearly_cost, general_information, bedrooms, bathrooms, img, initial_cost, location):
    form = AddApartmentForm(request.POST)
    newApartment = form.save(commit=False)
    newApartment.title = title
    newApartment.address = address
    newApartment.sqFeet = sqFeet
    newApartment.yearly_cost = yearly_cost
    newApartment.general_information = general_information
    newApartment.bedrooms = bedrooms
    newApartment.bathrooms = bathrooms
    newApartment.img = img
    newApartment.initial_cost = initial_cost
    newApartment.location = location
    newApartment.save()
    print('new apartment saved')

def addAllApartments(request):
    apartmemnt_1 = Apartment.objects.get(id=2)
    apartmemnt_2 = Apartment.objects.get(id=3)
    apartmemnt_3 = Apartment.objects.get(id=4)
    apartmemnt_4 = Apartment.objects.get(id=5)
    first_apartments = [[apartmemnt_1, '1'], [apartmemnt_2, '2'], [apartmemnt_3, '3'], [apartmemnt_4, '4']]
    locations = Location.objects.all()

    for location in locations:
        print('city: ', location.city)
        for apartment in first_apartments:
            print('the apartment: ', apartment[0].title)
            if apartment[1] == '1':
                cost = round((location.average_rent) * 12)
                initial = round((cost / 12) * 2)
                print(initial)
                print(cost)
            if apartment[1] == '2':
                cost = round((location.average_rent * 1.1) * 12)
                initial = round((cost / 12) * 2)
                print(initial)
                print(cost)
            if apartment[1] == '3':
                cost = round((location.average_rent * .7) * 12)
                initial = round(((cost / 12) * 2) / 2)
                print(initial)
                print(cost)
            if apartment[1] == '4':
                cost = round((location.average_rent * .9) * 12)
                initial = round(((cost / 12) * 2) / 3)
                print(initial)
                print(cost)

            apartment = apartment[0]
            apartmentAdd(request, apartment.title, apartment.address, apartment.sqFeet, cost, apartment.general_information, apartment.bedrooms, apartment.bathrooms, apartment.img, initial, location)

    print('adding all apartments')
    return render(request, 'Admin/create-locations.html')





def createOriginalJob(request):
    print('create original graph')
    id = 161
    for location in Location.objects.all():
        for job in Job.objects.filter(original='Yes'):
            jobForm = CreateNewJobForm(request.POST)
            theJobObject = jobForm.save(commit=False)
            theJobObject.original = 'No'
            theJobObject.title = job.title
            theJobObject.company = job.company
            theJobObject.job_id = id
            id += 1
            theJobObject.location = location.city
            theJobObject.job_city = location
            theJobObject.logo = job.logo
            theJobObject.salary_range = job.salary_range
            theJobObject.job_type = job.job_type
            theJobObject.job_hours = job.job_hours
            theJobObject.pay_structure = job.pay_structure
            theJobObject.company_401k = job.company_401k
            theJobObject.health = job.health
            theJobObject.dental = job.dental
            theJobObject.vision = job.vision
            theJobObject.pto = job.pto
            theJobObject.student_loan_assist = job.student_loan_assist
            theJobObject.relocation = job.relocation
            theJobObject.company_requirements = job.company_requirements
            theJobObject.company_qualifications = job.company_qualifications
            theJobObject.company_description = job.company_description
            theJobObject.major = job.major
            theJobObject.save()




    return render(request, 'Admin/create-locations.html')
