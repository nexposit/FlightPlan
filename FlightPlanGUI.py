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
import FlightPlan


class Ui_MainWindow(object):
    fp = pd.DataFrame()  # Dataframe for FlightPlan

    # Created by: PyQt5 UI code generator 5.15.4
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
        self.ruta_waypoints = QtWidgets.QLabel(self.centralwidget)
        self.ruta_waypoints.setText("")
        self.ruta_waypoints.setObjectName("ruta_waypoints")
        self.graphVerticalLayout.addWidget(self.ruta_waypoints)
        self.tableGraphHorizontalLayout.addLayout(self.graphVerticalLayout)
        self.verticalLayout_4.addLayout(self.tableGraphHorizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.dep_airport, self.SID)
        MainWindow.setTabOrder(self.SID, self.runway)

    # Created by: PyQt5 UI code generator 5.15.4
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FlightPlanGUI"))
        self.departureFormLabel.setText(_translate("MainWindow",
                                                   "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Departure</span></p></body></html>"))
        self.dp_runway_label.setText(_translate("MainWindow", "SID"))
        self.dp_sid_label.setText(_translate("MainWindow", "Runway"))
        self.dp_airport_label.setText(_translate("MainWindow", "Airport"))
        self.intermediateFormLabel.setText(_translate("MainWindow",
                                                      "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Intermediate</span></p></body></html>"))
        self.in_waypoints_label.setText(_translate("MainWindow", "Waypoints"))
        self.arrivalFormLabel.setText(_translate("MainWindow",
                                                 "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Arrival</span></p></body></html>"))
        self.ar_airport_label.setText(_translate("MainWindow", "Airport"))
        self.ar_iap_label.setText(_translate("MainWindow", "IAP"))
        self.submit.setText(_translate("MainWindow", "Generate"))
        self.to_excel.setText(_translate("MainWindow", "Export .xlsx"))

    # Setup all relationated with the form
    def setupForms(self):
        # Function that changes values of the drop-down when some data has changed
        def onChanged(table, selected, selectedText, affected, affectedComboBox):
            items = table[table[selected] == selectedText][affected].unique()
            affectedComboBox.clear()
            affectedComboBox.addItem(" ")
            affectedComboBox.addItems(items)

        self.dep_airport.addItem(" ")
        self.dep_airport.addItems(FlightPlan.departure['Airport'].unique())

        self.arr_airport.addItem(" ")
        self.arr_airport.addItems(FlightPlan.arrival['Airport'].unique())

        # When departure airport is selected, departure SID will change
        self.dep_airport.currentTextChanged.connect(
            lambda: onChanged(
                FlightPlan.departure,
                'Airport',
                self.dep_airport.currentText(),
                'SID',
                self.SID
            )
        )
        # When departure SID is selected, departure runway will change
        self.SID.currentTextChanged.connect(
            lambda: onChanged(
                FlightPlan.departure,
                'SID',
                self.SID.currentText(),
                'Runway',
                self.runway
            )
        )
        # When arrival airport is selected, arrival IAP will change
        self.arr_airport.currentTextChanged.connect(
            lambda: onChanged(
                FlightPlan.arrival,
                'Airport',
                self.arr_airport.currentText(),
                'IAP',
                self.IAP
            )
        )
    # Function that removes all whitespace and line break
    def cleanWaypointsInput(self):
        waypoints = self.inter_waypoints.toPlainText()
        waypoints = waypoints.replace(" ", "")
        waypoints = waypoints.replace("\n", "")
        waypoints = waypoints.split(',')
        return waypoints

    def generateFlightPlan(self):
        self.fp = FlightPlan.flight_plan(
            self.dep_airport.currentText(),
            self.SID.currentText(),
            self.runway.currentText(),
            self.cleanWaypointsInput(),
            self.arr_airport.currentText(),
            self.IAP.currentText()
        )

    def createTable(self):
        self.tabla_waypoints.clear()

        self.tabla_waypoints.setColumnCount(self.fp.shape[1])
        columns = self.fp.columns.values
        for i in range(self.fp.shape[1]):  # Create the table headers
            self.tabla_waypoints.setHorizontalHeaderItem(
                i,
                QtWidgets.QTableWidgetItem(columns[i])
            )

        self.tabla_waypoints.setRowCount(self.fp.shape[0] - 1)
        for i in range(self.fp.shape[0]):
            for j in range(self.fp.shape[1]):
                self.tabla_waypoints.setItem(
                    i,
                    j,
                    QtWidgets.QTableWidgetItem(str(self.fp.iloc[i, j]))
                )

    def crearGraph(self):
        fig, ax = plt.subplots()
        altitude = self.fp['Altitude']
        distance = self.fp['Leg_distance']
        ax.plot(distance, altitude)
        plt.title("Flight Plan")
        plt.xlabel("Distance (km)")
        plt.ylabel("Altitude (ft)")
        plt.savefig("output/flight_plan.png")
        self.showGraph()

    def showGraph(self):
        pixmap = QtGui.QPixmap('output/flight_plan.png')
        self.ruta_waypoints.setPixmap(pixmap)

    def setup(self):
        self.setupForms()

        def onGenerate():
            if (
                    self.dep_airport.currentText() != " " and self.SID.currentText() != " " and
                    self.runway.currentText() != " " and self.cleanWaypointsInput() != [""] and
                    self.arr_airport.currentText() != " " and self.IAP.currentText() != " "
            ):
                self.generateFlightPlan()
                self.createTable()
                self.crearGraph()

        def table_to_excel():
            self.fp.to_excel('output/waypoints.xlsx')

        self.submit.clicked.connect(onGenerate)
        self.to_excel.clicked.connect(table_to_excel)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.setup()
    MainWindow.show()
    sys.exit(app.exec_())
