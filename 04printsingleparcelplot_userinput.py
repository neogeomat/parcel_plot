import matplotlib.pyplot as plt
import ogr

# The only way to get MDBs to load in 64-bit is by renaming the Registry Key 
# HKEY_LOCAL_MACHINE\SOFTWARE\ODBC\ODBCINST.INI\Microsoft Access Driver (*.mdb, *.accdb) 
# to 
# HKEY_LOCAL_MACHINE\SOFTWARE\ODBC\ODBCINST.INI\Microsoft Access Driver (*.mdb) using regedit.

ds = ogr.Open(r'D:\Wordpress\Amritdai\04printmdb\Nilbarahi.mdb')
lyr = ds.GetLayer("Parcel")

#make list of all the parcelno this database have
all_parcel = list()
for parcel in lyr:
    all_parcel.append(parcel.GetField("PARCELNO"))

#take parcel no as input and if parcel no do not exist in database prompt for
#next parcel no
inparcelno = 0
def inputparcel():
    inparcelno1 = int(raw_input("enter parcel no"))    
    #print inparcelno1
    if inparcelno1 in all_parcel:
        global inparcelno
        inparcelno = inparcelno1 
    else:
        print "this parcel no doesnt exist in this dbase"
        inputparcel()
inputparcel()

#get the fid of corresponding parcel no
fid = 0
for parcel in lyr:
    parcelno1 = parcel.GetField("PARCELNO")
    #fid1 = parcel.GetField("OBJECTID")
    if parcelno1 == inparcelno:
        fid = parcel.GetField("OBJECTID")
        
#get geometry of this fid
thisparcel = lyr.GetFeature(fid)
geom = thisparcel.geometry()
ring = geom.GetGeometryRef(0)
centroid1 = geom.Centroid()
#print type(centroid1)
#print centroid1
#print centroid1.GetX(), centroid1.GetY()
coords = ring.GetPoints()
x,y = zip(*coords)

#plot the parcel
plt.plot(x,y, 'k')
plt.axis('equal')
plt.text(centroid1.GetX(),centroid1.GetY(), str(inparcelno))
plt.show()
        
    
    
               

