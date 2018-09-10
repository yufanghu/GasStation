#ifndef CHTTPAPI_H
#define CHTTPAPI_H

#include <QSettings>
#include <QNetworkRequest>
#include <QNetworkReply>
#include <QNetworkAccessManager>

class CHttpApi : public QObject
{
    Q_OBJECT
public:
    CHttpApi();
    ~CHttpApi();

    void Post(const QString & url, const QString & param);

private slots:
    void slot_ReplyFinished(QNetworkReply*);


};

#endif // CHTTPAPI_H
