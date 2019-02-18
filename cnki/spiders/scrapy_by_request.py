# -*- coding: utf-8 -*-
import requests
import json
import time
from collections import OrderedDict
import random

class Scrappy(object):
    url = 'http://dbpub.cnki.net/Grid2008/Dbpub/Brief.aspx?ID=SCPD&subBase=all'
    head_str = """Host: dbpub.cnki.net
Connection: keep-alive
Content-Length: 6541
Cache-Control: max-age=0
Origin: http://dbpub.cnki.net
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: http://dbpub.cnki.net/Grid2008/Dbpub/Brief.aspx?curpage=4&RecordsPerPage=20&QueryID=0&ID=SCPD&turnpage=1&systemno=&NaviDatabaseName=SCPD_ZJCLS&NaviField=%e4%b8%93%e9%a2%98%e5%ad%90%e6%a0%8f%e7%9b%ae%e4%bb%a3%e7%a0%81&navigatorValue=&subBase=all
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: ASP.NET_SessionId=adlv5fmrywyvocud1j0xwj45; AutoIpLogin=; LID=; Ecp_IpLoginFail=190218218.17.254.134; SID=130101; FileNameM=cnki%3A; CurTop10KeyWord=%2c%u516c%u53f8; c_m_LinID=LinID=WEEvREcwSlJHSldRa1Fhb09jT0pkYU1renJEYWdMaCtjR3R4RHh2alVycWM=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!&ot=02/18/2019 21:08:09; c_m_expire=2019-02-18 21:08:09
    """
    body_str = """ID=SCPD&hdnSearchType=&hdnIsAll=false&NaviField=%E4%B8%93%E9%A2%98%E5%AD%90%E6%A0%8F%E7%9B%AE%E4%BB%A3%E7%A0%81&NaviDatabaseName=SCPD_ZJCLS&systemno=&hdnFathorCode=sysAll&selectbox=A&selectbox=B&selectbox=C&selectbox=D&selectbox=E&selectbox=F&selectbox=H&selectbox=I&strNavigatorValue=%2CA%2CB%2CC%2CD%2CE%2CF%2CH%2CI&strNavigatorName=%2C%E5%9F%BA%E7%A1%80%E7%A7%91%E5%AD%A6%2C%E5%B7%A5%E7%A8%8B%E7%A7%91%E6%8A%80%E2%85%A0%E8%BE%91%2C%E5%B7%A5%E7%A8%8B%E7%A7%91%E6%8A%80%E2%85%A1%E8%BE%91%2C%E5%86%9C%E4%B8%9A%E7%A7%91%E6%8A%80%2C%E5%8C%BB%E8%8D%AF%E5%8D%AB%E7%94%9F%E7%A7%91%E6%8A%80%2C%E5%93%B2%E5%AD%A6%E4%B8%8E%E4%BA%BA%E6%96%87%E7%A7%91%E5%AD%A6%2C%E7%A4%BE%E4%BC%9A%E7%A7%91%E5%AD%A6%E2%85%A1%E8%BE%91%2C%E4%BF%A1%E6%81%AF%E7%A7%91%E6%8A%80&singleleafcode=&searchAttachCondition=&SearchQueryID=0&SearchFieldRelationDirectory=&updateTempDB=&bCurYearTempDB=1&fieldtips=%E7%AF%87%E5%90%8D%2F%5B%E5%9C%A8%E6%96%87%E7%8C%AE%E6%A0%87%E9%A2%98%E4%B8%AD%E6%A3%80%E7%B4%A2%E3%80%82%E5%AF%B9%E8%AF%A5%E6%A3%80%E7%B4%A2%E9%A1%B9%E7%9A%84%E6%A3%80%E7%B4%A2%E6%98%AF%E6%8C%89%E8%AF%8D%E8%BF%9B%E8%A1%8C%E7%9A%84%EF%BC%8C%E8%AF%B7%E5%B0%BD%E5%8F%AF%E8%83%BD%E8%BE%93%E5%85%A5%E5%AE%8C%E6%95%B4%E7%9A%84%E8%AF%8D%EF%BC%8C%E4%BB%A5%E9%81%BF%E5%85%8D%E6%BC%8F%E6%A3%80%E3%80%82%5D%2C%E5%85%B3%E9%94%AE%E8%AF%8D%2F%5B%E6%A3%80%E7%B4%A2%E6%96%87%E7%8C%AE%E7%9A%84%E5%85%B3%E9%94%AE%E8%AF%8D%E4%B8%AD%E6%BB%A1%E8%B6%B3%E6%A3%80%E7%B4%A2%E6%9D%A1%E4%BB%B6%E7%9A%84%E6%96%87%E7%8C%AE%E3%80%82%E5%AF%B9%E8%AF%A5%E6%A3%80%E7%B4%A2%E9%A1%B9%E7%9A%84%E6%A3%80%E7%B4%A2%E6%98%AF%E6%8C%89%E8%AF%8D%E8%BF%9B%E8%A1%8C%E7%9A%84%EF%BC%8C%E8%AF%B7%E5%B0%BD%E5%8F%AF%E8%83%BD%E8%BE%93%E5%85%A5%E5%AE%8C%E6%95%B4%E7%9A%84%E8%AF%8D%EF%BC%8C%E4%BB%A5%E9%81%BF%E5%85%8D%E6%BC%8F%E6%A3%80%E3%80%82%5D%2C%E7%AC%AC%E4%B8%80%E8%B4%A3%E4%BB%BB%E4%BA%BA%2F%5B%E8%AF%B7%E9%80%89%E6%8B%A9%E6%A3%80%E7%B4%A2%E9%A1%B9%E5%B9%B6%E6%8C%87%E5%AE%9A%E7%9B%B8%E5%BA%94%E7%9A%84%E6%A3%80%E7%B4%A2%E8%AF%8D%EF%BC%8C%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F%E6%96%B9%E5%BC%8F%E3%80%81%E5%8C%B9%E9%85%8D%E6%A8%A1%E5%BC%8F%E3%80%81%E6%96%87%E7%8C%AE%E6%97%B6%E9%97%B4%E7%AD%89%E9%99%90%E5%AE%9A%E6%9D%A1%E4%BB%B6%EF%BC%8C%E7%84%B6%E5%90%8E%E7%82%B9%E5%87%BB%E2%80%9C%E6%A3%80%E7%B4%A2%E2%80%9D%E3%80%82%5D%2C%E4%BD%9C%E8%80%85%2F%5B%E5%8F%AF%E8%BE%93%E5%85%A5%E4%BD%9C%E8%80%85%E5%AE%8C%E6%95%B4%E5%A7%93%E5%90%8D%EF%BC%8C%E6%88%96%E5%8F%AA%E8%BE%93%E5%85%A5%E8%BF%9E%E7%BB%AD%E7%9A%84%E4%B8%80%E9%83%A8%E5%88%86%E3%80%82%5D%2C%E6%9C%BA%E6%9E%84%2F%5B%E5%8F%AF%E8%BE%93%E5%85%A5%E5%AE%8C%E6%95%B4%E7%9A%84%E6%9C%BA%E6%9E%84%E5%90%8D%E7%A7%B0%EF%BC%8C%E6%88%96%E5%8F%AA%E8%BE%93%E5%85%A5%E8%BF%9E%E7%BB%AD%E7%9A%84%E4%B8%80%E9%83%A8%E5%88%86%E3%80%82%5D%2C%E4%B8%AD%E6%96%87%E6%91%98%E8%A6%81%2F%5B%E5%AF%B9%E8%AF%A5%E6%A3%80%E7%B4%A2%E9%A1%B9%E7%9A%84%E6%A3%80%E7%B4%A2%E6%98%AF%E6%8C%89%E8%AF%8D%E8%BF%9B%E8%A1%8C%E7%9A%84%EF%BC%8C%E8%AF%B7%E5%B0%BD%E5%8F%AF%E8%83%BD%E8%BE%93%E5%85%A5%E5%AE%8C%E6%95%B4%E7%9A%84%E8%AF%8D%EF%BC%8C%E4%BB%A5%E9%81%BF%E5%85%8D%E6%BC%8F%E6%A3%80%E3%80%82%5D%2C%E5%BC%95%E6%96%87%2F%5B%E8%AF%B7%E9%80%89%E6%8B%A9%E6%A3%80%E7%B4%A2%E9%A1%B9%E5%B9%B6%E6%8C%87%E5%AE%9A%E7%9B%B8%E5%BA%94%E7%9A%84%E6%A3%80%E7%B4%A2%E8%AF%8D%EF%BC%8C%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F%E6%96%B9%E5%BC%8F%E3%80%81%E5%8C%B9%E9%85%8D%E6%A8%A1%E5%BC%8F%E3%80%81%E6%96%87%E7%8C%AE%E6%97%B6%E9%97%B4%E7%AD%89%E9%99%90%E5%AE%9A%E6%9D%A1%E4%BB%B6%EF%BC%8C%E7%84%B6%E5%90%8E%E7%82%B9%E5%87%BB%E2%80%9C%E6%A3%80%E7%B4%A2%E2%80%9D%E3%80%82%5D%2C%E5%85%A8%E6%96%87%2F%E8%AF%B7%E9%80%89%E6%8B%A9%E6%A3%80%E7%B4%A2%E9%A1%B9%E5%B9%B6%E6%8C%87%E5%AE%9A%E7%9B%B8%E5%BA%94%E7%9A%84%E6%A3%80%E7%B4%A2%E8%AF%8D%EF%BC%8C%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F%E6%96%B9%E5%BC%8F%E3%80%81%E5%8C%B9%E9%85%8D%E6%A8%A1%E5%BC%8F%E3%80%81%E6%96%87%E7%8C%AE%E6%97%B6%E9%97%B4%E7%AD%89%E9%99%90%E5%AE%9A%E6%9D%A1%E4%BB%B6%EF%BC%8C%E7%84%B6%E5%90%8E%E7%82%B9%E5%87%BB%E2%80%9C%E6%A3%80%E7%B4%A2%E2%80%9D%E3%80%82%5D%2C%E5%9F%BA%E9%87%91%2F%5B%E6%A3%80%E7%B4%A2%E5%8F%97%E6%BB%A1%E8%B6%B3%E6%9D%A1%E4%BB%B6%E7%9A%84%E5%9F%BA%E9%87%91%E8%B5%84%E5%8A%A9%E7%9A%84%E6%96%87%E7%8C%AE%E3%80%82%5D%2C%E4%B8%AD%E6%96%87%E5%88%8A%E5%90%8D%2F%5B%E8%AF%B7%E8%BE%93%E5%85%A5%E9%83%A8%E5%88%86%E6%88%96%E5%85%A8%E9%83%A8%E5%88%8A%E5%90%8D%E3%80%82%5D%2CISSN%2F%5B%E8%AF%B7%E8%BE%93%E5%85%A5%E5%AE%8C%E6%95%B4%E7%9A%84ISSN%E5%8F%B7%E3%80%82%5D%2C%E5%B9%B4%2F%5B%E8%BE%93%E5%85%A5%E5%9B%9B%E4%BD%8D%E6%95%B0%E5%AD%97%E7%9A%84%E5%B9%B4%E4%BB%BD%E3%80%82%5D%2C%E6%9C%9F%2F%5B%E8%BE%93%E5%85%A5%E6%9C%9F%E5%88%8A%E7%9A%84%E6%9C%9F%E5%8F%B7%EF%BC%8C%E5%A6%82%E6%9E%9C%E4%B8%8D%E8%B6%B3%E4%B8%A4%E4%BD%8D%E6%95%B0%E5%AD%97%EF%BC%8C%E8%AF%B7%E5%9C%A8%E5%89%8D%E9%9D%A2%E8%A1%A5%E2%80%9C0%E2%80%9D%EF%BC%8C%E5%A6%82%E2%80%9C08%E2%80%9D%E3%80%82%5D%2C%E4%B8%BB%E9%A2%98%2F%5B%E4%B8%BB%E9%A2%98%E5%8C%85%E6%8B%AC%E7%AF%87%E5%90%8D%E3%80%81%E5%85%B3%E9%94%AE%E8%AF%8D%E3%80%81%E4%B8%AD%E6%96%87%E6%91%98%E8%A6%81%E3%80%82%E5%8F%AF%E6%A3%80%E7%B4%A2%E5%87%BA%E8%BF%99%E4%B8%89%E9%A1%B9%E4%B8%AD%E4%BB%BB%E4%B8%80%E9%A1%B9%E6%88%96%E5%A4%9A%E9%A1%B9%E6%BB%A1%E8%B6%B3%E6%8C%87%E5%AE%9A%E6%A3%80%E7%B4%A2%E6%9D%A1%E4%BB%B6%E7%9A%84%E6%96%87%E7%8C%AE%E3%80%82%E5%AF%B9%E4%B8%BB%E9%A2%98%E6%98%AF%E6%8C%89%E8%AF%8D%E6%A3%80%E7%B4%A2%E7%9A%84%EF%BC%8C%E8%AF%B7%E5%B0%BD%E5%8F%AF%E8%83%BD%E8%BE%93%E5%85%A5%E5%AE%8C%E6%95%B4%E7%9A%84%E8%AF%8D%EF%BC%8C%E4%BB%A5%E9%81%BF%E5%85%8D%E6%BC%8F%E6%A3%80%E3%80%82%5D&advancedfield1=%E4%B8%93%E5%88%A9%E5%90%8D%E7%A7%B0&advancedvalue1=%E8%AF%B7%E8%BE%93%E5%85%A5%E6%82%A8%E6%89%80%E9%9C%80%E7%9A%84%E6%A3%80%E7%B4%A2%E8%AF%8D&searchmatch=0&order=dec&RecordsPerPage=50&hdnUSPSubDB=%E4%B8%93%E5%88%A9%E7%B1%BB%E5%88%AB%2C%2B1%2B%2C3%2C1&TableType=PY&display=chinese&encode=gb&TablePrefix=SCPD&View=SCPD&yearFieldName=%E5%B9%B4&userright=&VarNum=1&MM_fieldValue_1_1=&MM_fieldValue_1_2=&MM_slt_updateTime=&MM_Update_Time=&MM_Update_EndTime=&MM_fieldValue_2_1=2000-01-01&MM_fieldValue_2_2=2015-12-31&MM_hiddenTxtName=MM_fieldValue_1_1%40%40%40MM_fieldValue_1_2%40%40%40MM_fieldValue_2_1%40%40%40MM_fieldValue_2_2%40%40%40MM_Update_Time%40%40%40MM_Update_EndTime&MM_fieldName=%E7%94%B3%E8%AF%B7%E6%97%A5%40%40%40%E7%94%B3%E8%AF%B7%E6%97%A5%40%40%40%E5%85%AC%E5%BC%80%E6%97%A5%40%40%40%E5%85%AC%E5%BC%80%E6%97%A5%40%40%40%E6%9B%B4%E6%96%B0%E6%97%A5%E6%9C%9F%40%40%40%E6%9B%B4%E6%96%B0%E6%97%A5%E6%9C%9F&MM_hiddenRelation=%3E%3D%40%40%40%3C%3D%40%40%40%3E%3D%40%40%40%3C%3D%40%40%40%3E%3D%40%40%40%3C%3D&lastpage=56793&RecordsPerPage2=50&systemno=%2C%2C%2C%2C&classtype=&QueryID=0&turnpage=1&curpage={}&curpage1={}&curpage2=1
    """
    @classmethod
    def get_head_dict(cls):
        d = OrderedDict()
        for kv in cls.head_str.split('\n'):
            parts = kv.split(':', 1)
            if len(parts) != 2:
                print "--", parts
            else:
                k, v = parts


            d[k.strip()] = v.strip()

        return d

    @classmethod
    def get_body_dict(cls, page):
        d = OrderedDict()
        body = cls.body_str.format(page)
        for kv in body.split('&'):
            k, v = kv.split('=')
            d[k.strip()] = v.strip()
        return d

    @classmethod
    def get_body_list_tuples(cls, page):
        d = []

        body = cls.body_str.format(page, page)
        for kv in body.split('&'):
            k, v = kv.split('=')
            d.append((k, v))
        return d


    def start(self):
        for page in range(1,200,1):
            print '---scrapy for page:', page
            body_list = Scrappy.get_body_list_tuples(page)
            head_d = Scrappy.get_head_dict()
            response = requests.post(self.url, data=body_list, headers=head_d)
            #self.save(response.text, 'willchen.html')
            got_line_count = self.save_response_data('result_1.0.txt', response)
            if got_line_count == 0:
                print '===Got nothing now, quit'
                break
            time.sleep(random.randint(1, 5))
        print '---Done'


    @classmethod
    def save(cls, text, filename):
        with open(filename, 'w') as f:
            f.write(text.encode('utf-8'))

    @classmethod
    def save_response_data(cls, filename, response):
        import json
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text)
        tbody = soup.find('tbody')
        whole_text = ''

        get_valid_line = 0
        for tr in tbody.find_all('tr'):
            tds = [td.get_text().strip('\n') for td in tr.find_all('td', attrs={'class':'s_tabletd_rb'})]
            if tds:
                index = tds[0].encode('ascii', errors='ignore')
                if index.isdigit():
                    line = json.dumps(tds, encoding='gbk', ensure_ascii=False)
                    whole_text += line + '\n'
                    print line
                    get_valid_line += 1
        with open(filename, 'a') as f:
            f.write(whole_text.encode('utf-8'))

        return get_valid_line


if __name__ == '__main__':
    s = Scrappy()
    s.start()
