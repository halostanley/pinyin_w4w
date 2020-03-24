import logging
import time
import requests
import json
import redis
import local_pytranslate

###############################################################################
logging.basicConfig(
    format='[%(asctime)s] [%(levelname)s] [%(processName)s] [%(threadName)s] : %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fh = logging.FileHandler("tencent_news.txt")
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s, %(name)s, [%(levelname)s] : %(message)s")
ch.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(fh)
###############################################################################

def is_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True


def tencent_news_ent():
    try:
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
            'Connection': 'keep-alive',
            'Referer': 'https://new.qq.com/'
        }
        url = 'https://pacaio.match.qq.com/irs/rcd?cid=135&token=6e92c215fb08afa901ac31eca115a34f&ext=ent&page=0&num=30'
        sess = requests.Session()
        res = sess.get(url, headers=headers, timeout=(10, 10))

        if res.status_code == 200:
            j = json.loads(res.text)
            acticles_l = j['data']

            acticles_save_l = []
            for acticle in acticles_l:
                d = {}
                d['title'] = acticle['title']
                d['link'] = acticle['surl']
                d['time'] = acticle['update_time']
                translate = local_pytranslate.LocalPyTranslte()
                title_pinyin = translate.text(d['title'])
                title_with_pinyin = ''

                for word in d['title']:
                    if is_chinese(word):
                        single_word_pinyin = translate.text(word)
                        title_with_pinyin += '{}<span class="pinyin_hint">{}</span>'.format(word, single_word_pinyin)
                    else:
                        title_with_pinyin += '{}'.format(word)

                d['title_pinyin'] = title_pinyin.replace('  ', ' ')
                d['title_with_pinyin'] = title_with_pinyin.replace('  ', ' ')

                acticles_save_l.append(d)

            acticles_str = json.dumps(acticles_save_l)
            redis_set('tencent_news_ent', acticles_str)
            logger.info('tencent_news_ent finished')
    except Exception as e:
        logger.info("tencent_news_ent error: {}".format(e))


def tencent_news_finance():
    try:
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
            'Connection': 'keep-alive',
            'Referer': 'https://new.qq.com/ch/finance/'
        }
        url = 'https://pacaio.match.qq.com/irs/rcd?ext=finance&cid=146&token=49cbb2154853ef1a74ff4e53723372ce&page=1&num=100'
        sess = requests.Session()
        res = sess.get(url, headers=headers, timeout=(10, 10))

        if res.status_code == 200:
            j = json.loads(res.text)
            acticles_l = j['data']

            acticles_save_l = []
            for acticle in acticles_l:
                d = {}
                d['title'] = acticle['title']
                d['link'] = acticle['surl']
                d['time'] = acticle['update_time']
                translate = local_pytranslate.LocalPyTranslte()
                title_pinyin = translate.text(d['title'])
                title_with_pinyin = ''

                for word in d['title']:
                    if is_chinese(word):
                        single_word_pinyin = translate.text(word)
                        title_with_pinyin += '{}<span class="pinyin_hint">{}</span>'.format(word, single_word_pinyin)
                    else:
                        title_with_pinyin += '{}'.format(word)

                d['title_pinyin'] = title_pinyin.replace('  ', ' ')
                d['title_with_pinyin'] = title_with_pinyin.replace('  ', ' ')

                acticles_save_l.append(d)

            acticles_str = json.dumps(acticles_save_l)
            redis_set('tencent_news_finance', acticles_str)
            logger.info('tencent_news_finance finished')
    except Exception as e:
        logger.info("tencent_news_finance error: {}".format(e))


def tencent_news_tech():
    try:
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
            'Connection': 'keep-alive',
            'Referer': 'https://new.qq.com/ch/tech/'
        }
        url = 'https://pacaio.match.qq.com/irs/rcd?cid=146&token=49cbb2154853ef1a74ff4e53723372ce&ext=tech&page=1&num=30'
        sess = requests.Session()
        res = sess.get(url, headers=headers, timeout=(10, 10))

        if res.status_code == 200:
            j = json.loads(res.text)
            acticles_l = j['data']

            acticles_save_l = []
            for acticle in acticles_l:
                d = {}
                d['title'] = acticle['title']
                d['link'] = acticle['surl']
                d['time'] = acticle['update_time']
                translate = local_pytranslate.LocalPyTranslte()
                title_pinyin = translate.text(d['title'])
                title_with_pinyin = ''

                for word in d['title']:
                    if is_chinese(word):
                        single_word_pinyin = translate.text(word)
                        title_with_pinyin += '{}<span class="pinyin_hint">{}</span>'.format(word, single_word_pinyin)
                    else:
                        title_with_pinyin += '{}'.format(word)

                d['title_pinyin'] = title_pinyin.replace('  ', ' ')
                d['title_with_pinyin'] = title_with_pinyin.replace('  ', ' ')

                acticles_save_l.append(d)

            acticles_str = json.dumps(acticles_save_l)
            redis_set('tencent_news_tech', acticles_str)
            logger.info('tencent_news_tech finished')
    except Exception as e:
        logger.info("tencent_news_tech error: {}".format(e))


def redis_set(key, val):
    try:
        pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        r.set(key, val)
        return True
    except Exception as e:
        logger.info("redis error: {}".format(e))


def redis_get(key):
    try:
        pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        val = r.get(key)
        print(val)
        return val
    except Exception as e:
        logger.info("redis error: {}".format(e))


if __name__ == "__main__":
    tencent_news_ent()
    tencent_news_finance()
    tencent_news_tech()
