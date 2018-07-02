import matplotlib.pyplot as plt
import ogr

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
this_parcel = lyr.GetFeature(fid)
geom_this_parcel = this_parcel.geometry()
lyr.ResetReading()
neighbor_parcel = list()
for parcel in lyr:
    geom_parcel = parcel.geometry()
    a = geom_this_parcel.Intersects(geom_parcel)
    if a:
        neighbor_parcel.append(parcel.GetFID())
#print neighbor_parcel
#def plot_parcel():
"""ring1 = geom_this_parcel.GetGeometryRef(0)
coords = ring1.GetPoints()
x,y = zip(*coords)
plt.plot(x,y,'k')"""


for item in neighbor_parcel:
    neighbor_feature = lyr.GetFeature(item)
    geom_feature = neighbor_feature.geometry()
    ring = geom_feature.GetGeometryRef(0)
    coords = ring.GetPoints()
    x,y = zip(*coords)
    plt.plot(x,y,'k')
    centroid = geom_feature.Centroid()
    x_centroid = centroid.GetX()
    y_centroid = centroid.GetY()
    plt.text(x_centroid,y_centroid, neighbor_feature.GetField("PARCELNO"))

plt.axis('equal')
plt.show()  
    



        
    
    
               

