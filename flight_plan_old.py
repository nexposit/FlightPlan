# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Flight_Plan_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import matplotlib.pyplot as plt
import main

fp = pd.DataFrame()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(723, 492)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stagesFormsHorizontalLayout = QtWidgets.QHBoxLayout()
        self.stagesFormsHorizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.stagesFormsHorizontalLayout.setObjectName("stagesFormsHorizontalLayout")
        self.departureVerticalLayout = QtWidgets.QVBoxLayout()
        self.departureVerticalLayout.setObjectName("departureVerticalLayout")
        self.departureFormLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.departureFormLabel.sizePolicy().hasHeightForWidth())
        self.departureFormLabel.setSizePolicy(sizePolicy)
        self.departureFormLabel.setObjectName("departureFormLabel")
        self.departureVerticalLayout.addWidget(self.departureFormLabel)
        self.departureForm = QtWidgets.QFormLayout()
        self.departureForm.setObjectName("departureForm")
        self.dep_airport = QtWidgets.QComboBox(self.centralwidget)
        self.dep_airport.setObjectName("dep_airport")
        self.departureForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dep_airport)
        self.dp_runway_label = QtWidgets.QLabel(self.centralwidget)
        self.dp_runway_label.setObjectName("dp_runway_label")
        self.departureForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.dp_runway_label)
        self.SID = QtWidgets.QComboBox(self.centralwidget)
        self.SID.setObjectName("SID")
        self.departureForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.SID)
        self.dp_sid_label = QtWidgets.QLabel(self.centralwidget)
        self.dp_sid_label.setObjectName("dp_sid_label")
        self.departureForm.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.dp_sid_label)
        self.runway = QtWidgets.QComboBox(self.centralwidget)
        self.runway.setObjectName("runway")
        self.departureForm.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.runway)
        self.dp_airport_label = QtWidgets.QLabel(self.centralwidget)
        self.dp_airport_label.setObjectName("dp_airport_label")
        self.departureForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.dp_airport_label)
        self.departureVerticalLayout.addLayout(self.departureForm)
        self.stagesFormsHorizontalLayout.addLayout(self.departureVerticalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.stagesFormsHorizontalLayout.addWidget(self.line)
        self.intermediateVerticalLayout = QtWidgets.QVBoxLayout()
        self.intermediateVerticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.intermediateVerticalLayout.setObjectName("intermediateVerticalLayout")
        self.intermediateFormLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.intermediateFormLabel.sizePolicy().hasHeightForWidth())
        self.intermediateFormLabel.setSizePolicy(sizePolicy)
        self.intermediateFormLabel.setObjectName("intermediateFormLabel")
        self.intermediateVerticalLayout.addWidget(self.intermediateFormLabel)
        self.in_waypoints_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.in_waypoints_label.sizePolicy().hasHeightForWidth())
        self.in_waypoints_label.setSizePolicy(sizePolicy)
        self.in_waypoints_label.setObjectName("in_waypoints_label")
        self.intermediateVerticalLayout.addWidget(self.in_waypoints_label)
        self.inter_waypoints = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inter_waypoints.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inter_waypoints.sizePolicy().hasHeightForWidth())
        self.inter_waypoints.setSizePolicy(sizePolicy)
        self.inter_waypoints.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inter_waypoints.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.inter_waypoints.setObjectName("inter_waypoints")
        self.intermediateVerticalLayout.addWidget(self.inter_waypoints)
        self.stagesFormsHorizontalLayout.addLayout(self.intermediateVerticalLayout)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.stagesFormsHorizontalLayout.addWidget(self.line_2)
        self.arrivalVerticalLayout = QtWidgets.QVBoxLayout()
        self.arrivalVerticalLayout.setObjectName("arrivalVerticalLayout")
        self.arrivalFormLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.arrivalFormLabel.sizePolicy().hasHeightForWidth())
        self.arrivalFormLabel.setSizePolicy(sizePolicy)
        self.arrivalFormLabel.setObjectName("arrivalFormLabel")
        self.arrivalVerticalLayout.addWidget(self.arrivalFormLabel)
        self.arrivalForm = QtWidgets.QFormLayout()
        self.arrivalForm.setObjectName("arrivalForm")
        self.ar_airport_label = QtWidgets.QLabel(self.centralwidget)
        self.ar_airport_label.setObjectName("ar_airport_label")
        self.arrivalForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ar_airport_label)
        self.arr_airport = QtWidgets.QComboBox(self.centralwidget)
        self.arr_airport.setObjectName("arr_airport")
        self.arrivalForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.arr_airport)
        self.ar_iap_label = QtWidgets.QLabel(self.centralwidget)
        self.ar_iap_label.setObjectName("ar_iap_label")
        self.arrivalForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ar_iap_label)
        self.IAP = QtWidgets.QComboBox(self.centralwidget)
        self.IAP.setObjectName("IAP")
        self.arrivalForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.IAP)
        self.arrivalVerticalLayout.addLayout(self.arrivalForm)
        self.stagesFormsHorizontalLayout.addLayout(self.arrivalVerticalLayout)
        self.verticalLayout_4.addLayout(self.stagesFormsHorizontalLayout)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.generateHorizontalLayout = QtWidgets.QHBoxLayout()
        self.generateHorizontalLayout.setObjectName("generateHorizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.generateHorizontalLayout.addItem(spacerItem)
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setObjectName("submit")
        self.generateHorizontalLayout.addWidget(self.submit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.generateHorizontalLayout.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.generateHorizontalLayout)
        self.tableGraphHorizontalLayout = QtWidgets.QHBoxLayout()
        self.tableGraphHorizontalLayout.setObjectName("tableGraphHorizontalLayout")
        self.tableVerticalLayout = QtWidgets.QVBoxLayout()
        self.tableVerticalLayout.setObjectName("tableVerticalLayout")
        self.tabla_waypoints = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabla_waypoints.sizePolicy().hasHeightForWidth())
        self.tabla_waypoints.setSizePolicy(sizePolicy)
        self.tabla_waypoints.setObjectName("tabla_waypoints")
        self.tabla_waypoints.setColumnCount(0)
        self.tabla_waypoints.setRowCount(0)
        self.tableVerticalLayout.addWidget(self.tabla_waypoints)
        self.to_excel = QtWidgets.QPushButton(self.centralwidget)
        self.to_excel.setObjectName("to_excel")
        self.tableVerticalLayout.addWidget(self.to_excel)
        self.tableGraphHorizontalLayout.addLayout(self.tableVerticalLayout)
        self.graphVerticalLayout = QtWidgets.QVBoxLayout()
        self.graphVerticalLayout.setObjectName("graphVerticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.graphVerticalLayout.addWidget(self.label)
        self.tableGraphHorizontalLayout.addLayout(self.graphVerticalLayout)
        self.verticalLayout_4.addLayout(self.tableGraphHorizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.dep_airport, self.SID)
        MainWindow.setTabOrder(self.SID, self.runway)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FlightPlanGUI"))
        self.departureFormLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Departure</span></p></body></html>"))
        self.dp_runway_label.setText(_translate("MainWindow", "SID"))
        self.dp_sid_label.setText(_translate("MainWindow", "Runway"))
        self.dp_airport_label.setText(_translate("MainWindow", "Airport"))
        self.intermediateFormLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Intermediate</span></p></body></html>"))
        self.in_waypoints_label.setText(_translate("MainWindow", "Waypoints"))
        self.arrivalFormLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Arrival</span></p></body></html>"))
        self.ar_airport_label.setText(_translate("MainWindow", "Airport"))
        self.ar_iap_label.setText(_translate("MainWindow", "IAP"))
        self.submit.setText(_translate("MainWindow", "Generate"))
        self.to_excel.setText(_translate("MainWindow", "Export .xlsx"))

    def setUp(self):
        departure_airport = main.departure['Airport'].unique()
        self.dep_airport.addItems([" "])
        self.dep_airport.addItems(departure_airport)
        self.dep_airport.currentTextChanged.connect(self.valores_sid)
        self.SID.currentTextChanged.connect(self.valores_runway)

        arrival_airport = main.arrival['Airport'].unique()
        self.arr_airport.addItems([" "])
        self.arr_airport.addItems(arrival_airport)

        self.arr_airport.currentTextChanged.connect(self.valores_iap)

        self.submit.clicked.connect(self.confirmar_formulario)
        self.to_excel.clicked.connect(self.table_to_excel)

    def valores_sid(self):
        airport = self.dep_airport.currentText()
        sid = main.departure[main.departure['Airport'] == airport]
        sid = sid['SID'].unique()
        self.SID.clear()
        self.SID.addItems([" "])
        self.SID.addItems(sid)

    def valores_runway(self):
        sid = self.SID.currentText()
        runway = main.departure[main.departure['SID'] == sid]
        runway = runway['Runway'].unique()
        self.runway.clear()
        self.runway.addItems([" "])
        self.runway.addItems(runway)

    def valores_iap(self):
        airport = self.arr_airport.currentText()
        iap = main.arrival[main.arrival['Airport'] == airport]
        iap = iap['IAP'].unique()
        self.IAP.clear()
        self.IAP.addItems([" "])
        self.IAP.addItems(iap)

    def confirmar_formulario(self):
        global fp
        dep_airport = self.dep_airport.currentText()
        sid = self.SID.currentText()
        runway = self.runway.currentText()
        waypoints = self.inter_waypoints.toPlainText()
        waypoints = waypoints.replace(" ", "")
        waypoints = waypoints.replace("\n", "")
        waypoints = waypoints.split(',')
        arr_airport = self.arr_airport.currentText()
        iap = self.IAP.currentText()

        if dep_airport != " " and sid != " " and runway != " " and arr_airport != " " and waypoints != "" and iap != " ":
            fp = main.flight_plan(dep_airport, sid, runway, waypoints, arr_airport, iap)
            self.crearTabla()
            self.crearGrafico()

    def crearTabla(self):
        global fp
        self.tabla_waypoints.clear()
        self.tabla_waypoints.setColumnCount(6)
        column = fp.columns.values
        for i in range(6):
            self.tabla_waypoints.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(column[i]))
        self.tabla_waypoints.setRowCount(fp.shape[0] - 1)
        for i in range(fp.shape[0]):
            for j in range(6):
                self.tabla_waypoints.setItem(i, j, QtWidgets.QTableWidgetItem(str(fp.iloc[i, j])))

    def crearGrafico(self):
        global fp
        fig, ax = plt.subplots()
        altitude = fp['Altitude']
        distance = fp['Leg_distance']
        ax.plot(distance, altitude)
        plt.title("Flight Plan")
        plt.xlabel("Distance (km)")
        plt.ylabel("Altitude (ft)")
        plt.savefig("output/flight_plan.png")
        self.mostrar_grafico()

    def table_to_excel(self):
        global fp
        fp.to_excel('output/ruta.xlsx')

    def mostrar_grafico(self):
        pixmap = QtGui.QPixmap('output/flight_plan.png')
        self.ruta_waypoints.setPixmap(pixmap)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.setUp()
    MainWindow.show()
    sys.exit(app.exec_())

