from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
import os
import pandas as pd
import geopandas as gpd
import pyproj
from shapely.geometry import Point

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(428, 362)
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(180, 160, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 200, 95, 16))
        self.label_6.setObjectName("label_6")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(180, 200, 69, 22))
        self.comboBox_2.setObjectName("comboBox")
        self.comboBox_2.addItem("<10 cm", 0.1)
        self.comboBox_2.addItem("<15 cm", 0.15)        
        self.comboBox_2.addItem("<20 cm", 0.2)
        self.comboBox_2.addItem("<25 cm", 0.25)
        self.comboBox_2.addItem("<30 cm", 0.3)
        self.comboBox_2.addItem("<35 cm", 0.35)
        self.comboBox_2.addItem("<40 cm", 0.4)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 40, 151, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 80, 151, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 120, 151, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(300, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(40, 300, 361, 21))
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setObjectName("progressBar")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(180, 270, 61, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 40, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 80, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 120, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dot Spraying Validation"))
        self.comboBox.setItemText(0, _translate("Dialog", "47N"))
        self.comboBox.setItemText(1, _translate("Dialog", "47S"))
        self.comboBox.setItemText(2, _translate("Dialog", "48N"))
        self.comboBox.setItemText(3, _translate("Dialog", "48S"))
        self.comboBox.setItemText(4, _translate("Dialog", "49N"))
        self.comboBox.setItemText(5, _translate("Dialog", "49S"))
        self.comboBox.setItemText(6, _translate("Dialog", "50N"))
        self.comboBox.setItemText(7, _translate("Dialog", "50S"))
        self.comboBox.setItemText(8, _translate("Dialog", "51S"))
        self.comboBox.setItemText(9, _translate("Dialog", "52S"))
        self.label.setText(_translate("Dialog", "Masukkan Folder Log UAV"))
        self.label_2.setText(_translate("Dialog", "Masukkan Folder .shp Palm"))
        self.label_3.setText(_translate("Dialog", "Masukkan Folder Hasil"))
        self.label_4.setText(_translate("Dialog", "Pilih Zona UTM"))
        self.label_6.setText(_translate("Dialog", "Pilih Tingkat Akurasi"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "<10 cm"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "<15 cm"))        
        self.comboBox_2.setItemText(2, _translate("Dialog", "<20 cm"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "<25 cm"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "<30 cm"))
        self.comboBox_2.setItemText(5, _translate("Dialog", "<35 cm"))
        self.comboBox_2.setItemText(6, _translate("Dialog", "<40 cm"))
        self.pushButton_2.setText(_translate("Dialog", "Pilih .log"))
        self.pushButton_2.clicked.connect(lambda: self.pushButton_handler1("Pilih .log"))
        self.pushButton_3.setText(_translate("Dialog", "Pilih .shp"))
        self.pushButton_3.clicked.connect(lambda: self.pushButton_handler2("Pilih .shp"))
        self.pushButton_4.setText(_translate("Dialog", "Pilih hasil"))
        self.pushButton_4.clicked.connect(lambda: self.pushButton_handler3("Pilih hasil"))
        self.pushButton.setText(_translate("Dialog", "Process"))
        self.pushButton.clicked.connect(lambda: self.pushButton_handler("Process"))
        self.label_5.setText(_translate("Dialog", "Loading..."))

    def pushButton_handler1(self, button_name):
        self.data = QFileDialog.getExistingDirectory()
        self.lineEdit.setText(f"{button_name} - Directory Selected: {self.data}")

    def pushButton_handler2(self, button_name):
        self.pohon = QFileDialog.getExistingDirectory()
        self.lineEdit_2.setText(f"{button_name} - Directory Selected: {self.pohon}")

    def pushButton_handler3(self, button_name):
        self.result = QFileDialog.getExistingDirectory()
        self.lineEdit_3.setText(f"{button_name} - Directory Selected: {self.result}")

    def pushButton_handler(self, button_name):
        if hasattr(self, 'data') and hasattr(self, 'pohon') and hasattr(self, 'result'):
            self.progressBar.setValue(0)
            self.process_data()
        else:
            QMessageBox.warning(self, "Warning", "Please select all directories before processing.")

    def process_data(self):
        self.progressBar.setValue(0)
        
        list_directory = ["merge_drone","merge_tree", "last_result"]
        merge_drone = os.path.join(self.result,list_directory[0])
        merge_tree = os.path.join(self.result,list_directory[1])
        last_result = os.path.join(self.result,list_directory[2])
        os.makedirs(merge_drone, exist_ok=True)
        os.makedirs(merge_tree, exist_ok=True)
        os.makedirs(last_result, exist_ok=True)
    
        zone_mapping = {
            "47N": 'EPSG:32647',
            "47S": 'EPSG:32747',
            "48N": 'EPSG:32648',
            "48S": 'EPSG:32748',
            "49N": 'EPSG:32649',
            "49S": 'EPSG:32749',
            "50S": 'EPSG:32750',
            "51S": 'EPSG:32751',
            "52S": 'EPSG:32752'
        }
        
        self.progressBar.setValue(2)
        for file in os.listdir(self.data):
            if file.find(".log") != -1:
                base = os.path.splitext(file)[0]
                with open(os.path.join(self.data,file),"r") as f:
                    gps_all = []
                    lines = f.readlines()
                    try:
                        for i in range(0,len(lines)-1,1):
                            if(lines[i].split(", ")[0]=="GPS"):
                                gps_all.append(lines[i])
                    except:
                        pass
                    gps_used = []

                    for i in range(0,len(gps_all)-1,1):
                        if int(gps_all[i].split(", ")[-1]) == int(1):
                            gps_used.append(gps_all[i])            
                    longitude = []
                    latitude = []
                    for row in gps_used:
                        longitude.append(row.split(", ")[9])
                        latitude.append(row.split(", ")[8])           
                    dict = {"x":longitude, "y":latitude}
                    df = pd.DataFrame(dict)
                    print("Generating " + base + " to csv")
                    df.to_csv(os.path.join(merge_drone, base + ".csv"))

        #gabung log
        csv_files = [file for file in os.listdir(merge_drone) if file.endswith('.csv')]

        dfs = []
        for csv_file in csv_files:
            df = pd.read_csv(os.path.join(merge_drone, csv_file))
            dfs.append(df)
        merged_df = pd.concat(dfs, ignore_index=True)

        merged_df.to_csv(os.path.join(merge_drone, 'merged_gps.csv'), index=False)
        print("Data GPS dari semua file log telah digabungkan dalam satu file CSV.") 
        
        self.progressBar.setValue(10)

        #gabung shp
        directory = self.pohon
        gdfs = []

        for filename in os.listdir(directory):
            if filename.endswith('.shp'):  # Hanya memproses file shapefile
                filepath = os.path.join(directory, filename)
                gdf = gpd.read_file(filepath)  # Membaca file shapefile dan memuatnya ke dalam GeoDataFrame
                gdfs.append(gdf)  # Menambahkan GeoDataFrame ke dalam daftar

        merged_gdf = gpd.GeoDataFrame(pd.concat(gdfs, ignore_index=True))

        merged_gdf.to_file(os.path.join(merge_tree, 'merged_file.shp'))
        print("Data .shp dari semua file log telah digabungkan dalam satu file.") 
        self.progressBar.setValue(20)

        #============================================================================
        point_palm = gpd.read_file(os.path.join(merge_tree, 'merged_file.shp'))
        point_palm['no'] = range(1, len(point_palm) + 1)

        kolom = ['geometry', 'no']
        point_palm2 = point_palm[kolom]

        point_palm3 = point_palm2.copy()
        point_palm3['geometry'] = point_palm3['geometry'].to_crs(epsg=4326)
        point_palm3['x'] = point_palm3['geometry'].x
        point_palm3['y'] = point_palm3['geometry'].y
        self.progressBar.setValue(25)

        kolom1 = ['no', 'x', 'y']
        point_palm3 = point_palm3[kolom1]

        point_palm_fix = pd.merge(point_palm2, point_palm3, on=["no"])

        point_uav = pd.read_csv(os.path.join(merge_drone, 'merged_gps.csv'))
        point_uav = point_uav.drop(columns='Unnamed: 0')
        self.progressBar.setValue(30)

        geometry = [Point(xy) for xy in zip(point_uav['x'], point_uav['y'])]

        crs_wgs84 = 'EPSG:4326'
        crs_utm48n = zone_mapping[self.comboBox.currentText()]

        transformer = pyproj.Transformer.from_crs(crs_wgs84, crs_utm48n, always_xy=True)
        transformed_geometry = [Point(transformer.transform(point.x, point.y)) for point in geometry]
        point_uav_proj = gpd.GeoDataFrame(point_uav, geometry=transformed_geometry, crs=crs_utm48n)
        point_uav_proj['no'] = range(1, len(point_uav_proj) + 1)
        
        self.progressBar.setValue(40)

        data_uav = point_uav_proj
        data_pohon = point_palm_fix
        
        buffer_pohon = data_pohon.buffer(1)
        hasil_pengukuran_terdekat = gpd.GeoDataFrame(columns=['x_penyemprotan', 'y_penyemprotan', 'jarak', 'penyemprotan'])
        self.progressBar.setValue(45)

        for idx, pohon in data_pohon.iterrows():
            buffer_area = buffer_pohon.iloc[idx]

            data_terbang_dalam_buffer = data_uav[data_uav.geometry.intersects(buffer_area)]

            titik_terbang_terdekat = None
            jarak_terpendek = float('inf')
            for idx, terbang in data_terbang_dalam_buffer.iterrows():
                jarak = pohon.geometry.distance(terbang.geometry)
                if jarak < jarak_terpendek:
                    jarak_terpendek = jarak
                    titik_terbang_terdekat = terbang.geometry
                    terbang = terbang

            selected_accuracy = self.comboBox_2.currentData()

            if jarak_terpendek < selected_accuracy:
                status_penyemprotan = 'penyemprotan tepat'
            elif jarak_terpendek > 1:
                status_penyemprotan = 'tidak disemprot'
            else:
                status_penyemprotan = 'penyemprotan bergeser'

            hasil_pengukuran_terdekat = hasil_pengukuran_terdekat._append({'x_penyemprotan': terbang['x'], 'y_penyemprotan': terbang['y'], 'jarak': jarak_terpendek, 'penyemprotan': status_penyemprotan}, ignore_index=True)
            hasil_pengukuran_terdekat.to_csv(os.path.join(last_result, 'hasil_pengukuran.csv'))
            
        self.progressBar.setFormat("Completed")  # Update progress bar format
        self.progressBar.setValue(100)
            
        print('selesai')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())