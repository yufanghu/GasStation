#include "HttpApi.h"
#include <qDebug>

CHttpApi::CHttpApi()
{

}

CHttpApi::~CHttpApi()
{

}

void CHttpApi::Post(const QString &url, const QString &param)
{
    QNetworkAccessManager * manager = new QNetworkAccessManager(this);
    QNetworkRequest * request = new QNetworkRequest(QUrl(url));

    connect(manager, SIGNAL(finished(QNetworkReply*)), this, SLOT(slot_ReplyFinished(QNetworkReply*)));
}

void CHttpApi::slot_ReplyFinished(QNetworkReply * reply)
{
    int statusCode = reply->attribute(QNetworkRequest::HttpStatusCodeAttribute).toInt();
    qDebug() << "http replay code[%d]" << statusCode;
    if(reply->error() == QNetworkReply::NoError){

    }
    else {

    }

    reply->deleteLater();
}
