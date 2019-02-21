import sys ,re
from PyQt4 import QtGui ,QtCore
from functools import partial

self.layout = QtGui.QVBoxLayout()

self.select_all_cb = QtGui.QCheckBox('Check All', self.ui.tab)
self.select_all_cb.setTristate(False) # Only enable tristate when necessary so the user doesn't click it through to partially checked
self.select_all_cb.setChecked(True)
self.select_all_cb.setStyleSheet('margin-left: 5px; font: bold')
self.select_all_cb.clicked.connect(self.selectAllCheckChanged) # clicked instead of stateChanged so this doesn't get triggered by ListView's changes
self.layout.addWidget(select_all_cb)

self.listview = QtGui.QListView(self.ui.tab)
self.listview.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
self.listview.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
self.listview.setSelectionRectVisible(False)

model = QStandardItemModel()
for checkItem in self.checkItems:
    item = QStandardItem(checkItem)
    item.setCheckable(True)
    item.setSelectable(False)
    item.setCheckState(QtCore.Qt.Checked)
    model.appendRow(item)
self.listview.setModel(model)
self.listview.clicked.connect(self.listviewCheckChanged)
self.layout.addWidget(listview)


def selectAllCheckChanged(self):
    ''' updates the listview based on select all checkbox '''
    model = self.listview.model()
    for index in range(model.rowCount()):
        item = model.item(index)
        if item.isCheckable():
            if self.select_all_cb.isChecked():
                item.setCheckState(QtCore.Qt.Checked)
            else:
                item.setCheckState(QtCore.Qt.Unchecked)

def listviewCheckChanged(self):
    ''' updates the select all checkbox based on the listview '''
    model = self.listview.model()
    items = [model.item(index) for index in range(model.rowCount())]

    if all(item.checkState() == QtCore.Qt.Checked for item in items):
        self.select_all_cb.setTristate(False)
        self.select_all_cb.setCheckState(QtCore.Qt.Checked)
    elif any(item.checkState() == QtCore.Qt.Checked for item in items):
        self.select_all_cb.setTristate(True)
        self.select_all_cb.setCheckState(QtCore.Qt.PartiallyChecked)
    else:
        self.select_all_cb.setTristate(False)
        self.select_all_cb.setCheckState(QtCore.Qt.Unchecked)