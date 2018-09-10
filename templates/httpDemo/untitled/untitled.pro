#-------------------------------------------------
#
# Project created by QtCreator 2018-07-11T15:51:11
#
#-------------------------------------------------

QT       += core gui
QT += network core
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = untitled
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    HttpApi.cpp

HEADERS  += mainwindow.h \
    HttpApi.h

FORMS    += mainwindow.ui
